var countPrimes = function(n) {
    let primes = Array(n+1).fill(false);
    let primeCount = 0;
    
    for (let i=2; i < n ; i++) {
        if (primes[i] == false) {
            primeCount++;
            for (let j=i; j*i < n ; j++) {
                primes[j*i] = true;  
            }
        }

    }
    return primeCount;
};
