#!/usr/bin/node

const factorial = (n) => {
  if (isNaN(n) || n < 0) {
    return 1;
  }

  return n === 0 ? 1 : n * factorial(n - 1);
};

const num = parseInt(process.argv[2]);

console.log(factorial(num));
