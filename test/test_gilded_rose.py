# -*- coding: utf-8 -*-
'''import unittest

from src.gilded_rose_refactor import *


def test_Backstage():
    assert Backstage("backstage_passes", 15, 0).update_quality() == 0
    assert Backstage("backstage_passes", 15, 4).update_quality() == 18
    assert Backstage("backstage_passes", 15, 6).update_quality() == 17
    assert Backstage("backstage_passes", 0, 11).update_quality() == 1
    assert Backstage("backstage_passes", 50, 0).update_quality() == 0


def test_Conjured():
    assert Conjured("conjured_flask", 20, 15).update_quality() == 18
    assert Conjured("conjured_flask", 20, -3).update_quality() == 16
    assert Conjured("conjured_flask", 0, -3).update_quality() == 0


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