from __future__ import division

import json
import glob


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
    return json.dumps(data, indent=4, sort_keys=True)


def calc_nodes_and_links(path):
    links = []
    nodes = {}
    for filename in glob.glob(path):
        with open(filename) as f:
            data = json.load(f)
            for connection, count in data.items():
                source, target, protocol = connection.split()
                link = {
                    "id": "%s %s" % (source, target),
                    "protocol": protocol,
                    "source": source,
                    "target": target,
                    "count": count,
                }
                links.append(link)

                add_node(source, nodes)
                add_node(target, nodes)
    return {"nodes": nodes, "links": links}
