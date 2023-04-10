#!/usr/bin/node

const number = parseInt(process.argv[2]);

if (number) {
  for (let i = 0; i < number; i++) {
    let str = '';
    for (let i = 0; i < number; i++) {
      str += 'X';
    }
    console.log(str);
  }
} else {
  console.log('Missing number of occurrences');
}
