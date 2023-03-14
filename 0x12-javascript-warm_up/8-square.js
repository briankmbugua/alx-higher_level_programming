#!/usr/bin/node
const input = Math.floor(process.argv[2]);
if (isNaN(input) || input === undefined) {
  console.log('Missing size');
} else if (input >= 0) {
  for (let r = 0; r < input; r++) {
    let row = '';
    for (let c = 0; c < input; c++) row += 'X';
    console.log(row);
  }
}
