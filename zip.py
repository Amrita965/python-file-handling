# Creating zip file
# import zipfile
#
# with zipfile.ZipFile("new.zip", "w") as zip:
#     zip.write("./my_dir")


# Extract from zip file
# import zipfile
#
# with zipfile.ZipFile('new.zip', 'r') as zip:
#     zip.extractall()
#     extracted_file = zip.namelist()
#     print(extracted_file)


# Make zip from directory
import shutil
shutil.make_archive('test', "zip", './my_dir') # shutil.make_archive(zip_file_name, file_format, root_dir)