#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];
  for (let count = list.length - 1; count >= 0; count--) {
    reversedList.push(list[count]);
  }
  return reversedList;
};
