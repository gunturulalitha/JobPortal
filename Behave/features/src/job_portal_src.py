import os
import re

global home_page
global upload_click
file_list = ["C:/bdd.txt", "C:/BDD_Word.docx", "C:/BDD_Word_lessthan20kb.docx"]


def file_size():
    for i in range(len(file_list)):
        st = os.stat(file_list[i])
        if (st.st_size / 1000) < 20:
            print("File name - ", file_list[i], " of Size - ", st.st_size, " is Uploaded successfully")
            return st.st_size
        else:
            print("File name - ", file_list[i], " of size - ", st.st_size, " is Exceeded size limit")
            return st.st_size


file_size()


def file_type():
    for i in range(len(file_list)):
        file_name, file_extension = os.path.splitext(file_size())
        if file_extension == ".doc" or ".docx":
            print("Inside If condition File type - ", file_extension)
            assert True
            return file_extension
        else:
            print("File type - ", file_extension)
            return file_extension


file_type()
