def count_semicolons(input_string):
    return input_string.count(';')
text = 'jeeva; raja;;'
result = count_semicolons(text)
print(f"Number of semicolons: {result}")