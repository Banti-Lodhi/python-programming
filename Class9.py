# creating class
#1. class myclass:
#     """A simple example class"""
#     i = 12345

#     def f(self):
#         return 'hello world'
#or        
# class sampleclass:
#     count = 0
#     def increase(self):
#         sampleclass.count+=1
# #Calling increase() on an object
# s1 = sampleclass()
# s1.increase()
# print(s1.count)
# # 
# # calling increase on one more
# # object
# s2 = sampleclass()
# s2.increase()
# print(s2.count)

# print(sampleclass.count)

# methods in python:-
# 1.instance method:-
# class Asianpublishers:
#     """Example Class"""
#     def __init__(self):
#         """Example Setup"""
#         print('Hello, World')
#         self.name = 'Asian publishers'
#     def example_fun(self):
#         """This method is an instance method"""
#         print('i\'m in instance method')  
#         print("My name is", self.name)
# de = Asianpublishers()
# de.example_fun() 

# 2.Static Method
# class AsianPublishers:
#     """Example Class"""
#     def __init__(self):
#         """Example Setup"""
#         print("Hello World")
#     @staticmethod
#     def exam_function():
#       """This method is a static method"""
#       print('I\'m a static method')
# de = AsianPublishers.exam_function()
# print(de)

# class method:
# class AsianPublishers:
#     """Example class"""
#     def __init__(self):
#         """Example Setup"""
#     print('Hello World')
#     @classmethod
#     def exam_fun(cls):
#       """This method is class method"""    
# print('I\'m a class method')
# de = AsianPublishers()
# de.exam_fun()            

# from datetime import date


# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         # a class method to create a person object by birth year
#     @classmethod
#     def birthDate(cls, name, age):
#         return cls(name, date.today().year - age)
#     #a static to check method if a person is adult or not
#     @staticmethod
#     def isadult(age):
#         return age>18
# person1 = Person('Ram', 22)

# person2 = Person.birthDate('Ram', 1996)
# print(person1.age)
# print(person2.age)

# print(Person.isadult(19))

                   
# 1.Create Dictionaries:-

# DIRECTORIES = {
#     "HTML":[".html5", ".html", ".htm", ".xhtml"],
#     "IMAGES":[".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg", ".heif", ".psd"],
#     "VIDEOS":[".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp"],
#     "DOCUMENTS":[".oxps", ".epub", ".pages", "docx", ".doc", ".fdf", ".ods", ".rvg", ".odt", ".pwi", ".xsn", ".xps", ".dotx", "docm", "dox", ".rtf", ".rtfd", ".wpd", ".xis", ".xisx", ".ppt", ".pptx"],
#     "ARCHIVES":[".a", ".ar", ".cpio", ".iso", ".tar", ".qz", ".rz", "7z", ".dmg", ".rar", ".xar", ".zip"], 
#     "AUDIO":[".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".mp3", ".msv", ".ogg", ".oga", ".raw", ".vox", ".wav", ".wma"],
#     "PLAIMTEXT":[".txt", ".in" ".out"],
#     "PDF":[".pdf"],
#     "PYTHON":[".py"], 
#     "XML":[".xml"],
#     "EXE":[".exe"], 
#     "SHELL":[".sh"]

# }

# print(DIRECTORIES)


# # Mapping 
# import os
# def oraganize_junk():
#     for entry in os.scandir():
#         if entry.is_dir():
#            continue
#         file_path = Path(entry) 
#         file_format = file_path.suffix.lower()
#         if file_format in FILE_FORMATS:
#             directory_path = Path(FILE_FORMATS[file_format])
#             directory_path.mkdir(exist_ok = True)
#             file_path.rename(directory_path.joinpath(file_path))
#         for dir in os.scandir():
#             try:
#                 os.rmdir(dir)
#             except:
#                 pass    


# 3.organizing
import os
from pathlib import Path

DIRECTORIES = {
    "HTML":[".html5", ".html", ".htm", ".xhtml"],
    "IMAGES":[".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg", ".heif", ".psd"],
    "VIDEOS":[".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp"],
    "DOCUMENTS":[".oxps", ".epub", ".pages", "docx", ".doc", ".fdf", ".ods", ".rvg", ".odt", ".pwi", ".xsn", ".xps", ".dotx", "docm", "dox", ".rtf", ".rtfd", ".wpd", ".xis", ".xisx", ".ppt", ".pptx"],
    "ARCHIVES":[".a", ".ar", ".cpio", ".iso", ".tar", ".qz", ".rz", "7z", ".dmg", ".rar", ".xar", ".zip"], 
    "AUDIO":[".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".mp3", ".msv", ".ogg", ".oga", ".raw", ".vox", ".wav", ".wma"],
    "PLAINTEXT":[".txt", ".in" ".out"],
    "PDF":[".pdf"],
    "PYTHON":[".py"], 
    "XML":[".xml"],
    "EXE":[".exe"], 
    "SHELL":[".sh"]

}
FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}

def oraganize_junk():
    for entry in os.scandir():
        if entry.is_dir():
           continue
        file_path = Path(entry) 
        file_format = file_path.suffix.lower()
        if file_format in FILE_FORMATS:
            directory_path = Path(FILE_FORMATS[file_format])
            directory_path.mkdir(exist_ok = True)
            file_path.rename(directory_path.joinpath(file_path))
        for dir in os.scandir():
            try:
                os.rmdir(dir)
            except:
                pass    
if __name__ == "__main__": 
    oraganize_junk()