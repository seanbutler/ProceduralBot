import random
import time
from utils import flatten
from formalgrammars import ContextFreeGrammar

from twitter import *
import secrets

import argparse

parser = argparse.ArgumentParser(description='Tweet a Procedural Design.')

parser.add_argument('--tweet',
                    action='store_true',
                    help='actually do the tweet')


print("Parsing Command Line Arguments")

args = parser.parse_args()
print(args)

grammar = None

while True:

    print ("Setting Up Grammar and Rules")
    grammar = ContextFreeGrammar()

    if random.random() < 0.9 :

        print ("Doing Text")

        grammar.AddRule('LEVEL',             ['BEGIN_PART SUCCESSIVE VALVE SUCCESSIVE MIDDLE_PART SUCCESSIVE MIDDLE_PART SUCCESSIVE MIDDLE_PART SUCCESSIVE END_PART'])

        grammar.AddRule('BEGIN_PART',        ['SPAWN SIMULTANEOUS REST'])
        grammar.AddRule('MIDDLE_PART',       ['CHALLENGE SUCCESSIVE REST'])
        grammar.AddRule('END_PART',          ['REST SIMULTANEOUS EXIT'])
        grammar.AddRule('CHALLENGE',         ['CHALLENGE_FEATURE SIMULTANEOUS DANGER_FEATURE' ])
        grammar.AddRule('REST',              ['REWARD_FEATURE SIMULTANEOUS SAFE_FEATURE'])

        grammar.AddRule('SPAWN',             ['Door', 'Motorboat', 'Yacht', 'Canoe', 'Cablecar', 'Running', 'Snowboard', 'Horse', 'Bicycle', 'Car', 'Motorbike', 'Van', 'Truck', 'Bus', 'Portal', 'Tunnel', 'Cave' ])
        grammar.AddRule('VALVE',             ['Long Drop', 'Closing Door', 'Collapsing Floor', 'Falling Rocks' ])
        grammar.AddRule('CHALLENGE_FEATURE', ['Moving Platform ', 'Collapse Platform ', 'Small Platform' ])
        grammar.AddRule('DANGER_FEATURE',    ['Lava', 'Spikes', 'Buzzsaw', 'Critter', 'Arrows', 'Enemy' ])
        grammar.AddRule('REWARD_FEATURE',    ['Health', 'Coin' ])
        grammar.AddRule('SAFE_FEATURE',      ['Large Platform ', 'Ladder ', 'Ground '])
        grammar.AddRule('EXIT',              ['Door ', 'Vehicle ', 'Portal ', 'Tunnel', 'Cave'])

        grammar.AddRule('SIMULTANEOUS',      ['and'])
        grammar.AddRule('SUCCESSIVE',        ['then'])
        grammar.AddRule('FINALLY',           ['finally'])

    else:

        print ("Doing Icons")

        grammar.AddRule('LEVEL',             ['BEGIN_PART SUCCESSIVE VALVE SUCCESSIVE MIDDLE_PART SUCCESSIVE MIDDLE_PART SUCCESSIVE MIDDLE_PART SUCCESSIVE MIDDLE_PART SUCCESSIVE MIDDLE_PART SUCCESSIVE MIDDLE_PART SUCCESSIVE MIDDLE_PART SUCCESSIVE MIDDLE_PART SUCCESSIVE MIDDLE_PART SUCCESSIVE END_PART'])

        grammar.AddRule('BEGIN_PART',        ['SPAWN SIMULTANEOUS REST'])
        grammar.AddRule('MIDDLE_PART',       ['CHALLENGE SUCCESSIVE REST'])
        grammar.AddRule('END_PART',          ['REST FINALLY EXIT'])
        grammar.AddRule('CHALLENGE',         ['CHALLENGE_FEATURE SIMULTANEOUS DANGER_FEATURE' ])
        grammar.AddRule('REST',              ['REWARD_FEATURE SIMULTANEOUS SAFE_FEATURE'])


        grammar.AddRule('SPAWN',             ['🚌', '🚤', '⛵', '🛬', '🚠', '🚣', '🏃', '🏂', '🏄', '🏇', '🚴', '🚪', '🚕', '🚗', '🌀 ', '🚀', '🚁', '🚂'])
        grammar.AddRule('VALVE',             ['⤵', '🕳', '🚪', '߹', '܊' ])
        grammar.AddRule('CHALLENGE_FEATURE', ['⇢', '↧', '↥', '-', '🧗', '🗻', '🛸'])
        grammar.AddRule('DANGER_FEATURE',    ['🤼', '🧛', '👹', '👺', '👻', '🧟', '🤺', '🤖', '🌋', '🦀', '🦂', '👾', '👽', '💀', '🦖', '🏹', '🔥', '🐉', '🐍'])
        grammar.AddRule('REWARD_FEATURE',    ['❤', '💷', '💎', '⭐'])
        grammar.AddRule('SAFE_FEATURE',      ['🏰', '🏠', '🏥', '⛪', '_'])
        grammar.AddRule('FINALLY',           ['🏁', '👍', '💑', '🎂', '🤴'])
        grammar.AddRule('EXIT',              ['🚌', '🚤', '⛵', '🚴', '🚪', '🚕', '🚗', '🌀', '🚀', '🚁', '🛌', '🛫', '🚂'])

        grammar.AddRule('SIMULTANEOUS',      [' '])
        grammar.AddRule('SUCCESSIVE',        ['👉', '👣', ])


    print("Generating Random Level Design")

    result = grammar.GenerateRandom('LEVEL')

    print("Munging Design Into Space Separated String")

    flat = flatten(result)
    raw = ' '.join(flat)
    neat = " ".join(raw.split())

    print(neat)

    if (args.tweet==True):
        print ("TWEET TWEET")

        tw = Twitter(
            auth=OAuth(secrets.ACCESS_TOKEN, secrets.ACCESS_TOKEN_SECRET, secrets.CONSUMER_API_KEY, secrets.CONSUMER_API_SECRET))

        tw.statuses.update(status=neat+ " #ProceduralLevelDesign")
