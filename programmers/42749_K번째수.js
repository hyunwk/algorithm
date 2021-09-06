function solution(array, commands) {
    var answer = [];
 	let sliced = [];
    commands.forEach(items => {;
        sliced = array.slice(items[0] - 1, items[1]).sort((a,b)=>a-b); 
console.log(sliced[items[2]-1]);
        answer.push(sliced[items[2]-1]);
    });
    return answer;
}
