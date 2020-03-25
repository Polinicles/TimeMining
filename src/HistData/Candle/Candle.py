class Candle:
    dateIndex = 0
    timeSeparator = ' '

    def __init__(self, time, open, high, low, close):
        self.time = time
        self.open = open
        self.high = high
        self.low = low
        self.close = close

    # Get date format "YYYYMMDD" from "YYYYMMMDD HHMMSS"
    def get_date_from_timestamp(self):
        date = self.time.split(self.timeSeparator)
        return date[self.dateIndex]

    def get_min_from_candle(self):
        min = self.open if self.open <= self.close else self.close
        return min

    def get_max_from_candle(self):
        max = self.close if self.close > self.open else self.open
        return max
