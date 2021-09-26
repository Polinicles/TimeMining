import sys
from src.HistData.File.FileParser import FileParser

# Time is in Eastern Standard Time (EST) WITHOUT Day Light Savings adjustments


def main():
    filename = 'data/HistData/2019_EUR_USD_M1.csv'
    parser = FileParser(filename)
    data = parser.extract_candles_data()

    same_close = []
    same_open = []
    full_match = []
    counter = 0
    dates = []

    for candle in data:
        open_matches = [match for match in data if candle.get_open() == match.get_open() and candle != match]
        close_matches = [match for match in data if candle.get_close() == match.get_close() and candle != match]
        full_matches = [match for match in data if candle.get_open == match.get_open() and candle.get_close() == match.get_close()]

        if len(close_matches) == 0:
            continue

        coincidences = []
        for match in close_matches:
            coincidences.append(match.get_full_date())
            data.remove(match)

        data.remove(candle)
        same_open.append(open_matches)
        same_close.append(close_matches)
        dates.append(coincidences)
        full_match.append(full_matches)

        counter += 1
        if counter > 50:
            break
    sys.exit(1)


if __name__ == '__main__':
    main()
