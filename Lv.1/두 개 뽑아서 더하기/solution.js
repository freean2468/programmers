// https://school.programmers.co.kr/learn/courses/30/lessons/68644
function solution(numbers) {
  return Array.from(
    numbers.reduce((p, cv, ci, a) => {
      a.slice(ci + 1)
        .map((v) => cv + v)
        .forEach((v) => p.add(v));
      return p;
    }, new Set())
  ).sort((a, b) => a - b);
}
