from pandas import DataFrame
import pytest
from data_utils.duplication import DfCounter


@pytest.fixture
def sample_dataframe() -> DataFrame:
    """
    Fixture function to create a sample DataFrame for testing.

    Returns:
    - pandas DataFrame: Sample DataFrame with duplicate rows.
    """
    data = {
        'col1': ['A', 'A', 'A', 'B', 'B', 'B', 'A'],
        'col2': ['a', 'b', 'c', 'a', 'b', 'c', 'a'],
        'col3': ['x', 'x', 'x', 'x', 'x', 'x', 'y'],
        'col4': [1, 1, 1, 1, 1, 1, 1]
    }
    return DataFrame(data)


def test_get_duplicate_rows(sample_dataframe: DataFrame):
    """
    Test the 'get_duplicate_rows' method of DfCounter.

    Parameters:
    - sample_dataframe: Sample DataFrame with duplicate rows.
    """
    counter = DfCounter(sample_dataframe, ['col1', 'col2'])

    result = counter.get_duplicate_rows()

    assert len(result) == 1


def test_total_duplicates(sample_dataframe: DataFrame):
    """
    Test the 'total_duplicates' method of DfCounter.

    Parameters:
    - sample_dataframe: Sample DataFrame with duplicate rows.
    """
    counter = DfCounter(sample_dataframe, ['col1'])

    result = counter.get_duplicates_count()

    assert result == 5
