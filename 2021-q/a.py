
def solve(nums):
    ans = 0
    for i in range(len(nums)-1):
        j = nums.index(min(nums[i:])) + 1
        ans += j - i
        nums[i:j] = nums[i:j][::-1]
    return ans


TC = int(input())
for tc in range(TC):
    input()
    nums = list(map(int, input().split()))
    ans = solve(nums)
    print("Case #{}: {}".format(tc+1, ans))

