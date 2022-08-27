class Stack {
  s = [];
  i = -1;

  push = (e) => {
    this.s.push(e);
    this.i += 1;

    while (true) {
      if (this.i >= 1 && this.s[this.i] == this.s[this.i - 1]) {
        this.s.pop();
        this.s.pop();
        this.i -= 2;
      } else {
        break;
      }
    }
  };

  index = () => this.i;
}

function solution(s) {
  const stack = new Stack();

  [...s].forEach((e) => {
    stack.push(e);
  });

  if (stack.index() == -1) {
    return 1;
  } else {
    return 0;
  }
}
