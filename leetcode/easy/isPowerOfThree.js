var isPowerOfThree = function(n) {
// 1 
     if (n%2 == 0 || n%5 == 0 || n%7 == 0)
         return false;
     if (n === 1)
         return true;
  
     if (n%3 == 0) {
         while (n > 1)
             n /= 3;
         if (n == 1)
             return true;
     }
     return false;
// 2
    let cnt = 0;
    for (let n=3; n<= 2**31-1 ; n*=3)
        cnt++;
    return n>0 && ((3 ** cnt % n) === 0)
};
