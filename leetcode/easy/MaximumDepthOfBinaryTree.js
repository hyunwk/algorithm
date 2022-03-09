// bfs
var maxDepth = function(root) {
    if (!root) {
        return 0;
    }
    
    let maxDepth = 0;
    let queue = [{node: root, depth:1}]
    while (queue.length) {
        let {node, depth} = queue.shift();
        
        if (depth > maxDepth) {
            maxDepth = depth;
        }
        if (node.left) {
            queue.push({node: node.left, depth: depth+1})
        }
        if (node.right) {
            queue.push({node: node.right, depth: depth+1})
        }
    }
    return maxDepth;
};

// dfs
var maxDepth = function(root) {
    if (!root) {
        return 0;
    }

    let maxDepth = 0;

    let queue = [{node: root, depth: 1}]

    while (queue.length !== 0) {
        let {node, depth} = queue.pop();
        if (depth > maxDepth) {
            maxDepth = depth;
        }

        if (node.left) queue.push({node: node.left, depth: depth+1})
        if (node.right) queue.push({node: node.right, depth: depth+1})
    }
    return maxDepth;
}

// dfs with recursion
var maxDepth = function(root) {
    let maxDepth = 0;

    const dfs = (node, depth) => {
        if (!node) {
            maxDepth = Math.max(depth, maxDepth);
            return ;
        }
        dfs(node.left, depth+1);
        dfs(node.right, depth+1)
    }
    dfs(root, 0);
}
