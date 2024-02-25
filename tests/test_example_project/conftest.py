import pytest
from pyspark.sql import SparkSession


@pytest.fixture
def spark_fixture():
    spark = SparkSession.builder.appName("Unit testing spark").getOrCreate()
    yield spark
