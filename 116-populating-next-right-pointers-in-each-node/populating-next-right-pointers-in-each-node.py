class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node':
        if not root:
            return None
        
        if root.left:
            root.left.next = root.right
        
        # 2. Connect the right child to the left child of the next parent
        # This only happens if 'root.next' has already been set (i.e., root is not 
        # the rightmost node of its level).
        if root.right and root.next:
            root.right.next = root.next.left
        
        # 3. Recurse down the tree
        self.connect(root.left)
        self.connect(root.right)
        
        return root