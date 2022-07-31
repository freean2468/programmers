// https://school.programmers.co.kr/learn/courses/30/lessons/77884
function solution(left, right) {
  var answer = 0;

  for (let i = left; i <= right; i += 1) {
    const divisors = [];
    for (let j = 1; j <= i / 2; j += 1) {
      if (i % j === 0) {
        divisors.push(j);
      }
    }
    divisors.push(i);
    answer += divisors.length % 2 === 0 ? i : -i;
  }

  return answer;
}
