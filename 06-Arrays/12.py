arr = [
    [2,5,4],
    [9,0,3]
]
print(arr)
print(f"rows: {len(arr)} columns: {len(arr[0])}")
print("5th: ",arr[0][1])
print("3rd: ",arr[1][-1])
for i in arr[1]:
    print(i, end=" ")
print("\n")
for i in arr:
    for j in i:
        print(j, end=" ")
    print("")
print("")
for i in arr:
    print(i[-1])
