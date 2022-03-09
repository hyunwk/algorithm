var inorderTraversal = function(root) {
    if (!root)
        return [];
    return [...inorderTraversal(root.left), root.val, ...inorderTraversal(root.right)];
}

var inorderTraversal = function(root) {
	let result = stack = [];
	let node = root;
    if (!root)
        return result;j

	while (node || stack.length) {
		while (node) {
			stack.push(node);
			node = node.left;
		}
		node = stack.pop();
		result.push(node);
		node = node.right;
	}
	return result;
}


var inorderTraversal = function(root) {
	let result = []
    let stack = [];
	let node = root;

	while (node || stack.length) {
		if (node) {
			stack.push(node);
			node = node.left;
		} else {
            node = stack.pop();
            result.push(node.val);
            node = node.right;
        }
	}
	return result;
}
