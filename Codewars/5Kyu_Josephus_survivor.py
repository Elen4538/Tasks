#https://www.codewars.com/kata/555624b601231dc7a400017a/train/python

# josephus_survivor(7,3) => means 7 people in a circle;
# one every 3 is eliminated until one remains
# [1,2,3,4,5,6,7] - initial sequence
# [1,2,4,5,6,7] => 3 is counted out
# [1,2,4,5,7] => 6 is counted out
# [1,4,5,7] => 2 is counted out
# [1,4,5] => 7 is counted out
# [1,4] => 5 is counted out
# [4] => 1 counted out, 4 is the last element - the survivor!


def josephus_survivor(n, k):
    if n ==1:
        return 1
    else:
    
        arr =[int(i) for i in range(1,n+1)] 
        
        ind = k - 1

        while len(arr) > 1:
            while ind >= len(arr):
                ind =ind - len(arr) 
              
            arr.pop(ind%n)
            ind += k - 1
        return arr[0]

print(josephus_survivor(7,3))       #4)
print(josephus_survivor(11,19))     #10)
print(josephus_survivor(1,300))     #1)
print(josephus_survivor(14,2))      #13)
print(josephus_survivor(100,1))     #100)