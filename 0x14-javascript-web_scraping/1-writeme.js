#!/usr/bin/node

const path = process.argv[2];
const insert = process.argv[3];
const fs = require('fs');

fs.writeFile(`${path}`, `${insert}`, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
