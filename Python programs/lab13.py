# Lab #13
# Coadiey Bryan/C00039405
# Lecture Section #3
# create an empty list to store the key for the test
key = []
print()
print("Grading Key: ")
# open the file of test key answers
infile = open("key.py", "r")
# read 20 characters from the file
for i in range(20):
    letter = infile.readline().strip()
    # append that letter to the test key list
    key.append(letter)
# print your key list, all on one line
print(key)
print()
# close the file of test key answers
infile.close()
# open the file of student answers
infile = open("studentAnswers.py", "r")
print("Student Grades: ")
# read 5 student answer sets
for i in range(5):
    # read an answer line
    answer = infile.readline().strip()
    # process a student's 20 answers, look for matches with key list
    count = 0
    for i in range(20):
        if key[i] == answer[i]:
            count += 1
        else:
            count +=0
    # print their grade
    print("Grade =", count, "/20")
# close the student answers file
infile.close()