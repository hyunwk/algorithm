var kthSmallest = function(root, k) {
    let result = [];
    let stack = [];
    
    if (!root) {
        return result;
    }
    
    while (root || stack.length) {
        if (root) {
            stack.push(root);
            root = root.left;
        } else {
            k--;
            if (!k)
                return stack.pop().val;
            root = stack.pop();
            result.push(root.val);
            root = root.right;
        }
    }
    return
};
