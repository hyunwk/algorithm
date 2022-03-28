// queue
var letterCombinations = function(digits) {
    if (digits == '')
        return [];

     const buttons = [
		 [],
		 [],
         ['a','b','c'],
         ['d','e','f'],
         ['g','h','i'],
         ['j','k','l'],
         ['m','n','o'],
         ['p','q','r','s'],
         ['t','u','v'],
         ['w','x','y','z'],
     ]
    const queue = [''];
    for (let i=0 ; i<digits.length ; i++) {
	    while (queue[0].length == i) {
	        const number = parseInt(digits.charAt(i));
			const newDigits = buttons[number];
	        console.log(newDigits)
	        const first = queue.shift();
			for (let digit of newDigits)
				queue.push(first+digit);
        }
	}
    return queue;
};
// 
var letterCombinations = function(digits) {
    if (digits == '')
        return [];
    
	 let result = [''];
     const buttons = [
		 [],
		 [],
         ['a','b','c'],
         ['d','e','f'],
         ['g','h','i'],
         ['j','k','l'],
         ['m','n','o'],
         ['p','q','r','s'],
         ['t','u','v'],
         ['w','x','y','z'],
     ]

	let i = 0;
	while (i < digits.length) {
		const number = parseInt(digits.charAt(i));
		const newDigits = buttons[number];
		const tempResult = [...result];
        console.log('tempResult',tempResult)
		result = [];
		for (let item of tempResult) {
			for (let newItem of newDigits) {
				result.push(item+newItem);
			}
		}
		i++;
	}
	return result;
};

