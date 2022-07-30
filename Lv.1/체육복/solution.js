// https://school.programmers.co.kr/learn/courses/30/lessons/42862#
function solution(n, lost, reserve) {
  const intersection = lost.filter((v) => reserve.indexOf(v) >= 0);
  lost = lost.filter((v) => intersection.indexOf(v) === -1);
  reserve = reserve.filter((v) => intersection.indexOf(v) === -1);

  for (let i = 0; i < n; i += 1) {
    const student = i + 1;
    const l_student = lost.indexOf(student);

    if (l_student >= 0) {
      const p_student = reserve.indexOf(student - 1);
      const n_student = reserve.indexOf(student + 1);

      if (p_student >= 0 && n_student >= 0) {
        continue;
      }

      if (p_student >= 0) {
        lost.splice(l_student, 1);
        reserve.splice(p_student, 1);
        continue;
      }

      if (n_student >= 0) {
        lost.splice(l_student, 1);
        reserve.splice(n_student, 1);
        continue;
      }
    }
  }

  for (let i = 0; i < reserve.length; i += 1) {
    const r = reserve[i];

    for (let j = 0; j < lost.length; j += 1) {
      const l = lost[j];

      if (l === r - 1) {
        reserve.splice(i, 1);
        lost.splice(j, 1);
      } else if (l === r + 1) {
        reserve.splice(i, 1);
        lost.splice(j, 1);
      }
    }
  }

  return n - lost.length;
}
