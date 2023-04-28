#!/usr/bin/node
const request = require('request');

const BaseUrl = 'https://swapi-api.hbtn.io/api';
request(BaseUrl + '/films/' + process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
  }
  console.log(JSON.parse(body).title);
});
