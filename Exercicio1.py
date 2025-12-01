# 1. Estatísticas Descritivas
print("### 1. Estatísticas Descritivas das Variáveis Numéricas ###")
print(df[['nsneeze', 'age', 'pollen']].describe())
# 2. Contagem de Variáveis Binárias (0/1)
print("\n### 2. Contagem das Variáveis Binárias ###")
for col in ['alcohol', 'antihist', 'smoker']:
    print(f"\nDistribuição de '{col}':")
    print(df[col].value_counts(normalize=True)) 


# Distribuição de 'nsneeze'
plt.figure(figsize=(4,2), dpi=200)
sns.histplot(df['nsneeze'], bins=50, kde=True)
plt.title("Distribuição da variável 'nsneeze'")
plt.xlabel("Número de espirros")
plt.ylabel("Frequência")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()

# Boxplot de 'nsneeze' por 'alcohol'
plt.figure(figsize=(4,2), dpi=200)
sns.boxplot(x='alcohol', y='nsneeze', data=df)
plt.title("'nsneeze' por ingestão de alcoól")
plt.xticks(rotation=45)
plt.show()

#  Boxplot de 'nsneeze' por 'antihist'
plt.figure(figsize=(4,2), dpi=200)
sns.boxplot(x='antihist', y='nsneeze', data=df)
plt.title("'nsneeze' por uso de anti-histamínico")
plt.show()

#  Boxplot de 'nsneeze' por 'smoker'
plt.figure(figsize=(4,2), dpi=200)
sns.boxplot(x='smoker', y='nsneeze', data=df)
plt.title("'nsneeze' por hábitos de fumo")
plt.show()

# Gráfico de dispersão entre 'nsneeze' e 'pollen'
sns.scatterplot(x='pollen', y='nsneeze', data=df)
plt.title('nsneeze vs. pollen')
plt.show()

# Gráfico de dispersão entre 'nsneeze' e 'age'
sns.scatterplot(x='age', y='nsneeze', data=df)
plt.title('nsneeze vs. age')
plt.show()


# Variáveis dummy para as variáveis categóricas
vars_categoricas = ['alcohol', 'antihist', 'smoker']
preditoras = pd.get_dummies(df[vars_categoricas + ['nsneeze']], drop_first=True).astype(float)
preditoras


# Correlação de nsneeze com todas as outras variáveis
correlation = df.corr()['nsneeze'].sort_values(ascending=False)
print("\n### Coeficientes de Correlação de Pearson com 'nsneeze' ###")
print(correlation)
