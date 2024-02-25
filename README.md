# pytest-kuunda

[<img src="https://img.shields.io/pypi/v/pytest-kuunda.svg">](https://pypi.org/project/pytest-kuunda) [<img src="https://img.shields.io/pypi/pyversions/pytest-kuunda.svg">](https://pypi.org/project/pytest-kuunda) [<img src="https://github.com/svenhofstede/pytest-kuunda/actions/workflows/main.yml/badge.svg">](https://github.com/svenhofstede/pytest-kuunda/actions/workflows/main.yml)

pytest plugin to help with test data setup for PySpark tests


## Features

* TODO


## Requirements

* TODO


## Installation

You can install "pytest-kuunda" via `pip`_ from `PyPI`_::

    $ pip install pytest-kuunda


## Usage

`transformation.py`

```python
def add_one(df: DataFrame):
    return df.withColumn("value_add_one", col("value") + 1)
```

`my_test_data/input.csv`

```csv
label,value
aaa,1
bbb,2
ccc,3
```

`my_test_data/expected.csv`

```csv
label,value,value_add_one
aaa,1,2
bbb,2,3
ccc,3,4
```

`test_transformation.py`

```python
@fixture
def my_test_dir(kuunda_dir):
    return kuunda_dir("my_test_data")

def test_example_1(spark_fixture, my_test_dir):
    result = add_one(my_test_dir["input_df"])

    result.collect() == my_test_dir["expected_df").collect()
```


## Contributing

Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the `MIT`_ license, "pytest-kuunda" is free and open source software


## Issues


## Credits

This `pytest`_ plugin was generated with `Cookiecutter`_ along with `@hackebrot`_'s `cookiecutter-pytest-plugin`_ template.