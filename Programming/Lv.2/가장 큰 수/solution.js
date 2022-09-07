// https://school.programmers.co.kr/learn/courses/30/lessons/42746?language=javascript#
function quickSort(arr) {
  if (arr.length <= 1) {
    return arr;
  }

  const pivot = arr[Math.floor(arr.length / 2)].toString();
  const lessers = [];
  const equals = [];
  const greaters = [];

  arr.forEach((s) => {
    const v = s.toString();

    if (v + pivot < pivot + v) {
      greaters.push(v);
    } else if (v + pivot > pivot + v) {
      lessers.push(v);
    } else {
      equals.push(v);
    }
  });

  return [...quickSort(lessers), ...equals, ...quickSort(greaters)];
}

function solution(numbers) {
  // JS에서 int로 표현하는 데에 한계가 있으므로, 이를 유념해야 한다. 무조건 int로 변환하면 오차가 발생한다.
  const answer = quickSort(numbers).join("");
  if (answer.split("").filter((s) => s !== "0").length === 0) {
    return "0";
  } else {
    return answer;
  }
}
