// https://school.programmers.co.kr/learn/courses/30/lessons/42840

Array.prototype.max = function () {
  return Math.max.apply(null, this);
};

function solution(answers) {
  const corrects = [0, 0, 0];
  const actions = [
    [1, 2, 3, 4, 5],
    [2, 1, 2, 3, 2, 4, 2, 5],
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
  ];
  const answer = [];

  answers.forEach((answer, i) => {
    actions.forEach((action, j) => {
      if (answer === action[i % action.length]) {
        corrects[j] += 1;
      }
    });
  });
  const max_corrects = corrects.max();

  corrects.forEach((v, i) => {
    if (v === max_corrects) {
      answer.push(i + 1);
    }
  });

  return answer;
}
