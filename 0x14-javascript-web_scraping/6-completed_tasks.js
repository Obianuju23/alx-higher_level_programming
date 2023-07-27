#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, resp, body) => {
  if (!err) {
    const data = JSON.parse(body);
    const total = {};
    data.forEach(todo => {
      if (todo.completed && total[todo.userId] === undefined) {
        total[todo.userId] = 1;
      } else if (todo.completed) {
        total[todo.userId] += 1;
      }
    });
    console.log(total);
  } else {
    console.log(err);
  }
});
