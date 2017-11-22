#reading a exist file,remember closed file.
f = open('txt/readme.txt','r')  #reading
data = f.read()
print(data)
f.close()

#writing some new test for exist file,then the content will be changed
f = open('txt/readme.txt','w')
data = 'this is new file~~'
_data = f.write(data)
print(data)
f.close()

#writing something, then you will get a new file in at once
data2 = 'I wanna to set a new file'
f = open('txt/newFile.txt','w')   #writing
_data2 = f.write(data2)
print(data2)
f.close()

#appending some contentes to exist file
data3 = 'appending :yeah, so sorry that i can\'t go around with you'
f3 = open('txt/newFile.txt','a')  #appending
_data3 = f3.write(data3)  #still write
print(data3)
f3.close()
