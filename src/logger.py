from sys import stdout
from typing import Any
from logging import getLogger, basicConfig, FileHandler, StreamHandler, DEBUG

class Logger:
    """Logger wrapper singleton class
    """
    LOGFILE = "resources/logger.log"
    def __new__(cls, logfile=None):
        """Constructor method

        Returns:
            _type_: the singleton instance

        """
        if not hasattr(cls, 'instance'):
            cls.instance = super(Logger, cls).__new__(cls)
        return cls.instance
    
    def __init__(self, logfile=None):
        """Init method

        Args:
            logfile (_type_, optional): Optional logfile location. Defaults to None.
        """

        logfile_path = logfile if logfile is not None else Logger.LOGFILE
        self._logger = getLogger('MOVIE-ANALYZER')#.addHandler(StreamHandler(stdout))
        basicConfig(
                    encoding='utf-8', 
                    level=DEBUG,
                    handlers=[
                        FileHandler(logfile_path),
                        StreamHandler(stdout)
                    ]
        )

    def debug(self, param: str) -> Any:
        """Debug method wrapper

        Args:
            param (str): Original parameter

        Returns:
            Any: return the logger implementation of debug
        """
        return self._logger.debug(param)

    def info(self, param: str) -> Any:
        """Info method wrapper

        Args:
            param (str): Original parameter

        Returns:
            Any: return the logger implementation of info
        """
        return self._logger.info(param)

    def warning(self, param: str) -> Any:
        """Warning method wrapper

        Args:
            param (str): Original parameter

        Returns:
            Any: return the logger implementation of warning
        """
        return self._logger.warning(param)

    def error(self, param: str) -> Any:
        """Error method wrapper

        Args:
            param (str): Original parameter

        Returns:
            Any: return the logger implementation of error
        """
        return self._logger.error(param)

