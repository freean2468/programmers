// https://school.programmers.co.kr/learn/courses/30/lessons/42889#
function solution(N, stages) {
  const stages_sorted = stages.sort((a, b) => a - b);
  return stages_sorted
    .reduce((t, cv, ci, a) => {
      if (cv < N + 1) {
        t[cv - 1] += 1;
      }

      return t;
    }, new Array(N).fill(0))
    .slice(0, N)
    .map((v, i) => [
      i + 1,
      v / (stages.length - stages_sorted.filter((sv) => sv < i + 1).length),
    ])
    .sort((a, b) => b[1] - a[1])
    .map((v) => v[0]);
}
