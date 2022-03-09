var levelOrder = function(root) {
    result = []
    
    if (!root)
        return result;

    const dfs = (node, depth) => {
        if (result.length <= depth)
            result.push(new Array());
        result[depth].push(node.val);
        
        if (node.left) dfs(node.left, depth+1);
        if (node.right) dfs(node.right, depth+1);
    }
    dfs(root, 0);
    return result;
};
