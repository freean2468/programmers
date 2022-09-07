// https://school.programmers.co.kr/learn/courses/30/lessons/72412

// 내 두 번째 시도
// 정확도는 통과하지만 효율성은 fail.
// function solution(info, query) {
//   const answer = [];
//   const db = [];
//   const columns = ["l", "c", "y", "f", "s"];

//   info.forEach((v) => {
//     const splitted = v.split(" ");
//     const score = parseInt(splitted.pop());
//     const t = {};

//     splitted.forEach((v, i) => {
//       t[columns[i]] = v;
//     });
//     t["s"] = score;

//     db.push(t);
//   });

//   query.forEach((q) => {
//     const splitted = q.split(" ").filter((v) => v !== "and");
//     const score = parseInt(splitted.pop());
//     let searching = Object.assign(db);

//     splitted.forEach((v, i) => {
//       if (v !== "-") {
//         searching = searching.filter((r) => r[columns[i]] === v);
//       }
//     });

//     answer.push(searching.filter((r) => r["s"] >= score).length);
//   });

//   return answer;
// }

// Binary Search -> LowerBound
function lowerBound(arr, target) {
  let low = 0;
  let high = arr.length;

  if (arr[high - 1] < target) {
    return -1;
  }

  while (low < high) {
    const mid = Math.floor((low + high) / 2);

    if (target <= arr[mid]) {
      high = mid;
    } else {
      low = mid + 1;
    }
  }
  return low;
}

function solution(info, query) {
  const answer = [];
  const db = {};

  info.forEach((v) => {
    const splitted = v.split(" ");
    const score = parseInt(splitted.pop());
    const l = [splitted[0], "-"];
    const c = [splitted[1], "-"];
    const y = [splitted[2], "-"];
    const f = [splitted[3], "-"];

    // 모든 경우의 수로 검색 키를 미리 만들어 둔다는 게 무식한 방법이라고 생각했는데 이게 정답이라니.
    for (let i = 0; i < 2; i += 1) {
      for (let j = 0; j < 2; j += 1) {
        for (let k = 0; k < 2; k += 1) {
          for (let m = 0; m < 2; m += 1) {
            const key = l[i] + c[j] + y[k] + f[m];
            if (db[key] === undefined) {
              db[key] = [score];
            } else {
              db[key].push(score);
            }
          }
        }
      }
    }
  });

  // 마지막에 점수들을 오름차순 정렬
  for (const k in db) {
    db[k].sort((a, b) => a - b);
  }

  query.forEach((v) => {
    const splitted = v.split(" ").filter((v) => v !== "and");
    const score = parseInt(splitted.pop());
    const key = splitted.join("");
    try {
      const index = lowerBound(db[key], score);
      if (index === -1) {
        answer.push(0);
      } else {
        answer.push(db[key].length - index);
      }
    } catch {
      answer.push(0);
    }
  });

  return answer;
}
