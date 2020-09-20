# include<iostream>
# include<string>
# include<vector>
# include<algorithm>
# include<stdio.h>
using
namespace
std;

int
main()
{
    string
frame, brick;
cin >> frame >> brick;
int
lenF = frame.length(), lenB = brick.length();

int
add0 = lenF - lenB;
int
res = 9999999;
for (int i = add0; i >= 0; i--) // 从第一个字符对齐开始，每次向后移动一位，进行错位相加
{
    string
temp = brick;
vector < int > arr(lenF, 0);
for (int j = 0; j < i; j++) // 对落下的方块后进行补0，方便相加
temp += "0";
for (int k = lenF - 1; k >= 0; k--) // 对应位置的数相加，保存在数组中
{
    arr[k] += frame[k] - '0';
if (k - (add0 - i) >= 0)
arr[k] += temp[k - (add0 - i)] - '0';
}
int
maxtemp = -9999999, mintemp = 9999999, maxH = -9999999;
for (int i = 0; i < arr.size();
i + +) // 求每次错位相加消除后，剩下的最高的一列的高度
{
    maxtemp = max(maxtemp, arr[i]);
mintemp = min(mintemp, arr[i]);
maxH = max(maxH, maxtemp - mintemp);
}
res = min(res, maxH); // 求每次错位相加的情况中的最小高度

}
cout << res << endl;

system("pause");
return 0;
}