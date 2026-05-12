# Lecture 10 - Reading Files
# zyBook 5.9
#
# Learning Objectives:
#   1. Open and read a file using open(), for line in f, and with
#   2. Parse CSV data using strip() and split()
#   3. Build a dictionary from file data
#   4. Use PIL to open image files

# Get the Pokemon data set
import os
import kagglehub
from PIL import Image

# Download latest version
path = kagglehub.dataset_download("vishalsubbiah/pokemon-images-and-types")

print("Path to dataset files:", path)
csv_file = os.path.join(path, "pokemon.csv")
images_dir = os.path.join(path, "images")


# ============================================================
# PART 1: Opening and reading a file
# ============================================================

# Step 1: manual open / read / close. 
# Read the first 200 characters in the file

f = open(csv_file)
contents = f.read()
print(contents[:200])
f.close()

# Step 2: with — closes automatically, even if an error occurs
# TODO: use with + for line in f to print the first 5 lines
print("\n\nOpen safely with the keyword with\n")
with open(csv_file) as f: # Simply replacing the open and close operations
    for i, line in enumerate(f):
        if i == 5:
            break
        print(line, end="")
  

# ============================================================
# PART 2: Parsing a CSV line
# ============================================================
# Each line looks like:  "bulbasaur,Grass,Poison,ivysaur\n"
# line.strip()           ->   "bulbasaur,Grass,Poison,ivysaur"
# line.strip().split(',') ->  ['bulbasaur', 'Grass', 'Poison', 'ivysaur']

# Concept Test — what does line.strip().split(',') return?
# A. ['bulbasaur,Grass,Poison,ivysaur']
# B. ['bulbasaur', 'Grass', 'Poison', 'ivysaur']
# C. ['bulbasaur', 'Grass', 'Poison', 'ivysaur\n']
# D. ('bulbasaur', 'Grass', 'Poison', 'ivysaur')


# ============================================================
# PART 3: Building a dictionary from the file
# ============================================================
# Goal: type -> [list of pokemon names]
# {'Grass': ['bulbasaur', 'ivysaur', ...], 'Fire': ['charmander', ...], ...}
# {}

def build_pokemon_dict(csv_file):
    '''Return a dict mapping Type1 -> [list of pokemon names].'''
    pokemon_dict = {} 
    # Open the file
    with open(csv_file) as f:
        # Read the header (one line) -- skip the header
        f.readline()
        # For every line in the file
        for line in f:
            # line = "bulbasaur,Grass,Poison,ivysaur\n"
            # strip the new line and split line into 4 parts
            # we need to get the name of the pokemon (index 0)
            # we need to get the type of the pokemon (index 1)
            parts = line.strip().split(",") # parts is a list with 4 elements
            # e.g. name = "bulbasaur"
            #      poke_type  = "Grass"
            name = parts[0]
            poke_type = parts[1]
            # pokemon_dict  may or may not be empty
            # assumes pokemon_dict is empty
            # {}  ---> {"Grass": ["bulbasaur"] }
            if poke_type not in pokemon_dict:
                pokemon_dict[poke_type] = []
            pokemon_dict[poke_type].append(name)
    return pokemon_dict

# TODO: call build_type_dict, print the keys, print all Fire-type pokemon
poke_dict = build_pokemon_dict(csv_file)
#print(poke_dict['Grass'][0:8])
print(list(poke_dict.keys()))
# ============================================================
# PART 4: Opening an image file with PIL
# ============================================================
# images are stored as:  images/{name}.png

def show_pokemon(name, images_dir):
    '''Open and display the image for the given pokemon.'''
    filepath = os.path.join(images_dir, name + ".png")
    # TODO: open with Image.open() and call img.show()
    img  = Image.open(filepath)
    img.show()
    pass

# TODO: show_pokemon("pikachu", images_dir)
# show_pokemon("pikachu", images_dir)

# ============================================================
# PART 5: Explore the data  [if time permits]
# ============================================================
import random

def show_random_pokemon_per_type(poke_dict, images_dir):
    '''Show one random pokemon for each type'''
    for type_name, pokemon_list in poke_dict.items():
        name = random.choice(pokemon_list)
        print(f"{type_name} : {name}")
        show_pokemon(name, images_dir)

show_random_pokemon_per_type(poke_dict, images_dir)
# ============================================================
# PRACTICE
# ============================================================
# Which type has the most Pokemon?
# Hint: write count_for_type(type_dict, t) and find_most_common(type_dict)
#       using the accumulator pattern
