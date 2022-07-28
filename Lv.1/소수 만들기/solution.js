// https://school.programmers.co.kr/learn/courses/30/lessons/12977
function solution(nums) {
  let prime_count = 0;

  for (let i = 0; i < nums.length; i += 1) {
    for (let j = i + 1; j < nums.length; j += 1) {
      for (let k = j + 1; k < nums.length; k += 1) {
        const sum = nums[i] + nums[j] + nums[k];
        const sqrt = ~~Math.sqrt(sum);
        let is_prime = true;
        for (let l = 2; l <= sqrt; l += 1) {
          if (sum % l === 0) {
            is_prime = false;
            break;
          }
        }
        if (is_prime) {
          prime_count += 1;
        }
      }
    }
  }

  return prime_count;
}
