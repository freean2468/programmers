// https://school.programmers.co.kr/learn/courses/30/lessons/62048?language=javascript
function gcd_two_numbers(x, y) {
  if (typeof x !== "number" || typeof y !== "number") return false;
  x = Math.abs(x);
  y = Math.abs(y);
  while (y) {
    var t = y;
    y = x % y;
    x = t;
  }
  return x;
}

function solution(w, h) {
  return w * h - (w + h - gcd_two_numbers(w, h));
}
