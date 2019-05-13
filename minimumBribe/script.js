'use strict';

// Messages
const MESSAGE = {
  ERROR: 'Too Chaotic!',
};

// Complete the minimumBribes function below.
function minimumBribes(q) {
  let n = q.length;
  let cnt = 0;

  for (let i = n - 1; i >= 0; i--) {
    if (q[i] !== i + 1) {
      if (q[i - 1] >= 0 && q[i - 1] === i + 1) {
        cnt++;
        q[i - 1] = q[i];
        q[i] = i + 1;
      } else if (q[i - 2] >= 0 && q[i - 2] === i + 1) {
        cnt += 2;
        q[i - 2] = q[i - 1];
        q[i - 1] = q[i];
        q[i] = i + 1;
      } else {
        console.log(MESSAGE.ERROR);
        return;
      }
    }
  }

  console.log(cnt);
  return;
}

minimumBribes('2 1 5 3 4');
