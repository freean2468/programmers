// https://school.programmers.co.kr/learn/courses/30/lessons/12912
function solution(a, b) {
  const range = [a, b].sort((a, b) => a - b);
  let t = 0;

  for (let i = range[0]; i <= range[1]; i += 1) {
    t += i;
  }

  return t;
}
