# LeeCode刷题
## 几数之和
题目1、15、18、454
### 两数之和
这个比较简单，只需要做一次hash即可，具体体现为设置成`key-value`存储模式即可。
### 三数之和
[双指针](https://leetcode-cn.com/problems/3sum/solution/hua-jie-suan-fa-15-san-shu-zhi-he-by-guanpengchn/) 解法

![双指针解法](https://pic.leetcode-cn.com/2124b524439bcf0eb159ba43be4420c76f60ff2b3b51f87de269c001a323ea1a-Video_2019-06-19_192352.gif)
### 四数之和
这是三数之和的翻版，多一层循环
### 四数相加
这是两数之和的翻版，分别两两做相加得到新的数组，再使用`collections.count()`转化为字典，对两字典使用两数之和的方法遍历。
## 字符串
### 子串
题目3

使用滑动窗口

### Review

p206递归、p1177dp、dfs39、原地哈希（自建哈希函数）p41

### 直接copy
p785