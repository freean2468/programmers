// https://school.programmers.co.kr/learn/courses/30/lessons/86051
function solution(numbers) {
  const list = [];
  for (let i = 0; i <= 9; i += 1) list.push(i);
  return list
    .map((v) => (numbers.indexOf(v) === -1 ? v : 0))
    .reduce((prev, next) => prev + next, 0);
}
