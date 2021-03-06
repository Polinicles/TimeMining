import sys
from src.HistData.File.FileParser import FileParser

# TODO: improve by getting only the first and last candle from everyday
def days_stadistics(data):
    bullDays = 0
    bearDays = 0
    lateralDays = 0

    startCandleMin = data[0].get_min_from_open_close()  # Initial open
    startCandleMax = data[0].get_max_from_candle()  # Initial close
    lastCandleMin = data[0].get_min_from_open_close()
    lastCandleMax = data[0].get_max_from_candle()
    day = data[0].get_date_from_timestamp()  # Initial day

    for candle in data:
        currentDay = candle.get_date_from_timestamp()
        if currentDay == day:  # if same day -> update min / max
            lastCandleMin = candle.get_min_from_open_close()
            lastCandleMax = candle.get_max_from_candle()
        else:
            if startCandleMax > lastCandleMin:
                bullDays += 1
            elif startCandleMax == startCandleMin:
                lateralDays += 1
            else:
                bearDays += 1
            startCandleMin = candle.get_min_from_open_close()
            startCandleMax = candle.get_max_from_candle()
            day = currentDay
    print 'bullish days ' + str(bullDays)
    print 'bearish days ' + str(bearDays)
    print 'equal days ' + str(lateralDays)


def main():
    filename = 'data/HistData/2019_EUR_USD_M1.csv'
    parser = FileParser(filename)
    days_stadistics(parser.extract_candles_data())
    sys.exit(1)

if __name__ == '__main__':
    main()
