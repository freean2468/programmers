// https://school.programmers.co.kr/learn/courses/30/lessons/12915
function solution(strings, n) {
  return strings.sort((a, b) => {
    const anth = a.substr(n, 1);
    const bnth = b.substr(n, 1);
    return anth.localeCompare(bnth) !== 0
      ? anth.localeCompare(bnth)
      : a.localeCompare(b);
  });
}
