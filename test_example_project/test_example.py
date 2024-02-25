from _pytest.fixtures import fixture

from example_project.example import add_one


@fixture
def my_test_dir(kuunda_dir):
    return kuunda_dir("my_test_data")

def skip_test_example_1(spark_fixture, my_test_dir):
    result = add_one(my_test_dir["input_df"])

    # result.collect() == my_test_dir["expected_df").collect()
