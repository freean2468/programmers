// https://school.programmers.co.kr/learn/courses/30/lessons/60058?language=javascript
class Stack {
  s = [];

  push = (b) => {
    this.s.push(b);
    const s_len = this.s.length;
    if (s_len > 1 && this.s[s_len - 1] === ")" && this.s[s_len - 2] === "(") {
      this.s.pop();
      this.s.pop();
    }
  };

  is_empty = () => {
    return this.s.length ? false : true;
  };
}

function solution(p) {
  if (p === "") {
    return "";
  }

  let [oc, cc, u, v] = [0, 0, "", ""];

  for (let i = 0; i < p.length; i += 1) {
    if (p[i] === "(") {
      oc += 1;
    } else if (p[i] == ")") {
      cc += 1;
    }

    if (oc === cc) {
      u = p.slice(0, i + 1);
      v = p.slice(i + 1);
      break;
    }
  }

  const stack = new Stack();
  [...u].forEach((e) => {
    stack.push(e);
  });

  if (stack.is_empty()) {
    return u + solution(v);
  } else {
    const e = "(" + solution(v) + ")";

    if (u.length) {
      u = [...u.slice(1, u.length - 1)];
    } else {
      u = [];
    }

    for (let i = 0; i < u.length; i += 1) {
      if (u[i] === ")") {
        u[i] = "(";
      } else if (u[i] === "(") {
        u[i] = ")";
      }
    }

    return e + u.join("");
  }
}
