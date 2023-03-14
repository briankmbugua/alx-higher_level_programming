#!/usr/bin/node
function factorial (n) {
  if (n === 0 || n === 1 || isNaN(n)) {
    return 1;
  }

  return n * factorial(n - 1);
}

console.log(factorial(process.argv[2]));
