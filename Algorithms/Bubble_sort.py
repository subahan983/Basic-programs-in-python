                                        # BUBBLE SORT

li = [80, 20, 100, 102, 14, 34]

print('List before sorting is : ')

for i in li:
        print(i, end = ' ')
print()

for i in range(len(li)):
        for j in range(len(li) - i - 1):
                if(li[j] > li[j + 1]):
                        li[j], li[j+1] = li[j+1], li[j] # swaps two numbers if left one is greater than the right one.
print('List after sorting is : ')

for i in li:
        print(i, end = ' ')
