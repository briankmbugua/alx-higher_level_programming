#!/usr/bin/node
'use strict';

const add = function addTwoNumbersFromArgv (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return NaN;
  }
  return parseInt(a) + parseInt(b);
};
console.log(add(process.argv[2], process.argv[3]));
