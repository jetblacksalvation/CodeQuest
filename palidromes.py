for x in range(int(input())):
    words = [input() for z in range(int(input()))]
    results = []
    for word in words:
        print(len(words))
 
        #temporarily store substring from zero->middle
        #from middle to end store substring, flip string and check
        # print(len(word)//2)
        # print(word[0:len(word)//2].lower(), '=', word[len(word)//2 +(0 if len(word)%2 == 0 else 1) :][::-1].lower())

        if word[0:len(word)//2].lower() == word[len(word)//2  +(0 if len(word)%2 == 0 else 1):][::-1].lower():
            pass
        else:
            results.append(words.index(word)+1)
        pass#odd
        
    if results == []:
        print(True)
    else:
        print(False, '- ', end='')
        print(*results, sep=', ')