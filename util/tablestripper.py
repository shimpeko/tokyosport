from html.parser import HTMLParser

class TableStripper(HTMLParser):

    def __init__(self):
        super().__init__()
        self.reset()
        self.rows = []
        self.cols = []
        self.is_row = False
        self.is_col = False

    def handle_starttag(self, t, attr):
        if t.upper() == "TR":
            self.is_row = True
            self.rows.append([])
        if t.upper() == "TD":
            del self.cols[:]
            self.is_col = True

    def handle_data(self, d):
        if (self.is_row and self.is_col) == True:
            self.cols.append(d)

    def handle_endtag(self, t):
        if t.upper() == "TR":
            self.is_row = False
        if t.upper() == "TD":
            self.is_col = False
            self.rows[-1].append("".join(self.cols))

    def get_rows(self):
        return self.rows

