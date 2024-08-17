const number = 5;

let [func1Output, func2Output, func3Output] = [0, 0, 0]

const findSum = (number) => {
  func1Output = func1(number);
  func2Output = func2(number);
  func3Output = func3(number);
}

function func1(number) {
  return (number * (number + 1)) / 2
}

function func2(number) {
  let sum = 0
  for (let i = 1; i <= number; i++) {
    sum += i;
  }
  return sum;
}

function func3(number) {
  let sum = 0;
  for (let i = 1; i <= number; i++) {
    for (let j = 1; j <= i; j++) {
      sum+=j;
    }
  }
  return sum;
}

function func3(number) {
  let sum = 0;
  for (let i = 1; i <= number; i++) {
    for (let j = 1; j <= i; j++) {
      sum ++;
    }
  }
  return sum;
}

findSum(number)

console.log(`func1Output: ${func1Output}, func2Output: ${func2Output}, func3Output: ${func3Output}`)
