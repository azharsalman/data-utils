# Data Utils

The Data Utils library is a versatile Python toolkit designed to streamline common data-related tasks and enhance the efficiency of your projects. It is intended to be a reusable and easily integratable solution for handling various aspects of data processing, cleaning, and analysis.

## Installation

To use the Data Utils library in your projects, follow the steps below:

### 1. Install Poetry

Make sure you have Poetry installed on your system. You can install Poetry by following the instructions on the [official Poetry website](https://python-poetry.org/docs/).

### 2. Install Dependencies

Run the following command to install the project dependencies using Poetry:

```bash
poetry install
```
This will create a virtual environment and install the required dependencies specified in the pyproject.toml file.

### 3. Creating a Build (Optional)

If you want to create a distributable package or build for your Data Utils library, you can use the following Poetry command:

```bash
poetry build
```

## Components & Usage
## 1. DfCounter

`DfCounter` is a Python class designed to help you analyze and count duplicates in a Pandas DataFrame based on specified columns.

### Usage

To use the functionality provided by `DfCounter`, follow the example below or use the `main.py` file.:

```python
import pandas as pd
from data_utils.duplication import DfCounter


if __name__ == '__main__':
    test_df = pd.DataFrame(data=[
        ['A', 'a', 'x', 1],
        ['A', 'b', 'x', 1],
        ['A', 'c', 'x', 1],
        ['B', 'a', 'x', 1],
        ['B', 'b', 'x', 1],
        ['B', 'c', 'x', 1],
        ['A', 'a', 'y', 1],
    ],
        columns=['col1', 'col2', 'col3', 'col4']
    )
    test_cols = ['col1']
    counter = DfCounter(test_df, test_cols)

    print(counter.duplicates_stats())
```
