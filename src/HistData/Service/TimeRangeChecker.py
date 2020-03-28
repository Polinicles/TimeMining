def hour_range_stadistics(data, fromTime, toTime):
    bullDays = 0
    bearDays = 0
    lateralDays = 0

    # Filter candles for the range
    candles = [candle for candle in data if fromTime == candle.get_hour_from_timestamp() or toTime == candle.get_hour_from_timestamp()]

    fromCandleMin = candles[0].get_min_from_candle()  # Initial open, e.g. 09:00
    fromCandleMax = candles[0].get_max_from_candle()  # Initial close, e.g. 09:00
    toCandleMin = candles[1].get_min_from_candle()  # e.g. 10:00
    toCandleMax = candles[1].get_max_from_candle()  # e.g. 10:00
    day = ''  # Initial day

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
    result = {}
    result['bullish'] = bullDays
    result['bearish'] = bearDays
    result['equal'] = lateralDays
    result['total'] = len(candles) / 2
    return result


def range_percentage(matches, totalDays):
    percentage = float(matches) / float(totalDays) * 100
    return str(round(percentage, 2))
