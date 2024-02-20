#!/usr/bin/node
const fs = require('fs');

const text = process.argv[3];
fs.writeFile(process.argv[2], text, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
