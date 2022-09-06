function solution(progresses, speeds) {
  const answer = [];

  while (progresses.length > 0) {
    let done = 0;

    while (progresses.length > 0 && progresses[0] >= 100) {
      progresses = progresses.slice(1);
      speeds = speeds.slice(1);
      done += 1;
    }

    if (done > 0) {
      answer.push(done);
    }

    let t = [];
    for (let i = 0; i < progresses.length; i += 1) {
      t.push(progresses[i] + speeds[i]);
    }
    progresses = t;
  }

  return answer;
}
