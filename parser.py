#
#   program usage: python parser.py data\input.txt my_output.txt
#

import sys

NAME_INDEX = 0

# function takes sys.args and should return input filename (look at the top of this file, in this case: data\input.txt)
# when there is no such argument should throw ValueError with message of how to use this program
def get_input_filename(my_args):
    return "data\input.txt"

# function takes sys.args and should return filename (look at the top of this file, in this case: my_output.txt)
# when there is no such argument should throw ValueError with message of how to use this program
def get_output_filename(my_args):
    return "my_output.txt"

# this function takes filename as argument and return the list of list of words from file
# example: [["Piotr", "Kowalski", "IT", "marwin1991"],["Karolina","Kowalska","Sales","aaabbbccc"]]
# when there is no such a file should throw ValueError wtih message
def read_from_file_to_list(filename):
    return [["Piotr", "Kowalski", "IT", "marwin1991"],["Karolina","Kowalska","Sales","aaabbbccc"]]

# this function should return string "Piotr, Karolina" for input [["Piotr", "Kowalski", "IT", "marwin1991"],["Karolina","Kowalska","Sales","aaabbbccc"]]
def get_names_as_string(data_list):
    return "Piotr, Karolina"

# this funtion should return list:
# ["Ilosc danych: 2", "Imiona: Piotr, Karolina"]
# For data_list: [["Piotr", "Kowalski", "IT", "marwin1991"],["Karolina","Kowalska","Sales","aaabbbccc"]]
def generate_report(data_list):
    return ["Ilosc danych: 2", "Imiona: Piotr, Karolina"]

# this function should save list ["Ilosc danych: 2", "Imiona: Piotr, Karolina"] to file
# every element of a list in new line
def save_report_to_file(report, filename):
    pass


def main():
    my_args = list(sys.argv)

    try:
        my_args = list(sys.argv)

        input_filename = get_input_filename(my_args)
        print(f"File to parse: {input_filename}")

        data_list = read_from_file_to_list(input_filename)
        report = generate_report(data_list)
        output_filename = get_output_filename(my_args)
        print(f"Saving raport to file: {input_filename}")

        save_report_to_file(report, output_filename)

        # Add new funtion:
        #
        # python parser.py data\input.txt --file my_output.txt
        # will save raport to file
        #
        # python parser.py data\input.txt --console
        # will print raport to console
        #
        # python parser.py data\input.txt --file my_output.txt --console
        # python parser.py data\input.txt --console --file my_output.txt
        # this two above will print to console and sace to file
        #
        # Following should raise error:
        # python parser.py data\input.txt --file
        # python parser.py data\input.txt --file --console
        # python parser.py data\input.txt --console --file
        # python parser.py data\input.txt --console --file --console


    except ValueError as error:
        print(error)
        return


if __name__ == "__main__":
    main()


