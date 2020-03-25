from src.HistData.Candle.Candle import Candle

class FileParser:
    timeIndex = 0
    openIndex = 1
    highIndex = 2
    lowIndex = 3
    closeIndex = 4
    cellSeparator = ';'
    fileOperation = 'rU'

    def __init__(self, filename):
        self.filename = filename

    # Get all rows from file
    # File format: DateTime Stamp; Bar OPEN Bid Quote; Bar HIGH Bid Quote; Bar LOW Bid
    def extract_candles_data(self):
        data = []
        f = open(self.filename, self.fileOperation)
        for line in f:
            lineData = line.split(self.cellSeparator)
            candle = Candle(
                lineData[self.timeIndex],
                float(lineData[self.openIndex]),
                float(lineData[self.highIndex]),
                float(lineData[self.lowIndex]),
                float(lineData[self.closeIndex])
            )
            data.append(candle)
        f.close()
        return data
