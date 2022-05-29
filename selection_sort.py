# Selction Sort

def Selection_sort(arr):

  n = len(arr)

  for i in range(n):

    min = i

    for j in range(i+1, n):

      if(arr[j] < arr[min]):

        min = j

    if(min != i):
      arr[min],arr[i] = arr[i],arr[min]


arr = list(map(int, input("Enter Array Elements: ").split()))

n = len(arr)

print("Array before sort: ")
print(arr)

Selection_sort(arr)

print("Array after sort: ")
print(arr)

