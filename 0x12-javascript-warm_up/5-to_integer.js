#!/usr/bin/node
const { argv } = require('node:process');

if (!Number.isInteger(argv[2])) {
  if (isNaN(parseFloat(argv[2]))) {
    console.log('Not a number');
  } else {
    console.log(`My number: ${parseInt(argv[2])}`);
  }
}
