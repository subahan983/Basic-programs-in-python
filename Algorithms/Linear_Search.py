li = [1, 2, 10, 12, 14, 34]
key = 34
for i in range(len(li)):
  if(li[i] == key): # Compares with every element in the list with the given key element.
    print(key, 'is present at : ', i, 'index')
    break
else: # Enters the else block if the key is not present in the list.
  print(key, 'is not in the list')
