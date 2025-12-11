

def process_input(file_path):
    output = []
    with open (file_path) as file:
        for line in file.readlines():
            list_line = []
            line = line.strip()
            for i in line:
                list_line.append(i)
            output.append(list_line)
    return output

def helper(row, col, word, array):
    directions = [
        (0, 1),  
        (1, 0), 
        (1, 1),  
        (1, -1), 
        (0, -1), 
        (-1, 0), 
        (-1, -1),
        (-1, 1)  
    ]
    count = 0 
    rows = len(array)
    cols = len(array[0])
    length = len(word)

    for x, y in directions:
        is_good = True
        for index in range(length):
            new_row = row + x * index
            new_col = col + y * index
            if not (0 <= new_row < rows and 0 <= new_col < cols) or array[new_row][new_col] != word[index]:
                is_good = False
                break
        if is_good:
            count += 1
    return count
    

def part2_helper(row, col, word, array):
    directions = [
        (1, 1),   # Down-Right
        ]
    count = 0 
    rows = len(array)
    cols = len(array[0])
    length = len(word)
    for x, y in directions:
        is_good = True
        for index in range(length):
            new_row = row + x * index
            new_col = col + y * index
            if not (0 <= new_row < rows and 0 <= new_col < cols) or array[new_row][new_col] != word[index]:
                is_good = False
                break
        if is_good:
            if set([array[row + x*2][col], array[row][col + y*2]]) == {'S', 'M'}:
                count += 1
    word = word[::-1]
    for x, y in directions:
        is_good = True
        for index in range(length):
            new_row = row + x * index
            new_col = col + y * index
            if not (0 <= new_row < rows and 0 <= new_col < cols) or array[new_row][new_col] != word[index]:
                is_good = False
                break
        if is_good:
            if set([array[row + x*2][col], array[row][col + y*2]]) == {'S', 'M'}:
                count += 1
    return count
    

def part1( word,array):
    result = 0
    rows = len(array)
    cols = len(array[0])
    for i in range(rows):
        for j in range(cols):
            result += helper(i, j, word, array)

    return result



def part2(word,array):
    result = 0
    rows = len(array)
    cols = len(array[0])
    for i in range(rows):
        for j in range(cols):
            result += part2_helper(i, j, word, array)
    return result

                

            


            

if __name__ == "__main__":
    input_file = './day4/input4.txt'
    listof= process_input(input_file)
    print(part1('XMAS', listof))
    print(part2('MAS', listof))
