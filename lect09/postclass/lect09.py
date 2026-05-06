# Lecture 9 - Dictionaries and Nested Dictionaries
# zyBook 5.1 - 5.6
#
# Learning Objectives:
#   1. Explain what a dictionary is and when to prefer it over a list
#   2. Perform the five core dict operations: create, lookup, search, insert, update, delete
#   3. Iterate over a dictionary using .items()
#   4. Read and modify a nested dictionary


# ============================================================
# PART 1: What is a dictionary + core operations
# ============================================================
# Maps keys to values. Keys must be unique. Values can be anything.
# Syntax: { key: value, key: value, ... }
# Dictionary is a good option when representing relationships
# {key: value,  ,  ,} 

# People and their age
ages = {'Ana': 3, 'Bob': 2, 'Rya': 5}

# Country and the capitol
capitols = { "USA": "Washington DC" , "Japan": "Tokyo", "Italy": "Rome" }

print(ages['Bob'])

# Concept Test — which is best suited for a dictionary?
# A. The order in which people finish a race
# B. The ingredients necessary for a recipe
# C. The names of world countries and their capital cities
# D. 50 random integers

# Concept Test — what is the most efficient way to find Rya's age?
# A. Loop through ages checking each value
# B. ages['Rya']  # correct
# C. ages.values()[2]
# D. ages.index('Rya')

ages = {'Ana': 3, 'Bob': 2, 'Rya': 5}
# Lookup:  ages[___]
print(ages['Ana'])
# Search:  ___ in ages
'Rya' in ages
'Mark' not in ages
# Insert:  ages['Mark'] = ___
ages['Ruby'] = 5
# Update:  ages[___] = 4
ages['Ruby'] = 4
# Delete:  del ages[___]

# ============================================================
# PART 2: Why dict beats parallel lists — bird counts
# ============================================================
# Option A: parallel lists
kinds  = ['falcon', 'owl', 'hawk', 'eagle']
counts = [1, 5, 2, 11]

# TODO: find eagle count from parallel lists
print(counts[kinds.index('eagle')])

# Option B: dictionary
bird_counts = {'falcon': 1, 'owl': 5, 'hawk': 2, 'eagle': 11}

bird = 'peacock'
if bird in bird_counts:
    print(bird_counts[bird])
else:
    print("The dictioanry doesn't contain", bird)
    bird_counts[bird] = 0

# TODO: find eagle count from dictionary  <- one line, no loop

# TODO: print each bird and its count using .items()
# Two ways to iterate over a dictionary
# First way
for key in bird_counts:
    print(key, end = " ")
print()

# Second way
# For a list we used ????? enumerate to ietarte through the list, get the index and the value
print("Iterating through a list with enumerate")
names = ['falcon', 'owl', 'hawk', 'eagle']
for i, elem in enumerate(names):
    print(i, elem)

# For the dictioanry use items() to get both teh key and the associated value
bird_counts = {'falcon': 1, 'owl': 5, 'hawk': 2, 'eagle': 11}

print("\nIterating through a dictionary with items()")
for bird, count in bird_counts.items():
    print(bird, count)
print()


# ============================================================
# PART 3: Nested dictionaries — music library
# ============================================================
music = {
    'Pink Floyd': {
        'The Dark Side of the Moon': {
            'songs': ['Speak to Me', 'Breathe', 'On the Run', 'Money'],
            'year': 1973
        }, 
        'The Wall': {
            'songs': ['Another Brick in the Wall', 'Mother', 'Hey You'],
            'year': 1979
        }
    },
    'Justin Bieber': {
        'My World': {
            'songs': ['One Time', 'Bigger', 'Love Me'],
            'year': 2010
        }
    }
}
# print(music)
# TODO: print all songs from 'The Wall' by Pink Floyd — one line
print(music['Pink Floyd']['The Wall']['songs'])

def print_library(library):
    '''Print each artist, their albums, and songs.
        Pink Floyd
            The Dark Side of the Moon : ['Speak to Me', ...]
            The Wall : ['Another Brick in the Wall', ...]
        Justin Bieber
            ...
    '''
    # TODO: outer loop over artists, inner loop over albums
    for artist in library:
        print(artist)
        for album in library[artist]:
            print('\t', album, ":", library[artist][album]['songs']) # print(music['Pink Floyd']['The Wall']['songs'])

    pass


def add_artist(library: dict, artist : str):
    '''Add artist to library if not already present.'''
    # TODO
    if artist in library:
        print(artist, "already exists in the music library")
    else:
        library[artist] = {}
    return


def add_album(library: dict, artist: str, album : str, songs: list , year : int):
    '''Add album under artist. Print message if artist missing or album exists.'''
    if artist not in library:
        print(artist, "not in the library")
        return
    
    if album in library[artist]:
        print(album, "already exists")
        return
    library[artist][album] = {'songs': songs, 'year': year}
      
    return


# Uncomment to test:
add_artist(music, 'The Eagles')
add_album(music, 'The Eagles', 'Hotel California', ['Hotel California', 'Desperado', 'One of These Nights'], 1976)
add_album(music, 'Mariah', 'Hotel California', ['Hotel California', 'Desperado', 'One of These Nights'], 1976)
print("Print the music library in a nice way!")
print_library(music)


# ============================================================
# PRACTICE
# ============================================================
# Write count_words(sentence) — returns a dict mapping each word
# to the number of times it appears.
# count_words("the cat sat on the mat") ->
#     {'the': 2, 'cat': 1, 'sat': 1, 'on': 1, 'mat': 1}
