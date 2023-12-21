import palindromeChecker

def test_single():
    answer = palindromeChecker.palindromeChecker('a')
    actualAnswer = True
    assert answer == actualAnswer

def test_double():
    answer = palindromeChecker.palindromeChecker('aa')
    actualAnswer = True
    assert answer == actualAnswer

def test_double_wrong():
    answer = palindromeChecker.palindromeChecker('ab')
    actualAnswer = False
    assert answer == actualAnswer

def test_palendrome():
    answer = palindromeChecker.palindromeChecker('racecar')
    actualAnswer = True
    assert answer == actualAnswer