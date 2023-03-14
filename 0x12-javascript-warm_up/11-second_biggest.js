#!/usr/bin/node
const newArray = [];
if (process.argv[2] === undefined || process.argv[3] === undefined) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    newArray.push(Number(process.argv[i]));
  }
  newArray.sort((a, b) => a - b);
  console.log(newArray[newArray.length - 2]);
}
