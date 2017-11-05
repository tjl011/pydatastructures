"""
Tests the BST functionality.

@license - please see the LICENSE file in this repository

@author Thomas Ludwig
"""
from bst import BST, BSTException
import random
import unittest

class TestBSTMethods(unittest.TestCase):

	def __populate_tree(self, tree, test_data):
		""" Adds data into the tree
			tree - the BST instance we are working with
			test_data - list of (key, value) tuples we want to insert
		"""
		for k, v in test_data:
			tree.add(k, v)

	def test_count_attribute(self):
		tree = BST()
		self.assertEquals(tree.count, 0)

		# add an element
		tree.add('a', 1)
		self.assertEquals(tree.count, 1)

		# add another element
		tree.add('b', 2)
		self.assertEquals(tree.count, 2)

		# delete an element
		tree.delete('a')
		self.assertEquals(tree.count, 1)

	def test_insert_lookup(self):
		"""tests to see if we can successfully insert data and
		   lookup the data that we insert.
		"""
		data = [("a", 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
		tree = BST()

		# insert the data
		for d in data:
			tree.add(*d)

		# lookup the data
		for d in data:
			self.assertEquals(tree.find(d[0]), d[1])

	def test_inorder_traversal(self):
		"""Tests if the in order tree traversal behaves correctly
		"""
		tree = BST()
		test_data = [(chr(i), i) for i in range(ord('a'), ord('e') + 1)]
		data_sorted = list(test_data)
		random.shuffle(test_data) # randomize the ordering of the test data

		self.__populate_tree(tree, test_data)

		traversal = []
		for k, v in tree.inorder_traversal():
			traversal.append((k, v))

		self.assertEquals(traversal, data_sorted)

	def test_deletion(self):
		"""Tests the deletion method. """
		tree = BST()
		test_data = [(chr(i), i) for i in range(ord('a'), ord('i') + 1)]
		sorted_test_data = sorted(test_data)
		random.shuffle(test_data)

		self.__populate_tree(tree, test_data)

		# delete some data
		delete_data = ['a', 'i', 'e']
		for k in delete_data:
			tree.delete(k)
			self.assertEquals(tree.find(k), None)

	def test_insertion(self):
		"""Tests if insertion works."""
		test_data = [(chr(i), i) for i in range(ord('a'), ord('z') + 1)]
		random.shuffle(test_data) # randomize the ordering of the test data

		tree = BST()
		self.__populate_tree(tree, test_data)

		for k, v in test_data:
			found_value = tree.find(k)
			self.assertEquals(found_value, v)

if __name__ == "__main__":
	unittest.main()