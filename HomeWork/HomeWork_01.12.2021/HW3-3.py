def my_func (a, b, c):
    sum = a + b + c
    return sum - min(a, b, c)

nums1 = float(input("a: "))
nums2 = float(input("b: "))
nums3 = float(input("c: "))
print(my_func(nums1, nums2, nums3))