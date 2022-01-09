var isAnagram = function(s, t) {
    map = {};
    s.split('').forEach((item) => map[item] = (map[item]|| 0) + 1);
    t.split('').forEach((item) => map[item] = (map[item] || 0) - 1);
    return Object.keys(map).every((key) => map[key] == 0);
};
