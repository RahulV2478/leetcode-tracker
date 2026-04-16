# Last updated: 4/15/2026, 11:49:22 PM
class Spreadsheet(object):

    def __init__(self, rows):
        """
        :type rows: int
        """
        row = [0] * 26
        self.matrix = [[0 for _ in range(26)] for _ in range(rows)]
        

    def setCell(self, cell, value):
        """
        :type cell: str
        :type value: int
        :rtype: None
        """
        col = ord(cell[0]) - ord("A")
        row = int(cell[1:]) - 1
        self.matrix[row][col] = value
            

    def resetCell(self, cell):
        """
        :type cell: str
        :rtype: None
        """
        self.setCell(cell, 0)

    def getValue(self, formula):
        """
        :type formula: str
        :rtype: int
        """
        parts = formula.split("+")
        parts[0] = parts[0][1:]
        s = 0
        for part in parts:
            if part[0].isalpha():
                col = ord(part[0]) - ord("A")
                row = int(part[1:]) - 1
                part = self.matrix[row][col]
            s += int(part)
        return s
                



# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)