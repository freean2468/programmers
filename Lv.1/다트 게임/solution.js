// https://school.programmers.co.kr/learn/courses/30/lessons/17682
function solution(dartResult) {
  const scores = new Array(11).map((v, i) => i);
  const bonuses = ["S", "D", "T"];
  const options = ["*", "#"];

  const matched = Array.from(dartResult.matchAll(/\d{0,}\w(\*|\#){0,1}/g)).map(
    (v) => v[0]
  );
  const converted = [];

  matched.forEach((v, i) => {
    const score = v.match(/\d{0,}/)[0];
    const bonus = v.match(/S|D|T/)[0];
    const option = v.match(/\*|\#/) ? v.match(/\*|\#/)[0] : null;
    let p_score = converted[i - 1];
    let final_score = 0;

    switch (bonus) {
      case "S":
        final_score = score;
        break;
      case "D":
        final_score = score ** 2;
        break;
      case "T":
        final_score = score ** 3;
        break;
    }

    switch (option) {
      case "*":
        if (p_score) {
          converted[i - 1] = p_score * 2;
        }
        final_score = final_score * 2;
        break;
      case "#":
        final_score = final_score * -1;
        break;
    }

    converted.push(final_score);
  });

  return converted.reduce((t, cv) => Number(t) + Number(cv));
}
