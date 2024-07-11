from pathlib import Path
from pandas import DataFrame, read_csv as pd_read_csv 
from pandas.errors import EmptyDataError as pdEmptyDataError, ParserError as pdParserError

from src.logger import Logger

class FileHandler():
    """FileHanlder class to hanle all file io operations.
    """
    def __init__(self, input_type: str, input_path: str):
        """Init method

        Args:
            input_type (str): Type of input file
            input_path (str): Path of input file
        """
        self._input_type = input_type
        self._input_path = input_path
        self._logger = Logger()
        self.dataframe = self._pandas_read_file()

    @property
    def dataframe(self):
        return self._dataframe
    
    @dataframe.setter
    def dataframe(self, value: DataFrame):
        self._dataframe = value

    def _pandas_read_file(self) -> DataFrame:
        """Factory method to read file via pandas

        Raises:
            NotImplementedError: Filetype that is not yet impemented
            ValueError: Filetype that is not recognized as valid

        Returns:
            DataFrame: Return the dataframe after reading it
        """
        if self._input_type == 'csv': 
            return self._pandas_read_csv()
        elif self._input_type == 'json':
            raise NotImplementedError("json read support will come in the near future")
        else:
            raise ValueError(self._input_type)

    def _pandas_read_csv(self) -> DataFrame:
        """Reading a CSV file into a pandas df

        Raises:
            FileNotFoundError: File not found
            pdEmptyDataError: No data in file
            pdParserError: File could not be parsed
            Exception: Other exceptions

        Returns:
            DataFrame: Dataframe containing the CSV data
        """
        # create Path object
        path = Path(self._input_path)

        # Log path used
        self._logger.debug(f"{path=}")

        # read dataframe
        try:
            dataframe = pd_read_csv(path)
        except FileNotFoundError:
            self._logger.error(f"File not found: {path}")
            raise
        except pdEmptyDataError:
            self._logger.error(f"No valid data in file {path}")
            raise
        except pdParserError as parser_err:
            self._logger.error(parser_err)
            raise pdParserError
        except Exception as error:
            self._logger.error(error)
            raise
        else:
            self._logger.debug(f"{path=}")
        
        return dataframe

    def save_df_as_file(self, output_type: str, output_path: str):
        """Factory method to save a file

        Args:
            output_type (str): Type of file to be saved
            output_path (str): Path of file to be saved

        Raises:
            NotImplementedError: File type not supported yet
            ValueError: File type not recognized as valid
        """
        if output_type == 'json': 
            self._save_df_as_json(output_path=output_path)
        elif self._input_type == 'csv':
            raise NotImplementedError("csv write support will come in the near future")
        else:
            raise ValueError(output_type)

    def _save_df_as_json(self, output_path: str):
        """Save file as JSON

        Args:
            output_path (str): Path of file to be saved

        Raises:
            pdEmptyDataError: No data error
            Exception: Other errors
        """
        if self._dataframe.empty:
            raise pdEmptyDataError

        path = Path(output_path)
        
        try:
            json = self._dataframe.to_json(path)
        except Exception as error:
            self._logger.error(error)
            raise
        else:
            self._logger.debug(f"File {path} successfully written.")
        
