# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root: return []
        ans=[];
        stack = [(root,"")]
        
        while stack:
            node,string = stack.pop();
            if not node.left and not node.right:
                ans.append(string+str(node.val))
                
            if node.left:
                stack.append((node.left,string+str(node.val)+"->"))
            if node.right:
                stack.append((node.right,string+str(node.val)+"->"))
        return ans
                