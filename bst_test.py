"""
Tests the BST functionality.

@license - please see the LICENSE file in this repository

@author Thomas Ludwig
"""
from bst import BST, BSTException

def test1():
    data = [("a", 1), ('b', 2), ('c', 3)]
    tree = BST()

    for d in data:
        print("inserting (%s, %d) into tree" % d)
        tree.add(*d)

    for d in data:
        v = tree.find(d[0])
        if v == d[1]:
            print("key %s successfully found in tree" % d[0])
        else:
            print("error key '%s' not found" % str(d[0]))

if __name__ == "__main__":
    test1()