from typing import List
from pathlib import Path

from src.file_handler import FileHandler
from src.analyzer import Analyzer
from src.logger import Logger

class Facade:
    """Facade class for the app. 
    """

    def __init__(self, input_type: str, input_path: str):
        """Init method

        Args:
            input_type (str): Type of input file
            input_path (str): Path of input file
        """
        self.logger = Logger()

        self._file_handler = FileHandler(input_type=input_type,
                                        input_path=input_path)

        self._dataframe = self._file_handler.dataframe

        self._analyzer = Analyzer(self._dataframe)

    def count_unique_rows(self, columns: List[str]) -> int:
        """Count unique rows based on column combination. 

        Args:
            columns (List[str]): List of columns to be used in aggregation.

        Returns:
            int: Return number of rows
        """
        count = self._analyzer.count_unique_rows(columns)
        
        return count

    def find_average(self, column: str) -> float:
        """Find average value of values in column

        Args:
            column (str): column name

        Returns:
            float: return average
        """
        average = self._analyzer.find_average(column)

        return average

    def find_top(self, sort_column: str, top: int, return_column: str) -> str:
        """Find the top N values of return_column, based on sort_column.

        Args:
            sort_column (str): Column to sort by
            top (int): Number of records to return
            return_column (str): Column to return values for

        Returns:
            str: Top N values for return_column
        """
        top_rated_movies = self._analyzer.find_top_rows(column=sort_column, top=top)[return_column]

        return top_rated_movies

    def movies_by_year(self, column: str) -> str:
        """Count movies by year

        Args:
            column (str): year column

        Returns:
            str: Return string representation of dataframe
        """
        list_of_count = self._analyzer.movies_by_year(column)#.values.tolist()

        return list_of_count.to_string()

    def movies_by_genre(self, column: str) -> str:
        """Count movies by genre.

        Args:
            column (str): genre column.

        Returns:
            str: Return string representation of dataframe
        """
        list_of_count = self._analyzer.movies_by_genre(column)#.values.tolist()

        return list_of_count.to_string()

    def save_as(self, output_type: str, output_path: str):
        """Save dataframe as file type

        Args:
            output_type (str): Type of the file to be saved
            output_path (str): Path of the file to be saved
        """
        self._file_handler.save_df_as_file(output_type=output_type, output_path=output_path)

