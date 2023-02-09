#!/usr/bin/node

const URL = process.argv[2];
const path = process.argv[3];
const request = require('request');
const fs = require('fs');

request(`${URL}`, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const content = body;
  fs.writeFile(`${path}`, content, 'utf-8', (error) => {
    if (error) {
      console.error(error);
    }
  });
});
