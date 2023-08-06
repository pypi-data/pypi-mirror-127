from geodome.tessellation import *
from geodome.neighbourhood_search import *

import numpy as np
import io

import unittest.mock as mock

try:
    import unittest2 as unittest
except ImportError:
    import unittest


class TestIsZero(unittest.TestCase):
    @mock.patch("sys.stdout", new_callable=io.StringIO)
    def assert_stdout(self, arr, expected_output, mock_stdout):
        is_zero.py_func(arr)
        self.assertEqual(expected_output, mock_stdout.getvalue())

    def test_not_zero(self):
        self.assert_stdout(np.array([1, 1, 1]), "")

    def test_zero(self):
        self.assert_stdout(
            np.array([0, 0, 0]), "Something is zero that shouldn't be: \n"
        )
