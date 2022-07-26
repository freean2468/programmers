// https://school.programmers.co.kr/learn/courses/30/lessons/67256
function solution(numbers, hand) {
  const left = [1, 4, 7, "*"];
  const middle = [2, 5, 8, 0];
  const right = [3, 6, 9, "#"];
  let l = [0, 3];
  let r = [2, 3];

  return numbers
    .map((v, i) => {
      const l_index = left.indexOf(v);
      const r_index = right.indexOf(v);

      if (l_index >= 0) {
        l = [0, l_index];
        return "L";
      } else if (r_index >= 0) {
        r = [2, r_index];
        return "R";
      } else {
        const m_index = middle.indexOf(v);
        let l_dis = 0;
        let r_dis = 0;

        if ((l[0] === 0 && r[0] === 2) || (l[0] === 1 && r[0] === 1)) {
          l_dis = Math.abs(l[1] - m_index);
          r_dis = Math.abs(r[1] - m_index);
        } else if (l[0] === 1) {
          l_dis = Math.abs(l[1] - m_index);
          r_dis = Math.abs(r[1] - m_index) + 1;
        } else {
          l_dis = Math.abs(l[1] - m_index) + 1;
          r_dis = Math.abs(r[1] - m_index);
        }

        if (l_dis < r_dis) {
          l = [1, m_index];
          return "L";
        } else if (r_dis < l_dis) {
          r = [1, m_index];
          return "R";
        } else {
          if (hand === "left") {
            l = [1, m_index];
            return "L";
          } else {
            r = [1, m_index];
            return "R";
          }
        }
      }
    })
    .join("");
}
