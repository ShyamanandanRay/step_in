# write a program to change position of every nth value with n+1 th value in a list

lst = []


n = int(input("Enter number of elements : "))


for i in range(0, n):
    ele = int(input())
    lst.append(ele)
first = lst[0]
for i in range(0, n):
    if i == n-1:
        lst[n-1] = first
    else:
        lst[i] = lst[i+1]

print(lst)

