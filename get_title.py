import fitz

# 35, 144, 201, 186

doc = fitz.open("cp44007.pdf")
page = doc[0]
words = page.get_text("words")
title_rect = fitz.Rect(35, 144, 201, 186)

mywords = [w for w in words if fitz.Rect(w[:4]) in title_rect]

def make_text(words):
    """Return textstring output of get_text("words").
    Word items are sorted for reading sequence left to right,
    top to bottom.
    """
    line_dict = {}  # key: vertical coordinate, value: list of words
    words.sort(key=lambda w: w[0])  # sort by horizontal coordinate
    for w in words:  # fill the line dictionary
        y1 = round(w[3], 1)  # bottom of a word: don't be too picky!
        word = w[4]  # the text of the word
        line = line_dict.get(y1, [])  # read current line content
        line.append(word)  # append new word
        line_dict[y1] = line  # write back to dict
    lines = list(line_dict.items())
    lines.sort()  # sort vertically
    return "\n".join([" ".join(line[1]) for line in lines])

print(make_text(mywords))