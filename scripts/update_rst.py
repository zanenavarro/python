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
    working_dir = os.getcwd()
    #os.chdir(os.path.dirname(os.path.dirname(file_path)))
    print(os.popen("ls -l").read())
    #os.chdir("./docs")
    print(folder_type)
    if (folder_type == "lib"):

        rst_file = '{}.rst'.format(folder_name)
        rst_str = ""

        with open(file_path, 'r') as file_py:
            py_contents = file_py.readlines()
            file_py.close()

        os.chdir("./{}/{}/docs/".format(folder_name, version_name))
        name_file = py_file.split(".")[0]
        for index, line in enumerate(py_contents):
            line_is_class = ""
            # regexp = re.compile(r'(class (.*):)')
            try: 
                line_is_class = re.search("(class (.*):)", line)
            except:
                pass
            if (line_is_class):
                try:
                    class_name = line_is_class.group(2).split('(')[0]
                    rst_str += ".. autoclass:: {0}.{1}\n  :members:\n".format(name_file, class_name)
                    print("adding {}".format(class_name))
                except:
                    print("regex didnt matchh on line.")
            # TODO : add support for auto generating functions if not class
        with open(rst_file, 'w') as read_file:
            read_file.write(rst_str)
            read_file.close()



if __name__ == "__main__":
    main()

