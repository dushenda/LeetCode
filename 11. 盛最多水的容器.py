class Solution(object):
    def maxArea(self, height):
        # 暴力法，超出时间限制
        area = 0
        for i in range(0, len(height) - 1):
            max_height_y = 0
            for j in range(len(height) - 1, i, -1):
                if height[j] > max_height_y:
                    max_height_y = height[j]
                    area_tmp = (j - i) * min(height[i], height[j])
                    if area_tmp > area:
                        area = area_tmp
        return area

    def maxArea2(self, height):
        i, j = 0, len(height) - 1
        area = (j - i) * min(height[j], height[i])
        while i < j:
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            tmp_area = (j - i) * min(height[j], height[i])
            if tmp_area > area:
                area = tmp_area
        return area


def main():
    a = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    b1 = [1, 1]
    s = Solution()
    res = s.maxArea2(a)
    print(res)


if __name__ == '__main__':
    main()
