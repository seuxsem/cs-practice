def parse_event(line):
    line = line.strip()
    if not line:
        raise ValueError('Пустая строка')
    line_parts = line.split(' ')
    if len(line_parts) >= 3:
        time, level, *message = line_parts
        message = ' '.join(message).strip()
    else:
        raise ValueError("Строка не делится на 3 части")
    valid_levels = {'DEBUG', 'INFO', 'WARNING', 'ERROR'}
    if level not in valid_levels:
        raise ValueError(f'Незнакомый уровень логирования: {level}')

    return {
        'time': time,
        'level': level,
        'message': message
    }

