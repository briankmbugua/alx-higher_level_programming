#!/usr/bin/node
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return console.log(NaN);
  }
  console.log(parseInt(a) + parseInt(b));
}
add(process.argv[2], process.argv[3]);
