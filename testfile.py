language = 'рус'
step_decipher = 5
text = 'Eat some more of these soft French rolls, and drink some tea y.'
newtext = []

if language == 'рус':
    for i in range(len(text)):
        if 65 <= ord(text[i]) <= 90 or 97 <= ord(text[i]) <= 122:
            newtext.append(chr(ord(text[i]) + step_decipher))
        else:
            newtext.append(text[i])
print(*newtext)
