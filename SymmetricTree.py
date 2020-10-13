class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution: 
  def isMirror(self, left, right):
    # if not right or not right:
    #   return left == right
    # if left.val != right.val:
    #   return False
    if not left and not right:
      return True
    if not left or not right: 
      return False
    if left.val == right.val:
      return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
    else:
      return False

  def isSymmetric(self, root):
    if not root:
      return True
    else:
      return self.isMirror(root.left, root.right)




tree = TreeNode([1,2,3,0,3,1,3])
result = Solution()
print(result.isSymmetric(tree))