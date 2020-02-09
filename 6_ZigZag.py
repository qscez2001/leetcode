s = "PAYPALISHIRING"

# others solution, i didn't solve this.
def convert(s: str, numRows: int):
    ans = ""
    if numRows == 1:
        return s
    rows = [""] * min(numRows, len(s))
    curRow = 0
    goingDown = False

    for c in s:
        rows[curRow] = rows[curRow] + c
        if curRow == 0 or curRow == numRows - 1:
            goingDown = not goingDown
        curRow = curRow + 1 if goingDown else curRow - 1
    for i in rows:
        # print(i)
        ans = ans + i

    return ans

print(convert(s, 3))

"""
class Solution {
public:
    string convert(string s, int numRows) {

        if (numRows == 1) return s;

        vector<string> rows(min(numRows, int(s.size())));
        int curRow = 0;
        bool goingDown = false;

        for (char c : s) {
            rows[curRow] += c;
            if (curRow == 0 || curRow == numRows - 1) goingDown = !goingDown;
            curRow += goingDown ? 1 : -1;
        }

        string ret;
        for (string row : rows) ret += row;
        return ret;
    }
};
"""