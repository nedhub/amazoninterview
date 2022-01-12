var insertIntoBST = function(root, val) {
    // empty tree case:
    if (root === null) return new TreeNode(val);
    if (val > root.val) {
        root.right = insertIntoBST(root.right, val);
    } else {
        root.left = insertIntoBST(root.left, val);
    }
    return root;
};

