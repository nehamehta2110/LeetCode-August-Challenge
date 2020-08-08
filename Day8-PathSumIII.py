# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root, sum):
        def utility(root, res):
            if not root:
                return 0
            next_res = [sum - root.val] + [i - root.val for i in res]

            return int(root.val == sum) + res.count(root.val) + utility(root.left, next_res) + utility(root.right,
                                                                                                       next_res)

        return utility(root, [])


def main():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    solve = Solution()
    print(solve.pathSum(root, 31))


if __name__ == '__main__':
    main()
