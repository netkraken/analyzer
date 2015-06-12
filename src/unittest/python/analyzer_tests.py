from __future__ import print_function

from datetime import datetime

import unittest
from mock import patch

from testhelper import myAssertDictEqual

import netkraken_analyzer


class AnalyzerTest(unittest.TestCase):

    def test_calc_index(self):
        self.assertEquals(0.886, netkraken_analyzer.calc_index("foo"))

    def test_calc_node(self):
        myAssertDictEqual({"name": "foo", "id": "foo", "group": 0, "index": 0.886}, netkraken_analyzer.calc_node("foo"))

    def test_add_node(self):
        nodes = {} 
        netkraken_analyzer.add_node("bar", nodes)
        self.assertIn("bar", nodes)

    # @patch("netkraken.get_current_datetime")
    # def test_get_current_timestrings(self, now_mock):
    #     now_mock.return_value = datetime(2042, 12, 12, 12, 12)
    #     # self.assertDictEqual({'day': '2042-12-12', 'hour': '2042-12-12T12', 'minute': '2042-12-12T12:12'},
    #                          # netkraken.get_current_timestrings())
    #     myAssertDictEqual({'day': '2042-12-12', 'hour': '2042-12-12T12', 'minute': '2042-12-12T12:12'},
    #                            netkraken.get_current_timestrings())


if __name__ == "__main__":
    unittest.main()
