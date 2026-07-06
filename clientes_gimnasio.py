import pandas as pd

pd.options.future.infer_string = False 


df = pd.read_csv("clientes_gimnasio.csv")
"""
print("Estructura del dataset:", df.shape)
print("\nPrimeras filas del dataset:")
print(df.head())
print("\nTipos de datos de cada columna:")
print(df.dtypes)
"""

#valores nulos por columna

print(df.isnull().sum())
print()
print((df.isnull().sum() / len(df) * 100).round(2))

#Estrategia para tratar los valores nulos

#Edad
df["Edad"] = df["Edad"].fillna(df["Edad"].median()) #Se usa la mediana para imputar los valores nulos
#sin que se vean afectados por los valores extremos u outliers. 

#Sucursal
df["Sucursal"] = df["Sucursal"].fillna(df["Sucursal"].mode()[0]) #Se usa la moda para imputar los valores nulos
#"Sucursal" es una variable categórica, por lo que la moda (valor que mas se repite) es una buena opcion 

#Email
df["Email"] = df["Email"].fillna("No proporcionado") #Se reemplaza los valores nulos por "No proporcionado"
#No se puede adivinar un Email ni imputarle un contendio con la moda al ser un identificador unico

#Tratar duplicados
print("Filas antes:", len(df))
df = df.drop_duplicates()
print("Filas después:", len(df))

#Verificar tipos de datos
df["Plan"] = df["Plan"].astype("category")
print(df.dtypes)