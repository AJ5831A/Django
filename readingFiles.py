countryFile = open('countries.txt' , 'r+')

#print(countryFile.readable())

print(countryFile.read())
countryFile.write("Halwa")
print(countryFile.read())
countryFile.close()
