import os
import unittest
from unittest import TestCase
from unittest.mock import patch, Mock

from app.disassembler.managers import DisassemblerManager
from tests.disassembler.data.managers import WIKIPEDIA_CONTENT, JS_SCRIPT_LIST


class TestDisassemblerManager(TestCase):
    """
    python -m unittest tests.disassembler.test_managers.TestDisassemblerManager
    """

    def test_extract_js_scripts_return_list(self):
        expected_element_list = JS_SCRIPT_LIST
        received_element_list = DisassemblerManager.extract_js_scripts(WIKIPEDIA_CONTENT)

        self.assertEquals(expected_element_list, received_element_list)

