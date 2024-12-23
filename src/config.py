# Here you should define all your constant variable that are parameters of your whole project
import logging

# ===================================================
# LOGS
# ===================================================
PATH_LOG_FILE = "../logs"
LOG_LEVEL = logging.INFO
CHURN_MAPPING = {"oui": 1, "non": 0}
PATH = "data/dataset.csv"
ML_FLOW_PATH = "C:/Users/victo/Documents/churn/mlruns"
TEST_SIZE = 0.2
RANDOM_STATE = 0
CAT_FEATURES = [
            "genre",
            "espace_client_web",
            "assurance_vie",
            "banque_principale",
            "compte_epargne",
            "credit_autres",
            "cartes_bancaires",
            "compte_courant",
            "espace_client",
            "PEA",
            "assurance_auto",
            "assurance_habitation",
            "credit_immo",
            "type",
            "compte_titres",
            "methode_contact",
            "segment_client",
        ]
NUM_FEATURES = [
            "anciennete_mois",
            "agios_6mois",
            "interet_compte_epargne_total",
            "age",
            "var_0",
            "var_18",
            "var_19",
            "var_20",
            "var_37",
            "var_38",
            "diff_var_0_19",
            "diff_var_0_20",
            "diff_var_20_38",
            "diff_var_0_38",
        ]
# ===================================================