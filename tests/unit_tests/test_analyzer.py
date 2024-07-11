from unittest import TestCase
from unittest.mock import Mock, patch

from pandas import DataFrame

from src.analyzer import Analyzer
from src.logger import Logger

class TestAnalyzer(TestCase):
    @classmethod
    def setUpClass(cls):
        Logger("resources/unit_tests.log")

    def setUp(self):
        data = {"test_column": [1, 2, 3, 4, 5, 10]}
        self._test_dataframe = DataFrame(data)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_find_average(self):
        # Arrange
        tested_class = Analyzer(self._test_dataframe)
        expected = 4.166666666666667

        # Act
        actual = tested_class.find_average('test_column')

        # Assert
        self.assertEqual(expected, actual, "Actual average doesn't match expected average")
    