# MIT6.0001- LECTURE 4: DECOMPOSITION, ABSTRACTIONS, FUNCTIONS

# # Function definition
# # Specification for Docs and help()
# def max(x, y):
#     """
#     Find max number of x and y
#     """
#     if x > y:
#         return x
#     else:
#         return y
# print(max(-1, 1))
# max()
# help(max)


# # Keyword Arguments
# def printName(firstName, lastName, reverse):
#     if reverse:
#         print(lastName + ', ' + firstName)
#     else:
#         print(firstName + ', ' + lastName)
#
# printName('Adam', 'Tran', False)
# printName('Adam', 'Tran', True)
# printName(firstName='Adam', lastName='Tran', reverse=False)
# printName('Adam', lastName='Tran', reverse=False)


# File process operators
# Open file to write
# FILE_NAME='lec4_file.txt'
# fileHandle = open(FILE_NAME, 'a') # 'w': overwrite file, 'a': append exist file
# for i in range(2):
#     name = input('Enter name: ')
#     fileHandle.write(name + '\n')
# fileHandle.close()
#
# # Open file to read
# fileHandle = open(FILE_NAME, 'r')
# for line in fileHandle:
#     print(line[:-1])
# fileHandle.close()
#
#
# ##############################################################
# #   COMMON FUNCTIONS FOR ACCESSING FILES                     #
# # fn =  file name                                            #
# # 1. open(fn, 'w'): create file for writing                  #
# #                  and returns a file handle                 #
# # 2. open(fn, 'r'): open exist file for reading              #
# #                   and returns a file handle                #
# # 3. open(fn, 'a'): open exist file for appending            #
# #                   and returns a file handle                #
# # 4. fh.read(): returns a string representing a file name    #
# # 5. fh.readline(): returns next line                        #
# # 6. fh.write(s): write string s to the end of file          #
# # 7. fh.writeLine(s): write each element of S to the file    #
# # 8. fh.close(): close file handle                           #
# ##############################################################


