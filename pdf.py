import fitz

class PDF:
    def __init__(self, file):
        self.file = file
        self.doc = fitz.open(file)

        self.page1 = self.doc[0]
        self.page2 = self.doc[1]
        self.page1_words = self.page1.get_text("words")
        self.page2_words = self.page2.get_text("words")

        self.county, self.state = self.get_location()
        self.number_of_farms = self.single_line_info(fitz.Rect(104, 288, 265, 300), self.page1_words)
        self.land_in_farms = self.single_line_info(fitz.Rect(122, 302, 265, 313), self.page1_words)
        self.average_size_of_farms = self.single_line_info(fitz.Rect(150, 316, 265, 327), self.page1_words)

    def get_words_page(self, page):
        return page.get_text("words")

    def words_in_rect(self, rect, page_words):
        words_rect = [w for w in page_words if fitz.Rect(w[:4]) in rect]
        return words_rect

    def make_text(self, words):
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
    
    def get_location(self):
        location_rect = fitz.Rect(35, 144, 201, 186)
        location_words = self.words_in_rect(location_rect, self.page1_words)

        location_line_text = self.make_text(location_words)
        location_text_list = location_line_text.splitlines()

        county = location_text_list[0]
        state = location_text_list[1]

        return county, state

    def single_line_info(self, rect, page_words):
        line_words = self.words_in_rect(rect, page_words)
        line_text = self.make_text(line_words)
        return line_text

if __name__ == '__main__':
    pdf = PDF('cp44007.pdf')
    print(pdf.state)
    print(pdf.county)
    print(pdf.number_of_farms)
    print(pdf.land_in_farms)
    print(pdf.average_size_of_farms)

