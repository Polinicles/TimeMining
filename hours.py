import sys
from src.HistData.File.FileParser import FileParser
from src.HistData.Service.TimeRangeChecker import hour_range_stadistics, range_percentage

# Time is in Eastern Standard Time (EST) WITHOUT Day Light Savings adjustments


def main():
    filename = 'data/HistData/2019_EUR_USD_M1.csv'
    parser = FileParser(filename)
    ranges = [('000000', '010000'), ('010000', '020000'), ('020000', '030000'), ('030000', '040000'),
              ('040000', '050000'), ('050000', '060000'), ('060000', '070000'), ('070000', '080000'),
              ('080000', '090000'), ('090000', '100000'), ('100000', '110000'), ('110000', '120000'),
              ('120000', '130000'), ('130000', '140000'), ('140000', '150000'), ('150000', '160000'),
              ('160000', '170000'), ('170000', '180000'), ('180000', '190000'), ('190000', '200000'),
              ('200000', '210000'), ('210000', '220000'), ('220000', '230000'), ('230000', '235900')] # Do not overlap with next day

    for range in ranges:
        start = range[0]
        end = range[1]
        result = hour_range_stadistics(parser.extract_candles_data(), start, end)
        total = result['total']
        print start + ' to ' + end + ':'
        print 'bullish days: ' + str(result['bullish']) + ' - ' + range_percentage(result['bullish'], total) + ' %'
        print 'bearish days: ' + str(result['bearish']) + ' - ' + range_percentage(result['bearish'], total) + ' %'
        print 'equal days: ' + str(result['equal']) + ' - ' + range_percentage(result['equal'], total) + ' %'

    sys.exit(1)


if __name__ == '__main__':
    main()
