#!/usr/bin/node
const input = process.argv[2];
if (isNaN(input) || input === undefined) {
  console.log('Missing size');
} else if (input >= 0) {
  let square = '';
  for (let i = 0; i < process.argv[2]; i++) {
    for (let j = 0; j < process.argv[2]; j++) {
      square += 'X';
    }
    square += '\n';
  }
  console.log(square);
}
