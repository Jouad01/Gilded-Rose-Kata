'''class Inventory(object):

    def __init__(self, items):
        self.items = list(items)

    def update_quality(self):
        for item in self.items:
            item.update_quality()


class Item:
    def __init__(self, name, quality, sell_in):
        self.name = name
        self.quality = quality
        self.sell_in = sell_in

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.quality, self.sell_in)

class Updateable:

    def update_quality(self):
        pass


class ConjuredItem(Item, Updateable):
    def __init__(self, name, quality, sell_in):
        Item.__init__(self, name, quality, sell_in)

    def update_sell_in(self):
        self.sell_in -= 1

    def update_quality(self):
        if self.sell_in > 0:
            quality_increase = -2
        elif self.sell_in < 0:
            quality_increase = -4
        self.quality += quality_increase
        if self.quality < 0:  # esto nos asegura que la calidad no sea negativa, lo cual no es posible######
            self.quality = 0
        return self.quality


class NormalItem(Item, Updateable):
    def __init__(self, name, quality, sell_in):
        Item.__init__(self, name, quality, sell_in)

    def update_sell_in(self):
        self.sell_in -= 1  # tenemos dudas

    def update_quality(self):
        if self.sell_in > 0:
            quality_increase = -1
        elif self.sell_in < 0:
            quality_increase = -2
        self.quality += quality_increase
        if self.quality < 0:
            self.quality = 0
        return self.quality


class Sulfuras(NormalItem):
    def __init__(self, name, quality, sell_in):
        Item.__init__(self, name, quality, sell_in)

    def update_quality(self):
        # Seteamos la calidad en 80 por si fuera el caso de que hubiera un error a la hora de introducir la calidad del sulfuras, no hacemos un assert porque es más eficiente que el programa no se pare, no??
        self.quality = 80
        return self.quality


class AgedBrie(NormalItem):
    def __init__(self, name, quality, sell_in):
        Item.__init__(self, name, quality, sell_in)

    def update_quality(self):
        if self.sell_in >= 0:
            quality_increase = 1
        elif self.sell_in < 0:
            quality_increase = 2
        self.quality += quality_increase
        if self.quality > 50:
            self.quality = 50
        return self.quality


class Backstage(NormalItem):
    def __init__(self, name, quality, sell_in):
        Item.__init__(self, name, quality, sell_in)

    def update_quality(self):
        if self.sell_in > 10:
            quality_increase = 1
        elif self.sell_in > 5:
            quality_increase = 2
        elif self.sell_in > 0:
            quality_increase = 3
        elif self.sell_in == 0:
            quality_increase = - self.quality
        self.quality += quality_increase
        if self.quality > 50:
            self.quality = 50
        return self.quality'''




'''def test_Backstage():
    assert Backstage("backstage_passes", 15, 0).update_quality() == 0
    assert Backstage("backstage_passes", 15, 4).update_quality() == 18
    assert Backstage("backstage_passes", 15, 6).update_quality() == 17
    assert Backstage("backstage_passes", 0, 11).update_quality() == 1
    assert Backstage("backstage_passes", 50, 0).update_quality() == 0


def test_ConjuredItem():
    assert ConjuredItem("conjured_flask", 20, 15).update_quality() == 18
    assert ConjuredItem("conjured_flask", 20, -3).update_quality() == 16
    assert ConjuredItem("conjured_flask", 0, -3).update_quality() == 0


def test_NormalItem():
    assert NormalItem("Elixir of the Mongoose", 20, 15).update_quality() == 19
    assert NormalItem("Elixir of the Mongoose", 20, -3).update_quality() == 18
    assert NormalItem("Elixir of the Mongoose", 0, -3).update_quality() == 0


def test_AgedBrie():
    assert AgedBrie("Aged Brie", 20, 15).update_quality() == 21
    assert AgedBrie("Aged Brie", 20, -2).update_quality() == 22
    assert AgedBrie("Aged Brie", 20, 0).update_quality() == 21
    assert AgedBrie("Aged Brie", 50, 0).update_quality() == 50
    assert AgedBrie("Aged Brie", 50, 4).update_quality() == 50
    assert AgedBrie("Aged Brie", 50, -6).update_quality() == 50'''