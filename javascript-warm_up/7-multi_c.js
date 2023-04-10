#!/usr/bin/node

const str = 'C is fun';
const number = parseInt(process.argv[2]);

if (number) {
  for (let i = 0; i < number; i++) {
    console.log(str);
  }
} else {
  console.log('Missing number of occurrences');
}
