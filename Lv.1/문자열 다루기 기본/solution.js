// https://school.programmers.co.kr/learn/courses/30/lessons/12918
function solution(s) {
  return (s.length === 4 || s.length === 6) && s.match(/[a-z]|[A-Z]/g) === null
    ? true
    : false;
}
