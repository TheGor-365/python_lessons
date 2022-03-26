class Table:
    def __init__(self, n_cols):
        self.rows = []
        self.n_cols = n_cols

    def shape(self):
        return len(self.rows), self.n_cols

    def get_table(self):
        return self.rows

    def add_row(self, item):
        if len(item) != self.n_cols:
            raise Exception("Incorrect length")
        self.rows.append(item)
