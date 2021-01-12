name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count = 0
tag1 = 0
hours = dict()

for line in handle:

    line.rstrip()
    if len(line) < 3:
        continue

    wds = line.split()
    if wds[0] != 'From':
        continue
    elif tag1 % 2 == 1:
        continue
    else:
        count = count + 1
        times = wds[5].split(':')
        hours[times[0]] = hours.get(times[0],0) + 1

list = []
for key,value in hours.items():
    newtuple = (key,value)
    list.append(newtuple)

#print(sorted([(key,value) for key,value in hours.items()]))
list2 = sorted(list)
for key,value in list2:
    print(key,value)
