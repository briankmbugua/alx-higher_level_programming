#!/usr/bin/node

exports.esrever = function (list) {
  const myArray = [];
  for (let i = (list.length - 1); i >= 0; i--) {
    myArray.push(list[i]);
  }
  return myArray;
};
