import matplotlib.pyplot as plt
import seaborn as sns
from src import config
import boto3
from botocore.exceptions import ClientError
import os
import logging


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client("s3")
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def bar_plot(data, x, hue, title="", xlabel="", ylabel=""):
    plt.figure(figsize=(8, 8))
    splot = sns.countplot(data=data, x=x, palette="GnBu", hue=hue)
    sns.set_style("ticks")
    total = float(len(data))
    for p in splot.patches:
        percentage = "{:.1f}%".format(100 * p.get_height() / total)
        x = p.get_x() + p.get_width()
        y = p.get_height()
        splot.annotate(percentage, (x, y), ha="center", va="center")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.show()
 






    

    

