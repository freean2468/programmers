// https://school.programmers.co.kr/learn/courses/30/lessons/12901
function solution(a, b) {
  const date = new Date(
    `2016-${String(a).padStart(2, 0)}-${String(b).padStart(2, 0)}`
  );
  const days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];
  return days[date.getDay()];
}
