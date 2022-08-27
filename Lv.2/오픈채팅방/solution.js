function solution(record) {
  const answer = [];
  const db = {};

  record.forEach((element) => {
    split = element.split(" ");
    if (split[0] !== "Leave") {
      db[split[1]] = split[2];
    }
  });

  reccord.forEach((element) => {
    split = element.split(" ");

    if (split[0] === "Enter") {
      answer.push(`${db[split[1]]}님이 들어왔습니다.`);
    } else if (split[0] == "Leave") {
      answer.push(`${db[split[1]]}님이 나갔습니다.`);
    }
  });

  return answer;
}
