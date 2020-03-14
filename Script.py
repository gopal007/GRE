import os

wordCount = 0
bufferLines = []
colonIndexForLine = []
position = -1


# returns index of ':'
def getColonIndexForLine(line):
    return line.find(":")

# add wordCount to lines
def addWordCount(listOfLines):
    global wordCount
    for i in range(len(listOfLines)):
        dotIndex = listOfLines[i].find(".")
        line = listOfLines[i]
        if dotIndex <= 4 and (getColonIndexForLine(line) != -1):
            wordCount += 1
            line = line[dotIndex+1 : :]
            temp = str(wordCount) + ". "
            line = temp + line
            listOfLines[i] = line

# inserts spaces needed... before colon
def rearrangeLines(listOfLines, indexOfColons):
    for i in range(len(listOfLines)):
        index = indexOfColons[i]
        line = listOfLines[i]

        maxColonPosition = max(indexOfColons)
        if index == -1:
            pass
        colonStr = " " * (maxColonPosition - index) + ": "
        line = line.replace(":",colonStr)
        listOfLines[i] = line


# reads file and lines
def readFileAndCreateIndexes():
    file = open("Words", "r")
    for line in file:
        line = line.rstrip("\n")
        colonIndexForLine.append(getColonIndexForLine(line))
        bufferLines.append(line)
    file.close()
    addWordCount(bufferLines)


#crete file with same name and write to it
def writeNewFile():
    newWordFile = open("NewWordsFile", "w")
    for line in bufferLines:
        newWordFile.write(line)
        newWordFile.write("\n")
    newWordFile.close()

def printOutput():
    for line in bufferLines:
        print(line)


# execution starts from here
def main():
    readFileAndCreateIndexes()
    rearrangeLines(bufferLines ,colonIndexForLine)
    # if os.path.exists("Words"):
    #   os.remove("Words")
    # else:
    #   print("The file does not exist")
    # writeNewFile()
    printOutput()


main()
