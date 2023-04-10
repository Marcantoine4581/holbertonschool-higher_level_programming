#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const list = process.argv;
  const allNum = list.slice(2, process.argv.lenght);
  const sortedNum = allNum.sort();
  console.log(sortedNum[allNum.length - 2]);
}
