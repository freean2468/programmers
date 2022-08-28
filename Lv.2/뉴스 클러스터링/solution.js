// https://school.programmers.co.kr/learn/courses/30/lessons/17677?language=javascript

pairwise = (l) => {
  const nl = [];
  for (let i = 0; i < l.length; i += 1) {
    if (i < l.length - 1) {
      const p = l[i] + l[i + 1];
      const m = Array.from(p.matchAll("^[a-z][a-z]$"));
      if (m.length) {
        nl.push(p);
      }
    }
  }
  return nl;
};

intersection = (l1, l2) => {
  const nl = [];
  const s = new Set(l1.concat(l2));

  s.forEach((v) => {
    for (
      let i = 0;
      i <
      Math.min(
        l1.filter((ch) => v === ch).length,
        l2.filter((ch) => v === ch).length
      );
      i += 1
    ) {
      nl.push(v);
    }
  });

  return nl;
};

union = (l1, l2) => {
  const nl = [];
  const s = new Set(l1.concat(l2));

  s.forEach((v) => {
    for (
      let i = 0;
      i <
      Math.max(
        l1.filter((ch) => v === ch).length,
        l2.filter((ch) => v === ch).length
      );
      i += 1
    ) {
      nl.push(v);
    }
  });

  return nl;
};

function solution(str1, str2) {
  str1 = str1.toLowerCase();
  str2 = str2.toLowerCase();

  if (str1 === str2) {
    return 65536;
  }

  const comb1 = pairwise(str1);
  const comb2 = pairwise(str2);
  const inter = intersection(comb1, comb2);
  const uni = union(comb1, comb2);

  if (!inter.length && !uni.length) {
    return 1;
  } else {
    return Math.floor(65536 * (inter.length / uni.length));
  }
}
