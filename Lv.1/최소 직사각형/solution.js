// https://school.programmers.co.kr/learn/courses/30/lessons/86491
function solution(sizes) {
  return sizes
    .map((v) => (v[0] < v[1] ? [v[1], v[0]] : v))
    .reduce(
      (p, cv) => {
        p[0] = p[0] < cv[0] ? cv[0] : p[0];
        p[1] = p[1] < cv[1] ? cv[1] : p[1];
        return p;
      },
      [0, 0]
    )
    .reduce((p, cv) => p * cv, 1);
}
