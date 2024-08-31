"""
This is the main script where all functions are called to create pipelines
"""
import logging
from src.logger import init_logger
from src.parser import simple_parser
import pandas as pd
from src.io_data import load_data
from src.viz import bar_plot
from src.dataprep import data_preparation
from src.preprocessing import split_data, Preprocessor
from src.modelling import benchmark
from src.config import PATH, CAT_FEATURES, NUM_FEATURES


def main():
    # Parsing argument
    parser = (
        simple_parser()
    )  # you can adjust the function in parser.py file in order to fit your need
    args = parser.parse_args()

    # init logger
    init_logger(level=args.log_level, file=True, file_path="logs/logs.txt")

    logging.info("This is my info log message")
    logging.debug("This is my debug log message")

    ## Your pipeline should be here
    df = load_data(args.data_set)  # replace with your own path

    bar_plot(
        data=df,
        x="type",
        hue="churn",
        title="Customer churns by type",
        xlabel="type",
        ylabel="Number of customers",
    )
    bar_plot(
        data=df,
        x="branche",
        hue="churn",
        title="Customer churns in different branche",
        xlabel="branche",
        ylabel="Number of customers",
    )
    logging.info(
        "on affiche les bar plots de répartition de churn: un en fonction du type de client, un en fonction de la branche"
    )
    df = data_preparation(df.copy())
    l = CAT_FEATURES + NUM_FEATURES
    for col in df.columns:
        if col not in l:
            print(f"{col} non identifié")

    X_train, X_test, y_train, y_test = split_data(df)

    preprocessor = Preprocessor()
    X_train = preprocessor.fit_transform(X_train)
    X_test = preprocessor.fit_transform(X_test)

    benchmark(
        ["lr", "gaussianNB", "svm", "linearSVM", "knn", "xgb"],
        X_train,
        X_test,
        y_train,
        y_test,
    )
    logging.info("on benchmark les modèles de classification")


if __name__ == "__main__":
    main()
