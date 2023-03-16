#!/usr/bin/node
exports.esrever = function (list) {
  let count = list.length - 1;
  const arr = [];
  let i = 0;
  for (; list[count]; count--) {
    arr[i] = list[count];
    i++;
  }
  return (arr);
};
