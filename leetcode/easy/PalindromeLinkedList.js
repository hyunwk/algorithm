var isPalindrome = function(head) {
	//  Array solution
	 let nums = [];
	 while (head)
	 {
	     nums.push(head.val);
	     head = head.next;
	 }
	 let left = 0;
	 let right = nums.length - 1
	 while (left <= right) {
	     if (nums[left] != nums[right])
	         return false
	     left++;
	     right--;
	 }
	 return true
    
    // two pointer 
    
    let fast = head;
    let slow = head;
    while (fast && fast.next) {
        fast = fast.next.next;
        slow = slow.next;
    }
    
    // reverse slow
    let prev = null;
    while (slow) {
        let temp = slow.next;
        slow.next = prev;
        prev = slow;
        slow = temp;
    }
    left = head;
    right = prev
    while (right) {
        if (left.val != right.val) {
            return false;
        }
        left = left.next;
        right = right.next;
    }
    return true;
};
