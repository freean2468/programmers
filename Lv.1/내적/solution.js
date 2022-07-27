// https://school.programmers.co.kr/learn/courses/30/lessons/70128
function solution(a, b) {
  return a.reduce((p, n, i) => p + n * b[i], 0);
}
