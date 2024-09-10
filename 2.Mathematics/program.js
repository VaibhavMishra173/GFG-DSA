
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

/**
 * Calculates the factorial of a given number using recursion.
 * The factorial of a number n is the product of all positive integers less than or equal to n.
 * 
 * @param {number} n - The number whose factorial is to be calculated.
 * @returns {number} The factorial of the given number.
 */
const factorial2 = (n) => {
  if (n === 0 || n === 1) {
    return 1;  // The factorial of 0 or 1 is 1
  } else {
    return n * factorial2(n - 1);  // Recursively calls the function to multiply n by the factorial of (n-1)
  }
}

/**
 * Counts the number of trailing zeros in the factorial of a given number using a naive approach.
 * This approach calculates the factorial first and then counts the number of trailing zeros.
 * 
 * @param {number} n - The number whose factorial's trailing zeros are to be counted.
 * @returns {number} The number of trailing zeros in the factorial of the given number.
 */
const trailingZeroNaive = (n) => {
  let factorial = factorial2(n);  // Calculate the factorial of n
  let count = 0;
  while (factorial % 10 === 0) {  // Check if the last digit is 0
    factorial = Math.floor(factorial / 10);  // Remove the last digit
    count++;  // Increment the trailing zero count
  }
  return count;
}

/**
 * Counts the number of trailing zeros in the factorial of a given number using an efficient approach.
 * This approach avoids calculating the factorial directly and instead counts the factors of 5 in the numbers from 1 to n.
 * 
 * @param {number} n - The number whose factorial's trailing zeros are to be counted.
 * @returns {number} The number of trailing zeros in the factorial of the given number.
 */
const trailingZeroEfficient = (n) => {
  let res = 0;
  for (let i = 5; i <= n; i = i * 5) {  // Iterate over multiples of 5
    res = res + Math.floor(n / i);  // Count how many times 5 is a factor in numbers from 1 to n
  }
  return res;
}

/**
 * Finds the Greatest Common Divisor (GCD) or Highest Common Factor (HCF) of two numbers.
 * The GCD of two numbers is the largest number that divides both of them without leaving a remainder.
 * 
 * @param {number} n1 - The first number.
 * @param {number} n2 - The second number.
 * @returns {number} The GCD or HCF of the two numbers.
 */
const findGreatestCommonDivisorOrHCF = (n1, n2) => {
  let smaller = n1 < n2 ? n1 : n2;  // Determine the smaller of the two numbers
  for (let i = smaller; i > 0; i--) {  // Loop from the smaller number down to 1
    if (n1 % i === 0 && n2 % i === 0) {  // Check if i divides both n1 and n2
      return i;  // Return the greatest common divisor
    }
  }
}

/**
 * Finds the Greatest Common Divisor (GCD) or Highest Common Factor (HCF) of two numbers
 * using the Euclidean algorithm.
 * The Euclidean algorithm works by repeatedly subtracting the smaller number from the larger one
 * until the two numbers become equal. This number is the GCD.
 * 
 * @param {number} n1 - The first number.
 * @param {number} n2 - The second number.
 * @returns {number} The GCD or HCF of the two numbers.
 */
const findGreatestCommonDivisorOrHCFWithEuclideanAlgo = (n1, n2) => {
  while (n1 !== n2) {  // Continue until both numbers are equal
    if (n1 > n2) {
      n1 = n1 - n2;  // Subtract the smaller number from the larger one
    } else {
      n2 = n2 - n1;  // Subtract the smaller number from the larger one
    }
  }
  return n1;  // Return the GCD, which is the value of n1 (or n2) when both are equal
}

/**
 * Finds the Greatest Common Divisor (GCD) or Highest Common Factor (HCF) of two numbers
 * using the optimized Euclidean algorithm with recursion.
 * The Euclidean algorithm works by recursively replacing the larger number with its remainder
 * when divided by the smaller number until the remainder is 0.
 * 
 * @param {number} n1 - The first number.
 * @param {number} n2 - The second number.
 * @returns {number} The GCD or HCF of the two numbers.
 */
const findGreatestCommonDivisorOrHCFWithEuclideanAlgoOptimized = (n1, n2) => {
  if (n2 === 0) {  // Base case: when n2 is 0, n1 is the GCD
    return n1;
  } else {
    return findGreatestCommonDivisorOrHCFWithEuclideanAlgoOptimized(n2, n1 % n2);  // Recursive case
  }
}

/**
 * Finds the Least Common Multiple (LCM) of two numbers using a naive method.
 * The method starts with the maximum of the two numbers and checks each number incrementally
 * to see if it is divisible by both numbers.
 * 
 * @param {number} n1 - The first number.
 * @param {number} n2 - The second number.
 * @returns {number} The LCM of the two numbers.
 */
const findLcmNaive = (n1, n2) => {
  let max = Math.max(n1, n2);  // Start with the maximum of n1 and n2
  while (true) {
    if (max % n1 === 0 && max % n2 === 0) {  // Check if max is divisible by both numbers
      return max;  // Return the LCM when found
    }
    max++;  // Increment max to check the next potential LCM
  }
}

/**
 * Finds the Least Common Multiple (LCM) of two numbers using an optimized method.
 * This method calculates the LCM using the relationship: LCM(a, b) = (a * b) / GCD(a, b).
 * 
 * @param {number} n1 - The first number.
 * @param {number} n2 - The second number.
 * @returns {number} The LCM of the two numbers.
 */
const findLcmOptimized = (n1, n2) => {
  const gcd = findGreatestCommonDivisorOrHCFWithEuclideanAlgoOptimized(n1, n2);  // Find GCD using Euclidean algorithm
  return (n1 * n2) / gcd;  // Calculate and return LCM using the GCD
}

/**
 * Checks if a number is prime using a naive approach.
 * A prime number is a natural number greater than 1 that is not divisible
 * by any number other than 1 and itself.
 * 
 * @param {number} n - The number to check for primality.
 * @returns {boolean} `true` if the number is prime, `false` otherwise.
 */
const isNumberPrimeNaive = (n) => {
  if (n === 1) return false;  // 1 is not considered a prime number
  for (let i = 2; i < n; i++) {  // Check divisibility from 2 to n-1
    if (n % i === 0) return false;  // If divisible, n is not prime
  }
  return true;  // If no divisors are found, n is prime
}

/**
 * Checks if a number is prime using an optimized approach.
 * A prime number is a natural number greater than 1 that is not divisible
 * by any number other than 1 and itself.
 * 
 * This function optimizes the process by only checking for factors up to
 * the square root of the number.
 * 
 * @param {number} n - The number to check for primality.
 * @returns {boolean} `true` if the number is prime, `false` otherwise.
 */
const isNumberPrimeOptimized = (n) => {
  if (n === 1) return false;  // 1 is not a prime number
  for (let i = 2; i * i <= n; i++) {  // Only check divisibility up to √n
    if (n % i === 0) return false;  // If divisible, n is not prime
  }
  return true;  // If no divisors are found, n is prime
}

/**
 * Checks if a number is prime using an even more optimized approach.
 * This function skips checking even numbers and multiples of 3 after handling
 * the smallest prime numbers (2 and 3) separately.
 * 
 * The loop checks potential divisors of the form 6k ± 1 up to the square root of n.
 * 
 * @param {number} n - The number to check for primality.
 * @returns {boolean} `true` if the number is prime, `false` otherwise.
 */
const isNumberPrimeMoreOptimized = (n) => {
  if (n === 1) return false;  // 1 is not prime
  if (n === 2 || n === 3) return true;  // 2 and 3 are prime numbers
  if (n % 2 === 0 || n % 3 === 0) return false;  // Eliminate multiples of 2 and 3

  for (let i = 5; i * i <= n; i += 6) {  // Check divisibility by 6k ± 1
    if (n % i === 0 || n % (i + 2) === 0) return false;
  }
  return true;  // If no divisors are found, n is prime
}

/**
 * Finds and returns all prime factors of a given number n.
 * This is a naive approach that checks every number from 2 to n.
 * 
 * @param {number} n - The number to find prime factors for.
 * @returns {number[]} An array of prime factors of n.
 */
const findPrimeFactorsNaive = (n) => {
  let arr = [];
  
  // Loop through all numbers from 2 to n
  for (let i = 2; i <= n; i++) {
    // Check if i is a divisor of n and if i is prime
    if (n % i === 0 && isNumberPrimeMoreOptimized(i)) {
      arr.push(i);
    }
  }
  
  return arr;
}

console.log(countDigit(1001));  // Output: 4
console.log(palindromeNumber(1001));  // Output: true
console.log(factorial1(5));  // Output: 120
console.log(factorial2(5));  // Output: 120
console.log(trailingZeroNaive(15));  // Output: 3
console.log(trailingZeroEfficient(100));  // Output: 24
console.log(findGreatestCommonDivisorOrHCF(4, 6));  // Output: 2
console.log(findGreatestCommonDivisorOrHCFWithEuclideanAlgo(4, 6));  // Output: 2
console.log(findGreatestCommonDivisorOrHCFWithEuclideanAlgoOptimized(56, 98));  // Output: 14
console.log(findLcmNaive(4, 6));  // Output: 12
console.log(findLcmOptimized(4, 6));  // Output: 12
console.log(isNumberPrimeNaive(71));  // Output: true
console.log(isNumberPrimeOptimized(71));  // Output: true
console.log(isNumberPrimeMoreOptimized(71));  // Output: true
console.log(findPrimeFactorsNaive(12));  // Output: [2, 3]


