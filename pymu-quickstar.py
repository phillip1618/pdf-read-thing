import fitz
doc = fitz.open('cp44007.pdf')

page1 = doc[0]
words = page1.get_text("words")
print(words)