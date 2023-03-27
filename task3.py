class TwoSum:
    def __init__(self,numbers,target):
        self.numbers = numbers
        self.target = target
    def find_indices(self):
        indices = {}
        for i,num in enumerate(self.numbers):
            complement = self.target - num
            if complement in indices:
                return indices[complement], i
            indices[num] = i
        return None

numbers = [ 10, 20, 10, 40, 50, 30, 70]
target=50
two_sum = TwoSum(numbers,target)
indices = two_sum.find_indices()
if indices:
    print(f"{indices[0]}, {indices[1]}")
else:
    print("No pair found.")