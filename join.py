import json

with open('file1.json', 'r') as file :
    file1 = json.load(file)

with open('file2.json', 'r') as file :
    file2 = json.load(file)

# sort both arrays nlogn + mlogm
file1 = sorted(file1, key=lambda k: k['id']) 

# print file1
for elem in file1:
    print(elem)

print("\n\n")

file2 = sorted(file2, key=lambda k: k['id']) 

# print file2
for elem in file2:
    print(elem)

print("\n\n")

i1 = 0
i2 = 0
saved_index = 0
result = []

while True:
    if i1 >= len(file1) or i2 >= len(file2):
        break
    elif file1[i1]['id'] == file2[i2]['id']:
        result.append({"id": file1[i1]['id'], "name": file1[i1]['name'], "skill": file2[i2]['skill']})
        saved_index = i2
        i2 = i2 + 1
    elif file1[i1]['id'] < file2[i2]['id']:
        i1 = i1 + 1
        if file1[i1]['id'] == file2[saved_index]['id']:
            i2 = saved_index
            saved_index = 0
            continue
    elif file1[i1]['id'] > file2[i2]['id']:
        i2 = i2 + 1


# print result
for elem in result:
    print(elem)








