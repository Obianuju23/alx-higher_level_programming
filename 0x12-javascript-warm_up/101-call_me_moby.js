#!/usr/bin/node

let count = 0;
function callMeMoby (x, theFunction) {
  while (count < x) {
    theFunction();
    count++;
  }
}
module.exports = {
  callMeMoby
};
