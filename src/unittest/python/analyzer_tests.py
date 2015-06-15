from __future__ import print_function

import unittest
from mock import patch, mock_open

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
        found = nodes.get("bar")
        self.assertNotEqual(found, None)

    def test_dumps(self):
        self.assertEqual("""{\n    "nodes": [\n        "a"\n    ], \n    "links": {\n        "foo": "bar"\n    }\n}""",
                         netkraken_analyzer.dumps({"foo": "bar"}, ["a"]))

    @patch("glob.glob")
    def test_calc_nodes_and_links(self, globglob):
        globglob.return_value = ("foo")

        dummy_db_as_string = """{
            "a b somehow": 42
        }"""
        with patch("netkraken_analyzer.open", mock_open(read_data=dummy_db_as_string), create=True) as m:
            result = netkraken_analyzer.calc_nodes_and_links(".../invalid_path")
            self.assertTrue(len(m.mock_calls) > 0)
        myAssertDictEqual({
            "a": {"index": 0.097, "name": "a", "id": "a", "group": 0},
            "b": {"index": 0.098, "name": "b", "id": "b", "group": 0}}, result["nodes"])
        myAssertDictEqual({'count': 42, 'source': u'a', 'protocol': u'somehow', 'id': u'a b', 'target': u'b'},
                          result["links"][0])

    # @patch("netkraken.get_current_datetime")
    # def test_get_current_timestrings(self, now_mock):
    #     now_mock.return_value = datetime(2042, 12, 12, 12, 12)
    #     # self.assertDictEqual({'day': '2042-12-12', 'hour': '2042-12-12T12', 'minute': '2042-12-12T12:12'},
    #                          # netkraken.get_current_timestrings())
    #     myAssertDictEqual({'day': '2042-12-12', 'hour': '2042-12-12T12', 'minute': '2042-12-12T12:12'},
    #                            netkraken.get_current_timestrings())


if __name__ == "__main__":
    unittest.main()
