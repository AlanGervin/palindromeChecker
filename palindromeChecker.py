# this file contains the palindromeChecker. returns a boolean value

def getHalfOfStringLengthFloored(string):
  return len(string)//2

def getStringFromRange(string, range):
  returnString = ""
  for n in range:
    returnString += string[n]
  return returnString

def isStringOddLength(string):
  remainder = len(string) % 2
  if (remainder == 0):
    return False
  else:
    return True
  
def splitStringInHalfIntoArry(string):
    length = len(string)
    halfLengthOfString = getHalfOfStringLengthFloored(string)
    firstHalfRange = range(halfLengthOfString)
    firstHalfOfWord = getStringFromRange(string, firstHalfRange)

    isOddLength = isStringOddLength(string)
 
    if (isOddLength):
      secondHalfRange = range(halfLengthOfString+1, length)
    else:   
      secondHalfRange = range(halfLengthOfString, length)
  
    secondHalfOfWord = getStringFromRange(string, secondHalfRange)
    return [firstHalfOfWord, secondHalfOfWord]


def palindromeChecker(string):
  # returns true as an edge case for strings of one character
  if (len(string) == 1):
    return True 
  wordHalfArry = splitStringInHalfIntoArry(string)
  #arrayLocation is the location in the secondHalfOfWord in the for loop
  halfWordLength = len(wordHalfArry[1])

  for n in range(halfWordLength):
    firstHalfLetter = wordHalfArry[0][n]
    secondHalfLetter = wordHalfArry[1][halfWordLength-1]
    print(f'comparing letters {firstHalfLetter} and {secondHalfLetter}')
    if secondHalfLetter != firstHalfLetter:
      return False
    else:
      halfWordLength -= 1 
  return True
