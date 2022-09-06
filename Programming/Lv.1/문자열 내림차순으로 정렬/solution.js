// https://school.programmers.co.kr/learn/courses/30/lessons/12917
function solution(s) {
  return s
    .split("")
    .sort((a, b) => {
      const ac =
        a.charCodeAt(0) - ("A".charCodeAt(0) >= a.charCodeAt(0) ? 50 : 0);
      const bc =
        b.charCodeAt(0) - ("A".charCodeAt(0) >= b.charCodeAt(0) ? 50 : 0);
      return bc - ac;
    })
    .join("");
}
