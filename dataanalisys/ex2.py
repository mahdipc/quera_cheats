# %%
from sklearn.ensemble import RandomTreesEmbedding
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestRegressor, GradientBoostingClassifier
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
import numpy as np
import pandas as pd

# %%
df_train = pd.read_csv('train.csv')
df_train.set_index('Customer Id', inplace=True)
y = df_train['TravelInsurance']
X = df_train.drop('TravelInsurance', axis=1)

df_test = pd.read_csv('test.csv')
df_test.set_index('Customer Id', inplace=True)


# %%
s = (X.dtypes == 'object')
object_cols = list(s[s].index)

print(object_cols)


# %%

# Make copy to avoid changing original data
label_X_train = X.copy()
label_X_valid = df_test.copy()

# Apply ordinal encoder to each column with categorical data
ordinal_encoder = OrdinalEncoder()
label_X_train[object_cols] = ordinal_encoder.fit_transform(X[object_cols])
label_X_valid[object_cols] = ordinal_encoder.transform(df_test[object_cols])

y[y == "Yes"] = 1
y[y == "No"] = 0

# %%
X_train, X_valid, y_train, y_valid = train_test_split(
    label_X_train, y,  test_size=0.25, random_state=0)
n_estimators = 100
max_depth = 5

model = RandomForestRegressor(
    n_estimators=n_estimators, max_depth=max_depth, random_state=1
)

clf = Pipeline(steps=[
    ('scaler', StandardScaler()),
    ('model', model)
])

clf.fit(X_train, y_train.to_numpy('float'))

preds = clf.predict(X_valid)
print(roc_auc_score(y_valid.to_numpy('float'), preds))

# %%
clf.fit(label_X_train, y)

preds_test = clf.predict(label_X_valid)

# %%


# %%
output = pd.DataFrame({'Customer Id': label_X_valid.index,
                       'prediction': preds_test})
output.to_csv('submission.csv', index=False)

# %%
