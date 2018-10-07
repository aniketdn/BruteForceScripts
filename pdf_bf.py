import itertools, os, PyPDF2

f = open("dict.txt", "w")
f.truncate(0)
fname = "abc"
print(os.walk("."))
for r, d, f in os.walk("."):
	print(r)
    for filename in files:
        if filename.endswith(".pdf"):
            fname=filename
print(fname)
f.write("bac321\n")
alphabets = ['a', 'b', 'c', 'd', 'e', '1', '2', '3', '4', '5']
count=6
words = itertools.product(alphabets, repeat = count)
for word in words:
	f.write(''.join(word)+"\n")

print("Word List created")
dictionary="dict.txt"

print("Check if file is pdf:")
try:
	fpdf=PyPDF2.PdfFileReader(open(fname,"rb"))
except PyPDF2.utils.PdfReadError:
	print("Error in reading pdf")
	
print("Encryption status")	
print(fpdf.isEncrypted)

password = None
print("Bruteforcing")
f=open(dictionary,"r")
for line in f.readlines():
	password = line.strip('\n')
	if(fpdf.decrypt(password)):
		print("Password is>>"+password)
		#fpdf.decrypt(password)
		pages=fpdf.getPage(0)
		content=pages.extractText()
		print("File contents:")
		print(content.encode('utf-8'))
		break
	else:
		continue

print("Done")
