## Rooms
rooms = {
    "Sanctuary of the First Roots": {
        "North": "Hall of the Twin Celestials"
    },
    "Hall of the Twin Celestials": {
        "North": "Bridge of Remembrance",
        "South": "Sanctuary of the First Roots",
        "East": "Sunlit Conservatory",
        "West": "Moonwell"
    },
    "Moonwell": {
        "East": "Hall of the Twin Celestials"
    },

    "Sunlit Conservatory": {
        "West": "Hall of the Twin Celestials"
    },
    "Bridge of Remembrance": {
        "South": "Hall of the Twin Celestials",
        "North": "Chamber of Equilibrium"
    },

    "Chamber of Equilibrium": {
        "North": "Heart of Gaia",
        "South": "Bridge of Remembrance",
        "East": "Keeper's Residence",
        "West": "The Weaver's Hollow"
    },

    "Keeper's Residence": {
        "West": "Chamber of Equilibrium",
        "South": "Reliquary"
    },
    "Reliquary": {
        "North": "Keeper's Residence"
    },
    "The Weaver's Hollow": {
        "South": "Crypt of the First Keepers",
        "East": "Chamber of Equilibrium"
    },
    "Crypt of the First Keepers": {
        "North": "The Weaver's Hollow"
    },
    "Heart of Gaia": {
        "South": "Chamber of Equilibrium"
    }
}

current_room = "Sanctuary of the First Roots"
inventory = set()
spider_defeated = False
injured = False

## Room Descriptions
descriptions = {
    "Sanctuary of the First Roots": (
        "Sprawling foliage creeps along walls of living wood. "
        "Lanterns sway gently overhead. Beneath your feet, "
        "something shifts. The tree is breathing."
    ),

    "Hall of the Twin Celestials": (
        "You enter a vast chamber decorated with faded "
        "carvings of the Sun and Moon. Passages lead "
        "north, east, west, and south."
    ),

    "Moonwell": (
        "A still pool lies beneath the shelter of ancient roots. "
        "Silver light dances across its surface, though no moon "
        "is visible overhead. Beneath the clear water, you "
        "notice a small stone pedestal."
    ),
    "Sunlit Conservatory": (
        "An ancient garden, "
        "blessed with the warmth of the summer's day. "
        "At the center of the conservatory, "
        "you notice a small stone pedestal."
    ),

    "Bridge of Remembrance": (
        "A narrow bridge stretches above a seemingly bottomless "
        "chasm. Ancient memorial tablets line its edges, their "
        "inscriptions worn by centuries of silence. "
        "One tablet near the center sits strangely crooked."
    ),

    "Chamber of Equilibrium": (
        "You enter a vast circular chamber, where patterns of "
        "sunlight and moonlight intertwine across the floor. "
        "Passages branch in four directions. "
        "An ornate doorway stands to the east."
    ),

    "Keeper's Residence": (
        "The abandoned quarters of Gaia's keepers lie before you. "
        "Dust covers old furnishings, and delicate roots curl "
        "around the bedposts. The room is quiet, but not empty "
        "of memory."
    ),
    "Reliquary": (
        "The door creaks open beneath your hand. "
        "Empty weapon racks line the walls, and pale roots "
        "creep between ancient flagstones. "
        "An ornate wooden chest rests against the western wall. "
        "A tall wardrobe stands behind hanging ivy. "
        "Near the rear of the chamber, a stone altar lies "
        "concealed beneath a dusty cloth. "
        "A faint green light pulses through the fabric."
    ),

    "The Weaver's Hollow": (
        "Thick strands of webbing hang between the ancient pillars. "
        "The air is stale, and the stone floor is littered with "
        "the husks of unfortunate creatures. "
        "Somewhere above you, something enormous begins to move."
    ),

    "Crypt of the First Keepers": (
        "The passage descends into an ancient crypt. "
        "Rows of weathered stone coffins rest beneath "
        "arches tangled with pale roots. "
        "At the far end stands a carved shrine, "
        "its surface marked with the symbols of Sun and Moon."
),

    "Heart of Gaia": (
        "At the center of the temple lies a vast hollow chamber "
        "where root and stone have grown together. "
        "Broken machinery juts from the roots like iron thorns. "
        "Thick fumes seep from cracked vents. "
        "At the center of it all, something vast and breathing "
        "slowly turns toward you."
),


}

## Items
searchable_objects = {
    "Moonwell": {
        "pedestal": {
            "item": "Moon Stone",
            "description": (
                "You peer beneath the water's surface. "
                "Resting upon a submerged pedestal is a "
                "smooth, silver stone. It shimmers faintly "
                "in the darkness."
            )
        }
    },
    "Sunlit Conservatory": {
        "pedestal": {
            "item": "Sun Stone",
            "description": (
                "You step toward the pedestal. "
                "The stone resting upon it burns brightly, "
                "like the radiating sun in an endless stream of despair. "
                "It is warm to the touch."
            )
        }
    },

    "Bridge of Remembrance": {
        "tablet": {
            "item": "Keeper's Key",
            "description": (
                "You examine an ancient memorial tablet. "
                "Beneath its cracked stone base rests a small "
                "iron key, marked with the crest of Gaia's keepers. "
                "You carefully retrieve it."
            )
        }
    },

    "Reliquary": {
        "chest": {
            "item": "Thornkeeper's Blade",
            "description": (
                "You open the ornate chest. "
                "Inside rests a short blade, its ancient steel "
                "still gleaming beneath centuries of dust."
            )
        },
        "wardrobe": {
            "item": "Mantle of the Twin Celestials",
            "description": (
                "You open the Keeper's wardrobe. "
                "Nestled between dusty rags and mildewed tunics "
                "rests an ornate cloak, "
                "practically radiating with protective magic."
            )
        },
        "altar": {
            "item": "Seed of the First Grove",
            "description": (
                "It takes some effort, "
                "but you free the altar from under the heavy tarp. "
                "Nestled in a proud crowning lay a simple seed, "
                "blooming with hope."
            )
        },
    },

    "Crypt of the First Keepers": {
        "shrine": {
            "item": "Heartstone of Gaia",
            "description": (
                "You approach the shrine and brush away "
                "centuries of dust. Nestled within a small "
                "recess rests a luminous green stone. "
                "As your fingers close around it, "
                "a faint heartbeat echoes through the crypt."
            )
        }
    },
}

## Spider scenes
spider_scenes = {
    "defeat": """
The creature stirs.

Eight enormous legs unfold from the darkness, each ending
in a hooked point that scratches against the ancient stone.

You reach instinctively for a weapon.

Your fingers close around nothing.

The spider pauses.

For one terrible moment, you stare at one another.

Then it lunges.

You turn to flee, but the webbing catches your ankle.
The ground rushes toward you.

There is a brief sensation of weightlessness.

A flash of fangs.

And then...

Nothing.
""",

    "wounded_victory": """
You barely manage to raise your blade before the creature lunges.

Its enormous forelegs strike against the ancient steel,
forcing you backward. Your shoulder collides painfully
with the wall.

The spider advances.

You swing wildly. Once. Twice.

The third strike finds its mark.

With a terrible shudder, the creature collapses into
its tangled webbing.

For several moments, you do nothing but breathe.

Your arm trembles. Blood trickles beneath your sleeve.
Every movement sends a sharp ache through your ribs.

But you're alive.

And beyond the webbing, you can just make out a passage
descending into darkness.
""",

    "decisive_victory": """
The spider lunges.

You brace yourself.

Its fangs strike your shoulder, only to skid harmlessly
across the shimmering fabric of your mantle.

For a brief moment, the enormous creature seems almost confused.

You seize the opportunity.

One swift movement sends your blade flashing through the darkness.

The spider staggers.

A second strike finishes the encounter.

You stand amid the settling dust, examining your mantle.

Not so much as a torn thread.

You straighten the fabric, retrieve your blade,
and continue toward the crypt.

Perhaps the ancient keepers knew a thing or two about
proper equipment after all.
"""
}

## Venious scenes
venious_scenes = {
    "defeat": """
You raise what little you have against the horror before you,
but the Heart of Gaia does not answer your desperation.

Venious surges forward in a storm of root, vapor, and hunger.

You do not survive long enough to regret coming here.

Far beyond the shattered chamber, the forest waits in silence.
""",

    "victory": """
The Heartstone warms in your grasp.

The mantle settles against your shoulders like a second skin.
The old blade feels steady in your hand.

And when you draw forth the Seed of the First Grove,
the chamber itself seems to pause.

Venious screams and lunges.

Its poisoned breath washes over you, dulled by the ancient mantle.
You meet its charge with steel, cutting through vine and bloom
and rot. The monster thrashes, roots tearing up the stone,
but the old blade holds true.

At last, when Venious falters, you fall to your knees before
the wounded heart of the temple and press the Seed into
the waiting roots.

For a moment, nothing happens.

Then the chamber exhales.

The machinery shudders. Light spills through the old carvings.
Somewhere beyond the temple walls, birdsong returns.

Venious gives one final, trembling shiver and falls still.

Not as a monster.

Only as something that suffered for too long.
"""
}

## Death endings

death_endings = {
    "spider": """
The roots continue their restless breathing.

Somewhere beyond the temple, a little fox waits
beside an empty doorstep.

You do not return.

But beneath the earth, where the oldest trees
keep their secrets, something holds fast to the
memory of a small creature who tried.
""",

    "venious": """
Far beyond the shattered chamber, the forest
waits in silence.

The corruption continues to spread.

And somewhere beneath the dying trees,
the memory of your journey remains.
"""
}

## Victory endings

victory_endings = {
    "wounded": """
You stagger through the temple's ancient doors.

Your wounds ache with every step, and the blade
feels impossibly heavy in your hand.

But the forest is singing.

A familiar little fox waits beside your doorstep.
At the sight of you, it raises its head and
bounds toward you.

You fall to your knees, laughing through the pain.

You have returned.

And the forest remembers you.
""",

    "uninjured": """
You step beyond the temple's ancient doors.

Warm sunlight spills between the branches.
The forest hums with life once more.

At your doorstep, a familiar little fox waits.

It looks up, sees you, and races forward.

You kneel to gather it into your arms.

You have returned.

And the forest remembers you.
"""
}


## Opening narrative

opening_scene = """
The forest has been quiet for three days.

Not peaceful. Quiet.

The sort of silence that settles when even the insects
have abandoned their songs.

This morning, you discovered a little fox curled beneath
your doorstep. Its breathing was shallow, and the fur
around its muzzle had begun to pale.

Beyond your home, the ancient trees were shedding leaves
despite the warmth of the season.

And far to the north, something was breathing beneath
the earth.

You packed what little you owned, tucked a loaf of bread
into your satchel, and set off toward the Temple of Gaia.

You were not a warrior.

You were not particularly brave.

But the fox had looked at you as though you could help.

And that, apparently, was enough.
"""


## Room Function

def display_room(room_name):
    print(f"\n{room_name}")

    if room_name == "The Weaver's Hollow" and spider_defeated:
        print("The enormous spider lies still among its broken webs.")
    else:
        print(descriptions.get(room_name, "No description available."))

    exits = rooms[room_name]
    print("Exits:", ", ".join(exits.keys()))


## Search Function

def check_object(room_name, object_name):
    room_objects = searchable_objects.get(room_name, {})

    if object_name not in room_objects:
        print("You find nothing of interest.")
        return

    object_data = room_objects[object_name]
    item = object_data["item"]

    if item in inventory:
        print("You've already collected that item.")
        return

    print(object_data["description"])
    inventory.add(item)
    print(f"\nYou obtained: {item}!")


## Spider encounter

def spider_encounter(inventory):
    if "Thornkeeper's Blade" not in inventory:
        return "defeat"

    elif "Mantle of the Twin Celestials" in inventory:
        return "decisive_victory"

    else:
        return "wounded_victory"

def resolve_spider_encounter():
    global spider_defeated, injured

    outcome = spider_encounter(inventory)

    print(spider_scenes[outcome])

    if outcome == "defeat":
        return "death"

    spider_defeated = True

    if outcome == "wounded_victory":
        injured = True
    else:
        injured = False

    return "survived"


## Venious Encounter

def venious_encounter(inventory):
    if (
        "Thornkeeper's Blade" in inventory
        and "Mantle of the Twin Celestials" in inventory
        and "Seed of the First Grove" in inventory
    ):
        return "victory"

    else:
        return "defeat"

def resolve_venious_encounter():
    outcome = venious_encounter(inventory)

    print(venious_scenes[outcome])

    if outcome == "victory":
        if injured:
            print(victory_endings["wounded"])
        else:
            print(victory_endings["uninjured"])

        return "victory"

    return "death"


## Restart

def restart_game(cause):
    global current_room, spider_defeated, injured

    print(death_endings[cause])

    print("\n             GAME OVER")
    print("       The forest remembers you.")

    input("\nPress Enter to begin a new journey...")


    current_room = "Sanctuary of the First Roots"
    inventory.clear()
    spider_defeated = False
    injured = False

    print("\nA new journey begins.")
    print(opening_scene)

    input("\nPress Enter to return to the temple...")

    display_room(current_room)


## Opening

print("Welcome to the Temple of Gaia!")

print(opening_scene)

input("\nPress Enter to begin your journey...")

print("\nCommands: go [direction], check [object], inventory, look, help, exit")

display_room(current_room)

## Loop
while True:

    command = input("What would you like to do? ").lower().strip()

    if command == "exit":
        print("The forest awaits your return.")
        break


    elif command == "look":
        display_room(current_room)

    elif command == "help":
        print("\nAvailable commands:")
        print("go north / south / east / west")
        print("check [object]")
        print("inventory")
        print("look")
        print("help")
        print("exit")

    elif command == "inventory":
        if inventory:
            print("You are carrying:")
            for item in sorted(inventory):
                print(f"- {item}")
        else:
            print("Your pockets are empty.")

    elif command.startswith("check "):
        object_name = command[6:].strip()
        check_object(current_room, object_name)

    elif command.startswith("go "):
        direction = command[3:].capitalize()

        if direction in rooms[current_room]:
            next_room = rooms[current_room][direction]

            if (current_room == "Hall of the Twin Celestials"
                    and next_room == "Bridge of Remembrance"
                    and not (
                            "Moon Stone" in inventory
                            and "Sun Stone" in inventory
                    )):
                print("The bridge remains sealed.")
                print("Two celestial stones are required.")

            elif (current_room == "Chamber of Equilibrium"
                  and next_room == "Keeper's Residence"
                  and "Keeper's Key" not in inventory):
                print("The residence door is locked.")
                print("You need the Keeper's Key.")

            elif (current_room == "Chamber of Equilibrium"
                  and next_room == "Heart of Gaia"
                  and "Heartstone of Gaia" not in inventory):
                print("The Heart of Gaia remains sealed.")
                print("The writhing vines snap viciously, "
                  "forcing you to retreat. ")
                print("You need the Heartstone of Gaia.")



            else:

                current_room = next_room
                print("You continue through the temple.")
                display_room(current_room)

                if (current_room == "The Weaver's Hollow"

                        and not spider_defeated):

                    result = resolve_spider_encounter()

                    if result == "death":
                        restart_game("spider")

                if current_room == "Heart of Gaia":
                    result = resolve_venious_encounter()

                    if result == "death":
                        restart_game("venious")

                    elif result == "victory":
                        print("\nTHE END")
                        break

        else:
            print("You seem to have smacked right into a wall. Be careful!")

