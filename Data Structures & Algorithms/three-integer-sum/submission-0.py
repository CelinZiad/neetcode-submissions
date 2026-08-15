class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        #print(f"nums: {nums}")


        for i in range(0,len(nums)):
            left = i+1
            right = len(nums)-1
            #print(f"i: {i}")
            #print(f"left: {left}")
            #print(f"right: {right}")

            while (left<right):
                #print(f"nums i: {nums[i]}")
                #print(f"nums left: {nums[left]}")
                #print(f"nums right: {nums[right]}")
                test = nums[i] + nums[left] + nums[right]
                #print(f"test: {test}")

                if test ==0:
                    #print(f"test is 0")
                    zero = [nums[i],nums[left],nums[right]]
                    if zero not in result:
                        result.append(zero)
                    #print(f"zero: {zero}")
                    #print(f"result: {result}")
                    left+=1
                    #print(f"left: {left}")
                    right-=1
                    #print(f"right: {right}")
                    

                elif test>0:
                    #print(f"test: is positive")
                    right=right-1

                elif test<0:
                    #print(f"test is negative")
                    left=left+1
                    
        return result

        """
        LOGIC:
        sort nums
        for i in 

        """