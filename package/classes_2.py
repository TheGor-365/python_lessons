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


class TableFormatter:
    def __init__(self, table):
        self._table = table

    def to_csv(self):
        return "\n".join(",".join(map(str, row)) for row in self._table.get_table())


if __name__ == '__main__':
    table = Table(3)
    table.add_row([1, 2, 3])
    table.add_row([3, 2, 1])
    print(table.get_table())

    formatter = TableFormatter(table)
    print(formatter.to_csv())
