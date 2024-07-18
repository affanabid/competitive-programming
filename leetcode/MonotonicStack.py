def MonotonicStack(nums):
    stack = []
    for n in nums:
        while stack and n < stack[-1]:
            stack.pop()
        stack.append(n)
    return stack

n = [5,4,3,2,1]
print(MonotonicStack(n))
