#!/usr/bin/node

const request = require('request');

let data;
const dataDict = {};
const api = process.argv.slice(2)[0];
request(api, function (err, res, body) {
  if (err) console.error(err);
  else {
    data = JSON.parse(body);
    for (const id in data) {
      if (data[id].completed === true) {
        if (!(data[id].userId in dataDict)) dataDict[data[id].userId] = 1; else dataDict[data[id].userId] += 1;
      }
    }
    console.log(dataDict);
  }
});
