#!/usr/bin/node

const URL = process.argv[2];
const request = require('request');
let count = 0;
request(`${URL}`, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const arrayOfObjects = JSON.parse(body).results;
  for (const object of arrayOfObjects) {
    const characters = object.characters;
    for (let i = 0; i < characters.length; i++) {
      if (characters[i] === 'https://swapi-api.alx-tools.com/api/people/18/') {
        count += 1;
      }
    }
  }
  console.log(count);
});
