# main document of program
newtext = []

# Функция проверки корректности ввода слов
def exam_cipher(enter, choice):
    if enter not in choice:
        return True
    else:
        return False

# Функция шифрования пользовательского текста
def cipher_func(language, step_decipher, text):
    if language == 'англ':
        for i in range(len(text)):
            if 65 <= ord(text[i]) <= 90:
                if ord(text[i]) + step_decipher > 90:
                    newtext.append(chr(ord(text[i]) + step_decipher - 90 + 64))
                else:
                    newtext.append(chr(ord(text[i]) + step_decipher))
            elif 97 <= ord(text[i]) <= 122:
                if ord(text[i]) + step_decipher > 122:
                    newtext.append(chr(ord(text[i]) + step_decipher - 122 + 96))
                else:
                    newtext.append(chr(ord(text[i]) + step_decipher))
            else:
                newtext.append(text[i])
        return print(*newtext, sep='')
    elif language == 'рус':
        for i in range(len(text)):
            if 1072 <= ord(text[i]) <= 1103:
                if ord(text[i]) + step_decipher > 1103:
                    newtext.append(chr(ord(text[i]) + step_decipher - 1103 + 1071))
                else:
                    newtext.append(chr(ord(text[i]) + step_decipher))
            elif 1040 <= ord(text[i]) <= 1071:
                if ord(text[i]) + step_decipher > 1071:
                    newtext.append(chr(ord(text[i]) + step_decipher - 1071 + 1039))
                else:
                    newtext.append(chr(ord(text[i]) + step_decipher))
            else:
                newtext.append(text[i])
        return print(*newtext, sep='')

#  Функция дешифрования пользовательского текста
def decipher_func(language, step_decipher, text):
    if language == 'англ':
        for i in range(len(text)):
            if 65 <= ord(text[i]) <= 90:
                if ord(text[i]) - step_decipher < 65:
                    newtext.append(chr(90 - (64 - ord(text[i]) - step_decipher)))
                else:
                    newtext.append(chr(ord(text[i]) - step_decipher))
            elif 97 <= ord(text[i]) <= 122:
                if ord(text[i]) - step_decipher < 97:
                    newtext.append(chr(122 - (97 - ord(text[i]) - step_decipher)))
                else:
                    newtext.append(chr(ord(text[i]) - step_decipher))
            else:
                newtext.append(text[i])
        return print(*newtext, sep='')
    elif language == 'рус':
        for i in range(len(text)):
            if 1072 <= ord(text[i]) <= 1103:
                if ord(text[i]) - step_decipher < 1072:
                    newtext.append(chr(1103 - (1072 - ord(text[i]) - step_decipher)))
                else:
                    newtext.append(chr(ord(text[i]) - step_decipher))
            elif 1040 <= ord(text[i]) <= 1071:
                if ord(text[i]) - step_decipher < 1040:
                    newtext.append(chr(1071 - (1040 - ord(text[i]) - step_decipher)))
                else:
                    newtext.append(chr(ord(text[i]) - step_decipher))
            else:
                newtext.append(text[i])
        return print(*newtext, sep='')



print('Добро пожаловать в программу шифрования различных текстов с помощью шифра Цезаря!')

print('Вы хотите зашифровать или расшифровать сообщение?')
cipher = input()
choice_cipher = 'зашифроватьрасшифровать'
while exam_cipher(cipher, choice_cipher):
    print('Введите слово "зашифровать" или слово "расшифровать"')
    cipher = input()

print('Какой язык вы хотите использовать? (Русский - "рус", Английский - "англ"')
language = input()
choice_language = 'русангл'
while exam_cipher(language, choice_language):
    print('Введите "рус" если текст на русском языке или "англ" если текст на английском')
    language = input()

if language == 'рус' and cipher == 'зашифровать':
    print('Введите шаг шифрования от 1 до 31')
    step_cipher = int(input())
    print('Введите текст который хотите зашифровать:')
    text_cipher = input()
    print('Ваш зашифрованный текст:')
    cipher_func(language, step_cipher, text_cipher)
elif language == 'рус' and cipher == 'расшифровать':
    print('Введите шаг расшифровки от 1 до 31')
    step_decipher = int(input())
    print('Введите текст который хотите расшифровать:')
    text_cipher = input()
    print('Ваш расшифрованный текст:')
    decipher_func(language, step_decipher, text_cipher)
elif language == 'англ' and cipher == 'зашифровать':
    print('Введите шаг шифрования от 1 до 25')
    step_cipher = int(input())
    print('Введите текст который хотите зашифровать:')
    text_cipher = input()
    print('Ваш зашифрованный текст:')
    cipher_func(language, step_cipher, text_cipher)
elif language == 'англ' and cipher == 'расшифровать':
    print('Введите шаг расшифровки от 1 до 25')
    step_decipher = int(input())
    print('Введите текст который хотите расшифровать:')
    text_cipher = input()
    print('Ваш расшифрованный текст:')
    decipher_func(language, step_decipher, text_cipher)

