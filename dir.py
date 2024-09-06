
# 1. Creating a Directory
# 2. Reading a Directory
# 3. Writing to a File in a Directory
# 4. Renaming a Directory
# 5. Deleting a Directory

# import os
# l = os.listdir('./my_dir')
# for item in l:
#     print(item)
#
# for item in l:
#     if '.txt' in item:
#         os.remove(f'./my_dir/{item}')
#
# print("\nAfter deleting all text file:")
# for item in l:
#     print(item)

# Removing a directory
# import os
# os.remove("new_new/test.txt")
# os.rmdir("new_new")

# Renaming a Directory
# import os
# os.rename("new", "new_new")

# Writing to a File in a Directory
# with open("./new/test.txt", "r") as file:
#     content = file.read()
#     print(content)

# Reading a Directory
# import os
# l = os.listdir("./new")
# print(l)

# Create a directory
# import os
# os.mkdir("new")