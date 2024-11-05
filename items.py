class Item:
    def __init__(self,slot,name,strength,defense,health,agility,intelligence):
        self.slot=slot
        self.name=name
        self.strength=strength
        self.defense=defense
        self.health = health
        self.agility = agility
        self.intelligence = intelligence

cardboardHelm = Item('head','Cardboard Helm',0,2,0,2,5)
scaleMail = Item('chest','Scale Mail',5,10,10,0,5)
rustyBlade = Item('weapon','Rusty Blade',7,0,0,2,0)
