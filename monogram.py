for input_count in range(int(input())):
    monogram_list = []
    for word_count in range(int(input())):
        nested_temp_letters = ''
        for letter in (input()+' ').split():
            nested_temp_letters += letter[0].capitalize()
        pass
        monogram_list.append(*[nested_temp_letters[0] + nested_temp_letters[2] + nested_temp_letters[1]])
    print(*monogram_list , sep='\n')
    pass
