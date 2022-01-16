# %%
import numpy as np
import pandas as pd

# %%
df = pd.read_csv('supermarket.csv')
df.set_index('Customer Id', inplace=True)

# %%
df.groupby('Product').count()

# %%
df.groupby('Date').count().mean()

# %%
df.groupby('Product').count().sort_values('Date')

# %%
df["Date"] = pd.to_datetime(df['Date'], format='%Y-%m-%d')


# %%
df[df["Date"] > '2020'].groupby(['Customer Id', 'Date']).count()

# %%
df[df["Date"] > '2020'].groupby(['Customer Id', 'Date']).count().groupby(
    'Customer Id').count().sort_values('Product', ascending=False).head(15)

# %%
df[df.index == '0ZRF32AJ06BC'].groupby("Date").count()

# %%
df.groupby(df['Date'].dt.day_name()).count().sort_index()

# %%
sabad = df.groupby(['Customer Id', 'Date'])

# %%
mahsolat = df['Product'].unique()

# %%
for name, itemgroup in sabad:
    print(itemgroup['Product'])
    break

# %%
len(mahsolat)

# %%
dic = []
for item in mahsolat:
    s = 0
    for name, itemgroup in sabad:
        if item in itemgroup['Product'].to_numpy():
            s = s+1
    dic.append([item, s])


# %%
df_suppport = pd.DataFrame(np.array(dic), columns=["product", "support"])
df_suppport["support"] = pd.to_numeric(df_suppport["support"])

# %%
df_suppport.sort_values("support", ascending=False)

# %%
dic_2 = []
for item1 in mahsolat:
    for item2 in mahsolat:
        if item1 != item2:
            s = 0
            for name, itemgroup in sabad:
                if (item1 in itemgroup['Product'].to_numpy()) & (item2 in itemgroup['Product'].to_numpy()):
                    s = s+1
            dic_2.append([item1, item2, s])
