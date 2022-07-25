morse_code_dict = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '.': '.-.-.-',
    ',': '--..--',
    '-': '-....-',
    '?': '..--..',
    '!': '-.-.--',
    "'": '.----.',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----'
}

# reversed dictionary
morse_to_text_dict = {val: key for (key, val) in morse_code_dict.items()}


def text_to_morse(text):
    morse_message = ''
    for character in text:
        if character in morse_code_dict:
            # spaces are needed to morse characters readable
            morse_message += (morse_code_dict[character] + ' ')
        else:
            morse_message += ' '

    print(morse_message)


def morse_to_text(message):
    text_message = ''
    character = ''
    for symbol in message:
        if symbol == '.' or symbol == '-':
            character += symbol
        else:
            if character != ' ':
                if character == '' and symbol == ' ':
                    text_message += ' '
                else:
                    text_message += morse_to_text_dict[character]
                    # need to reset character to start forming the new one
                    character = ''
    text_message += morse_to_text_dict[character]
    print(text_message)


typed = input("What is the type of the message? Type T for text or M for Morse:\n").upper()
if typed == 'T':
    text = input("Type your message:\n").upper()
    text_to_morse(text)
elif typed == 'M':
    message = input("Type your message with spaces between each letter. The program accepts letters, numbers, "
                    "and five symbols ( . , ' ? !):\n")
    morse_to_text(message)
else:
    print("I didn't get that. Please try again.")





