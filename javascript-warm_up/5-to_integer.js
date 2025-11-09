#!/usr/bin/node
const arg = process.argv[2];
const intVal = parseInt(arg);

if (isNaN(intVal)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${intVal}`);
}