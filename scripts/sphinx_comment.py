import argparse
import os
import re
parser = argparse.ArgumentParser(
                    prog = 'ProgramName',
                    description = 'What the program does',
                    epilog = 'Text at the bottom of help'
            )
parser.add_argument('-file_name', '--file_name',action='store')
parser.add_argument('-dir', "-dir_name", action="store")
parser.add_argument('-title', "-title", action="store")




class Sphinx:
    def __init__(self):
        self.title = ""
        self.user_options = {}
        self.import_files = []

    def get_options(self):
        args = parser.parse_args()
        self.user_options = args.__dict__

    def main(self):
        self.title = self.user_options["title"]
        structure_str = "{}\n{}\n\n".format(self.title, len(self.title) * "=")

        if (self.user_options["file_name"] != None):
            file_name = self.user_options["file_name"]
            structure_str += self.get_rst_str(file_name)

        elif ("dir" in self.user_options):
            dir_name = self.user_options["dir"]
            print(dir_name)
            for file_name in os.listdir(dir_name):
                print(file_name)
                structure_str += self.get_rst_str("{}/{}".format(dir_name, file_name))

        with open("{}.rst".format(self.title), "a") as struct_file:
            struct_file.write(structure_str)
            struct_file.close()
        print(self.import_files)

    def get_rst_str(self, file_name):
        name = (file_name.split("/")[-1]).split(".")[0]
        structure_str = ""

        with open(file_name, "r") as file_to_check:
            python_file_l = file_to_check.readlines()
            file_to_check.close()

        for index, line in enumerate(python_file_l):
            
            regexp = re.compile(r'(class (.*):\n)')
            line_is_class = regexp.search(line)
            if (line_is_class):
                try:
                    class_name = line_is_class.group(2)
                    structure_str += ".. autoclass:: {0}.{1}\n  :members:\n".format(name, class_name)
                except:
                    print("regex didnt matchh on line.")
        if (name != ""):
            self.import_files.append("import {}\n".format(name))
        return structure_str
    
    def update_conf(self):
        conf_str = ""
        for items in self.import_files:
            conf_str += items
        conf_str += os.popen("cat {}".format(self.conf_file)).read()


if __name__ == "__main__":
    s = Sphinx()
    s.get_options()
    s.main()