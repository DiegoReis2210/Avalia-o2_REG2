resposta = df['nsneeze']
preditoras = df[['alcohol', 'antihist', 'smoker', 'age', 'pollen']]

formula = "nsneeze ~ C(alcohol) + C(antihist) + C(smoker) + age + pollen"

modelo_pois = smf.glm(
    formula=formula,
    data=df,
    family=sm.families.Poisson()
)

ajuste_pois = modelo_pois.fit()
print(ajuste_pois.summary())

print(f"Fator de mudança para cada variável:")
print(f"Alcohol: {np.exp(0.3477)}")
print(f"Antihist: {np.exp(-0.5969)}")
print(f"Smoker: {np.exp(0.6700)}")
print(f"Age: {np.exp(-0.0127)}")
print(f"Pollen: {np.exp(0.0301)}")

