def hour_range_stadistics(data, from_time, to_time):
    bull_days = 0
    bear_days = 0
    lateral_days = 0

    # Filter candles for the range
    candles = [candle for candle in data if
               from_time == candle.get_hour_from_timestamp() or to_time == candle.get_hour_from_timestamp()]

    from_candle_max = candles[0].get_max_from_candle()  # Initial close, e.g. 09:00
    to_candle_max = candles[1].get_max_from_candle()  # e.g. 10:00
    both_days = 0
    day = candles[0].get_date_from_timestamp()

    for candle in candles:
        current_day = candle.get_date_from_timestamp()

        if day != current_day and both_days < 2:  # In case we only have one of two candles from the range
            both_days = 0
            if is_end_of_list(candles, candle):
                day = candles[candles.index(candle) + 1].get_date_from_timestamp()

        if candle.get_full_date() == current_day + ' ' + from_time:
            from_candle_max = candle.get_max_from_candle()
            both_days += 1
        elif candle.get_full_date() == current_day + ' ' + to_time:
            to_candle_max = candle.get_max_from_candle()
            both_days += 1

        if both_days == 2:  # if we have both candles, update the result
            if from_candle_max < to_candle_max:
                bull_days += 1
            elif from_candle_max == to_candle_max:
                lateral_days += 1
            elif from_candle_max > to_candle_max:
                bear_days += 1
            both_days = 0

            if is_end_of_list(candles, candle):  # update the day if there's a next candle
                day = candles[candles.index(candle) + 1].get_date_from_timestamp()

    result = {}
    result['bullish'] = bull_days
    result['bearish'] = bear_days
    result['equal'] = lateral_days
    result['total'] = bull_days + bear_days + lateral_days

    return result


def range_percentage(matches, total_days):
    percentage = float(matches) / float(total_days) * 100
    return str(round(percentage, 2))


def is_end_of_list(list, item):
    return (list.index(item) + 1) < len(list)
