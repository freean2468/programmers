function solution(numbers, target) {
  if (!numbers.length && target === 0) {
    return 1;
  } else if (!numbers.length) {
    return 0;
  } else {
    return (
      solution(numbers.slice(1), target - numbers[0]) +
      solution(numbers.slice(1), target + numbers[0])
    );
  }
}
