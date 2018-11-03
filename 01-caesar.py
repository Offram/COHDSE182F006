#Input
inputtext = input ("Input text:")


#Define character set
alphabetset = "abcdefghijklmnopqrstuvwxyz"


#Set Key
key = 3 


#Define cipher variable
cipher =''


#Process
for c in inputtext:
    
 if c in alphabetset:
        
  cipher += alphabetset[(alphabetset.index(c)+key)%(len(alphabetset))]

#Output
print("The encrypted message is:" + cipher)
