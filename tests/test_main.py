import os
import unittest
from unittest import TestCase
from unittest.mock import patch, Mock


class TestMain(TestCase):
    """
    python -m unittest tests.test_main.TestMain
    """

    def test_suite_works(self):
        self.assertTrue(True)

