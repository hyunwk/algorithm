var isSymmetric = function(root) {
    const bst = (l, r) => {
        if (!l && !r) {
            return true;
        }
        if (!l || !r) {
            return false;
        }
        if (l.val !== r.val) {
            return false;
        }  
        return bst(l.left, r.right) && bst(l.right, r.left);
    }
    return bst(root.left, root.right);
};
