function solution(clothes) {
	return Object.values(clothes.reduce((obj, clothe)=> {
        if (!obj[clothe[1]])
            obj[clothe[1]] = 1;
    	obj[clothe[1]] += 1;
        return obj;
    }, {})).reduce((a,b)=>a*b) -1;
}
