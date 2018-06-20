# define our method
def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text
# our text the replacement will take place
f = open("chuck.py", 'r').read()
print(f)
# f now holds the text of the file you opened

my_text = f
# our dictionary with our key:values.
# we want to replace 'H' with '|-|'
# 'e' with '3' and 'o' with '0'
reps = {'Chuck':'Angelica', 'Norris':'Colliver'}
 
# bind the returned text of the method
# to a variable and print it
txt = replace_all(my_text, reps)
print(txt)    # it prints '|-|3ll0 3v3ryb0dy'
 
# of course we can print the result
# at once with:
# print replace_all(my_text, reps)
