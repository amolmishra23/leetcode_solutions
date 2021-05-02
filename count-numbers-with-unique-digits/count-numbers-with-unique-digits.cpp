/*
Say we have an i-bit-number, the MSB is not 0.

For the MSB, we can put 1 ~ 9, that is 9 options.

And for the second MSB, we can put 0 ~ 9 exclude the digit we already used for the MSB, so that should be 9 options.

Then, the third MSB, put 0 ~ 9 exclude the digits we used for the left two bits. That's 8 options.

...

Totally, we have 9 * 9 * 8 * 7 * ... till the LSB.
*/
class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        int res = 0;
        for (int i=n; i>=1; i--) {
            int part = 9;
            for (int j=0; j<i-1; j++) {
                part *= 9-j;
            }
            res += part;
        }
        return res+1;
    }
};