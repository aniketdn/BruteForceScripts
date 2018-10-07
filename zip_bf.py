import itertools, os
import zipfile

f = open("dict.txt", "w")
f.truncate(0)
fname = "abc"

for root, dirs, files in os.walk("."):
    for filename in files:
        if filename.endswith(".zip"):
            fname=filename
print(fname)

alphabets = ['a', 'b', 'c', 'd', 'e', '1', '2', '3', '4', '5']
count=6
words = itertools.product(alphabets, repeat = count)
for word in words:
	f.write(''.join(word)+"\n")


dictionary="dict.txt"
password = None
print("Bruteforcing")

file_to_open = zipfile.ZipFile(fname)
f=open(dictionary,"r")
for line in f.readlines():
	password = line.strip('\n')
	try:
		file_to_open.extractall(pwd=password)
		print("Brute force successful", password)
		break
	except:
		pass


for root, dirs, files in os.walk("."):
    for filename in files:
        if filename.endswith(".txt"):
			if(filename!="dict.txt"):
				fname=filename

f1=open(fname,"r")
print("File contents are:>>>>")
for line in f1.readlines():
	print(line)

print("Done")



