from typing import ItemsView


class GildedRose:
    def __init__(self, items):
        self.stock = items 
    
    def update_quality(self):
        for item in self.stock:
            item.update_quality()

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
    
    def __repr__(self):
        # Devuelve, no imprime, algo como toString pero en Python
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class Interfaz: # Con duda de mantenerlo
    def update_quality(self):
        # Busca pero pasa del objeto
        pass 

class NormalItem(Item, Interfaz): # Conecta con Item
    def __init__(self, name, sell_in, quality):
        item.__init__(self, name, sell_in, quality)

    def setSell_in(self):
        self.sell_in = self.sell_in - 1 # Tener en cuenta para más adelante
    
    def set_quality(self):
        if self.set_quality + valor > 50:
            self.set_quality = 50
        elif self.set_quality + valor >= 0:
            self.set_quality = self.set_quality + valor
        else:
            self.set_quality = 0
        # assert 0 <=
