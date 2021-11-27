# https://leetcode.com/problems/container-with-most-water/

def func(height):
  
    area = 0
    l,r = 0, len(height)-1

    while l < r:
        left_elem, right_elem = height[l], height[r]

        area = max(area, min(left_elem, right_elem)*abs(r-l))

        if left_elem < right_elem:
            l+=1
        else:
            r-=1

    return area

print(func([1,8,6,2,5,4,8,3,7])) # 49
