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
