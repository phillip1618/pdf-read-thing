import fitz

class PDF:
    def __init__(self, file):
        self.file = file
        self.doc = fitz.open(file)

        self.page1 = self.doc[0]
        self.page2 = self.doc[1]
        self.page1_words = self.page1.get_text("words")
        self.page2_words = self.page2.get_text("words")
        print(self.page2_words)

        self.county, self.state = self.multi_line_info(fitz.Rect(35, 144, 201, 186), self.page1_words)
        self.number_of_farms = self.single_line_info(fitz.Rect(104, 288, 265, 300), self.page1_words)
        self.land_in_farms = self.single_line_info(fitz.Rect(122, 302, 265, 313), self.page1_words)
        self.average_size_of_farms = self.single_line_info(fitz.Rect(150, 316, 265, 327), self.page1_words)

        self.acres_1_9, self.acres_10_49, self.acres_50_179, self.acres_180_499, self.acres_500_999, \
            self.acres_1000_plus = self.multi_line_info(fitz.Rect(448, 601, 464, 679), self.page1_words)

        self.cropland, self.pastureland, self.woodland, self.other = \
            self.multi_line_info(fitz.Rect(560, 372, 577, 423), self.page1_words)

        self.broilers, self.cattle, self.goats, self.hogs, self.horses, self.layers, self.pullets, \
            self.sheep, self.turkeys = self.multi_line_info(fitz.Rect(500, 572, 577, 667), self.page2_words)

        self.crop_sales = self.single_line_info(fitz.Rect(63, 159, 302, 171), self.page2_words)
        self.livestock_sales = self.single_line_info(fitz.Rect(175, 292, 302, 304), self.page2_words)

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

    def single_line_info(self, rect, page_words):
        line_words = self.words_in_rect(rect, page_words)
        line_text = self.make_text(line_words)
        return line_text

    def multi_line_info(self, rect, page_words):
        multi_line_words = self.words_in_rect(rect, page_words)
        multi_line_text = self.make_text(multi_line_words)
        multi_text_list = multi_line_text.splitlines()

        for text in multi_text_list:
            yield text

if __name__ == '__main__':
    pdf = PDF('cp44007.pdf')
    print(pdf.state)
    print(pdf.county)

    print(pdf.crop_sales)
    print(pdf.livestock_sales)