// https://school.programmers.co.kr/learn/courses/30/lessons/12982#
function solution(d, budget) {
  d.sort((a, b) => a - b);
  let candidate = [];

  for (let i = 0; i < d.length; i += 1) {
    for (let j = i + 1; j <= d.length; j += 1) {
      const start = d.slice(i, j);
      for (let k = j; k < d.length; k += 1) {
        for (let l = 1; k + l <= d.length; l += 1) {
          const chunk = d.slice(k, k + l);
          const t =
            start.reduce((p, c) => p + c) + chunk.reduce((p, c) => p + c);
          const predicate = start.concat(chunk);
          if (t <= budget && predicate.length > candidate.length) {
            candidate = predicate;
          }
        }
      }
      const t = start.reduce((p, c) => p + c);
      if (t <= budget && start.length > candidate.length) {
        candidate = start;
      }
    }
  }

  return candidate.length;
}
