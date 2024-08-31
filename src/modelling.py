from sklearn.metrics import f1_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split, learning_curve
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
import xgboost as xgb
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
import mlflow
from mlflow.tracking import MlflowClient
import logging
from src import config


def evaluation(model, X_train, X_test, y_train, y_test, model_name):
    # Path where experiences are recorded (can be a local path /data/projects/...)
    mlflow_tracking_uri = f"file:///{config.ML_FLOW_PATH}"  # mlruns folder will be created automatically
    mlflow.set_tracking_uri(mlflow_tracking_uri)

    # set experiment name
    experiment_name = "Churn progression predictions"
    experiment = MlflowClient().get_experiment_by_name(experiment_name)
    exp_id = (
        experiment.experiment_id
        if experiment
        else MlflowClient().create_experiment(experiment_name)
    )

    # start run
    with mlflow.start_run(experiment_id=exp_id, run_name=model_name) as run:
        model.fit(X_train, y_train)
        ypred = model.predict(X_test)

        print(confusion_matrix(y_test, ypred))
        print(classification_report(y_test, ypred))

        N, train_score, val_score = learning_curve(
            model,
            X_train,
            y_train,
            cv=4,
            scoring="f1",
            train_sizes=np.linspace(0.1, 1, 10),
        )

        plt.figure(figsize=(12, 8))
        plt.plot(N, train_score.mean(axis=1), label="train score")
        plt.plot(N, val_score.mean(axis=1), label="validation score")
        plt.title(model_name)
        plt.legend()
        plt.savefig("my_plot.png")
        plt.close()
        mlflow.log_artifact("my_plot.png", "myplot")
        mlflow.log_param("taille du trainingset", len(X_train))
        mlflow.log_metric("f1", f1_score(y_test, ypred))

    mlflow.end_run()


def benchmark(
    models, X_train, X_test, y_train, y_test, models_params=None
):  # models_params shoud be a dict {"model_name" : dict(params)}
    if models_params is None:
        models_params = {}
    if "lr" in models:
        if "lr" in models_params:
            lr = LogisticRegression(**models_params["lr"])
        else:
            lr = LogisticRegression()
        lr.fit(X_train, y_train)
        print("lr")
        evaluation(lr, X_train, X_test, y_train, y_test, "lr")
    if "gaussianNB" in models:
        if "gaussianNB" in models_params:
            nb = GaussianNB(**models_params["gaussianNB"])
        else:
            nb = GaussianNB()
        nb.fit(X_train, y_train)
        print("gaussianNB")
        evaluation(nb, X_train, X_test, y_train, y_test, "gaussianNB")
    if "svm" in models:
        if "svm" in models_params:
            svm = SVC(**models_params["svm"])
        else:
            svm = SVC()
        svm.fit(X_train, y_train)
        print("svm")
        evaluation(svm, X_train, X_test, y_train, y_test, "svm")

    if "linearSVM" in models:
        if "linearSVM" in models_params:
            lsvc = LinearSVC(**models_params["linearSVM"])
        else:
            lsvc = LinearSVC()
        lsvc.fit(X_train, y_train)
        print("linearSVM")
        evaluation(lsvc, X_train, X_test, y_train, y_test, "linearSVM")

    if "knn" in models:
        if "knn" in models_params:
            knn = KNeighborsClassifier(**models_params["knn"])
        else:
            knn = KNeighborsClassifier()
        knn.fit(X_train, y_train)
        print("knn")
        evaluation(knn, X_train, X_test, y_train, y_test, "knn")
    if "xgb" in models:
        if "xgb" in models_params:
            xgbmodel = xgb.XGBClassifier(**models_params["xgb"])
        else:
            xgbmodel = xgb.XGBClassifier(random_state=0)
        xgbmodel.fit(X_train, y_train)
        print("xgb")
        evaluation(xgbmodel, X_train, X_test, y_train, y_test, "xgb")
