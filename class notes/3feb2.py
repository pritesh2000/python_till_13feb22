# Lists: Mutable & Ordered collections of members
l1 = [110,202,34,49,63, -94, -38]
# in:   0   1  2  3  4
# -ve: -5 -4  -3 -2 -1
print(l1[1])
print(l1[-2])
l1[1] = 404
print(l1)
print(type(l1))
print(len(l1))
print(max(l1))
print(min(l1))
print(sorted(l1))      # sorted will always return a NEW LIST
print(l1)

vegetables = ["Tomato", "potato", "lady's finger", "carrot", "onions"]
print(vegetables)
"""
print(vegetables[0])
print(vegetables[1])
print(vegetables[2])
print(vegetables[3])
print(vegetables[4])
"""
print(min(vegetables))
print(max(vegetables))
print(sorted(vegetables))

mix_veg = ["tomato", 0.5, "potato", -2, "lady's finger", 1, "carrot", 5, "onions", 2]
mix_veg2 = ["tomato", "0.5", "potato", "-2", "lady's finger", "1", "carrot", "5", "onions", "2"]
print(mix_veg)
# print(min(mix_veg))           Error
print(min(mix_veg2))
print(max(mix_veg2))
print(sorted(mix_veg2))

# Slicing is exactly the same as it was in strings:
numbers = [11, 22, 33, 22, 44, 22, 67, 99, 22, -4006, 9898, 0, -33, 22]
print(numbers[2:9])     # slicing never changes the original data
print(numbers)
"""
HW:
use all the ways to slice the above list and give comments.
"""