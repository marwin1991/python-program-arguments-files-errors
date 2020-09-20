import sys


def get_filename(my_args):
    if len(my_args) >= 2:
        filename = my_args[1]
        return filename
    else:
        print("[ WARNING ] You should run this program by calling: python parser.py filename")
        return ""


def main():
    my_args = list(sys.argv)
    filename = get_filename(my_args)

    if len(filename) == 0:
        return
    
    print(f"File to parse: {filename}")
    


if __name__ == "__main__":
    main()



