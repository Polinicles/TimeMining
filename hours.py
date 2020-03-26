import sys
from src.HistData.File.FileParser import FileParser

def hour_range_stadistics(data, fromTime, toTime):
    bullDays = 0
    bearDays = 0
    lateralDays = 0

    candles = [candle for candle in data if fromTime == candle.get_hour_from_timestamp() or toTime == candle.get_hour_from_timestamp()]

    fromCandleMin = candles[0].get_min_from_candle()  # Initial open 09:00
    fromCandleMax = candles[0].get_max_from_candle()  # Initial close 09:00
    toCandleMin = candles[1].get_min_from_candle() # 10:00
    toCandleMax = candles[1].get_max_from_candle() # 10:00
    day = candles[0].get_date_from_timestamp()  # Initial day

    for candle in candles:
        currentDay = candle.get_date_from_timestamp()
        if currentDay == day:
            if candle.get_full_date() == currentDay + ' ' + fromTime:
                fromCandleMin = candle.get_min_from_candle()
                fromTimeMax = candle.get_max_from_candle()
            elif candle.get_full_date() == currentDay + ' ' + toTime:
                toCandleMin = candle.get_min_from_candle()
                toCandleMax = candle.get_max_from_candle()
        else:
            if fromCandleMax > toCandleMin:
                bullDays += 1
            elif fromCandleMax == fromCandleMin:
                lateralDays += 1
            else:
                bearDays += 1
            fromCandleMin = candle.get_min_from_candle()
            fromCandleMax = candle.get_max_from_candle()
            day = currentDay
    print fromTime + ' to ' + toTime + ':'
    print 'bullish days ' + str(bullDays)
    print 'bearish days ' + str(bearDays)
    print 'equal days ' + str(lateralDays)

def main():
    filename = 'data/HistData/2019_EUR_USD_M1.csv'
    parser = FileParser(filename)
    hour_range_stadistics(parser.extract_candles_data(), '090000', '100000')
    sys.exit(1)

if __name__ == '__main__':
    main()
