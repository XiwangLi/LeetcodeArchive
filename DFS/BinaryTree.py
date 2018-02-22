#!/usr/bin/env python

from __future__ import division
from math import log10

class Node(object):
    def __init__(self, val=0,
                 left=None, right=None, 
                 id=None, parent=None):
        self.id = id
        self.left = left
        self.right = right
        self.val = val
        self.parent = parent
    
    def __str__(self):
        if self.left is None and self.right is None:
            return str(self.val)
        else:
            return '%s (%s, %s)' % (
                    str(self.val), 
                    str(self.left), 
                    str(self.right))
    
    def __repr__(self):
        s = 'TreeNode Object (id=' + str(self.id) + \
            ' val='+str(self.val)+')'
        return s
    
    def pretty_print(self):
        # get each levels
        level = [self]
        to_prints = [[self.val]]
        while True:
            is_all_none = True
            next_level = []
            to_print = []
            for n in level:
                if n is None:
                    next_level += [None, None]
                    to_print += ['#','#']
                else:
                    is_all_none = False
                    next_level += [n.left, n.right]
                    left_val = n.left.val if n.left and n.left.val else '#'
                    right_val = n.right.val if n.right and n.right.val else '#'
                    to_print += [left_val, right_val]
            if is_all_none: break
            level = next_level
            to_prints.append(to_print)

        
        to_prints = to_prints[:-1] # remove the last row with only '#'
        to_pretty_prints = []
        to_prints.reverse()
        for i, row in enumerate(to_prints):
            row = map(str,row)
            #row = [' '*(max_val_digits-len(v))+v for v in row]
            sep = ' '*(2**(i+1) - 1)
            space = ' '*(2**i - 1)
            to_pretty_prints.insert(0, space + sep.join(row) + space)
        print '\n'.join(to_pretty_prints)

