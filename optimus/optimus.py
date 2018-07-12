from pyspark.sql.session import SparkSession
from optimus.dataframe.extension import Create
from optimus.io.save import Save
from optimus.io.load import Load
from optimus.spark import get_spark

# Bound columns operation to the DataFrame Class
from optimus.dataframe import columns, rows


class Optimus:
    def __init__(self, spark=None):
        self.spark = spark

        if self.spark is None:
            print("Creating Spark Session...")
            self.spark = get_spark()
        else:
            print("Using a created Spark Session...")

        self.sc = self.spark.sparkContext

        #
        self.create = Create()
        self.load = Load()
        self.save = Save()

        print("Done.")
