import ast, string, sys

with open('wordleWords.txt') as f:
    lines = f.readlines()
words = [ast.literal_eval(line) for line in lines][0]

def wordle():
    frequencyVals = letterFrequency(words)
    wordVals = wordEval(words, frequencyVals)
    
    attempt = 0
    while attempt < 6:
        attempt += 1 
        guess = bestWord(words, wordVals)
        print('guess #', attempt, '->', guess, '\n')
        print('was this the correct answer? yes(1) no(0)')

        flag = False
        choice = ""
        while not flag:
            choice = input('choice -> ')
            if choice == '0' or choice == '1':
                flag = True
            else:
                print('invalid input')
        
        if choice == '1':
            print('\nword found, ending program')
            return
        else:
            if attempt == 6:
                print('\nword not found, ending program')
                return
            eleminateWords(words, guess)


def eleminateWords(words, guess):
    print('\ninput 5 digit sequence representing wordle colors: black(0) yellow(1) green(2)')
    flag = False
    vals = ""
    while not flag:
        vals = input('input ->')
        if validSequence(vals):
            flag = True
        else:
            print('invalid input')

    index = 0
    for num in vals:
        if num == '0':
            blackLetter(words, guess, index)
        elif num == '1':
            yellowLetter(words, guess, index)
        else:
            greenLetter(words, guess, index)
        index += 1

def blackLetter(words, guess, index):
    temp = [word for word in words if guess[index] in word]
    for x in temp:
        words.remove(x)

def yellowLetter(words, guess, index):
    temp = [word for word in words if guess[index] ==  word[index]]
    temp += [word for word in words if guess[index] not in word]
    for x in temp:
        words.remove(x)

def greenLetter(words, guess, index):
    temp = [word for word in words if guess[index] !=  word[index]]
    for x in temp:
        words.remove(x)

def validSequence(seq):
    if len(seq) != 5:
        return False
    lst = list(set(seq))
    lst = [x for x in lst if x != '0' and x != '1' and x != '2']
    if lst != []:
        return False
    return True

def letterFrequency(words):
    listAlphabet = list(string.ascii_lowercase)
    frequencyVals = {}
    for letter in listAlphabet:
        frequencyVals[letter] = 0
    for word in words:
        for letter in word:
            frequencyVals[letter] += 1
    return frequencyVals

def wordEval(words, frequencyVals):
    wordVals = {}
    for word in words:
        score = 0
        uniqueLetters = ''.join(set(word))
        for letter in uniqueLetters:
            score += frequencyVals[letter]
        wordVals[word] = score
    return wordVals

def bestWord(words, wordVals):
    if words == []:
        return ''
    maxWord = words[0]
    for word in words:
        if wordVals[word] > wordVals[maxWord]:
            maxWord = word 
    return maxWord

wordle()