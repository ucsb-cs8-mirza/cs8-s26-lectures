# Lecture 10 - Reading Files
# zyBook 5.9
#
# Learning Objectives:
#   1. Open and read a file using open(), for line in f, and with
#   2. Parse CSV data using strip() and split()
#   3. Build a dictionary from file data
#   4. Use PIL to open image files

# Get the Pokemon dataset


# ============================================================
# PART 1: Opening and reading a file
# ============================================================

# Step 1: manual open / read / close. 
# Read the first 200 characters in the file


# Step 2: with — closes automatically, even if an error occurs
# with open(csv_file) as f:
#     for line in f:
#         print(line, end="")

# TODO: use with + for line in f to print the first 5 lines


# ============================================================
# PART 2: Parsing a CSV line
# ============================================================
# Each line looks like:  "bulbasaur,Grass,Poison,ivysaur\n"
# line.strip()           ->  
# line.strip().split(',') -> 

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

def build_type_dict(csv_file):
    '''Return a dict mapping Type1 -> [list of pokemon names].'''
    type_dict = {}
    return type_dict

# TODO: call build_type_dict, print the keys, print all Fire-type pokemon


# ============================================================
# PART 4: Opening an image file with PIL
# ============================================================
# images are stored as:  images/{name}.png

def show_pokemon(name, images_dir):
    '''Open and display the image for the given pokemon.'''
    filepath = os.path.join(images_dir, name + ".png")
    # TODO: open with Image.open() and call img.show()
    pass

# TODO: show_pokemon("pikachu", images_dir)


# ============================================================
# PART 5: Explore the data  [if time permits]
# ============================================================




# ============================================================
# PRACTICE
# ============================================================
# Which type has the most Pokemon?
# Hint: write count_for_type(type_dict, t) and find_most_common(type_dict)
#       using the accumulator pattern
