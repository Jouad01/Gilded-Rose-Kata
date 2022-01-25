class GildedRose(object):
    def __init__(self, items):
        self.items = items
    
    def update_quality(self):
        for item in self.items:
        # Los items que hay en este if
            item.update_quality()

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
    
    def __repr__(self):
        return "%s, %s, %s," % (self.name, self.sell_in, self.quality)
    
class AgedBrie:
    def update_quality(self):
        self.upgrade_quality()
        self.reduce_sell_in()
        if self.item.sell_in < 0:
            self.upgrade_quality()
