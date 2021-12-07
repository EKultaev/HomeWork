def my_func_1 (x,y):
    return x ** y

def my_func_2 (x,y):
    n = 1
    for i in range(y * -1):
        n *= x
    return 1 / n

nums1 = float(input("x: "))
nums2 = int(input("y: "))
print(my_func_1(nums1, nums2))
print(my_func_2(nums1, nums2))