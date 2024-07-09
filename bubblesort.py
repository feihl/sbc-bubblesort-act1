list = ["M", "B", "D", "R", "N", "C"]
print("\nUnsorted: ", list, "\n")
n = len(list)
for i in range(n-1):
    for j in range(n-i-1):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
            print("Process: ", list)
print("\nSorted: ", list, "\n")