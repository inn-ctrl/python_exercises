def two_sum(nums, target): 
    
    seen = {}

    for i, num in enumerate(nums): 
        compliment = target - num

        if compliment in seen: 
            return [seen[compliment], i]
        
        seen[num] = i


my_list = [1, 2, 3, 4, 5]
target = 9
result = two_sum(my_list, target)
print(f"Indices of the two numbers that add up to {target} are: {result}")