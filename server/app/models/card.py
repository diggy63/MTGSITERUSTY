class Card:
    def __init__(self, id, artist, artistids, asciiname, attractionlights, availability, boostertypes,
                 bordercolor, cardparts, coloridentity, colorindicator, colors, defense, dueldeck, edhrecrank,
                 edhrecsaltiness, faceconvertedmanacost, faceflavorname, facemanavalue, facename, finishes,
                 flavorname, flavortext, frameeffects, frameversion, hand, hasalternativedecklimit, hascontentwarning,
                 hasfoil, hasnonfoil, isalternative, isfullart, isfunny, isonlineonly, isoversized, ispromo,
                 isrebalanced, isreprint, isreserved, isstarter, isstoryspotlight, istextless, istimeshifted,
                 keywords, language, layout, leadershipskills, life, loyalty, manacost, manavalue, name, number,
                 originalprintings, originalreleasedate, originaltext, originaltype, otherfaceids, power, printings,
                 promotypes, rarity, rebalancedprintings, relatedcards, securitystamp, setcode, side, signature,
                 sourceproducts, subsets, subtypes, supertypes, text, toughness, type, types, uuid, variations, watermark):
        self.id = id
        self.artist = artist
        self.artistids = artistids
        self.asciiname = asciiname
        self.attractionlights = attractionlights
        self.availability = availability
        self.boostertypes = boostertypes
        self.bordercolor = bordercolor
        self.cardparts = cardparts
        self.coloridentity = coloridentity
        self.colorindicator = colorindicator
        self.colors = colors
        self.defense = defense
        self.dueldeck = dueldeck
        self.edhrecrank = edhrecrank
        self.edhrecsaltiness = edhrecsaltiness
        self.faceconvertedmanacost = faceconvertedmanacost
        self.faceflavorname = faceflavorname
        self.facemanavalue = facemanavalue
        self.facename = facename
        self.finishes = finishes
        self.flavorname = flavorname
        self.flavortext = flavortext
        self.frameeffects = frameeffects
        self.frameversion = frameversion
        self.hand = hand
        self.hasalternativedecklimit = hasalternativedecklimit
        self.hascontentwarning = hascontentwarning
        self.hasfoil = hasfoil
        self.hasnonfoil = hasnonfoil
        self.isalternative = isalternative
        self.isfullart = isfullart
        self.isfunny = isfunny
        self.isonlineonly = isonlineonly
        self.isoversized = isoversized
        self.ispromo = ispromo
        self.isrebalanced = isrebalanced
        self.isreprint = isreprint
        self.isreserved = isreserved
        self.isstarter = isstarter
        self.isstoryspotlight = isstoryspotlight
        self.istextless = istextless
        self.istimeshifted = istimeshifted
        self.keywords = keywords
        self.language = language
        self.layout = layout
        self.leadershipskills = leadershipskills
        self.life = life
        self.loyalty = loyalty
        self.manacost = manacost
        self.manavalue = manavalue
        self.name = name
        self.number = number
        self.originalprintings = originalprintings
        self.originalreleasedate = originalreleasedate
        self.originaltext = originaltext
        self.originaltype = originaltype
        self.otherfaceids = otherfaceids
        self.power = power
        self.printings = printings
        self.promotypes = promotypes
        self.rarity = rarity
        self.rebalancedprintings = rebalancedprintings
        self.relatedcards = relatedcards
        self.securitystamp = securitystamp
        self.setcode = setcode
        self.side = side
        self.signature = signature
        self.sourceproducts = sourceproducts
        self.subsets = subsets
        self.subtypes = subtypes
        self.supertypes = supertypes
        self.text = text
        self.toughness = toughness
        self.type = type
        self.types = types
        self.uuid = uuid
        self.variations = variations
        self.watermark = watermark

    # Optionally, you can define a method to serialize the card object
    def serialize(self):
        return {
            'id': self.id,
            'uuid':self.uuid,
            'name': self.name,
            'mana': self.manacost,
            'card_text':self.text,
            'power': self.power,
            'toughness': self.toughness,
            'type':self.type,
            'card_subtype':self.subsets,
            'set_code':self.setcode,
            'availability':self.availability,
            'colors':self.colors,
            'keywords':self.keywords,
            
            # Add other attributes as needed
        }
