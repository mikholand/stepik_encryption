def encryption_caesar(direction, language, step, text):
    lower_ru_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    upper_ru_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    lower_en_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_en_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    step = int(step)
    if language == 'ru':
        lower_alphabet = lower_ru_alphabet
        upper_alphabet = upper_ru_alphabet
        alphabet = 32
    elif language == 'en':
        lower_alphabet = lower_en_alphabet
        upper_alphabet = upper_en_alphabet
        alphabet = 26

    for i in range(len(text)):
        if direction == 'en':
            if text[i].isalpha():
                if text[i] == text[i].lower():
                    index_alpha = lower_alphabet.find(text[i])
                    print(lower_alphabet[(index_alpha + step) % alphabet], end='')
                elif text[i] == text[i].upper():
                    index_alpha = upper_alphabet.find(text[i])
                    print(upper_alphabet[(index_alpha + step) % alphabet], end='')
            else:
                print(text[i], end='')
        elif direction == 'de':
            if text[i].isalpha():
                if text[i] == text[i].lower():
                    index_alpha = lower_alphabet.find(text[i])
                    print(lower_alphabet[(index_alpha - step) % alphabet], end='')
                elif text[i] == text[i].upper():
                    index_alpha = upper_alphabet.find(text[i])
                    print(upper_alphabet[(index_alpha - step) % alphabet], end='')
            else:
                print(text[i], end='')


print('Добро пожаловать в программу, которая шифрует текст по методу Цезаря.\n')

direction = input('Что будем делать? Шифровать или дешифровать? Введите en/de ').lower()
while direction != 'en' and direction != 'de':
    direction = input('Вы ввели что-то не то. Пожалуйста, повторите ввод: en/de ').lower()

language = input('Какой язык? Русский или английский? Введите ru/en ').lower()
while language != 'ru' and language != 'en':
    language = input('Вы ввели что-то не то. Пожалуйста, повторите ввод: ru/en ').lower()

if language == 'ru':
    step = input('Введите шаг шифровки/дешифровки от 0 до 32 ').lower()
    while step.isdigit() is False or int(step) < 0 or int(step) > 32:
        step = input('Вы ввели что-то не то. Пожалуйста, повторите ввод шага шифровки/дешифровки ').lower()
elif language == 'en':
    step = input('Введите шаг шифровки/дешифровки от 0 до 26 ').lower()
    while step.isdigit() is False or int(step) < 0 or int(step) > 26:
        step = input('Вы ввели что-то не то. Пожалуйста, повторите ввод шага шифровки/дешифровки ').lower()

text = input('Введите текст для шифрования:\n')
while text.isspace() or text.isdigit() or text == '':
    text = input('Вы ввели что-то не то. Пожалуйста, повторите ввод текста:\n')

encryption_caesar(direction, language, step, text)
