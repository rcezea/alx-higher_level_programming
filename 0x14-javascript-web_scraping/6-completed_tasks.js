#!/usr/bin/node
const request = require('request');
require('process');
const completedTask = {};
request.get(process.argv[2], (err, resp, body) => {
  if (err) {
    return console.log(err);
  }
  const tasks = JSON.parse(body);
  for (const task of tasks) {
    if (task.userId in completedTask) {
      if (task.completed === true) {
        completedTask[task.userId] += 1;
      }
    } else {
      if (task.completed === true) {
        completedTask[task.userId] = 1;
      }
    }
  }
  console.log(completedTask);
});
