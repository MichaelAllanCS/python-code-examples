# SFS Lab 3 - Python Regex Questions
# EC May, 2022
# Add your answer to each of the questions
import re


# Q1 Import the apache log and print out the contents
# your code here
access_log = open("Lab3Regex\\apache_log.txt", "r")
data = access_log.read()

#text= "192"

#with open("Lab3Regex\\apache_log.txt", "r") as f:
    #for line in f:
        #if text in line:
            #print(line)

#occurrences = data.count("Opera")
#print("Number of occurrences of the word : ", occurrences)

# once you have answer for Q1 comment out the print statement to keep things tidy

# Q2 Use regex to find any instance of the word notice?
# your code here
with open ("Lab3Regex\\apache_log.txt", "r") as f:
    x = re.findall('notice', data)
    print(len(x))

# Q3 Use regex to find any instance of the word error?
# your code here
with open("Lab3Regex\\apache_log.txt", "r") as f:
    for line in f:
        if "error" in line:
            print(line)

# Q4 Use regex to count any instance of the word notice?
# your code here
with open ("Lab3Regex\\apache_log.txt", "r") as f:
    x = re.findall('notice', data)
    print(len(x))

# Q5 Use regex to count any instance of the word error?
# your code here
with open ("Lab3Regex\\apache_log.txt", "r") as f:
    x = re.findall('error', data)
    print(len(x))


# Q6 Use regex to count any instance of the letter p?
# your code here
with open ("Lab3Regex\\apache_log.txt", "r") as f:
    x = re.findall('p', data)
    print(len(x))

# Q7 Use regex to find any instance of the string jk2_init?
# your code here
with open("Lab3Regex\\apache_log.txt", "r") as f:
    for line in f:
        if "jk2_init" in line:
            print(line)

# Q8 Use regex to find any appearance of the number 6754?
# your code here
with open("Lab3Regex\\apache_log.txt", "r") as f:
    for line in f:
        if "6754" in line:
            print(line)

# Q9 Use regex to find any appearance of the number 6?
# your code here
with open("Lab3Regex\\apache_log.txt", "r") as f:
    for line in f:
        if "6" in line:
            print(line)

# Q10 Use regex to find any ip addresses?
# your code here
ipadd =  re.findall("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", data)
print(ipadd)

# Q11 Create a script that will ask for user input, ask the user to enter a letter, then use regex to return any matches of that letter in the file?
# your code here
userInput = input("Enter a letter you want to search for: ")

with open("Lab3Regex\\apache_log.txt", "r") as f:
    for line in f:
        if str(userInput) in line:
            print("Here are all the lines with that letter: " + line)

# Q12 adapt your answer from Q11, to use a function to search the file, the function should take one parameter - the letter you are searching for?
# your code here
def letterSRC():

    userInput = input("Enter a letter you want to search for: ")

    with open("Lab3Regex\\apache_log.txt", "r") as f:
        for line in f:
            if str(userInput) in line:
                print("Here are all the lines with that letter: " + line)

letterSRC()

