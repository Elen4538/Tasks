# O(n^2)
# two pointers

def triplets(nums):
    size = len(nums)
    nums = sorted(nums)
    res = set()

    for i in range(0,size):
        elem = -nums[i]
        l = i + 1
        r = size - 1

        while l < r:
            two_sum = nums[l] + nums[r]

            if two_sum < elem:
                l +=1
            elif two_sum > elem:
                r -=1
            else:
                res.add((nums[i], nums[l], nums[r]))
                l+=1
                r-=1

    return res

print(triplets([0,0,0,0]))
print(triplets([3,0,-2,-1,1,2]))


# 2 variant best

def threesum(nums):
    res = []
    nums.sort()
    ls = len(nums)
    for i in range(ls - 2):
        if i > 0 and nums[i] == nums[i - 1]: # skip the same nums
            continue
        l = i + 1
        r = ls - 1
        while l < r:
            curr = nums[i] + nums[l] + nums[r]
            if curr == 0:
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1 # сдвигаем левый указатель если цифры одинаковые
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1 # сдвигаем правый указатель если цифры одинаковые
                l += 1 # двигаемся по массиву
                r -= 1
            elif curr < 0:
                l += 1
            else:
                r -= 1
    return res
