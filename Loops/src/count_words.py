#this program is for count the maximum time occurence of any word in the file
# and just find out the word in the file and display it on the screen 
# it also show how many times it occures in the file

name=input('Enter file: ')
handle= open(name,'r')      #open the file in read access mode
text=handle.read()          #read the above opened file
words=text.split()          #split the words inside the files for analysis
counts=dict()
for word in words:
    counts[word]=counts.get(word,0) + 1
bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword=word
        bigcount=count
         
print(bigword)
print(bigcount)