from translate import Translator

# translator("input.txt", "output.txt")

translator = Translator(to_lang="ja")

try:
    with open(r'''db.txt''', mode='r') as translate:
        text = translate.read()
        result = translator.translate(text)
        print(result)
        try:
            with open('db_translate.txt', mode='a',encoding='utf-8') as db_translate:
                db_translate.write(result)
        except IOError as err:
            print(f"Error: {err}")
            raise err
except IOError as err:
    print(f"Error: {err}")
    raise err



