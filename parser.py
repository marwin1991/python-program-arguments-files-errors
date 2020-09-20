import sys


def get_filename(my_args):
    if len(my_args) >= 2:
        filename = my_args[1]
        return filename
    else:
        print("[ WARNING ] You should run this program by calling: python parser.py filename")
        return ""


def read_from_file_to_list(filename):
    output = []

    with open(filename,"r") as file_to_read:
        for line in file_to_read.readlines():
            row = line.replace("\n","").split(" ")
            output.append(row)
    
    return output


def main():
    my_args = list(sys.argv)
    filename = get_filename(my_args)

    if len(filename) == 0:
        return
    
    print(f"File to parse: {filename}")
    data_list = read_from_file_to_list(filename)
    print(data_list)
    


if __name__ == "__main__":
    main()


