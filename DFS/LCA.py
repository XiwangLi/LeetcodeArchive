#!/usr/bin/env python

#from __futrue__ import division
import random
from BinaryTree import Node, BST, root

# if there is no parent node, we will need to traverse from the bottom
# There are serverl cases: 1: a is the aancester of b, then return a
# case 2: a and b are in two subtree, then return root

def LCA(root, a, b):
	if not root or root.val == a or root.val == b:
		return root
	left = LCA(root.left, a, b)
	right = LCA(root.right, a, b)
	if left and right:
		return root
	else:
		return right if not left else left

# with parent node
def LCA_para(root, a, b):
	h_a = height(root, a)
	h_b = height(root, b)
	if h_a < h_b:
		h_a, h_b = h_b, h_a

	for _ in range(h_a - h_b):
		node_b = node_b.parent
	while node_a != node_b:
		node_a = node_a.parent
		node_b = node_b.parent
	return node_a


def height(root, node):
	h = 0
	while node:
		node =  node.parent
		h += 1
	return h

#LCA III
# if not exist
def LCAIII(root, a, b):
	result = LCA(root, a, b)
	if results != a and results != b:
		return results
	elif results == a:
		if LCA(a, b, b) == a:
			return a
	elif results == b:
		if LCA(b, a, a) == b:
			return b
	else:
		return None
