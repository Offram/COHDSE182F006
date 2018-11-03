def getMode():

     while True:

         print('Do you wish to encrypt or decrypt a message?')

         mode = input().lower()

         if mode in 'encrypt e decrypt d'.split():

             return mode

         else:

             print('Enter either "encrypt" or "e" or "decrypt" or "d".')

mode = getMode()

#Input string
inputtext = input ("Input text:")


#Define character set
alphabetset = "abcdefghijklmnopqrstuvwxyz"


#Set Key
def getKey():

     key = 0

     while True:

         print('Enter the key number (1-%s)' % (26))

         key = int(input())

         if (key >= 1 and key <= 26):

             return key
key = getKey() 


if mode[0] == 'd':
	key = -key

#Define cipher variable
cipher =''


#Process
for c in inputtext:
    
 if c in alphabetset:
        
  cipher += alphabetset[(alphabetset.index(c)+key)%(len(alphabetset))]

#Output
print("The translated message is:" + cipher)
