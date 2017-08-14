import os
import pickle
import urllib.request
import webbrowser

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


# Before writting to a new file, it will check out whether the target file exists.
# if not, write to file.
def write_without_overriding(file_path, file_name, content):
     if is_file_exist(file_path):
          print("The target file exists.")
     else:
          # invoke write_file() method.
          write_file(file_path, file_name, content)

# append specific content to a file.
# file_name: the target file need to be appended.
# content:   appended content.
def append_text(file_name, content):
     if(file_name == "" or content == ""):
          return
     
     with open(file_name, 'a') as file:
          file.write(content)

# insert a title to start of target file.
def insert_title(file_path, title):
     # 'r+' means that a file is opened by reading and writing mode.
     f = open(file_path, 'r+')

     # get file content and save it to a string var
     temp = f.read();

     # now, temp has title content.
     temp = title + "\n\n" + temp;

     # let file pointer to start position for writing to a new file
     f.seek(0)

     f.write(temp)

# Check a file whether it is a gif file.
# a gif file always starts with four bytes = 0x47 0x49 0x46 0x38
# a tuple works like an array in Java.
def is_gif(file_name):
     file = open(file_name, 'br')
     first_four_bytes = tuple(file.read(4))
     return first_four_bytes == (0x47, 0x49, 0x46, 0x38)

# Make a pickled file
def make_pickled_file(file_path):
     grades = {
               'Alan' : [4, 8, 10, 10],
               'Tom'  : [7, 7, 7, 8],
               'Eric' : [3, 8, 10, 9]}

     # 'wb' means write binary
     outfile = open(file_path, 'wb')

     # dump data structure to outlet file
     pickle.dump(grades, outfile)

# This really seems like Serializable and Deserializable.
def read_pickled_file(file_path):
     file = open(file_path, 'rb')
     grades = pickle.load(file)
     return grades

# read a webpage into a target file.
def read_website_page(web_addr, read_all):
     try:
          page = rullib.request.urlopen(web_addr);
          html = page.read();

          if (read_all):
               write_file("/Users/sucong/Desktop/Workspaces/PythonToolbox", "HTML_READ.html", html)

     except Exception as e:
          print("Website open failed. Sorry for this happened.");
          # print(traceback.format_exc());

     finally:
          # run cleaning code
          print("Connection and other resources are cleaned by system here.")
          # urllib.request.close()

# access website via module webbrowser
def access_website(addr):
     webbrowser.open(addr)
          
          
     
     
