def parse_record(line):
    line = line.split(';')
    if len(line) != 3:
        raise ValueError('полей не ровно 3')
    else:
        city, temp_str, date = line
    if not city.strip() or not date.strip():
        raise ValueError('город или дата пустые')
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError('температура не число')
    return {
        'city': city,
        'temp': temp,
        'date': date
    }

    

