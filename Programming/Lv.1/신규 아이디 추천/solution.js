// https://school.programmers.co.kr/learn/courses/30/lessons/72410
function solution(new_id) {
  const case_diff = "a".charCodeAt(0) - "A".charCodeAt(0);

  let converted = new_id
    .split("")
    .map((v) => {
      const code = v.charCodeAt(0);

      if (code >= "A".charCodeAt(0) && code <= "Z".charCodeAt(0)) {
        v = String.fromCharCode(code + case_diff);
      }

      return v;
    })
    .join("")
    .replace(/(?!([a-z]|[0-9]|\-|\_|\.))./g, "")
    .replace(/\.{2,}/g, ".")
    .replace(/^\.|\.$/g, "");

  if (converted === "") {
    converted = "a";
  }

  if (converted.length >= 16) {
    converted = converted.split("").splice(0, 15).join("").replace(/\.$/g, "");
  }

  if (converted.length <= 2) {
    const splited = converted.split("");
    const last = splited.pop();

    while (splited.join("").length < 3) {
      splited.push(last);
    }

    converted = splited.join("");
  }

  return converted;
}

// function solution(new_id) {
//     const answer = new_id
//         .toLowerCase() // 1
//         .replace(/[^\w-_.]/g, '') // 2
//         .replace(/\.+/g, '.') // 3
//         .replace(/^\.|\.$/g, '') // 4
//         .replace(/^$/, 'a') // 5
//         .slice(0, 15).replace(/\.$/, ''); // 6
//     const len = answer.length;
//     return len > 2 ? answer : answer + answer.charAt(len - 1).repeat(3 - len);
// }
