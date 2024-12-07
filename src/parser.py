import argparse


def simple_parser():
    parser = argparse.ArgumentParser(
        description="CHURN PROJECT", epilog="Developped by VJ"
    )

    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Log level",
    )
    parser.add_argument(
        "--data-set", 
        default = 'C:/Users/vjesequel/Documents/vj_training_albus/datasetchurn.csv', 
        help="Path to your dataset")
    return parser
