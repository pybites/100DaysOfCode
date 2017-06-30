from archive import parse_csv
from archive import calc_stats
from archive import print_header, print_results

data = parse_csv()

stats = calc_stats(data)

print_header()

print_results(title='Whose tweets', counter=stats['tweets'])
print_results(title='Most mentioned', counter=stats['mentions'])
print_results(title='Most used hashtags', counter=stats['hashtags'])
print_results(title='Most active months', counter=stats['activity'])
print_results(title='Sources used', counter=stats['sources'])
