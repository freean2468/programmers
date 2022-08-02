// https://school.programmers.co.kr/learn/courses/30/lessons/12903
function solution(s) {
  return s.length % 2 === 1
    ? s.substr(~~(s.length / 2), 1)
    : s.substr(~~(s.length / 2) - 1, 2);
}
