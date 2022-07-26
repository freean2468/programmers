// https://school.programmers.co.kr/learn/courses/30/lessons/77484
function solution(lottos, win_nums) {
  const zero_count = lottos.filter((v) => v === 0).length;
  const rest = lottos.filter((v) => v !== 0);
  const hit_count = win_nums
    .map((v, i) => {
      let hit = false;
      for (let j = 0; j < rest.length; j += 1) {
        if (rest[j] === v) {
          hit = true;
          break;
        }
      }

      return hit ? 1 : -1;
    })
    .filter((v) => v === 1).length;

  const max = hit_count + zero_count;
  const min = hit_count;

  return [Math.min(6 - max + 1, 6), Math.min(6 - min + 1, 6)];
}
