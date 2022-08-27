const c = ["1", "2", "4"];

const ex = (n) => {
  const three_count = Math.floor((n - 1) / 3);
  const index = (n % 3) - 1 >= 0 ? (n % 3) - 1 : 2;

  if (three_count === 0) {
    return n % 3 === 0 ? c[2] : c[index];
  } else {
    return ex(three_count) + c[index];
  }
};

function solution(n) {
  return ex(n);
}
