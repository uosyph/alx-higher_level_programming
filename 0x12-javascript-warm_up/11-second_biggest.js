#!/usr/bin/node
let secondMax = 0;
const arr = process.argv.slice(2);
if (arr.length > 1) {
	arr.sort();
	secondMax = arr[arr.length - 2];
}
console.log(secondMax);
