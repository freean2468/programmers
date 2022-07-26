// https://school.programmers.co.kr/learn/courses/30/lessons/92334

function solution(id_list, report, k) {
  const reported_counts = new Array(id_list.length).fill(0);
  const who_to_whom = new Array(id_list.length);
  for (let i = 0; i < who_to_whom.length; i += 1) {
    who_to_whom[i] = new Set();
  }
  const report_set = new Set(report);

  report_set.forEach((e) => {
    const [reporter, reported] = e.split(" ");
    const reporter_id_index = id_list.indexOf(reporter);
    const reported_id_index = id_list.indexOf(reported);
    reported_counts[reported_id_index] += 1;
    who_to_whom[reporter_id_index].add(reported_id_index);
  });

  return id_list.map((v, i) => {
    let answer = 0;

    who_to_whom[i].forEach((reported_id_index) => {
      if (reported_counts[reported_id_index] >= k) {
        answer += 1;
      }
    });

    return answer;
  });
}
