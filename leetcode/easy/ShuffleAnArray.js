var Solution = function(nums) {
    this.nums = nums;
    this.array = nums.slice();
};

Solution.prototype.reset = function() {
    this.array = this.nums;
    return this.array;
};

Solution.prototype.shuffle = function() {
    this.array = this.nums.slice();
    for (let i = 0; i < this.array.length; i++) {
        const randomIdx = Math.floor(Math.random() * (this.array.length - i)) + i;
        [this.array[i], this.array[randomIdx]] = [this.array[randomIdx], this.array[i]];
    }
    return this.array;
};
