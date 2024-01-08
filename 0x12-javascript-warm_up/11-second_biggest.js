#!/usr/bin/node

const numbers = process.argv.slice(2).map(Number).filter(num => !isNaN(num));

if (numbers.length === 0 || numbers.length === 1) {
  console.log(0);
} else {
  const sortedNumbers = numbers.sort((a, b) => b - a);

  console.log(sortedNumbers[1]);
}
