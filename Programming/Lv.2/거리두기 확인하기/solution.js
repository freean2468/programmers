let p = null;

const dfs = (d, ori, oci, ri, ci) => {
  const rooms = [
    [ri, ci - 1],
    [ri, ci + 1],
    [ri + 1, ci],
    [ri - 1, ci],
  ].filter((v) => v[0] > -1 && v[1] > -1 && !(v[0] === ori && v[1] === oci));
  const answer = [];

  rooms.forEach((r) => {
    try {
      const rv = p[r[0]][r[1]];

      if (rv === "P") {
        return 0;
      }
      if (d === 1 && rv === "O") {
        answer.push(dfs(d + 1, ori, oci, r[0], r[1]));
      }
    } catch (e) {}
  });

  if (d === 2) {
    return 1;
  } else {
    if (0 in answer) {
      return 0;
    } else {
      return 1;
    }
  }
};

const loop_c = (ri, rv) => {
  for (let i = 0; i < rv.length; i += 1) {
    if (rv[i] === "P" && dfs(1, ri, i, ri, i) === 0) {
      return 0;
    }
  }

  return 1;
};

const loop_r = (e) => {
  for (let i = 0; i < e.length; i += 1) {
    if (loop_c(i, e[i]) === 0) {
      return 0;
    }
  }
  return 1;
};

function solution(places) {
  p = places;
  const answer = [];

  places.forEach((e) => {
    p = e;
    answer.push(loop_r(p));
  });

  return answer;
}
