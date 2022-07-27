// https://school.programmers.co.kr/learn/courses/30/lessons/76501
function solution(absolutes, signs) {
  return absolutes
    .map((v, i) => v * (signs[i] ? 1 : -1))
    .reduce((p, n) => p + n, 0);
}
