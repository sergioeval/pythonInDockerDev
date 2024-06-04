#%%
import pandas as pd

data = [
    {'nombre': 'juan'},
    {'nombre': 'pepe'}
]


df = pd.DataFrame(data)

df.head()

print(df)