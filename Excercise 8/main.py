def writeToFile(filename, text):
    with open(filename, 'w') as fh:
        fh.write(text)

def appendToFile(filename, text):
    with open(filename, 'a') as fh:
        fh.write(text)

def readFromFile(filename):
    with open(filename, 'r') as fh:
        return fh.read()


writeToFile('greet.txt', 'Hello!\n') 
appendToFile('greet.txt', 'Goodbye!\n') 

### Test Case
assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n' 
