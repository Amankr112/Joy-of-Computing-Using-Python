#  File Handling:
# File is named location on disk to store related information.
# It is used to permanently store data in a non-volatile memory(e.g, HardisK).

# In Python, a file operation takes palce in the following order:

# 1.) Open a file
# 2.) Read or write(perform operation)
# 3.) close the file



# f= open("file.csv", 'r')
# print(f.readlines())
# print(f.readlines())
# print(f.readlines())
# f.close()


# f= open("file.csv", 'r')
# for line in f:
#     print(line)    
# f.close()



# import pandas as pd
# file=pd.read_csv('file.csv')
# print(file)


# with open('file.csv') as f:
#     for line in f:
#         print(line)


# with open('file.csv') as f:
#     print(f.read()) 



# with open('file.csv') as f:
#     print(f.read(10))   # only 10 words will print
#     f.seek(0)      # it is used to move cursor
#     print(f.read(10))



# Writing to a file:
# Open the file using 'w' mode. we get a file object that can be used to write into thefiles.

# with open('write_file.txt', 'w') as f:
#     f.write('Hey Aman,\n Hello')

lines_data =['Piyush\n', 'Anish\n', 'Bhakta']
with open('write_file.txt', 'a') as f:
    f.write('\nAman\n')
    f.writelines(lines_data)







