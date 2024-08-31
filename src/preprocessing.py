from sklearn.model_selection import train_test_split, learning_curve
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from src.config import TEST_SIZE
from src.config import RANDOM_STATE
from src.config import CAT_FEATURES
from src.config import NUM_FEATURES
import logging


def split_data(df, test_size=TEST_SIZE):
    logging.debug(f"Taille du Dataframe df {df.shape}")
    X = df.drop("churn", axis=1)
    y = df["churn"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=RANDOM_STATE
    )
    return X_train, X_test, y_train, y_test


class Preprocessor:
    """Une instance de classe est une pipeline de preprocessing"""

    def __init__(self):
        cat_features = CAT_FEATURES

        num_features = NUM_FEATURES

        pipe_most_freq_onehot = Pipeline(
            [
                ("imput_most_frequent", SimpleImputer(strategy="most_frequent")),
                (
                    "one_hot",
                    OneHotEncoder(
                        drop="if_binary", sparse=False, handle_unknown="ignore"     # Si une nvll categ arrive, il l'ignore
                    ),
                ),
            ]
        )
        pip_mean_scale = Pipeline(
            [
                ("imput_mean", SimpleImputer(strategy="mean")),
                ("standard_scaler", StandardScaler()),
            ]
        )

        feature_encoder = ColumnTransformer(
            transformers=[
                ("imp_most_freq_onehot", pipe_most_freq_onehot, cat_features),
                ("imp_mean_scale", pip_mean_scale, num_features),
            ]
        )
        self.preprocessor = feature_encoder

    def fit_transform(self, X):
        return self.preprocessor.fit_transform(X)

    def fit(self, X):
        return self.preprocessor.fit(X)

    def transform(self, X):
        return self.preprocessor.transform(X)

    def get_features_name(self):
        """Retrive features name after preprocessing (usefull for interpretation)"""
        feat_names = []
        for transf in self.preprocessor.transformers_:
            if transf[0] != "remainder":
                names_out = transf[1][-1].get_feature_names_out()
                names_in = transf[2]
                for i, name in enumerate(names_in):
                    names_out_tmp = [
                        c.replace("x%d" % i, "%s" % name) for c in names_out
                    ]
                    names_out = names_out_tmp
                feat_names.extend(names_out)
        return feat_names
