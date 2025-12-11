def process_input(path_file):
    #ex 7777742220-7777814718,3201990-3447830,49-86,653243-683065,91-129,24-41
    output = []
    with open(path_file) as file:
        for line in file:
            output.extend(line.strip().split(','))
    return output

def input_praser(line :str) -> tuple[int,int]:
    a,b = line.split('-')
    return (int(a),int(b))

def part1(list1 :list[str]) -> int:
    result = 0
    for i in list1:
        a,b = input_praser(i)
        for j in range(a,b+1):
            j_1 = str(j)[:len(str(j))//2]
            j_2 = str(j)[len(str(j))//2:]
            if j_1 == j_2:
                result += j
    return result
def part2(list1 :list[str]) -> int:
    result = 0
    for i in list1:
        a,b = input_praser(i)
        for j in range(a,b+1):
            j_str = str(j)
            len_j = len(j_str)
            if len_j % 2 == 0:
                j_1 = j_str[:len_j//2]
                j_2 = j_str[len_j//2:]
                if j_1 == j_2:
                    result += j
                    continue
            if len_j % 3 == 0:
                j_1 = j_str[:len_j//3]
                j_2 = j_str[len_j//3:2*len_j//3]
                j_3 = j_str[2*len_j//3:]
                if j_1 == j_2 == j_3:
                    result += j
                    continue
            if len_j % 5 == 0:
                j_1 = j_str[:len_j//5]
                j_2 = j_str[len_j//5:2*len_j//5]
                j_3 = j_str[2*len_j//5:3*len_j//5]
                j_4 = j_str[3*len_j//5:4*len_j//5]
                j_5 = j_str[4*len_j//5:]
                if j_1 == j_2 == j_3 == j_4 == j_5:
                    result += j
                    continue
            if len_j % 7 == 0:
                j_1 = j_str[:len_j//7]
                j_2 = j_str[len_j//7:2*len_j//7]
                j_3 = j_str[2*len_j//7:3*len_j//7]
                j_4 = j_str[3*len_j//7:4*len_j//7]
                j_5 = j_str[4*len_j//7:5*len_j//7]
                j_6 = j_str[5*len_j//7:6*len_j//7]
                j_7 = j_str[6*len_j//7:]
                if j_1 == j_2 == j_3 == j_4 == j_5 == j_6 == j_7:
                    result += j
                    continue
            
    return result

def part2_cleaner(list1 :list[str]) -> int:

    def is_repeated_equal_parts(s: str, k: int) -> bool:
        return (len(s) % k == 0) and (s == s[:len(s)//k] * k)

    result = 0
    for i in list1:
        a, b = input_praser(i)
        for j in range(a, b + 1):
            s = str(j)
            for k in (2, 3, 5, 7):
                if is_repeated_equal_parts(s, k):
                    result += j
                    break 
    return result



if __name__ == "__main__":
    path = './input.txt'
    input_lines = process_input(path)
    result = part2(input_lines)
    print(f'Result: {result}')