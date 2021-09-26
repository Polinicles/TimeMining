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
            line_data = line.split(self.cellSeparator)
            candle = Candle(
                line_data[self.timeIndex],
                float(line_data[self.openIndex]),
                float(line_data[self.highIndex]),
                float(line_data[self.lowIndex]),
                float(line_data[self.closeIndex])
            )
            data.append(candle)
        f.close()
        return data
