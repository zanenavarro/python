import argparse
import re
import os
parser = argparse.ArgumentParser(
        prog='update_rst',
        description='What the program does',
        epilog='Text at the bottom of help'
    )
parser.add_argument(
                    '-file_name',
                    '--file_name',
                    action='store'
                )
count = 0

def main():
    args = parser.parse_args()
    user_options = args.__dict__
    file_path = user_options["file_name"]
    file_info = file_path.split("/")

    folder_name = file_info[0]
    version_name = file_info[1]
    folder_type = file_info[2]
    py_file = file_info[3]  

    os.chdir(os.path.dirname(os.path.dirname(file_path)))
    print(os.popen("ls -l").read())
    #os.chdir("./docs")
    print(folder_type)
    if (folder_type == "lib"):

        rst_file = '{}.rst'.format(folder_name)
        print(rst_file)
        print(os.path.isfile(rst_file))
        os.chdir(folder_name)
        os.chdir(version_name)
        os.chdir("docs")
        # os.chdir('{}/{}/docs/'.format(folder_name, version_name))
        # if (os.path.isfile(rst_file)):
        rst_str = ""

        with open(file_path, 'r') as py_file:
            py_contents = py_file.readlines()
            py_file.close()

        name_file = py_file.split(".")[0]
        for index, line in enumerate(py_contents):
            print(line)
            # regexp = re.compile(r'(class (.*):)')
            line_is_class = re.search("(class (.*):)", line).group(2)
            print(line_is_class)
            if (line_is_class):
                try:
                    class_name = line_is_class.group(2)
                    rst_str += ".. autoclass:: {0}.{1}\n  :members:\n".format(name_file, class_name)
                    print("adding {}".format(class_name))
                except:
                    print("regex didnt matchh on line.")

        with open(rst_file, 'w') as read_file:
            read_file.write(rst_str)
            read_file.close()


        
def get_state(state, line):
    comment_line = '"""'

    if (comment_line in line):
        count += 1
        if (count == 1 and state == "SEARCHING"):
            state = "SAMPLING"
        elif (count == 2 and state == "SAMPLING"):
            state = "SEARCHING"
    



    return state








if __name__ == "__main__":
    main()

