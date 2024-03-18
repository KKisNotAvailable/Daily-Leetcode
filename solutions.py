class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort()

        res = len(points)
        prev = points[0]

        for i in range(1, len(points)):
            cur = points[i]

            if cur[0] <= prev[1]:
                res -= 1
                prev = [cur[0], min(cur[1], prev[1])]
            else:
                prev = cur

        return res


def main():
    sol = Solution()
    m1 = [[10,16],[2,8],[1,6],[7,12]]

    q452 = sol.findMinArrowShots(m1)
    print(q452)



if __name__ == "__main__":
    main()