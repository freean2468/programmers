// https://school.programmers.co.kr/learn/courses/30/lessons/17681
function solution(n, arr1, arr2) {
  return arr1
    .map((v, i) => v | arr2[i])
    .map((v) => {
      const b = String(v.toString(2)).padStart(n, "0").split("");
      const temp = [];
      for (let i = 0; i < n; i += 1) {
        temp.push(b[i] === "1" ? "#" : " ");
      }
      return temp.join("");
    });
}
