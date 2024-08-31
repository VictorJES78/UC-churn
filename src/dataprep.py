import numpy as np
import pandas as pd
from src.config import CHURN_MAPPING


def drop_columns(df):
    """_summary_

    Args:
        df (_type_): _description_

    Returns:
        _type_: _description_
    """
    df.drop("id_client", axis=1, inplace=True)
    df.drop("branche", axis=1, inplace=True)  # we drop branche for sake of simplicity
    return df


def clean_churn(df):
    """drop missing values

    Args:
        df (_type_): _description_

    Returns:
        _type_: _description_
    """

    df.dropna(subset=["churn"], inplace=True)
    df["churn"] = df["churn"].map(CHURN_MAPPING)
    return df


def impute_na(df):
    """replace empty values by Nan

    Args:
        df (_type_): _description_

    Returns:
        _type_: _description_
    """
    df = df.replace(r"^\s*$", np.nan, regex=True)
    return df


def clean_interet_compte_epargne_total(df):
    df["interet_compte_epargne_total"] = pd.to_numeric(
        df["interet_compte_epargne_total"]
    )
    return df


def clean_compte_epargne(df):
    """when compte_epargne is unknown, replace by oui

    Args:
        df (_type_): _description_

    Returns:
        _type_: _description_
    """
    df.loc[
        (df["cartes_bancaires"] == "medium") & (df["compte_epargne"].isnull()),
        "compte_epargne",
    ] = "oui"
    df.loc[
        (df["cartes_bancaires"] == "premium") & (df["compte_epargne"].isnull()),
        "compte_epargne",
    ] = "oui"
    return df


def clean_var_i(df):
    """remove correlated variables

    Args:
        df (_type_): _description_

    Returns:
        _type_: _description_
    """
    for i in range(1, 18):
        df.drop("var_" + str(i), axis=1, inplace=True)
    for i in range(21, 37):
        df.drop("var_" + str(i), axis=1, inplace=True)

    # transform remaining vars into differences
    df["diff_var_0_19"] = df["var_0"] - df["var_19"]
    df["diff_var_0_20"] = df["var_0"] - df["var_20"]
    df["diff_var_20_38"] = df["var_20"] - df["var_38"]
    df["diff_var_0_38"] = df["var_0"] - df["var_38"]
    return df


def data_preparation(df):
    """voilà un script bien plus clair"""
    # drop useless columns
    df = drop_columns(df)

    # clean churn column (outcome)
    df = clean_churn(df)

    # impute empty values
    df = impute_na(df)

    # clean interet_compte_epargne_total column
    df = clean_interet_compte_epargne_total(df)

    # clean compte_epargne column
    df = clean_compte_epargne(df)

    # clean var_i columns
    df = clean_var_i(df)

    return df
