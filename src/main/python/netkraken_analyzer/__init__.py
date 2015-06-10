from __future__ import division

import json


def calc_index(name):
    sum = 0
    for c in name:
        sum = 7 * sum + ord(c)
    return (sum % 1000) / 1000


def calc_node(name):
    return {
        "name": name,
        "id": name,
        "index": calc_index(name),
        "group": 0
    }


def add_node(nodename, nodes):
    if nodename not in nodes:
        nodes[nodename] = calc_node(nodename)


def dumps(links, nodes):
    data = {"links": links, "nodes": nodes}
    return json.dumps(data, indent=4)
