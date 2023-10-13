def alarm_clock(day, vacation):
    return '7:00' if 1 <= day <= 5 and not vacation else '10:00' if not 1 <= day <= 5 and not vacation else '10:00' if 1 <= day <= 5 and vacation else 'off'