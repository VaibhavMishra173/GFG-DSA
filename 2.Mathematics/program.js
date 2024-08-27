/**
 * Counts the number of digits in a given number.
 * 
 * @param {number} n - The number whose digits are to be counted.
 * @returns {number} The number of digits in the given number.
 */
const countDigit = (n) => {
  let count = 0;
  while (n > 0) {
    n = Math.floor(n / 10);  // Removes the last digit from n
    count++;  // Increments the digit count
  }
  return count;
}

/**
 * Checks if a given number is a palindrome.
 * A palindrome is a number that reads the same backward as forward.
 * 
 * @param {number} n - The number to be checked.
 * @returns {boolean} True if the number is a palindrome, false otherwise.
 */
const palindromeNumber = (n) => {
  let temp = n;
  let revNum = 0;
  while (temp > 0) {
    revNum = revNum * 10 + temp % 10;  // Appends the last digit of temp to revNum
    temp = Math.floor(temp / 10);  // Removes the last digit from temp
  }
  return revNum === n;  // Checks if the reversed number is equal to the original number
}

/**
 * Calculates the factorial of a given number.
 * The factorial of a number n is the product of all positive integers less than or equal to n.
 * 
 * @param {number} n - The number whose factorial is to be calculated.
 * @returns {number} The factorial of the given number.
 */
const factorial1 = (n) => {
  let factorial = 1;
  if (n === 0) {
    return factorial;  // The factorial of 0 is 1
  }
  for (let i = 1; i <= n; i++) {
    factorial = factorial * i;  // Multiplies factorial by each number from 1 to n
  }
  return factorial;
}

console.log(countDigit(1001));  // Output: 4
console.log(palindromeNumber(1001));  // Output: true
console.log(factorial1(5));  // Output: 120
