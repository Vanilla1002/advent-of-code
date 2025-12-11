dictionary_of_pages = {}
line_breaker = 0
result = 0
part2_list = []
result2 = 0

def changer(list1):
    helper = []
    for j in list1:
        for page in dictionary_of_pages.get(j, []):
            if page in helper:
                list1.remove(j)
                list1.insert(helper.index(page), j)
                
                return list1
        helper.append(j)

def isgood(list1):
    helper = []
    for j in list1:
        for page in dictionary_of_pages.get(j, []):
            if page in helper:
                return False
        helper.append(j)
    return True



with open ('./day5/input5.txt') as f:
    for line_number, line in enumerate(f):
        if line.strip() == '':
            line_breaker = line_number
            break
        x = line[3:5]
        y = line[:2]
        if y in dictionary_of_pages:
            dictionary_of_pages[y].add(x)
        else:
            dictionary_of_pages[y] = {x}


with open('./day5/input5.txt') as f:
    for line_number, line in enumerate(f):
        if line_number <= line_breaker:
            continue
        is_valid = True
        line = line.split()
        list_of_strings = ','.join(line).split(',')

        if isgood(list_of_strings):
            middle = len(list_of_strings) // 2
            result += int(list_of_strings[middle])
        else:
            part2_list.append(list_of_strings)


breakpls = False

for i in part2_list:
    helper = []
    while not isgood(i):
        i = changer(i)
    
for i in part2_list:
    middle = len(i) // 2
    result2 += int(i[middle])

print(result)
print(result2)
    





