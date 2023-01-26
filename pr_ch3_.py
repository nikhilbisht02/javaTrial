from datetime import date


print('''Dear: <NAME>,
 you are selected !
 DATE: <|DATE|>''')
letter = '''Dear: <NAME>,
 you are selected !
 DATE: <|DATE|>'''
name = input("enter your name:")
date= input("enter date:")
letter= letter.replace("<NAME>",name)
letter= letter.replace("<|DATE|>",date)
print(letter)