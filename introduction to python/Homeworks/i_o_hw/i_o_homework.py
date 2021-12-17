f = open("student_names.txt","r+")


content = f.read() # qs1 : read all the file in a variable


content = content + "julia\ngarcia\nnogla\n "
f.write(content) # qs2 : write random names in the file 


# qs3 read the first line in a variable 
f.seek(0)
firstline = f.readline()
print(firstline)

# qs4 read the last n line of a file 
n = int(input("How many lines you want to read  ? "))
f.seek(0)
lines  = f.readlines()
for x in lines[-n:]:
    print(x)
    
    
#qs5 search fo a name in the file || note in order to be more a curate we can assume that each name is in a line
f.seek(0)
lines = f.readlines()
seekedName  = input("Give the name to seek : ")
print(seekedName in lines)

#qs6 generate files named after the alphabets 
for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    f = open(x+".txt","a")

f.close()