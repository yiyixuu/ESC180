def squirrel_play(temp, is_summer):
    return (60 <= temp <= 100 and is_summer) or (60 <= temp <= 90 and not is_summer)