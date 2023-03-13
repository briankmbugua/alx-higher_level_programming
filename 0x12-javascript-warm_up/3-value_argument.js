#!/usr/bin/node
const { argv } = require('node:process');
if (argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
