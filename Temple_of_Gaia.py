## Cass was here <3

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


## Direction aliases

direction_aliases = {
    "up": "North",
    "down": "South",
    "left": "West",
    "right": "East"
}

current_room = "Sanctuary of the First Roots"
inventory = set()
spider_defeated = False
injured = False


## Room Descriptions

descriptions = {

    "Sanctuary of the First Roots": """
        Sprawling foliage creeps along walls of living wood.
        The leaves have begun to curl inward, their once-vibrant
        green fading to a sickly grey.

        Ancient lanterns sway overhead.

        There is no breeze.

        Beneath your feet, something shifts.

        The tree is breathing.

        Each slow movement travels through the roots beneath
        the floor, followed by an irregular tremor.

        Once, the Sanctuary of the First Roots welcomed every
        creature of the forest. Pilgrims came to leave offerings
        beneath its branches, and children played among the
        great roots without fear.

        Now, even the moss seems reluctant to grow.

        To the north, an archway of intertwined branches leads
        deeper into the temple.

        It looks perfectly safe.

        Which, given the circumstances, is hardly reassuring.
        """,

    "Hall of the Twin Celestials": """
        The passage opens into a vast circular hall.

        Two towering figures stand carved into the opposing walls:
        the Sun God, crowned in golden rays, and the Moon Goddess,
        veiled beneath an arch of silver stars.

        Once, their outstretched hands nearly touched above the
        center of the chamber.

        Now a jagged fracture runs between them.

        The golden mosaics beneath the Sun God's feet are warm
        to the touch, while frost clings to the stones beneath
        the Moon Goddess. Where their patterns meet, the floor
        has split, and something dark pulses in the cracks.

        A low hum echoes through the chamber.

        It rises.

        Falters.

        Then begins again.

        Whatever ancient magic once held this place together
        appears to be doing so through sheer stubbornness.

        A quality you can respect.

        Four passages lead away from the hall.

        To the east, pale sunlight spills through a vine-covered
        archway. To the west, a cool silver glow flickers against
        the walls.

        The southern passage leads back toward the Sanctuary.

        To the north, an ancient doorway stands sealed beneath
        two circular recesses, one shaped like the sun and the
        other like the moon.

        The stone surrounding them is covered in deep scratches.

        Apparently, you are not the first person to consider
        forcing the door open.

        Judging by the absence of an obvious success story,
        you decide to investigate the other passages first.
        """,

    "Moonwell": """
        The passage opens into a secluded grotto.

        Ancient roots curl along the walls, their surfaces
        draped in pale moss that glimmers like frost beneath
        a moonless sky.

        At the chamber's center lies a pool of perfectly still
        water. Silver light dances across its surface, though
        no moon is visible overhead.

        For a moment, you understand why pilgrims once
        travelled for days to reach this place.

        Then you notice the smell.

        Something beneath the sweet scent of wet stone and
        flowering moss carries the sharp, metallic tang of
        decay.

        You approach the water.

        Your reflection follows.

        A moment too late.

        You stop.

        The reflection stops.

        Eventually.

        That seems perfectly normal, and you decide not to
        think about it too closely.

        Beneath the water, you can make out a small stone
        pedestal. Something silver rests upon its surface,
        untouched by the dark tendrils creeping across the
        bottom of the pool.

        The water ripples once.

        Nothing has moved.

        A narrow passage leads east, back toward the Hall
        of the Twin Celestials.
        """,

    "Sunlit Conservatory": """
        Once, this must have been a magnificent garden.

        Ancient stone pathways wind between raised flowerbeds,
        their edges softened by centuries of moss and creeping
        vines. Weathered statues stand among the foliage,
        their faces turned toward the heavens in silent prayer.

        Above, sunlight pours through the glass ceiling.

        It is warm. Golden. Beautiful.

        And somehow, the garden remains dark.

        A strange gloom clings to the corners of the chamber,
        pooling beneath the leaves and stretching between the
        statues. The sunlight reaches the ground, but the
        shadows refuse to retreat.

        You step between the flowerbeds.

        Roses droop upon thorny stems. Pale lilies curl inward,
        their petals browned and brittle. Even the climbing
        vines have begun to wither, hanging from their trellises
        like abandoned ropes.

        Yet the earth beneath your feet is warm.

        Something has been tending this place.

        Or trying to.

        At the rear of the conservatory stands a dilapidated
        gardener's shed, nearly swallowed by ivy. Its roof
        sags beneath the weight of dead branches, and one
        wooden door hangs crookedly from a rusted hinge.

        A collection of broken tools lies scattered outside.

        Apparently, even divine gardening requires someone
        to remember where they left the pruning shears.

        Near the center of the garden, a small stone pedestal
        rises from a circular bed of dying sunflowers.

        Upon it rests a golden stone, glowing with a warmth
        the surrounding flowers can no longer seem to absorb.

        For a moment, a faint breeze passes through the garden.

        The sunflowers turn toward you.

        Then, slowly, they bow their heads again.

        A passage to the west leads back toward the Hall
        of the Twin Celestials.
    """,

    "Bridge of Remembrance": """
        The northern passage opens onto a narrow stone bridge.

        Beneath it stretches a chasm so deep that the darkness
        seems almost solid. No sound rises from below, though
        the occasional pebble slips from the crumbling edges
        and vanishes into the abyss.

        You wait for it to strike something.

        It never does.

        Along either side of the bridge stand rows of ancient
        memorial tablets, their surfaces worn smooth by the
        passing centuries.

        Names have been carved into the stone.

        Some are accompanied by dates. Others bear small
        symbols: a flowering branch, a crescent moon, a
        sunburst, or the impression of a child's hand.

        You pause beside one tablet.

        Its inscription has nearly disappeared, but beneath
        the weathered lettering someone once carved a
        small, carefully rendered fox.

        For a moment, you think of home.

        You continue onward.

        The air grows colder toward the middle of the bridge.
        Pale roots emerge from cracks in the stone, winding
        around the memorials as though the temple itself
        refuses to let them fall.

        Most of the tablets stand perfectly upright.

        One does not.

        Near the bridge's center, a memorial sits crooked
        upon its base. The surrounding stone is undisturbed,
        but the tablet appears to have been moved recently.

        You glance into the abyss.

        Then back at the tablet.

        Whatever secrets this place keeps, you sincerely
        hope none of them require climbing down there.

        The bridge continues north toward a circular chamber,
        while the southern passage leads back to the Hall
        of the Twin Celestials.
    """,

    "Chamber of Equilibrium": """
        The passage opens into an immense circular chamber.

        High above, a vaulted ceiling disappears into darkness.
        Ancient carvings spiral across the walls, depicting the
        Sun and Moon in an endless dance around the roots of
        a great and flowering tree.

        Once, this must have been the heart of the Keepers'
        most sacred ceremonies.

        Now, something has been driven through it.

        Great iron pipes run along the walls, their surfaces
        stained with rust and an oily black residue. They
        emerge from jagged openings in the southern stonework
        and disappear into the northern passage, where the
        roots grow thickest.

        Every few moments, something inside them knocks.

        Three times.

        Then silence.

        You decide that whatever lives inside an iron tube
        may continue doing so without your assistance.

        Near the eastern wall stands an enormous contraption
        of metal and glass.

        It rests upon two broad, segmented tracks, and a long
        jointed arm extends from its body. At the end hangs
        a great iron claw, its teeth buried in the remains
        of the chamber's once-beautiful mosaic floor.

        You approach cautiously.

        The thing has no eyes, no mouth, and no obvious
        means of movement.

        Nevertheless, it looks rather pleased with the
        damage it has caused.

        A faded emblem is stamped upon its side: a circle bisected by a jagged line, accompanied by unfamiliar lettering.

        You cannot decipher the words.

        This is mildly insulting.

        You can read Fae. Most Elvish, too, provided the writer hasn't gotten particularly inventive with the lettering.

        Whatever language these people have chosen, however, appears to have been invented specifically to inconvenience you.

        You study the markings for another moment.

        Nothing.

        Only the damage makes sense.

        Beneath the machine, broken tiles reveal a network
        of ancient roots. Several have been severed cleanly.
        Others coil around the iron claw, blackened where
        they touch the metal.

        The chamber trembles.

        For one brief moment, golden light races across the
        remaining floor carvings, followed by a pale silver
        glow.

        The two lights meet.

        Falter.

        And vanish.

        Whatever balance once sustained this place is still
        struggling to survive.

        Four passages lead away from the chamber.

        To the south, the Bridge of Remembrance offers a
        return to familiar ground.

        An ornate doorway stands to the east, its ancient
        locking mechanism still intact.

        To the west, a dark corridor disappears beneath
        thick curtains of webbing.

        And to the north, the iron pipes vanish into a
        passage choked with enormous, pulsing roots.

        Something beyond them exhales.

        The sound travels through the walls beneath your feet.

        You rather wish it hadn't.
    """,

    "Keeper's Residence": """
        The ornate eastern doorway opens with a reluctant groan.

        Beyond it lies a modest living chamber, its furnishings
        half-swallowed by creeping roots and centuries of dust.

        For the first time since entering the temple, you find
        a place that looks unmistakably lived in.

        A narrow bed rests against the far wall. Its blankets
        are tangled, the pillow bearing the faint impression
        of a head that has long since departed.

        Beside it stands a small wooden table.

        Two cups sit upon its surface.

        One has fallen onto its side, spilling something that
        dried into a dark stain upon the wood long ago.

        The other remains upright.

        You find this considerably more troubling than the
        number of limbs possessed by the local wildlife.

        A small hearth occupies the northern wall. Cold ashes
        fill its basin, and a blackened cooking pot hangs
        above it.

        Someone has carefully arranged a bundle of dried herbs
        beside the hearth.

        You recognize several of them.

        Moonwort. Feverleaf. A sprig of winter's breath.

        Medicinal plants.

        Whatever happened here, someone had been preparing
        to treat the sick.

        Near the bed stands a writing desk, its surface
        cluttered with parchment, charcoal sketches, and
        a leather-bound journal.

        Most of the pages are written in familiar Fae script.

        You recognize careful observations of the temple's
        gardens, the changing seasons, and the movements
        of the ancient roots.

        But the later pages are different.

        The writing becomes hurried.

        Drawings of strange iron contraptions replace the
        delicate illustrations of flowers and woodland
        creatures.

        One page depicts a network of metal pipes piercing
        the roots beneath the Chamber of Equilibrium.

        Another shows a great flowering plant, its petals
        spread wide beneath the sun.

        The following drawing depicts the same plant.

        Its petals are black.

        Its roots twist around something resembling a
        broken iron vessel.

        Beneath the illustration, a single sentence has
        been written in Ancient Fae.

        "The guardian no longer recognizes our voices."

        You stare at the drawing for a long moment.

        A loose sheet of parchment lies beneath the journal.
        Its surface bears unfamiliar Common lettering,
        painstakingly copied beside a sketch of a jagged
        emblem.

        You recognize the emblem.

        It was stamped upon the iron creature in the
        Chamber of Equilibrium.

        The words remain entirely meaningless.

        You are beginning to suspect this language was
        invented specifically to inconvenience you.

        At the foot of the bed rests a small wooden chest.
        Its contents have been disturbed, as though someone
        packed in haste and then thought better of leaving.

        A narrow passage leads south toward a chamber
        lined with ancient stonework.

        To the west, the doorway returns to the
        Chamber of Equilibrium.

        You glance once more toward the two cups.

        Whoever lived here had expected company.

        You rather hope they found it.
    """,

    "Reliquary": """
        The southern passage opens into a chamber that has
        apparently served several purposes over the centuries.

        A sacred repository.

        A workshop.

        A storeroom.

        And, judging by the present state of affairs, a place
        where the Keepers put things they intended to deal
        with later.

        Much, much later.

        Dust lies thick upon the flagstones. Ancient roots
        wind between overturned tables and broken chairs,
        their pale tendrils curling around discarded tools
        and bundles of brittle parchment.

        Several wooden staffs lean against a workbench.

        One has been carefully sanded but never polished.
        Another lies in three pieces, its broken shaft
        bound together with strips of linen.

        A third is missing its upper half entirely.

        You suspect its owner eventually grew tired of
        waiting for repairs and simply became shorter.

        Empty weapon racks line the western wall.

        Most have long since collapsed beneath the weight
        of time, though a few still hold rusted blades,
        cracked shields, and ceremonial implements whose
        original purposes are no longer obvious.

        Near the center of the chamber stands an enormous
        wooden wardrobe, its doors hanging slightly askew.

        A curtain of ivy has claimed most of its surface,
        but the wood beneath remains remarkably intact.

        Against the western wall rests an ornate chest.

        Its hinges have turned green with age, and a thick
        layer of dust obscures the intricate carvings
        along its lid.

        Unlike the surrounding debris, it appears to
        have been placed here with considerable care.

        At the rear of the chamber stands a broad stone
        altar, almost entirely concealed beneath a heavy,
        moth-eaten cloth.

        Something faintly green pulses beneath the fabric.

        You stare at it.

        It pulses again.

        Well.

        That seems considerably more promising than
        the collection of broken furniture.

        Along the eastern wall, however, something
        altogether different catches your attention.
        
        A heap of unfamiliar metal contraptions lies
        beneath a collapsed shelving unit.
        
        Lengths of iron tubing spill across the floor.
        Small glass cylinders rest in a wooden crate,
        their contents dried into a dark, oily residue.
        
        Beside them sits a squat metal box, its surface
        marked with the same jagged emblem you noticed
        in the Chamber of Equilibrium.
        
        Several strange symbols have been stamped
        along its side.
        
        Common, presumably.
        
        You still cannot read it.
        
        One of the cylinders makes a faint clicking sound.
        
        You consider investigating.
        
        Then you remember the enormous iron creature
        currently dismantling the temple's foundations.
        
        You decide the mysterious clicking box may
        continue its important work without your assistance.
        
        A rare moment of excellent judgment.
        
        Above the scattered debris, faded carvings of
        the Sun and Moon stretch across the ceiling.
        
        Their intertwined rays converge upon the altar,
        where the roots beneath the stone glow faintly
        with ancient magic.
        
        Whatever this chamber became in its final years,
        it was once a place of extraordinary reverence.
        
        And despite everything, something sacred
        still sleeps among the rubbish.
        
        The northern passage leads back toward the
        Keeper's Residence.
    """,

    "The Weaver's Hollow": """
        The western passage narrows considerably.
        
        At first, you mistake the pale strands hanging
        from the ceiling for the roots of the temple.
        
        Then one brushes against your cheek.
        
        Silk.
        
        Thick ropes of webbing stretch between ancient
        pillars, sagging beneath the weight of things
        you would rather not identify.
        
        The chamber smells of damp stone, rotting leaves,
        and something unpleasantly sweet.
        
        The floor is scattered with brittle husks.
        Insects. Small animals. Something with a boot.
        
        You decide not to investigate the boot.
        
        High above, a dark shape clings to the ceiling.
        
        It moves.
        
        Not across the stone.
        
        Beneath it.
        
        One long limb unfolds from the shadows.
        
        Then another.
        
        Then several more.
        
        Each joint bends in a direction that seems
        entirely unnecessary.
        
        A faint clicking begins overhead.
        
        The sound grows louder.
        
        And then, quite suddenly, it stops.
        
        You realize the webbing beneath your feet
        has begun to tighten.
        
        To the east, the passage returns to the
        Chamber of Equilibrium.
        
        A narrow opening descends south into darkness.
        
        You sincerely hope whatever lives above you
        has no interest in either.
    """,

    "Crypt of the First Keepers": """
        The southern passage descends into darkness.
        
        The stairs are narrow, worn smooth by countless
        footsteps. A cold draft rises from below, carrying
        the stale scent of dust, old stone, and something
        you would rather not identify.
        
        With each step, the sounds of the temple fade.
        
        Even the roots seem quieter here.
        
        At the bottom, an immense burial chamber opens
        before you.
        
        Rows of stone coffins rest beneath vaulted arches,
        their lids carved with the likenesses of the
        Keepers who sleep within.
        
        Some bear the symbols of the Sun.
        
        Others, the Moon.
        
        A few depict both, their rays and crescents
        intertwined around peaceful, sleeping faces.
        
        You approach the nearest coffin.
        
        Its lid sits slightly crooked.
        
        There is a gap just wide enough for something
        to peer through.
        
        You decide that whatever might be looking out
        deserves its privacy.
        
        Farther along the chamber, several coffins
        have broken open beneath the weight of
        encroaching roots.
        
        Ancient bones lie scattered across the floor.
        
        A skull rests beside a fallen column,
        its empty sockets turned toward you.
        
        You stare at it.
        
        It stares back.
        
        Presumably.
        
        A faint scraping sound echoes from somewhere
        among the tombs.
        
        You freeze.
        
        The sound comes again.
        
        Slow.
        
        Deliberate.
        
        Then you notice a pale root dragging itself
        across the stone.
        
        You have never been so relieved to discover
        that a plant is moving.
        
        Near the center of the crypt, the air changes.
        
        The oppressive cold gives way to a gentle warmth.
        
        There, beneath a great arch of intertwining
        branches, stands a magnificent stone shrine.
        
        Unlike the rest of the chamber, it bears
        no dust.
        
        Its carvings remain sharp and beautiful,
        depicting the Sun God and Moon Goddess
        standing together beneath the boughs
        of the First Grove.
        
        Fresh-looking flowers bloom along its base.
        
        Their petals are white and gold.
        
        Their leaves are a deep, healthy green.
        
        You approach cautiously.
        
        No rot stains the stone.
        
        No blackened roots pierce its foundation.
        
        Even the air feels cleaner here.
        
        At the shrine's center, a small recess
        cradles a luminous green stone.
        
        A faint pulse moves through it.
        
        Once.
        
        Twice.
        
        Like a heartbeat.
        
        For the first time since entering the temple,
        the rhythm feels steady.
        
        You reach toward the shrine.
        
        The surrounding roots stir gently, but
        do not retreat from your touch.
        
        Whatever sacred power protects this place
        has not forgotten its purpose.
        
        You glance back toward the coffins.
        
        The bones remain exactly where you left them.
        
        You find this deeply encouraging.
        
        The northern stairway leads back toward
        the Weaver's Hollow.
    """,

    "Heart of Gaia": """
        The northern passage yields reluctantly.
    
        Thick roots pull away from the ancient doorway,
        their surfaces trembling beneath your touch.
    
        Beyond them lies the Heart of Gaia.
    
        Or what remains of it.
    
        The chamber is immense.
    
        Once, its vaulted ceiling must have disappeared
        beneath a canopy of living branches, their leaves
        catching the sacred light of Sun and Moon alike.
    
        Now, almost nothing grows.
    
        The roots are black.
    
        The stone is black.
    
        Even the air seems stained.
    
        A suffocating haze hangs throughout the chamber,
        carrying the sharp smell of scorched metal,
        rotting vegetation, and something sickeningly sweet.
    
        You cover your mouth.
    
        It does very little.
    
        Great iron pipes descend from the ceiling,
        driven through the ancient stonework and buried
        deep within the temple's living roots.
    
        Several have ruptured.
    
        Thick, oily liquid drips from their broken seams,
        collecting in stagnant pools across the floor.
    
        Where it touches the roots, their surfaces blister.
    
        Where it touches the stone, something pale and
        unrecognizable begins to grow.
    
        You have seen these machines before.
    
        Or pieces of them.
    
        But never so many.
    
        The chamber's eastern wall has been torn open,
        revealing an enormous apparatus of iron, glass,
        and grinding metal.
    
        Its great wheels turn with agonizing slowness.
    
        A series of pistons drives something dark through
        the surrounding pipes.
    
        Every movement sends a shudder through the floor.
    
        Every shudder is answered by the roots.
    
        It takes you a moment to recognize the rhythm.
    
        The temple is breathing.
    
        And the machinery is breathing with it.
    
        You approach the center of the chamber.
    
        There, beneath the remains of a shattered canopy,
        stands an enormous flowering creature.
    
        At least, you believe it was once a flower.
    
        Its great petals hang in ragged folds,
        their edges blackened and splitting.
    
        Thick vines coil around its immense body,
        twisting into shapes that resemble limbs.
    
        Its roots have forced their way through the stone,
        anchoring it to the chamber's ruined foundation.
    
        Then you notice the metal.
    
        Several iron tubes pierce the creature's lower body.
    
        Others have become embedded beneath its outer flesh,
        their surfaces disappearing into swollen growths
        of bark and diseased tissue.
    
        A broken mechanical arm protrudes from one side,
        its rusted joints wrapped so tightly in vines
        that you cannot tell where the machinery ends
        and the creature begins.
    
        A glass cylinder hangs beneath the largest bloom.
    
        Black liquid pulses through it.
    
        Once.
    
        Twice.
    
        With each movement, the creature shudders.
    
        A low, wet groan escapes from somewhere deep
        within its tangled body.
    
        You freeze.
    
        The flower moves.
    
        Slowly, its great head turns toward you.
    
        Several petals peel apart.
    
        Beneath them, rows of thornlike teeth glisten
        with a thick, dark fluid.
    
        A long vine drags across the floor.
    
        Another rises behind it.
    
        The creature's body contracts.
    
        The iron pipes groan.
    
        Something within the machinery begins to shriek.
    
        You take a step backward.
    
        The creature follows.
    
        For a moment, its enormous bloom tilts
        toward the faint light filtering through
        the shattered ceiling.
    
        Almost as though searching for the sun.
    
        Then one of the glass cylinders convulses.
    
        A fresh surge of black liquid courses
        through the metal embedded in its body.
    
        The creature twists violently.
    
        Its petals flare.
    
        A terrible cry fills the chamber.
    
        You understand very little about the iron
        contraptions surrounding you.
    
        But you understand pain.
    
        And whatever this creature once was,
        it has been made to endure far too much.
    
        The enormous bloom turns toward you again.
    
        This time, it opens wide.
    
        You have the distinct impression that
        negotiations are no longer an option.
    
        Behind you, the southern passage remains open.
    
        Before you stands Venious.
    
        The wounded guardian of Gaia.
    
        And the last obstacle between your dying forest
        and the hope of its restoration.
    """,
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


## Spider intro

spider_introduction = """
        Something drops from the ceiling.

        It does not land.

        Eight enormous limbs catch against the pillars,
        holding a swollen body suspended above the floor.

        For an instant, the creature hangs motionless.

        Then its legs begin to move.

        One at a time.

        The first unfolds with a wet, brittle crack.

        The second scrapes backward across the stone.

        The third bends beneath its body, then twists
        around until the hooked point faces forward.

        The remaining limbs follow in a rapid,
        horribly uneven sequence.

        Its abdomen drags against the webbing.

        Something pulses beneath the stretched surface.

        You hear a faint grinding sound.

        The creature's head jerks toward you.

        Then past you.

        Then back again.

        Its many eyes catch the light.

        Several blink.

        Not together.

        You have encountered many spiders in your life.

        You would like to formally object to this one.
    """


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


    "uninjured_victory": """
        The Heartstone warms in your grasp.
        
        The mantle settles against your shoulders,
        its ancient threads shimmering with the
        intertwined light of Sun and Moon.
        
        You draw the Thornkeeper's Blade.
        
        Venious screams.
        
        A great vine lashes toward you.
        
        You raise your arm instinctively, and the
        creature's thorned appendage strikes the mantle
        with enough force to send you stumbling.
        
        The fabric holds.
        
        Barely.
        
        You look toward the enormous bloom.
        
        Then toward the iron pipes buried in its flesh.
        
        With every pulse of the machinery, black liquid
        courses through the creature's swollen roots.
        
        With every pulse, Venious screams again.
        
        You understand.
        
        The creature is not protecting the machines.
        
        It is trapped within them.
        
        Another vine strikes.
        
        You duck beneath it and bring your blade down
        upon a narrow iron tube protruding from the
        creature's side.
        
        Steel meets metal.
        
        A sharp crack echoes through the chamber.
        
        The tube splits.
        
        Black fluid spills across the stone.
        
        Venious convulses.
        
        Its enormous bloom twists toward you, petals
        pulling apart to reveal rows of terrible thorns.
        
        You stagger backward.
        
        A second vine catches your shoulder.
        
        The mantle flares with pale silver light.
        
        You slash instinctively, severing the vine
        before it can tighten around your throat.
        
        The creature recoils.
        
        You hesitate.
        
        An apology climbs your throat,
        
        but another pipe shudders beside you.
        
        You decide the apology can wait.
        
        You strike again.
        
        And again.
        
        One by one, the smaller tubes rupture beneath
        your blade.
        
        The machinery begins to shriek.
        
        Deep within the eastern wall, enormous gears
        grind against one another.
        
        You turn toward the great iron apparatus.
        
        A thick conduit stretches from its central
        mechanism into the roots beneath Venious.
        
        You follow it with your eyes.
        
        That cannot possibly be safe.
        
        Then you raise your blade,
        
        and strike.
        
        The first blow glances harmlessly away.
        
        The second sends a spray of sparks across
        the floor.
        
        The third finds a weakened seam.
        
        Something inside the conduit breaks.
        
        The machinery gives a tremendous, grinding
        shudder.
        
        Then stops.
        
        
        Silence falls.
        
        
        For the first time since entering the
        Heart of Gaia, the pipes are still.
        
        Venious trembles.
        
        Its great bloom hangs low, supported by
        roots that have begun to loosen around
        the broken iron.
        
        You approach slowly.
        
        The guardian raises a single thorned vine.
        
        You stop.
        
        It does not strike.
        
        Beneath the blackened petals, you notice
        something you had not seen before.
        
        Green.
        
        A single, narrow strip of living tissue
        beneath the rot.
        
        You remember the Seed of the First Grove.
        
        Kneeling before the guardian, you draw
        the tiny seed from your belongings.
        
        It seems impossibly small.
        
        A rather underwhelming solution to a
        catastrophe of this magnitude.
        
        Nevertheless, you press it into the
        earth beneath Venious.
        
        The Heartstone pulses.
        
        Once.
        
        Twice.
        
        Golden light spills across the shattered
        floor, followed by a cool silver radiance.
        
        The two lights meet beneath your hands.
        
        For a moment, nothing happens.
        
        Then the roots move.
        
        Not violently.
        
        Not in pain.
        
        They curl gently around the seed, drawing
        it beneath the soil.
        
        A faint green glow spreads outward.
        
        The blackened roots begin to soften.
        
        The terrible oily residue retreats into
        the cracks between the stones.
        
        Above you, Venious gives a low, trembling
        sound.
        
        You look up.
        
        One of its ruined petals unfolds.
        
        Beneath it, a new petal has begun to grow.
        
        Then another.
        
        The old, blackened growth falls away
        in brittle fragments.
        
        The guardian's immense body shudders as
        the last of the iron machinery is pushed
        free from its roots.
        
        A broken pipe falls to the floor.
        
        Then a rusted cylinder.
        
        Then the great mechanical arm, its joints
        finally released from the living vines
        that held it captive.
        
        Venious rises.
        
        Its enormous bloom opens toward the light
        filtering through the shattered ceiling.
        
        For the first time, you see its true colors.
        
        Deep green leaves.
        
        Petals of gold and pale violet.
        
        At its center, a warm amber glow.
        
        The guardian turns toward you.
        
        You stand very still.
        
        Considering the events of the past several
        minutes, this seems prudent.
        
        A slender vine extends toward your hand.
        
        You hesitate.
        
        Then offer your fingers.
        
        The vine curls gently around them.
        
        Warm.
        
        Alive.
        
        The chamber exhales.
        
        Beyond the temple walls, birdsong returns.
        
        Venious lowers its great flowering head,
        and for a moment you rest your forehead
        against one enormous, golden petal.
        
        You came here expecting to destroy
        something monstrous.
        
        Instead, you have saved something beautiful.
    """,
    "wounded_victory": """
        The Heartstone warms in your grasp.
        
        You raise the Thornkeeper's Blade.
        
        Venious screams.
        
        A thorned vine lashes toward you, striking the
        mantle with enough force to send you stumbling.
        
        Your wounded shoulder catches against the stone.
        
        Pain flashes through your chest.
        
        For a moment, you cannot breathe.
        
        Across the chamber, another surge of black liquid
        courses through the iron pipes.
        
        Venious convulses.
        
        You see the machinery buried in its roots.
        
        You understand what must be done.
        
        You strike at the nearest conduit.
        
        Metal splits.
        
        The guardian screams again.
        
        You stagger toward the next pipe, but your injured
        arm refuses to rise.
        
        A vine coils around your ankle.
        
        The floor rushes toward you.
        
        Venious draws you closer.
        
        Its enormous bloom opens, revealing rows of thorns
        slick with poisoned sap.
        
        You look toward the great mechanical apparatus.
        
        Too far.
        
        Then toward the Seed of the First Grove.
        
        You cannot reach the roots beneath the creature.
        
        Not while it lives.
        
        Your grip tightens around the blade.
        
        "I'm sorry."
        
        You strike.
        
        The ancient steel pierces the guardian's heart.
        
        Venious shudders.
        
        Its vines loosen.
        
        For one terrible moment, the enormous flower
        seems to look directly at you.
        
        Then its petals fold inward.
        
        The machinery continues grinding.
        
        You crawl beneath the fallen guardian, dragging
        your wounded body across the broken stone.
        
        With the last of your strength, you drive the
        blade into the main conduit.
        
        The iron splits.
        
        The machinery falls silent.
        
        You draw the Seed of the First Grove from your
        belongings and press it into the waiting earth.
        
        Golden light spills through the roots.
        
        Silver follows.
        
        The chamber exhales.
        
        All around you, the blackened growth begins
        to soften. Healthy green spreads through the
        ancient roots, climbing toward the shattered
        ceiling.
        
        Beyond the temple, birdsong returns.
        
        You look back at Venious.
        
        The guardian lies still.
        
        Its ruined petals have begun to change.
        
        The black fades from their edges, revealing
        the faintest traces of gold and violet.
        
        For a moment, you wait.
        
        Perhaps the light will reach its heart.
        
        Perhaps it will rise.
        
        It does not.
        
        A small flower pushes through the earth
        beside its fallen body.
        
        You touch one trembling petal.
        
        "... I'm so sorry," you whisper.
        
        The forest has been saved.
        
        You wish you could have saved all of it.
        """,

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


## Narrative text formatting

def print_story(passage):
    """Remove source-code indentation while preserving story line breaks."""
    cleaned = "\n".join(line.strip() for line in passage.strip().splitlines())
    print(cleaned)


## Room Function

def display_room(room_name):
    print(f"\n{room_name}")

    if room_name == "The Weaver's Hollow" and spider_defeated:
        print("The enormous spider lies still among its broken webs.")
    else:
        print_story(descriptions.get(room_name, "No description available."))

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

    print_story(object_data["description"])
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

    print_story(spider_introduction)
    print_story(spider_scenes[outcome])

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

    if outcome == "victory":
        if injured:
            print_story(venious_scenes["wounded_victory"])
            print_story(victory_endings["wounded"])
        else:
            print_story(venious_scenes["uninjured_victory"])
            print_story(victory_endings["uninjured"])

        return "victory"

    print_story(venious_scenes["defeat"])
    return "death"


## Restart

def restart_game(cause):
    global current_room, spider_defeated, injured

    print_story(death_endings[cause])

    print("\n             GAME OVER")
    print("       The forest remembers you.")

    input("\nPress Enter to begin a new journey...")


    current_room = "Sanctuary of the First Roots"
    inventory.clear()
    spider_defeated = False
    injured = False

    print("\nA new journey begins.")
    print_story(opening_scene)

    input("\nPress Enter to return to the temple...")

    display_room(current_room)


## Opening

print("Welcome to the Temple of Gaia!")

print_story(opening_scene)

input("\nPress Enter to begin your journey...")

print("\nMove using 'go north/south/east/west' or 'go up/down/left/right'.")
print("Type 'help' to see all available commands.")

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
        print("go up / down / left / right")
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
        direction = command[3:].strip().lower()

        direction = direction_aliases.get(
            direction,
            direction.capitalize()
        )

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
                        input("\nPress Enter to close the game...")
                        break


        else:
            print("You seem to have smacked right into a wall. Be careful!")
