def parse_record(line):
    line = line.split(';')
    if len(line) != 3:
        raise ValueError('полей не ровно 3')
    else:
        city, temperature_str, date = line
    if not city.strip() or not date.strip():
        raise ValueError('город или дата пустые')
    try:
        temperature = float(temperature_str)
    except ValueError:
        raise ValueError('температура не число')
    return {
        'city': city,
        'temperature': temperature,
        'date': date
    }

def read_valid(lines):
    valid_records = []
    for line in lines:
        if not line:
            continue
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            continue
    return valid_records

def average_by_city(records):
    totals = {}
    counts = {}
    for r in records:
        city = r['city']
        totals[city] = totals.get(city, 0.0) + r['temperature']
        counts[city] = counts.get(city, 0) + 1
    averages = {}
    for city in totals:
        averages[city] = round(totals[city] / counts[city], 1)
    return averages

def warmest_city(records):
    if not records:
        return ''
    averages = average_by_city(records)
    best_city = ''
    for city in averages:
        if best_city == '':
            best_city = city
        elif averages[city] > averages[best_city]:
            best_city = city
        elif averages[city] == averages[best_city] and city < best_city:
            best_city = city
    return best_city


