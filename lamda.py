import re

def f(x):
    return x * 2


for i in range(10):
    print('{0}:{1}'.format(i, f(i)), end=' ')
else:
    print()


for i in range(10):
    print('{0}:{1}'.format(i, (lambda x: x*2)(i)), end=' ')
else:
    print()

#########################################################################
states = ['Alabama', ' Georgia!', 'Georgia ', 'georgia', 'FlOrIda', 'south carolina   ', 'West virginia?']

def clean_strings(strings, *funcs):
    results = []
    for string in strings:
        for func in funcs:
            string = func(string)
        results.append(string)
    return results

states = clean_strings(states, str.strip, str.title, lambda s: re.sub('[!#?]', '', s))
print(states)








