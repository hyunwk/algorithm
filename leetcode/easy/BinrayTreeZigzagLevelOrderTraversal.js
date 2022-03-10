var zigzagLevelOrder = function(root) {
    result = [];
    const dfs = (node, depth, result) => {
        if (!node) 
            return false
        
        if (!result[depth]) 
            result[depth] = [];
        
        depth % 2 == 0
        ? result[depth].push(node.val)
        : result[depth].unshift(node.val)
        
        if (node.left) 
            dfs(node.left, depth+1, result);      
        if (node.right) 
            dfs(node.right, depth+1, result);           
    }
    dfs(root, 0, result);
    return result;
};
