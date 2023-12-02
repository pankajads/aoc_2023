#pass your puzzle input in below path
filename="input2.txt"
sum=0

#Fuction will help to find word and pull the respective digit
def convert_words_digit(str):
    str = str.replace('one', 'o1ne')
    str = str.replace('two', 't2wo')
    str = str.replace('three', 't3hree')
    str = str.replace('four', 'f4our')
    str = str.replace('five', 'f5ive')
    str = str.replace('six', 's6ix')
    str = str.replace('seven', 's7even')
    str = str.replace('eight', 'e8ight')
    str = str.replace('nine', 'n9ine')
    str = str.replace('zero', 'z0ero')
    return str

#Reading Input file and parse it line by line
with open(filename) as filehandler:
    numarray=[]
    for line in filehandler.readlines():
        line = convert_words_digit(line)
        #print(line)
        #initialise 
        numarray=[]
        for i in range(0,len(line)):
            item = line[i]
            try:
                if isinstance(int(item), int):
                    numarray.append(item)
                    #numarray.push
                else:
                    continue    
            except:
                continue
        #pull the first and last digit from array & add it in SUM    
        sum += int(numarray[0] + numarray[-1])
print(sum)
                