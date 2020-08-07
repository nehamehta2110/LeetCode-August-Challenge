"""
Given a binary tree, return the vertical order traversal of its nodes values.
For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).
Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes,
we report the values of the nodes in order from top to bottom (decreasing Y coordinates).
If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.
Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.
"""
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root):
        dic = collections.defaultdict(list)

        def traverse(node, coord, layer):
            if not node:
                return
            dic[coord].append((layer, node.val))
            traverse(node.left, coord - 1, layer + 1)
            traverse(node.right, coord + 1, layer + 1)

        traverse(root, 0, 0)
        return [[val for _, val in sorted(v)] for k, v in sorted(dic.items())]


def main():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    solve = Solution()
    print(solve.verticalTraversal(root))


if __name__ == '__main__':
    main()
