class Candle:
    dateIndex = 0
    hourIndex = 1
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

    # Get date format "HHMMSS" from "YYYYMMMDD HHMMSS"
    def get_hour_from_timestamp(self):
        date = self.time.split(self.timeSeparator)
        return date[self.hourIndex]

    def get_full_date(self):
        return self.time

    # Get min value between Open / Close values
    def get_min_from_open_close(self):
        return self.open if self.open <= self.close else self.close

    # Get max value between Open / Close values
    def get_max_from_candle(self):
        return self.close if self.close > self.open else self.open

    def get_open(self):
        return self.open

    def get_close(self):
        return self.close
