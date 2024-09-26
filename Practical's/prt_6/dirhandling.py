import os
import shutil

# getcwd()
current_directory = os.getcwd()
print("Current Directory: ", current_directory)

# #chdir()
# os.chdir("/path/to/another/directory")
# new_directory = os.getcwd()
# print("New Current Directory: ", new_directory)
#
# os.chdir(current_directory)
#
# # mkdir()
# os.mkdir("new_directory")
# print("Directory 'new_directory' created.")
#
# # rmdir()
# os.rmdir("new_directory")
# print("Directory 'new_directory' removed.")
#
# # listdir()
# items = os.listdir(current_directory)
# print("Contents of the directory:", items)
#
# # rename()
# os.mkdir("old_directory")
# os.rename("old_directory", "renamed_directory")
# print("Directory 'old_directory' renamed to 'renamed_directory'.")
#
# # remove()
# with open("sample_file.txt", "w") as f:
#     f.write("Sample content.")
# os.remove("sample_file.txt")
# print("File 'sample_file.txt' removed.")
#
# # shutil.rmtree()
# os.mkdir("dirwithfile")
# with open("dirwithfile/file.txt", "w") as f:
#     f.write("Some content.")
# shutil.rmtree("dirwithfile")
# print("Directory 'dirwithfile' removed with all its contents.")
#
# # exists()
# path_exists = os.path.exists("renamed_directory")
# print("Does 'renamed_directory' exist? ", path_exists)
#
# # isdir(path)
# is_directory = os.path.isdir("renamed_directory")
# print("Is 'renamed_directory' a directory? ", is_directory)
