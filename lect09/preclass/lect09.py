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

ages = {'Ana': 3, 'Bob': 2, 'Rya': 5}

# Concept Test — which is best suited for a dictionary?
# A. The order in which people finish a race
# B. The ingredients necessary for a recipe
# C. The names of world countries and their capital cities
# D. 50 random integers

# Concept Test — what is the most efficient way to find Rya's age?
# A. Loop through ages checking each value
# B. ages['Rya']
# C. ages.values()[2]
# D. ages.index('Rya')

# Lookup:  ages[___]
# Search:  ___ in ages
# Insert:  ages['Mark'] = ___
# Update:  ages[___] = 4
# Delete:  del ages[___]

# ============================================================
# PART 2: Why dict beats parallel lists — bird counts
# ============================================================
# Option A: parallel lists
kinds  = ['falcon', 'owl', 'hawk', 'eagle']
counts = [1, 5, 2, 11]

# Option B: dictionary
bird_counts = {'falcon': 1, 'owl': 5, 'hawk': 2, 'eagle': 11}

# TODO: find eagle count from parallel lists
# TODO: find eagle count from dictionary  <- one line, no loop
# TODO: print each bird and its count using .items()


# ============================================================
# PART 3: Nested dictionaries — music library
# ============================================================
music = {
    'Pink Floyd': {
        'The Dark Side of the Moon': {
            'songs': ['Speak to Me', 'Breathe', 'On the Run', 'Money'],
            'year': 1973,
        },
        'The Wall': {
            'songs': ['Another Brick in the Wall', 'Mother', 'Hey You'],
            'year': 1979,
        }
    },
    'Justin Bieber': {
        'My World': {
            'songs': ['One Time', 'Bigger', 'Love Me'],
            'year': 2010,
        }
    }
}

# TODO: print all songs from 'The Wall' by Pink Floyd — one line


def print_library(library):
    '''Print each artist, their albums, and songs.
        Pink Floyd
            The Dark Side of the Moon : ['Speak to Me', ...]
            The Wall : ['Another Brick in the Wall', ...]
        Justin Bieber
            ...
    '''
    # TODO: outer loop over artists, inner loop over albums
    pass


def add_artist(library, artist):
    '''Add artist to library if not already present.'''
    # TODO
    pass


def add_album(library, artist, album, songs, year):
    '''Add album under artist. Print message if artist missing or album exists.'''
    # TODO
    pass


# Uncomment to test:
# add_artist(music, 'The Eagles')
# add_album(music, 'The Eagles', 'Hotel California',
#           ['Hotel California', 'Desperado', 'One of These Nights'], 1976)
# print_library(music)


# ============================================================
# PRACTICE
# ============================================================
# Write count_words(sentence) — returns a dict mapping each word
# to the number of times it appears.
# count_words("the cat sat on the mat") ->
#     {'the': 2, 'cat': 1, 'sat': 1, 'on': 1, 'mat': 1}
