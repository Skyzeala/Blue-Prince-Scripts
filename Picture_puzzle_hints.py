# This script is designed to give synonyms to the pictures found on the estate
# The goal is to give ideas and inspiration rather than the answer, but answers are present

# !!! This script contains major spoilers for many phases of the game !!!
# do not assume you have seen them all

# The script will ask for a description of the picture, and give synonyms for the closest match

# Some pictures are combined into one result, 
#   for example saying "person" will lead to multiple painting answers, with some extras mixed in

import re
import random



print()
print("Please enter one or more key words to describe the image.")
print("For example, 'tree', or 'ace of spades'.")
print()
words = input("Description: ")

words = re.sub('[^A-Za-z0-9\\s&]+', '', words)

word_list = words.split()

print("Looking for pictures matching: ", ", ".join(word_list))
print()

high_score = 0
score = 0
matched_synonyms = []
many_matches = False



picture_list = [
    ["ace of spades", "ace", "spade", "card", "play", "hand", "one"],
    ["queen of diamonds", "queen", "diamond", "card", "play", "hand", "face card", "face", 
     "dame", "twelve"],
    ["house", "manor", "estate", "home", "place", "cabin", "palace", "cottage", "mansion",
     "castle", "villa", "lodge", "bungalow", "chateau"],
    ["crown", "royal", "king", "prince", "baron", "lord", "jewel", "treasure", "reign"],
    ["blueprint", "plan", "draft", "letter", "design", "diagram", "map", "layout", "outline"],
    ["tie", "necktie", "neck", "knot", "band", "scarf", "ruff", "strap"],
    ["tiered cake holder", "tier", "cake", "bake"],
    ["plot of land", "plot", "forest", "section"],
    ["person", "man", "woman", "pilot", "herbert", "chief", "chef", "cook", "baker", "bride", 
     "wife", "husband", "nurse", "agent", "beard", "farmer", "ranger", "lord", "lady", "miner"],
    ["hose", "garden hose", "pipe", "tube", "water", "sprinkler"],
    ["cliff", "sea", "ocean", "coast", "beach", "landscape", "hillside"],
    ["ten", "necklace", "tag", "price tag", "price", "cost", "luggage tag", "10"],
    ["plane", "flier", "airplane", "skies", "sky", "clouds", "cloud", "fly"],
    ["cloud", "clouds", "rain", "hale", "weather", "sky"],
    ["planet", "globe", "create", "art", "world", "paint", "brush", "hand", "earth", "realm"],
    ["plant", "flower", "herb", "greenery", "flora", "vegetable", "bloom", "sage", "basil", 
     "oregano", "thyme"],
    ["mountain", "hill", "top", "snowtop", "peak", "summit", "alp", "mt", "holly", "snow"],
    ["tree", "pine", "fir", "evergreen", "cedar", "spruce", "holly", "bush", "shrub"],
    ["deer", "stag", "antler", "moose", "buck", "fawn", "reindeer", "doe", "antelope", 
     "caribou", "elk", "hart", "hoof"],
    ["window", "windowpane", "pane", "glass", "glazing", "tile", "mosaic", "sheet of glass", 
     "sheet", "broken", "shatter", "crack"],
    ["crow", "raven", "bird", "rook", "corvid", "pigeon", "dove", "jay", "magpie"],
    ["spine", "bone", "vertebrae", "spinal", "back", "backbone"],
    ["cart", "minecart", "railroad", "car", "rail car"],
    ["car", "old", "vehicle", "automobile", "motor", "antique", "vintage", "classic", "carriage"],
    ["pint", "beer", "alcohol", "jug", "pitcher", "ale", "brew", "booze", "hop", "stout"],
    ["coat", "mannequin", "holder", "jacket", "robe", "clothing", "chronograph", "timer"],
    ["lamp", "oil lamp", "light", "lantern"],
    ["match", "light", "hand", "fire", "heat", "lit"],
    ["tiger", "cat", "big cat"],
    ["stage", "theater", "curtain", "curtains", "chairs", "runway", "platform", "stand",
     "drama", "play"],
    ["tub", "bath", "tank", "bathtub", "spa", "bowl", "wash", "soak", "dip", "shower", "clean",
     "bathe", "rinse"],
    ["clock", "time", "grandfather", "tick", "tock", "hour", "minute", "second"],
    ["tent", "forest", "outdoors", "camp", "campsite", "site", "shelter", "tarp"],
    ["fan", "sensu", "ogi"],
    ["tube", "liquid", "vial", "potion", "flask", "tincture", "test", "beaker", "elixir",
     "tonic", "acid", "reagent", "science", "bottle", "mixture", "sample", "poison", "cork"],
    ["sand", "desert", "wavy lines", "wave", "dune", "beach", "sandbar", "sandbank", "bar", 
     "hill", "bank", "wasteland", "sahara"],
    ["dessert", "flan", "jello", "pudding", "spoon", "plate", "custard", "platter", "saucer"],
    ["boat", "rowboat", "row", "canoe", "raft", "paddle", "oar", "paddleboat", "cruise", "ferry", 
     "dinghy", "dory"],
    ["and", "&", "also", "too", "with", "plus"],
    ["cot", "bed", "hammock"],
    ["wheat", "grain", "bunch", "bundle", "spelt", "grass", "clump", "bind", "wreath"], 
    ["crate", "box", "wooden crate", "wood", "storage", "store"],
    ["road", "travel", "trek", "path", "highway", "roadway", "pavement", "street", "route", "way",
     "track", "trail", "drive", "lane", "forest", "trees"],
    ["rod", "pole", "fish", "fishing", "line", "cast", "casting", "tackle", "fishpole", "reel"],
    ["paint", "can", "color", "brush", "housepaint"],
    ["bat", "forest", "hear", "wing", "wings", "webbed wing", "web"],
    ["lock", "padlock", "key", "keyhole", "unlock", "latch", "locker"],
    ["pea", "peas", "pod", "peapod", "vegetable", "seed", "snow peas", "snow", "snap peas", "snap"],
    ["stair", "stairs", "staircase", "spiral", "handrail", "corkscrew", "helix", "helical", 
     "circular", "screw", "step", "steps", "coil"],
    ["star", "stars", "diamond", "diamondus", "major", "constellation", "cluster", "group"],
    ["bridge", "path", "river", "stream", "cross", "crossing", "arch", "overpass"],
    ["pray", "hand", "bead", "beads", "clap", "puzzle", "necklace", "beg", "plead", "hands"],
    ["crowbar", "pry", "bar", "lever", "handle", "handspike", "prybar", "jimmy", "tool"],
    ["pin", "safety", "clip", "clamp", "tack", "clasp", "fasten"],




    ["graph", "rate", "rise", "spike", "plot", "chart", "diagram", "table", "figure"],
    ["book", "author", "novel", "story", "diary", "journal", "volume", "tome", "title", "chapter",
     "mary", "bible", "holy"],
    ["christmas", "tree", "noel", "merry", "yule", "advent", "holiday", "gift", "present",
     "presents"],
    ["shoelace", "end", "aglet", "lace"],
    ["calendar", "year", "month", "day", "date", "tear", "eight", "8"],
    ["thorn", "stem", "vine", "rose", "spike", "barb"],
    ["ear", "lobe", "hear"],
    ["steam", "pot", "boil", "stock", "soup", "burn"],
    ["landscape", "stream"],
    ["trellis", "arch", "arbor"],
    ["ship", "port", "harbor", "pier", "sail"],
    ["music", "note", "song", "tune", "bar", "melody"],
    ["win", "medal", "one", "1", "1st place", "place", "first"],
    ["boar", "pig"],
    ["tin", "can", "open", "tab"],
    ["farm", "ranch", "barn", "field"],
    ["fountain", "pen", "ink"],
    ["wine", "bottle", "cork"],
    ["tarot", "moon", "card", "the moon", "eclipse", "crescent"],
    ["bait", "worm", "fishing bait"],
    ["horse", "mustang", "stallion", "gallop", "trot", "canter", "run", "speed", "steed", 
     "racehorse", "bronco", "pony", "mount", "equine", "race", "hoof"],
    ["banana", "rot", "decay", "yellow", "brown"],
]


       
for pic_word_list in picture_list:
    score = len(set(word_list) & set(pic_word_list))

    if score > high_score:
        high_score = score
        matched_synonyms = pic_word_list
        many_matches = False
    elif score == high_score:
        many_matches = True

if many_matches == True:
    print("Too many matching pictures, try adding more descriptive words")
    exit()

random.shuffle(matched_synonyms)
print("Best match: ")
print(", ".join(matched_synonyms))
