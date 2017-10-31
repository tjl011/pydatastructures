"""
Implementation of a dictionary as a Binary Search Tree.
Keys in the dictionary must be unique and comparable.

@license - please see the LICENSE file in this repository

@author Thomas Ludwig
"""

class BSTException(Exception):
    """ All BST exceptions will be raised here
    """
    pass

class _BSTNode(object):
    def __init__(self, key, value, parent=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def _get_min(self):
        """ Returns the minimum node in the subtree rooted at self.
        """
        n = self
        while n.left:
            n = n.left
        return n
    def _get_inorder_succ(self):
        """ Returns the in order successor of node self (or None if
            there is not an in order successor)
        """

        if self.right:
            return self.right._get_min()

        par = self.parent
        tmp = self
        while par and par.right == tmp:
            tmp = par
            par = par.parent
        return par


class BST(object):
    """ Implementation of a binary search tree.
    """

    def __init__(self):
        self.root = None
        self.count = 0 # number of nodes in subtree

    def find(self, key, isExceptRaised=False):
        """ Returns the value associated with key
        """
        n = self.root

        while n:
            if n.key == key:
                break
            elif n.key < key:
                n = n.right
            else:
                n = n.left

        if isExceptRaised and n is None:
            raise BSTException("error key %s not found in BST" % str(key))
        elif n is None:
            return None
        else:
            return n.value

    def add(self, key, value):
        """ Inserts (key, value) into BST if key is not already present.
            Throws a BSTException if the key is already there
        """
        if self.root is None:
            self.root = _BSTNode(key, value)
        else:
            p = self.root
            while p:
                if p.key == key:
                    raise BSTException("error key %s already present in BST" % str(key))
                elif p.key < key:
                    if p.right is None:
                        p.right = _BSTNode(key, value, p)
                        break
                    else:
                        p = p.right
                else:
                    if p.left is None:
                        p.left = _BSTNode(key, value, p)
                        break
                    else:
                        p = p.left
        self.count += 1

    def update(self, key, new_value):
        """Updates the node whose key is 'key' by settings its associated
           value to 'value'

           Raises a BSTException if the key is not there
        """

        p = self.root
        while p:
            if p.key == key:
                p.value = new_value
                return
            elif p.key < key:
                p = p.right
            else:
                p = p.left

        raise BSTException("error key %s not present in BST" % str(key))

    def delete(self, key):
        """ Deletes the node whose key is 'key'
            Raises a BSTException if key is not present in the BST
        """
        raise Exception("Error method 'delete' not yet implemented!")