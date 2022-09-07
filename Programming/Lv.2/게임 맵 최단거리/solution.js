// https://school.programmers.co.kr/learn/courses/30/lessons/1844?language=javascript
function solution(maps) {
  const dfs = (x, y) => {
    const dx = [0, 0, -1, 1];
    const dy = [-1, 1, 0, 0];
    const queue = [[y, x]];

    while (queue.length > 0) {
      const [y, x] = queue.shift();

      for (let i = 0; i < 4; i += 1) {
        const nx = x + dx[i];
        const ny = y + dy[i];

        if (ny < 0 || ny >= maps.length || nx < 0 || nx >= maps[0].length) {
          continue;
        }

        if (maps[ny][nx] === 0) {
          continue;
        }

        if (maps[ny][nx] === 1) {
          maps[ny][nx] = maps[y][x] + 1;
          queue.push([ny, nx]);
        }
      }
    }

    return maps.pop().pop();
  };

  const answer = dfs(0, 0);
  return answer === 1 ? -1 : answer;
}
