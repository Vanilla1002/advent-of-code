#did it in efficent way, less than o(n)

left_list = []
right_list = []
length = 0
with open('input.txt') as f:
    for line in f:
        line = line.split()
        left_list.append(int(line[0]))
        right_list.append(int(line[1]))
        length +=1


left_list.sort()
right_list.sort()


total_distance = 0

for i in range(len(left_list)):
    total_distance += abs(left_list[i] - right_list[i])

pointer1 = 0
pointer2 = 0
count1 = 0
count2 = 0
result = 0 

while pointer1 < length:

    while pointer2 < length and left_list[pointer1] > right_list[pointer2]:
        pointer2 += 1
    
    while pointer2 < length and left_list[pointer1] == right_list[pointer2]:
        count2 += 1
        pointer2 += 1
    count1 = 1  
    while pointer1 < length - 1 and left_list[pointer1] == left_list[pointer1 + 1]:
        count1 += 1
        pointer1 += 1
    print(left_list[pointer1], count1, count2)
    result += left_list[pointer1] * (count1+count2 -1)
    count2 = 0
    pointer1 +=1
    
print(result)
print(total_distance)   