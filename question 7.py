
seti = set()


n = int(input("Enter number of elements : "))


for i in range(0, n):
    ele = int(input())
    seti.add(ele)

print("Maximum : ", max(seti))
print("Minimum :", min(seti))