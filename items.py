class Item:
    def __init__(self,slot,name,strength,defense,health,agility,intelligence):
        self.slot=slot
        self.name=name
        self.strength=strength
        self.defense=defense
        self.health = health
        self.agility = agility
        self.intelligence = intelligence
#types of slot: head, neck, chest, belt, feet, hands, arms, weapon
cardboardHelm = Item('head','Cardboard Helm',0,2,0,2,5)
rustyBlade = Item('weapon','Rusty Blade',7,0,0,2,0)
tunic = Item('chest','Old Tunic',0,1,5,2,0)
wornBoots = Item('feet','Worn boots',0,4,0,3,0)

scaleMail = Item('chest','Scale Mail',5,10,10,0,5)
strengthBelt = Item('belt','Belt of Giant Strength',15,0,0,0,0)
speedPendant = Item('neck','Pendant of Speed',0,0,0,10,0)
armorBracers = Item('arms',"Bracers of Armor",0,8,0,0,0)
mithrilGloves = Item("hands",'Mithril Gauntlets',7,9,5,3,4)

