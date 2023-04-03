import pyttsx3 

meu_livro = open(r'AudioBook\book.txt', 'r')
texto_livro = meu_livro.readlines()
engine = pyttsx3.init()

for i in texto_livro:
    engine.say(i)
    engine.runAndWait()