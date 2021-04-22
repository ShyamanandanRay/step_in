# program to convert a list into nested dictionary in python
num_list = []
n = int(input("Enter number of elements : "))

print("Enter the elements: ")
for i in range(0, n):
    ele = int(input())
    num_list.append(ele)

new_dict = current = {}
for name in num_list:
    current[name] = {}
    current = current[name]
print(new_dict)