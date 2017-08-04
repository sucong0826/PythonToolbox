import os

def print_file_to_console(file_name):
     f = open(file_name, 'r')
     for line in f:
          print(line, end = "")
     f.close()

# Use this method to print a file to console.
# file_name: the name of a file that you want to print it out.
def print_file(file_name):
     print(open(file_name, 'r').read())

# Check whether the given path points a file.
# file_path: an conical file path and name
def is_file_exist(file_path):
     return os.path.isfile(file_path)

# write file content to a file with give path and name.
# file_path: where the file is.
# file_name: what the name of file is.
def write_file(file_path, file_name, content):
     f = open(file_path + '\\' + file_name, 'w')
     f.write(content)
