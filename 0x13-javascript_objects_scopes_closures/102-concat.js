#!/usr/bin/node
const fs = require('fs');
const nArg = process.argv;
const fArg = fs.readFileSync(nArg[2]).toString();
const sArg = fs.readFileSync(nArg[3]).toString();
fs.writeFileSync(nArg[4], fArg + sArg);
