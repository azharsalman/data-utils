from pandas import DataFrame
import typing as tt


class DfCounter:

    df: DataFrame
    columns: tt.List[str]

    def __init__(self, df: DataFrame, columns: tt.List[str]):
        """
        Initialize the DfCounter with a DataFrame and columns.

        Parameters:
        - df: pandas DataFrame
        - columns: list of column names to consider for duplicate checking
        """
        self.df = df
        self.columns = columns

    def get_duplicate_rows(self) -> DataFrame:
        """
        Get a DataFrame containing duplicate rows based on specified columns.

        Returns:
        - pandas DataFrame with duplicate rows
        """
        duplicated_values = self.df.duplicated(subset=self.columns, keep='first')
        duplicated_df = self.df[duplicated_values].groupby(self.columns).size().reset_index(name='number_of_duplicates')
        return duplicated_df

    def get_duplicates_count(self) -> int:
        """
        Calculate the total count of duplicate rows based on specified columns.

        Returns:
        - total count of duplicate rows as an integer
        """
        duplicated_values = self.df.duplicated(subset=self.columns, keep='first')
        return len(self.df[duplicated_values])

    def duplicates_stats(self) -> tt.Dict[str, tt.Union[int, DataFrame]]:
        """
        Calculate the total count of duplicate rows based on specified columns.

        Returns:
        - a dictionary with count and samples of duplicates
        """
        return {
            "count": self.get_duplicates_count(),
            "samples": self.get_duplicate_rows()
        }
