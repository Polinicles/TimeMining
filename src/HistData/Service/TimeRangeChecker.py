def hour_range_stadistics(data, fromTime, toTime):
    bullDays = 0
    bearDays = 0
    lateralDays = 0

    # Filter candles for the range
    candles = [candle for candle in data if fromTime == candle.get_hour_from_timestamp() or toTime == candle.get_hour_from_timestamp()]

    fromCandleMax = candles[0].get_max_from_candle()  # Initial close, e.g. 09:00
    toCandleMax = candles[1].get_max_from_candle()  # e.g. 10:00
    bothDays = 0
    day = candles[0].get_date_from_timestamp()
    for candle in candles:
        currentDay = candle.get_date_from_timestamp()

        if day != currentDay and bothDays < 2: # In case we only have one of two candles from the range
            bothDays = 0
            if is_end_of_list(candles, candle):
                day = candles[candles.index(candle) + 1].get_date_from_timestamp()

        if candle.get_full_date() == currentDay + ' ' + fromTime:
            fromCandleMax = candle.get_max_from_candle()
            bothDays += 1
        elif candle.get_full_date() == currentDay + ' ' + toTime:
            toCandleMax = candle.get_max_from_candle()
            bothDays += 1

        if bothDays == 2: # if we have both candles, update the result
            if fromCandleMax < toCandleMax:
                bullDays += 1
            elif fromCandleMax == toCandleMax:
                lateralDays += 1
            elif fromCandleMax > toCandleMax:
                bearDays += 1
            bothDays = 0

            if is_end_of_list(candles, candle): # update the day if there's a next candle
                day = candles[candles.index(candle) + 1].get_date_from_timestamp()

    result = {}
    result['bullish'] = bullDays
    result['bearish'] = bearDays
    result['equal'] = lateralDays
    result['total'] = bullDays + bearDays + lateralDays

    return result


def range_percentage(matches, totalDays):
    percentage = float(matches) / float(totalDays) * 100
    return str(round(percentage, 2))

def is_end_of_list(list, item):
    return (list.index(item) + 1) < len(list)