import os
from logstats import parse_event, count_levels, top_errors, format_report

def main():
    file_name = input().strip()
    
    if not os.path.exists(file_name):
        return
    
    with open(file_name, mode='r', encoding='utf8') as file:
        counts = count_levels(file)

    with open(file_name, mode='r', encoding='utf8') as file:
        errors = top_errors(file, 3)

    total_parsed = sum(v for k, v in counts.items() if k != 'BROKEN')
    error_count = counts['ERROR']
    broken_count = counts['BROKEN']

    print(total_parsed)
    print(error_count)
    print(broken_count)

    report_text = format_report(counts, errors)
    with open('report.txt', mode='w', encoding='utf-8') as report_file:
        report_file.write(report_text)

if __name__ == '__main__':
    main()