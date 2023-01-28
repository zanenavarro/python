import argparse
import re
parser = argparse.ArgumentParser(
                    prog = 'ProgramName',
                    description = 'What the program does',
                    epilog = 'Text at the bottom of help')
parser.add_argument('-file_name', '--file_name',
                    action='store')


def main():
    args = parser.parse_args()
    user_options = args.__dict__
    file_name = user_options["file_name"]
    name = (file_name.split("/")[-1]).split(".")[0]
    structure_str = ""

    with open(file_name, "r") as file_to_check:
        python_file_l = file_to_check.readlines()
        file_to_check.close()

    for index, line in enumerate(python_file_l):
        
        regexp = re.compile(r'(class (.*):)')
        line_is_class = regexp.search(line)
        if (line_is_class):
            try:
                class_name = line_is_class.group(1)
                structure_str += ".. autoclass:: {0}.{1}\n  :members:\n".format(name, class_name)
            except:
                print("regex didnt matchh on line.")


    with open("structure.rst", "a") as struct_file:
        struct_file.write(structure_str)
        struct_file.close()

if __name__ == "__main__":
    main()