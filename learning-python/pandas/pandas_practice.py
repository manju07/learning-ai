import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)
print(myvar.head(), end='\n\n')

list = [
    {
        'name': 'Manju'
    }
]

df = pd.DataFrame(list)

print(df, end='\n\n')
print(df.loc[0], end='\n\n')
print(df.loc[0], end='\n\n')

print(pd.__version__)
