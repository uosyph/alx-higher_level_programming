#!/usr/bin/node
(function add (a, b) {
  a = Number(process.argv[2]);
  b = Number(process.argv[3]);
  if (isNaN(a) || isNaN(b) || process.argv.length < 3) {
    console.log(NaN);
  } else {
    console.log(a + b);
  }
})();
