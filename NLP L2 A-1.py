#open the text file
text_file=open("C:\\Users\\ADMIN\\Downloads\\testing.txt",'r', encoding='utf-8')

#read the data
read_text=text_file.read()

#Datatype of the data read
print(type(read_text))
print("\n")

#print the entire story text
print(read_text)

#length of the text
print(len(read_text))
