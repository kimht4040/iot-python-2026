
arr = [10,20,30]

print(arr)
arr.append(40)

print(arr)


arr2 = arr.copy()

print(arr2)


arr2.insert(2,80)
print(arr2)



print(arr2.count(10))

print(len(arr2))

arr.clear()

print(arr)


arr2.remove(80)
print(arr2)

arr.extend(arr2)
print(arr)

arr2.reverse()

print(arr2)


arr2.sort()

print(arr2)
arr2.sort(reverse=True)
print(arr2)


arr2.append([60,70,80,90])

print(arr2[1][2])