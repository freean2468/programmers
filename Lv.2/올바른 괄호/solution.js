// https://school.programmers.co.kr/learn/courses/30/lessons/12909?language=javascript
class Stack {
  s = [];
  Stack() {}

  push = (item) => {
    if (this.s.length && item === ")" && this.s[this.s.length - 1] == "(") {
      this.s.pop();
    } else {
      this.s.push(item);
    }
  };

  is_empty = () => {
    return this.s.length ? false : true;
  };
}

function solution(s) {
  const stack = new Stack();

  [...s].forEach((element) => {
    stack.push(element);
  });

  return stack.is_empty();
}
