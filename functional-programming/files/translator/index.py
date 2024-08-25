from idlelib.iomenu import encoding

from translate import Translator

translator = Translator(to_lang='es')
try:
    print('enter text to translate below\n')
    text = input(": ")
    result = translator.translate(text)
    print('\n')
    print(f'{result}')
    try:
        with open('db_translate.txt', mode='a', encoding='utf-8') as translated_words:
            translated_words.write(result)
    except IOError as err:
        print(f"IOError!!! {err}")
except:
    print("error please some went wrong!!!")
