def toString(fileName):
    #This function returns the text from a given file.
    #Any new lines are written as \n
    f = open(fileName)
    out = ""
    for line in f:
        out += line
    return out
#print(toString("ExampleText.txt")=="Here is the text\ni am another line")

def longestLine(fileName):
    #Given a file return the longest line from within that file
    lengths = []
    f = open(fileName)
    for line in f:
        lengths.append([len(line), line])
    return max(lengths)[1]

longestLine('hello.txt')

def toBinary(fileName):
    #Given a file that is only 0's and 1's return a list of the file broken into bytes.
    #An example return might be ['01101001', '00101010', '1010']
    newList = []
    string = toString(fileName)
    while string:
        append = ''
        while len(append) < 8:
            if len(string) < 8 and append == '':
                append = string
                string = ''
                break
            elif string[0] == "\n":
                string = string[1:]
            else:
                append += string[0]
                string = string[1:]
        newList.append(append)
    return newList
