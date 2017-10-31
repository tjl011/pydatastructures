"""
Tests the BST functionality.

@license - please see the LICENSE file in this repository

@author Thomas Ludwig
"""
from bst import BST, BSTException
import random

def populate_tree(tree, test_data):
    """ Adds data into the tree
        tree - the BST instance we are working with
        test_data - list of (key, value) tuples we want to insert
    """
    for k, v in test_data:
        tree.add(k, v)

def count_attribute_test():
    """Tests to see if the BST.count attribute works correctly
        Checks if count is initialized to 0, then is incremented and
        decremented correctly if we add and remove an element, respectively.
    """
    tree = BST()
    if tree.count != 0:
        print("error tree count initialized to %d, not 0!" % tree.count)
        return False

    tree.add('a', 1)
    if tree.count != 1:
        print("error tree count after addition is not 1 (it is %d)" % tree.count)
        return False

    tree.add('b', 2)
    if tree.count != 2:
        print("error tree count after addition is not 2, its %d" % tree.count)

    return True


def test_insert_lookup():
    """ Checks to see if we can successfully insert data
    """
    data = [("a", 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
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

def test_inorder_traversal():
    """ Tests if the in order tree traversal behaves correctly
    """
    tree = BST()
    test_data = [(chr(i), i) for i in range(ord('a'), ord('e') + 1)]
    data_sorted = list(test_data)
    random.shuffle(test_data) # randomize the ordering of the test data

    populate_tree(tree, test_data)

    traversal = []
    for k, v in tree.inorder_traversal():
        traversal.append((k, v))

    if traversal != data_sorted:
        print("error in order traversal failed")
        print("expected: %s" % str(data_sorted))
        print("our traversal: %s" % str(traversal))

def test_deletion():
    """ Tests to make sure that we successfully delete the data
    """
    tree = BST()
    test_data = [(chr(i), i) for i in range(ord('a'), ord('i') + 1)]
    sorted_test_data = sorted(test_data)
    random.shuffle(test_data)

    populate_tree(tree, test_data)

    # delete some data
    delete_data = ['a', 'i', 'e']
    for k in delete_data:
        tree.delete(k)
        if tree.find(k):
            print("error key %s still in BST" % str(k))

def test_insertion():
    """Tests if insertion works
    """
    test_data = [(chr(i), i) for i in range(ord('a'), ord('z') + 1)]
    random.shuffle(test_data) # randomize the ordering of the test data

    tree = BST()
    populate_tree(tree, test_data)

    for k, v in test_data:
        found_value = tree.find(k)
        if found_value is None:
            print("error for key %s - failed to find in tree" % str(k))
        elif found_value != v:
            print("error for key %s - found value %s != expected value %s" % ((str(k), str(found_value), str(v))))

if __name__ == "__main__":
    count_attribute_test()
    test_deletion()
    test_insertion()
    test_inorder_traversal()
