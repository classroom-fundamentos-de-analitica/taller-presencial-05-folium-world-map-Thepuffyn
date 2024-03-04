"""Taller Presencial Evaluable"""

import pandas as pd

def load_affiliations():
    """Carga el archivo scopus-papers.csv y retorna un dataframe con la columna 'Affiliations'"""
    dataframe = pd.read_csv(
        "https://raw.githubusercontent.com/jdvelasq/datalabs/master/datasets/scopus-papers.csv",
        sep=",",
        index_col=None,
    )[["Affiliations"]]
    return dataframe
  
def remove_na_rows(affiliations):
    """Elimina las filas con valores nulos en la columna 'Affiliations'"""

    affiliations = affiliations.copy()
    affiliations = affiliations.dropna(subset=["Affiliations"])

    return affiliations
  

df = load_affiliations()
df = remove_na_rows(df)
for i in range(5):
    print(df.Affiliations.values[i])
  
  
def add_countries_column(affiliations):
    """Transforma la columna 'Affiliations' a una lista de paises."""

    affiliations = affiliations.copy()
    affiliations["countries"] = affiliations["Affiliations"].copy()
    affiliations["countries"] = affiliations["countries"].str.split(";")
    affiliations["countries"] = affiliations["countries"].map(
        lambda x: [y.split(",") for y in x]
    )
    affiliations["countries"] = affiliations["countries"].map(
        lambda x: [y[-1].strip() for y in x]
    )
    affiliations["countries"] = affiliations["countries"].map(set)
    affiliations["countries"] = affiliations["countries"].str.join(", ")

    return affiliations
  
  
