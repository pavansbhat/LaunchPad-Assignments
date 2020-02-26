sentence=str(input("Enter a sentence to reverse"))
inpWrd=sentence.split(" ")
outwrd=inpWrd[-1::-1]
outOne=" ".join(outwrd)
print(outOne.capitalize())
