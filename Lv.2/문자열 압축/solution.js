// # https://school.programmers.co.kr/learn/courses/30/lessons/60057
function solution(s) {
  const answer = [];

  for (let step = 1; step <= s.length / 2; step += 1) {
    const compressed = [];
    let count = 0;
    let prev_chunk = null;
    let chunk = null;

    for (let i = 0; i < s.length + 1; i += step) {
      chunk = s.slice(i, i + step);

      if (prev_chunk !== null && prev_chunk !== chunk) {
        if (count == 1) {
          compressed.push(prev_chunk);
        } else {
          compressed.push(`${count}${prev_chunk}`);
        }
        count = 0;
      }
      count += 1;

      prev_chunk = chunk;
    }

    if (chunk.length !== step && prev_chunk !== ``) {
      compressed.push(prev_chunk);
    }
    answer.push(compressed.join("").length);
  }

  return s.length > 1 ? Math.min(...answer) : 1;
}
