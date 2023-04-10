#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0)
} else {
  const list = process.argv;
  const all_num = list.slice(2, process.argv.lenght);
  const sorted_num = all_num.sort();
  console.log(sorted_num[all_num.length - 2]);
}
