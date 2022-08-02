// https://school.programmers.co.kr/learn/courses/30/lessons/12906
function solution(arr) {
  var answer = [];

  arr.forEach((v, i, a) => {
    if (i === 0) {
      answer.push(v);
    } else if (a[i - 1] !== v) {
      answer.push(v);
    }
  });

  return answer;
}
