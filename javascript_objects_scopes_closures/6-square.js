#!/usr/bin/node

const Rectangle = require('./5-square');

class Square extends Rectangle {
  charPrint (c = 'X') {
    super.print(c);
  }
}

module.exports = Square;
