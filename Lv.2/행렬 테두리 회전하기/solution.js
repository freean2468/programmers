// https://school.programmers.co.kr/learn/courses/30/lessons/77485?language=javascript
class Queue {
  q = [];
  i = -1;

  push = (n) => {
    this.q.push(n);
    this.i += 1;
  };

  shift = () => {
    const v = this.q[this.i];
    this.i = (this.i + 1) % this.q.length;
    return v;
  };

  mini = () => {
    return Math.min(...this.q);
  };
}

function solution(rows, columns, queries) {
  const lists = [];

  for (let i = 0; i < rows; i += 1) {
    const row = [];
    for (let j = 0; j < columns; j += 1) {
      row.push(j + 1 + i * columns);
    }
    lists.push(row);
  }
  const answer = [];

  queries.forEach((q) => {
    const [y1, x1, y2, x2] = q;
    const queue = new Queue();

    for (let i = x1 - 1; i < x2; i += 1) {
      queue.push(lists[y1 - 1][i]);
    }

    for (let i = y1; i < y2; i += 1) {
      queue.push(lists[i][x2 - 1]);
    }

    for (let i = x2 - 2; i >= x1 - 1; i -= 1) {
      queue.push(lists[y2 - 1][i]);
    }

    for (let i = y2 - 2; i >= y1; i -= 1) {
      queue.push(lists[i][x1 - 1]);
    }

    for (let i = x1 - 1; i < x2; i += 1) {
      lists[y1 - 1][i] = queue.shift();
    }

    for (let i = y1; i < y2; i += 1) {
      lists[i][x2 - 1] = queue.shift();
    }

    for (let i = x2 - 2; i >= x1 - 1; i -= 1) {
      lists[y2 - 1][i] = queue.shift();
    }
    for (let i = y2 - 2; i >= y1; i -= 1) {
      lists[i][x1 - 1] = queue.shift();
    }

    answer.push(queue.mini());
  });

  return answer;
}
