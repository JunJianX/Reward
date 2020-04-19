dic = {'a': 1, 'b': 2, 'c': 3, 'd': 1}

# save to local
f = open(".\dict.txt", 'w')
f.write(str(dic))
f.close()
print("save dict successfully.")