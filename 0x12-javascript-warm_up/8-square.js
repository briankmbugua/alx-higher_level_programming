#!/usr/bin/node
if (process.argv[2] > 0 || isNaN(process.argv[2])) {
  if (process.argv[2] === undefined || isNaN(process.argv[2])) {
    console.log('Missing size');
  } else {
    let square = '';
    for (let i = 0; i < process.argv[2]; i++) {
      for (let j = 0; j < process.argv[2]; j++) {
        square += 'X';
      }
      square += '\n';
    }

    console.log(square);
  }
}
