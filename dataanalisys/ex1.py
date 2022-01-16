# %%
import numpy as np
import pandas as pd

# %%
df = pd.read_csv('train.csv')
df.head()

# %%
df.shape

# %%
df.AnnualIncome.mean()

# %%
df[df.EverTravelledAbroad == 'Yes'].shape

# %%
df.groupby('Employment Type').count()

# %%
(1155)/(1155+435) * 100

# %%
df[(df['ChronicDiseases'] == 1) & (df['TravelInsurance'] == "Yes")].count()

# %%
df[df['ChronicDiseases'] == 1]['ChronicDiseases'].count()

# %%
167/445*100

# %%
