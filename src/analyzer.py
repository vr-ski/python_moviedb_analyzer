from typing import List
from pandas import DataFrame, to_datetime

from src.logger import Logger

class Analyzer:
    """Analyzer class. Uses pandas dataframe method and functions to provide statistics and aggregations
    """
    def __init__(self, dataframe: DataFrame):
        """Init method

        Args:
            dataframe (DataFrame): Dataframe to be analyzed
        """
        self._dataframe = dataframe
        self._logger = Logger()

        self._logger.debug(f"{self._dataframe.columns=}")

    def count_unique_rows(self, columns: List[str]) -> int:
        """Count unique rows 

        Args:
            columns (List[str]): List of columns

        Returns:
            int: Number of unique rows
        """
        count = self._dataframe[columns].drop_duplicates().shape[0]

        return count

    def find_average(self, column) -> float:
        """Find average based on column

        Args:
            column (_type_): column to get average of

        Returns:
            float: the average of the column values
        """
        average = self._dataframe[column].mean()

        return average

    def find_top_rows(self, column: str, top: int) -> DataFrame:
        """Find top N rows

        Args:
            column (str): column to sort by
            top (int): number of top rows to return

        Returns:
            DataFrame: Dataframe containing the top rows only
        """
        top_rows = self._dataframe.sort_values(by=[column], ascending=False).head(top)

        return top_rows

    def movies_by_year(self, column: str) -> DataFrame:
        """Count movies by year

        Args:
            column (str): Movies column name

        Returns:
            DataFrame: Dataframe containing the counts
        """
        tmp_df = self._dataframe
        
        tmp_df['year'] = tmp_df[column].str[:4]
        
        self._logger.debug(f"{tmp_df.columns=}")

        counts = tmp_df.groupby(['year']).size()

        self._logger.debug(f"{type(counts)=}")
        
        return counts
    
    def movies_by_genre(self, column: str) -> DataFrame:
        """Count movies by genre

        Args:
            column (str): Genre column name

        Returns:
            DataFrame: Dataframe containing the counts
        """
        tmp_df = self._dataframe
        
        tmp_df = tmp_df.explode(column)
        
        self._logger.debug(f"{tmp_df.head(5)=}")

        counts = tmp_df.groupby(column).size()
        
        self._logger.debug(f"{type(counts)=}")
        
        return counts

