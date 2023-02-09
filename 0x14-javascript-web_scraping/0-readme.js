#!/usr/bin/node

const arg1 = process.argv[2];

const fs = require('fs');

fs.readFile(arg1, 'utf-8', (err, data) => {
  if (err){
	console.error(err);
  }
  console.log(data);
});

