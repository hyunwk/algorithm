var maxProfit = function(prices) {
    let maxProfit = 0;
    let minPrice = prices[0];
    for (let idx=1; idx<prices.length ; idx++) {
        minPrice = Math.min(minPrice, prices[idx]);
        maxProfit = Math.max(maxProfit, prices[idx] - minPrice);
    }
    return maxProfit;
};
