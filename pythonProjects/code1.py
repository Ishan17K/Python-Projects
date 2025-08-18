nums = [3,2,4]
target = 6
for i in range(len(nums)):
    sol = (target - nums[i])
    for j in range(i+1,len(nums)):
        if sol - nums[j] == 0:
            print (j,i)
