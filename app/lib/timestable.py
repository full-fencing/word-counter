class TimesTable():

    def __init__(self, maxNumber=12):
        self.maxNumber = maxNumber
        self.table = []
        self.generate_table()

    def generate_table(self):
        for i in range(1, self.maxNumber + 1):
            temporary_table = []
            for j in range(1, self.maxNumber + 1):
                temporary_table.append(i * j)
            self.table.append(temporary_table)

