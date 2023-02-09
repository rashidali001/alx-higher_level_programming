#!/usr/bin/node

const id = process.argv[2];
const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${id}`, function (error, response, body) {
  console.error(error);
  console.log(JSON.parse(body).title);
});
