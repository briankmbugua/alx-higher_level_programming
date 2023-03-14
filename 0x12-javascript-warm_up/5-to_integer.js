#!/usr/bin/node
if (!Number.isInteger(process.argv[2])) {
  if (isNaN(parseFloat(process.argv[2]))) {
    console.log('Not a number');
  } else {
    console.log(`My number: ${parseInt(process.argv[2])}`);
  }
}
