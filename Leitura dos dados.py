df = pd.read_csv('/content/sneeze5.csv')
df = df.iloc[:, 1:]

print(df)

print(df.columns)
