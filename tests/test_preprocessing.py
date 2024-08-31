from multiprocessing.sharedctypes import Value
import pandas as pd
import numpy as np
import pytest
from src import preprocessing


def test_split_data():
    df = pd.DataFrame(
        np.random.randn(20, 10), columns=["var_%d" % i for i in range(0, 10)]
    )
    df["churn"] = [np.random.randint(0, 2) for _ in range(20)]

    X_train, X_test, y_train, y_test = preprocessing.split_data(df)
    assert X_train.shape[0] == 16
    assert X_train.shape[1] == 10
    assert X_test.shape[0] == 4
    assert X_test.shape[1] == 10
    assert y_train.shape[0] == 16
    assert y_test.shape[0] == 4

    X_train, X_test, y_train, y_test = preprocessing.split_data(df, 0.1)
    assert X_train.shape[0] == 18
    assert X_train.shape[1] == 10
    assert X_test.shape[0] == 2
    assert X_test.shape[1] == 10
    assert y_train.shape[0] == 18
    assert y_test.shape[0] == 2

    # Testing if function fails if df does not contain target column as stated in function docstring
    df = df.drop("churn", axis=1)
    with pytest.raises(KeyError):
        X_train, X_test, y_train, y_test = preprocessing.split_data(df, 0.1)
