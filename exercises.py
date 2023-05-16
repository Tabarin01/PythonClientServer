#5.Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
def input_names():
 first_name= input("Insert ur first name: ")
 last_name= input("Insert ur last name:")
 print(last_name+""+first_name)

#6.Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
def creating_list():
 numbers = input("Input some comma seprated numbers: ")
 list = numbers.split(",")
 print(list)

#7.Write a Python program that accepts a filename from the user and prints the extension of the file.
def exentions():
 filename = input("Input the Filename: ")
 f_extns = filename.split(".")
 print ("The extension of the file is : " + repr(f_extns[-1]))

#8.Write a Python program to display the first and last colors from the following list.
def first_last():
 color_list = ["Red","Green","White" ,"Black"]
 print(color_list[0]+" "+color_list[-1])

#9.Write a Python program to display the examination schedule. (extract the date from exam_st_date).
def convert_numbers_in_date():
 exam_st_date = (11,12,2014)
 print( "The examination will start from : %i / %i / %i"%exam_st_date)

#10.Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
def exercise10():
 number = int(input("Insert a number: "))
 n1 = int( "%s" % number )
 n2 = int( "%s%s" % (number,number) )
 n3 = int( "%s%s%s" % (number,number,number))
 print (n1+n2+n3)

#11.Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
print(abs.__doc__)