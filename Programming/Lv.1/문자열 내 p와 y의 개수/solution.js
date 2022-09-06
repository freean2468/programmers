// https://school.programmers.co.kr/learn/courses/30/lessons/12916
function solution(s) {
  let count = 0;
  s.toLowerCase()
    .split("")
    .forEach((v) => {
      if (v === "p") count += 1;
      else if (v === "y") count -= 1;
    });

  return count === 0 ? true : false;
}
