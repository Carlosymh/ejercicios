def polindromo(word):
    word=word.replace(' ','').lower()
    newWord=''
    for letters in word:
        newWord=letters+newWord
    print(newWord)
    if word == newWord:
        return 'Es polindromo'
    else:
        return 'No es polindromo'
print(polindromo('Anita lava la tina'))
