li = [1, 2, 10, 12, 14, 34]
key = 34
for i in range(len(li)):
  if(li[i] == key):
    print(key, 'is present at : ', i, 'index')
    break
else:
  print(key, 'is not in the list')
