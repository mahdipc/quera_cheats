# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import pandas as pd


# %%
df = pd.read_csv('train.csv')
df['counts'] = 1

df.head()


# %%
df1 = df.copy()
len(df1['playerId'].unique())


# %%
df2 = df.copy()
df2[df2["outcome"] == "گُل"].groupby('playerId', sort=True)[
    'playerId'].count().nlargest(2)


# %%
df3 = df.copy()
df3['out'] = 0
df3.loc[df3['outcome'] == 'گُل', 'out'] = 1

df3_group = df3.groupby(['playerId'])['out'].agg([np.mean])
df3_group.sort_values(['mean'], ascending=False)


# %%
df4 = df.copy()
df4['max_xy'] = np.sqrt(df4['x']**2+df4['y']**2)
df4.sort_values(['max_xy'], ascending=False)


# %%
