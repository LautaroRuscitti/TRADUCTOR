from translate import Translator

traductor = Translator(from_lang="en", to_lang="es")
texto = input("Ingrese la o las palabras que quiera en ingles para poder traducirlo: ")
traduccion = traductor.translate(texto)
print(traduccion)

traductor = Translator(from_lang="es", to_lang="en")
texto = input("Ingrese la o las palabras que quiera en español para poder traducirlo: ")
traduccion = traductor.translate(texto)
print(traduccion)
