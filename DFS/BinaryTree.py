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
        
        #max_val_digits = max([max([len(str(v)) for v in r]) for r in to_prints])
        #print max_val_digits
        
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


root = Node(val=5,
            left=Node(val=4,
                 left=Node(val=1,
                      right=Node(val=2))
            ),
            right=Node(val=8,
                 left=Node(val=3),
                 right=Node(val=4,
                    left=Node(val=9),
                    right=Node(val=1))
            )
        )

BST = Node(val=5,
            left=Node(val=2,
                 left=Node(val=1,
                    right=Node(val=1.5, 
                        left=Node(val=1.2))),
                 right=Node(val=3)
            ),
            right=Node(val=9,
                 left=Node(val=7),
                 right=Node(val=15,
                    right=Node(val=16)
                 )
            )
        )

root_with_id = Node(id=0,val=-3,
                    left=Node(id=1,val=-2,
                         left=Node(id=3,val=3,
                              left=Node(id=7,val=1,
                                    left=Node(id=11,val=4)),
                              right=Node(id=8,val=1)),
                         right=Node(id=4,val=-1,
                              left=Node(id=9,val=4),
                              right=Node(id=10,val=2))
                    ),
                    right=Node(id=2,val=2,
                         left=Node(id=5,val=-1),
                         right=Node(id=6,val=3,
                            right=Node(id=12,val=2))
                    )
                )


if __name__ == '__main__':
    root.pretty_print()
    print
    BST.pretty_print()
