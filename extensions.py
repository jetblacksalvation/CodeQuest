extension_dict = {}
for x in range(int(input())):
    temp = input()
    if temp[temp.find('.')+1:] in extension_dict:
        extension_dict[temp[temp.find('.')+1:]] +=1
    else:
        extension_dict[temp[temp.find('.')+1:]] = 1

for key in extension_dict:
    print(key, extension_dict[key])
