// https://school.programmers.co.kr/learn/courses/30/lessons/64061
function solution(board, moves) {
  let removed_count = 0;
  const v_board = new Array(board.length);
  const basket = [];

  for (let i = 0; i < v_board.length; i += 1) {
    v_board[i] = new Array();
  }

  const board_reverse = board.reverse();

  for (let i = 0; i < board_reverse.length; i += 1) {
    for (let j = 0; j < board_reverse[i].length; j += 1) {
      if (board_reverse[j][i] !== 0) {
        v_board[i].push(board_reverse[j][i]);
      }
    }
  }

  moves.forEach((v) => {
    const picked_up = v_board[v - 1].pop();
    if (picked_up) {
      basket.push(picked_up);

      const l = basket.length;
      if (l >= 2 && basket[l - 2] === basket[l - 1]) {
        basket.pop();
        basket.pop();
        removed_count += 2;
      }
    }
  });

  return removed_count;
}
