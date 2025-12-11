def process_input(file_path):
    list_of_input =[]
    helper = False
    with open(file_path) as file:
        file = file.read()
        counter = 0
        for number in file:
            number = int(number)
            if not helper:
                for _ in range(number):
                    list_of_input.append(counter)
                counter +=1
            else:
                for _ in range(number):
                    list_of_input.append(-1)
            helper = not helper
        return list_of_input
    
def part1(numbers : list):
    pointer1 =0
    pointer2 =len(numbers) - 1

    while pointer2 >= pointer1:
        if numbers[pointer2] != -1:
            while pointer2 >= pointer1 and numbers[pointer1] !=-1 :
                pointer1+=1
            if pointer2 <= pointer1:
                break
            numbers[pointer1] = numbers[pointer2]
            numbers.pop()
            pointer1+=1
            pointer2-=1
        else:
            while numbers[pointer2] == -1:
                pointer2-=1
                numbers.pop()
    result = 0
    for i, number in enumerate(numbers):
        result += i*number
    return result
            

if __name__ == "__main__":
    input_file = './day9/input9.txt'
    listof= process_input(input_file)
    
    print(part1(listof))
    
