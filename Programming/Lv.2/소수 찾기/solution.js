// https://school.programmers.co.kr/learn/courses/30/lessons/42839?language=javascript
function permu(str) {
  if (str.length === 1) {
    return str;
  }

  const agg = [];

  [...str].forEach((v, i) => {
    agg.push(v);
    [...permu(str.slice(0, i).concat(str.slice(i + 1)))].forEach((v2, j) => {
      agg.push(v + v2);
    });
  });

  return agg;
}

function solution(numbers) {
  let answer = 0;
  const cases = new Set([...permu(numbers)].map((v) => parseInt(v)));

  cases.forEach((c) => {
    c = parseInt(c);
    let flag = false;
    for (let i = 2; i < Math.floor(c / 2) + 1; i += 1) {
      if (c % i === 0) {
        flag = true;
        break;
      }
    }

    if (c >= 2 && flag === false) {
      answer += 1;
    }
  });

  return answer;
}
