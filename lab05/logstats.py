def parse_event(line: str) -> dict:
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

def count_levels(lines) -> dict:
    counts = {'DEBUG': 0, 'INFO': 0, 'WARNING': 0, 'ERROR': 0, 'BROKEN': 0}
    for line in lines:
        cleaned = line.strip()
        if not cleaned:
            continue
        try:
            event = parse_event(cleaned)
            counts[event['level']] += 1
        except ValueError:
            counts['BROKEN'] += 1
    return counts

def top_errors(lines, n: int) -> list[list]:
    error_counts = {}
    for line in lines:
        cleaned = line.strip()
        if not cleaned:
            continue
        try:
            event = parse_event(cleaned)
            if event['level'] == 'ERROR':
                msg = event['message']
                error_counts[msg] = error_counts.get(msg, 0) + 1
        except ValueError:
            continue

    sorted_errors = sorted(error_counts.items(), key=lambda x: (-x, x))
    return [list(item) for item in sorted_errors[:n]]

def format_report(counts: dict, errors: list[list]) -> str:
    lines = ['Отчёт по журналу', '']
    
    for level in sorted(counts.keys()):
        lines.append(f'{level}: {counts[level]}')
        
    lines.append('')
    lines.append('Частые ошибки:')
    for msg, count in errors:
        lines.append(f'- {msg} — {count}')
        
    return '\n'.join(lines) + '\n'