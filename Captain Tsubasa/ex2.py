# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn import svm
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score


# %%
def pred_score(y_test, y_prob):
    macro_roc_auc_ovo = roc_auc_score(y_test, y_prob, multi_class="ovo",
                                      average="macro")
    weighted_roc_auc_ovo = roc_auc_score(y_test, y_prob, multi_class="ovo",
                                         average="weighted")
    macro_roc_auc_ovr = roc_auc_score(y_test, y_prob, multi_class="ovr",
                                      average="macro")
    weighted_roc_auc_ovr = roc_auc_score(y_test, y_prob, multi_class="ovr",
                                         average="weighted")
    print("One-vs-One ROC AUC scores:\n{:.6f} (macro),\n{:.6f} "
          "(weighted by prevalence)"
          .format(macro_roc_auc_ovo, weighted_roc_auc_ovo))
    print("One-vs-Rest ROC AUC scores:\n{:.6f} (macro),\n{:.6f} "
          "(weighted by prevalence)"
          .format(macro_roc_auc_ovr, weighted_roc_auc_ovr))


# %%
df = pd.read_csv('train.csv').drop(['matchId', 'playerId'], axis=1)
df_test = pd.read_csv('test.csv')

df.head()


# %%
y = df['outcome'].copy()
y[(y == 'گُل') | (y == 'گُل به خودی')] = 1
y[(y == 'برخورد به تیردروازه') | (y == 'مهار توسط دروازه بان')
  | (y == 'موقعیت از دست رفته') | (y == 'برخورد به دفاع')] = 0

X = df.drop('outcome', axis=1)

X_test = df_test

X.loc[X['interferenceOnShooter'].isnull(
), 'interferenceOnShooter'] = 'بیش از یک بازیکن'
X_test.loc[X_test['interferenceOnShooter'].isnull(
), 'interferenceOnShooter'] = 'بیش از یک بازیکن'


# X.drop(['minute','second'],axis=1)
# X_test.drop(['minute','second'],axis=1)


# %%
# Shape of training data (num_rows, num_columns)
print("train size is {}".format(X.shape))
print("test size is {}".format(X_test.shape))

# Number of missing values in each column of training data
missing_val_count_by_column = (X.isnull().sum())
print("missing val count by column {}".format(
    missing_val_count_by_column[missing_val_count_by_column > 0]))


# %%
# Get list of categorical variables
s = (X.dtypes == 'object')
object_cols = list(s[s].index)

print("Categorical variables:")
print(object_cols)


# %%

# Apply one-hot encoder to each column with categorical data
OH_encoder = OneHotEncoder(handle_unknown='error',
                           sparse=False, dtype=np.int64)
train_X_encoded = OH_encoder.fit_transform(X[object_cols])
column_name = OH_encoder.get_feature_names(object_cols)

OH_cols_train = pd.DataFrame(train_X_encoded, columns=column_name)
OH_cols_test = pd.DataFrame(OH_encoder.transform(
    X_test[object_cols]), columns=column_name)

# One-hot encoding removed index; put it back
OH_cols_train.index = X.index
OH_cols_test.index = X_test.index

# Remove categorical columns (will replace with one-hot encoding)
num_X = X.drop(object_cols, axis=1)
num_X_test = X_test.drop(object_cols, axis=1)

# Add one-hot encoded columns to numerical features
OH_X = pd.concat([num_X, OH_cols_train], axis=1)
OH_X_test = pd.concat([num_X_test, OH_cols_test], axis=1)
print('train shape', OH_X.shape)
print('test shape', OH_X_test.shape)


# %%
y = y.astype('int')
x_train, x_test, y_train, y_test = train_test_split(
    OH_X, y, test_size=0.35, random_state=0)


# %%
SVM = svm.SVC(probability=True)
SVM.fit(OH_X, y)
y_prob = SVM.predict_proba(OH_X_test)


# %%


# %%
df = pd.DataFrame(y_prob[:, 1])
df.to_csv('output.csv')


# %%
