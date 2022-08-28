// https://school.programmers.co.kr/learn/courses/30/lessons/72411?language=javascript
combinations = (arr, depth) => {
  if (depth === 1) {
    return arr;
  }

  const t = [];
  for (let i = 0; i < arr.length; i += 1) {
    const res = combinations(arr.slice(i + 1), depth - 1);
    res.forEach((menu) => t.push(arr[i] + menu));
  }
  return t;
};

function solution(orders, course) {
  const answer = [];
  const len_db = {};

  orders.forEach((o) => {
    const menus = o.split("").sort();
    course.forEach((c) => {
      const res = combinations(menus, c);
      res.forEach((combination) => {
        const comb_len = combination.length;
        if (comb_len in len_db && len_db[comb_len].has(combination)) {
          len_db[comb_len].set(
            combination,
            len_db[comb_len].get(combination) + 1
          );
        } else if (comb_len in len_db) {
          len_db[comb_len].set(combination, 1);
        } else {
          len_db[comb_len] = new Map();
          len_db[comb_len].set(combination, 1);
        }
      });
    });
  });

  course.forEach((c) => {
    if (len_db[String(c)]) {
      const len_max = Math.max(...len_db[String(c)].values());

      const filtered = new Map(
        Array.from(len_db[c]).filter(([k, v]) => v === len_max && v > 1)
      );

      filtered.forEach((v, k) => {
        answer.push(k);
      });
    }
  });

  answer.sort();

  return answer;
}
