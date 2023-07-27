#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];

request(URL, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const dict = {};
    const tasks = JSON.parse(body);
    tasks.forEach((task) => {
      if (task.completed && dict[task.userId] === undefined) {
        dict[task.userId] = 1;
      } else if (task.completed) {
        dict[task.userId]++;
      }
    });
    console.log(dict);
  }
});
