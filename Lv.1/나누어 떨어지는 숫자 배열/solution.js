// https://school.programmers.co.kr/learn/courses/30/lessons/12910
function solution(arr, divisor) {
  const answer = arr.filter((v) => v % divisor === 0);
  if (answer.length === 0) {
    answer.push(-1);
  }
  answer.sort((a, b) => a - b);
  return answer;
}
