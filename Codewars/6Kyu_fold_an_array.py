"""
https://www.codewars.com/kata/57ea70aa5500adfe8a000110

In this kata you have to write a method that folds a given array of integers by the middle x-times.
As you see, if the count of numbers is odd, the middle number will stay. Otherwise the fold-point is between the middle-numbers, so all numbers would be added in a way.

The array will always contain numbers and will never be null. The parameter runs will always be a positive integer greater than 0 and says how many runs of folding your method has to do.

If an array with one element is folded, it stays as the same array.

The input array should not be modified!
"""

def fold_array(array, runs):
    res = []
    if len(array) == 1:
        return array
    
    else:
        runs -=1
        middle = len(array) // 2
        
        if len(array) % 2 == 1:
            middle +=1
        list1 = array[:middle]
        list2 = array[middle:]

        for i in list1:
            if len(list2) > 0:
                res.append(i+list2.pop())
            elif len(list2) == 0:
                res.append(i)

        if runs == 0:
            return res
        else:
            return fold_array(res, runs)


print(fold_array([1, 2, 3, 4, 5], 3))

