# !!! This script contains major spoilers for many phases of the game !!!
# The script itself does try to mitigate spoilers in outputs

# This script will give synonyms to the pictures found on the estate based on a description
# The goal is to give ideas and inspiration rather than the answer
# I tried to capture as many descriptions and misinterpretations of the images i could think of

# Some pictures are combined into one result, 
#   for example saying "person" will lead to multiple painting answers, with some extras mixed in

import re #regex for text manipulation
import random #show results in a random order



print()
print("Please enter one or more key words to describe the image.")
print("For example, 'tree', or 'ace of spades'.")
print()

words = input("Description: ")

words = re.sub('[^A-Za-z0-9\\s&]+', '', words) #remove unwanted characters

word_list = words.split()

print("Looking for pictures matching: ", ", ".join(word_list))
print()

#set up variables for finding the best match
high_score = 0
score = 0
matched_synonyms = []
many_matches = False



#list of words for each picture
picture_list = [
    #44 rooms
    ["ace of spades", "ace", "spade", "card", "play", "hand", "one"],
    ["queen of diamonds", "queen", "diamond", "card", "play", "hand", "face card", "face", 
     "dame", "twelve"],
    ["house", "manor", "estate", "home", "place", "cabin", "palace", "cottage", "mansion",
     "castle", "villa", "lodge", "bungalow", "chateau"],
    ["crown", "royal", "king", "prince", "baron", "lord", "jewel", "treasure", "reign"],
    ["blueprint", "plan", "draft", "letter", "design", "map", "layout", "outline"],
    ["tie", "necktie", "neck", "knot", "band", "scarf", "ruff", "strap"],
    ["tiered", "tier", "cake", "bake", "dish", "layer", "layered", "three", "stand", "stacked",
     "display", "decor", "decorative", "tower", "serving", "tray", "platter", "stack", "holder",
     "pastry", "centerpiece", "cupcake", "bakery", "holder", "etagere", "serve", "whatnot"],
    ["plot", "forest", "section", "lot", "land", "patch", "acre", "property", "site", "strip",
     "parcel", "park", "garden", "ground", "trees", "fence"],
    ["hose", "garden hose", "pipe", "tube", "water", "sprinkler"],
    ["cliff", "sea", "ocean", "coast", "beach", "landscape", "hillside"],
    ["ten", "necklace", "tag", "price", "cost", "10"],
    ["cloud", "clouds", "rain", "hale", "weather", "sky", "cloudy"],
    ["plane", "flier", "airplane", "skies", "sky", "clouds", "cloud", "fly", "flight", "cloudy",
     "flyer", "amelia earhart", "aviator"],
    ["plant", "flower", "herb", "greenery", "flora", "vegetable", "bloom", "sage", "basil", 
     "oregano", "thyme", "flowers", "leaves", "leaf"],
    ["mountain", "hill", "top", "snowtop", "peak", "summit", "alp", "mt", "holly", "snow"],
    ["tree", "pine", "fir", "evergreen", "cedar", "spruce", "holly", "bush", "shrub"],
    ["deer", "stag", "antler", "moose", "buck", "fawn", "reindeer", "doe", "antelope", 
     "caribou", "elk", "hart", "hoof", "antlers"],
    ["window", "windowpane", "pane", "glass", "glazing", "tile", "mosaic", "sheet of glass", 
     "sheet", "broken", "shatter", "crack"],
    ["crow", "raven", "bird", "rook", "corvid", "pigeon", "dove", "jay", "magpie"],
    ["spine", "bone", "vertebrae", "spinal", "back", "backbone"],
    ["cart", "minecart", "railroad", "car", "rail car"],
    ["car", "old", "vehicle", "automobile", "motor", "antique", "vintage", "classic", "carriage"],
    ["pint", "beer", "alcohol", "jug", "pitcher", "ale", "brew", "booze", "hop", "stout", "mead"],
    ["coat", "mannequin", "holder", "jacket", "robe", "clothing", "rack", "clothes", "dress",
     "outfit", "gear", "apparel", "wear", "outer", "attire", "garb", "wardrobe"],
    ["lamp", "light", "lantern", "torch", "beacon", "oil", "candle"],
    ["tiger", "cat", "big cat", "big", "kitten", "jaguar", "feline", "beast", "panther", "leopard",
     "cougar", "puma", "lion", "wild", "lynx", "kitty", "calico", "tabby", "roar", "stare"],
    ["stage", "theater", "curtain", "curtains", "chairs", "runway", "platform", "stand",
     "drama", "play", "isle", "performance", "perform"],
    ["tub", "bath", "tank", "bathtub", "spa", "bowl", "wash", "soak", "dip", "shower", "clean",
     "bathe", "rinse"],
    ["clock", "time", "grandfather", "tick", "tock", "hour", "minute", "second", "timer",
     "chronograph", "chrono", "moment", "now", "period"],
    ["tent", "forest", "outdoors", "camp", "campsite", "site", "shelter", "tarp", "camping"],
    ["fan", "sensu", "ogi"],
    ["tube", "liquid", "vial", "potion", "flask", "tincture", "test", "beaker", "elixir",
     "tonic", "acid", "reagent", "science", "bottle", "mixture", "sample", "poison", "cork",
     "chemistry", "chemical"],
    ["sand", "desert", "wavy", "wave", "dune", "beach", "sandbar", "sandbank", "bar", 
     "hill", "bank", "wasteland", "sahara", "mountains", "hills"],
    ["dessert", "flan", "jello", "pudding", "spoon", "plate", "custard", "platter", "saucer",
     "dish"],
    ["boat", "rowboat", "row", "canoe", "raft", "paddle", "oar", "paddleboat", "cruise", "ferry", 
     "dinghy", "dory"],
    ["and", "&", "also", "too", "with", "plus", "ampersand", "symbol"],
    ["cot", "bed", "hammock", "sleep", "rest"],
    ["wheat", "grain", "bunch", "bundle", "spelt", "grass", "clump", "bind", "wreath", "blight",
     "harvest", "rye"], 
    ["crate", "chest", "case", "trunk", "box", "wooden crate", "wood", "storage", "store"],
    ["road", "travel", "trek", "path", "highway", "roadway", "pavement", "street", "route", "way",
     "track", "trail", "drive", "lane", "forest", "trees"],
    ["rod", "pole", "fish", "fishing", "line", "cast", "casting", "tackle", "fishpole", "reel"],
    ["paint", "can", "color", "brush", "housepaint", "bucket", "pail", "color", "stain"],
    ["bat", "forest", "hear", "wing", "wings", "webbed wing", "web", "above", "high", "fly"],
    ["lock", "padlock", "key", "keyhole", "unlock", "latch", "locker"],
    ["pea", "peas", "pod", "peapod", "vegetable", "snow peas", "snow", "snap peas", "snap"],
    ["stair", "stairs", "staircase", "spiral", "handrail", "corkscrew", "helix", "helical", 
     "circular", "screw", "step", "steps", "coil"],
    ["star", "stars", "diamond", "diamondus", "minor", "constellation", "cluster", "group"],
    ["bridge", "path", "river", "stream", "cross", "crossing", "arch", "overpass", "landscape"],
    ["pray", "hand", "bead", "beads", "clap", "puzzle", "necklace", "beg", "plead", "hands", 
     "clasp", "rosary", "faith", "bracelet", "saint", "prayer"],
    ["crowbar", "pry", "bar", "lever", "handle", "handspike", "prybar", "jimmy", "tool"],
    ["pin", "safety", "clip", "clamp", "tack", "clasp", "fasten"],
    ["match", "light", "hand", "fire", "heat", "lit", "flame", "burn", "ignite", "scorch", "warm",
     "flare", "torch", "kindle", "strike", "start", "fuse"],
    ["person", "man", "woman", "pilot", "herbert", "chief", "chef", "cook", "baker", "bride", 
     "wife", "husband", "nurse", "agent", "beard", "farmer", "ranger", "lord", "lady", "miner",
     "baron", "human", "figure", "simon", "clara", "mary", "groom", "dress", "wed", "major",
     "officer", "captain", "guard", "general", "maid", "aviator"],
    
    #the gallery
    ["red", "p", "stop", "sign", "stopsign", "rose", "fire", "hydrant", "mirror", "reverse",
     "backward", "invert", "apple", "wagon", "leaf", "reflect", "synonym",
     "this puzzle has hints and solutions in-game", "p on top of red items", "red is reversed"],
    ["actual", "objective", "eyes", "eyeballs", "veri", "genu", "wine", "table", "real", "sign",
     "this puzzle has hints and solutions in-game", "synonym"],
    ["infinity", "8", "eight", "nail", "nails", "hubris", "envy", "lust", "wrath", "gluttony",
     "sloth", "avarice", "deadly", "sins", "room", "synonym",
     "this puzzle has hints and solutions in-game", "eight in room"],
    ["thick", "handcuffs", "comet", "hand", "reflect", "thic", "k", "pond", "thin", "synonym",
     "this puzzle has hints and solutions in-game", "thin k"],

    #the other 44 rooms
    ["spear", "pike", "sharp", "harpoon", "stab", "pierce", "lance", "poke", "impale", "jab",
     "skewer", "shaft", "cut", "weapon", "blade", "edge"],
    ["leash", "lead", "tether", "rope", "cord", "strap", "halter"],
    ["planet", "globe", "create", "art", "world", "paint", "brush", "hand", "earth", "realm",
     "sphere", "ball", "orb", "earth art"],
    ["graph", "rate", "rise", "spike", "plot", "chart", "diagram", "table", "figure", "peak",
     "fall", "decline", "climb", "drop", "dip", "grow", "data", "bar", "line", "histogram"],
    ["book", "author", "novel", "story", "diary", "journal", "volume", "tome", "title", "chapter",
     "mary", "bible", "holy", "spine"],
    ["christmas", "tree", "noel", "merry", "yule", "advent", "holiday", "gift", "present",
     "presents", "pine"],
    ["seed", "sprout", "sprouted", "plant", "root", "germ", "germinate", "grow", "growth", "sow"],
    ["shoelace", "end", "aglet", "lace", "strap", "string", "cord", "tie", "knot"],
    ["calendar", "year", "month", "day", "date", "tear", "eight", "8"],
    ["thorn", "stem", "vine", "rose", "spike", "barb"],
    ["ear", "lobe", "hear", "sound", "noise", "earlobe"],
    ["steam", "pot", "boil", "stock", "soup", "burn", "cook", "stock"],
    ["sign", "post", "direction", "directions", "signpost", "signal", "landmark", "mark", "marker",
     "pointer", "guide", "guidepost", "point"],
    ["trellis", "arch", "arbor", "lattice", "frame", "gazebo", "pergola", "canopy", "planter",
     "arbour", "bower", "gate"],
    ["ship", "port", "harbor", "harbour", "pier", "sail", "sailboat", "boat", "launch", "bay"],
    ["music", "note", "song", "tune", "bar", "melody", "sheet", "score", "compose", "stave",
     "chord", "notation", "tone", "sound", "jingle", "part", "beat", "time", "carol", "lullaby",
     "requiem", "tempo", "measure"],
    ["win", "medal", "one", "1", "1st place", "place", "first"],
    ["boar", "pig", "hog", "sow", "swine", "ham", "pork", "bacon"],
    ["farm", "ranch", "barn", "field", "range", "grange", "farmhouse", "farmland"],
    ["tin", "can", "open", "tab", "empty", "aluminum", "jar", "package", "pull", "lid",
     "ring", "pop", "top", "opener", "rim", "handle"],
    ["fountain", "pen", "ink", "calligraphy", "write", "reservoir", "marker", "nib"],
    ["wine", "liquor", "alcohol", "bottle", "cork", "booze", "juice", "drink", "sake", "rum"],
    ["lunch", "box", "lunchbox", "tin", "meal", "suitcase", "case", "metal"],
    ["rat", "mouse", "rodent", "vermin", "varmint", "gnawer", "hamster"],
    ["tarot", "moon", "card", "the moon", "eclipse", "crescent"],
    ["bait", "worm", "fishing bait", "chum", "lure", "earthworm", "wiggler", "compost"], 
    ["horse", "mustang", "stallion", "gallop", "trot", "canter", "run", "speed", "steed", 
     "racehorse", "bronco", "pony", "mount", "equine", "race", "hoof"],
    ["banana", "rot", "decay", "yellow", "brown", "pear", "fruit", "orange", "apple", "blight",
     "spoil", "lemon", "berry", "berries", "kiwi", "tangerine", "mandarin", "clementine", "melon",
     "fig", "grape", "grapes", "cherry", "cherries", "rotten", "mold", "moldy", "bad", "ferment"],
    ["pi", "three", "3.14", "circle", "math", "symbol", "greek", "ratio"],




]


       
for pic_word_list in picture_list:
    words_in_common = set(word_list) & set(pic_word_list)
    score = len(words_in_common)

    if score > high_score:
        high_score = score
        matched_synonyms = pic_word_list
        many_matches = False

        #if there is only one key word, only show the first result found
        if len(word_list) < 2:
            break
    elif score == high_score:
        many_matches = True

if high_score == 0:
    print("Could not find a matching image, try different descriptive words")
    exit()
elif many_matches == True:
    print("Too many matching pictures, try adding more descriptive words")
    exit()

random.shuffle(matched_synonyms)
print("Best match: ")
print(", ".join(matched_synonyms))
