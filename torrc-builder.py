'''
data from: https://metrics.torproject.org/rs.html#aggregate/cc
country codes: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
~/Downloads/tor-browser-linux-x86_64-14.0.6/tor-browser/Browser/TorBrowser/Data/Tor/torrc
'''

coutrylist_eu = ['de', 'nl', 'fr', 'se', 'pl', 'fi',
                 'at',  'cz', 'lu', 'ro', 'it', 'dk',
                 'es', 'bg', 'hu', 'ie', 'lt', 'pt']
coutrylist_team1 = ['us', 'gb', 'ch', 'ca', 'au', 'il']
coutrylist_team2 = ['ru', 'ua', 'al', 'in', 'sg', 'am', 'tr', 'ba', 'rs', 'jp', 'br', 'my', 'za', 'bd', 'kr']

coutrylist_exclude = ['de']


# lets start build the torrc file

print('StrictNodes 1')
print('NumEntryGuards 10')

# Guard
print('EntryNodes ',end='')
flag = 0
for element in coutrylist_team2:
    if element not in coutrylist_exclude:
        if flag == 0:
            print('{' f'{element}' + '}', end='')
            flag = 1
        else:
            print(',{' f'{element}' + '}', end='')

# Middle
print('\nMiddleNodes ',end='')
flag = 0
for element in coutrylist_team1:
    if element not in coutrylist_exclude:
        if flag == 0:
            print('{' f'{element}' + '}', end='')
            flag = 1
        else:
            print(',{' f'{element}' + '}', end='')

# Exit
print('\nExitNodes ',end='')
flag = 0
for element in coutrylist_eu:
    if element not in coutrylist_exclude:
        if flag == 0:
            print('{' f'{element}' + '}', end='')
            flag = 1
        else:
            print(',{' f'{element}' + '}', end='')
        
# Exclude
print('\nExcludeNodes ',end='')
flag = 0
for element in coutrylist_exclude:
    if flag == 0:
        print('{' f'{element}' + '}', end='')
        flag = 1
    else:
        print(',{' f'{element}' + '}', end='')   
