var isValidBST = function(root) {
    let stack = [];
    let preNode;
    
    while (root || stack.length) {
        if (root) {
            stack.push(root);
            root = root.left;
        } else { 
            root = stack.pop();
            if (preNode && root.val <= preNode.val) return false;
            preNode = root;
            root = root.right;
        }
    }
    return true;
};
