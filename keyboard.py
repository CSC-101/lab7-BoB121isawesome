from convert import str_to_float

def gather_numbers()->list[float]:
    num_list=[]
    while True:
        line = input("Input a number: ")
        if line == "done":
            break
        num_list.append(str_to_float(line))
    return num_list

if __name__ == '__main__':
    print(gather_numbers())