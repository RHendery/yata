"""
Copyright 2019 kivou.2000607@gmail.com

This file is part of yata.

    yata is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    yata is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with yata. If not, see <https://www.gnu.org/licenses/>.
"""

from django.core.management.base import BaseCommand
from django.utils import timezone

from faction.models import Faction
from yata.handy import apiCall

import json


class Command(BaseCommand):
    def handle(self, **options):
        print("[command.faction.update] start")
        for faction in Faction.objects.filter(nKeys__gt=0):
            print("[command.faction.update] faction {}".format(faction))
            try:
                print("[command.faction.update] faction {}: clean history".format(faction))
                faction.cleanHistory()
                print("[command.faction.update] faction {}: check keys".format(faction))
                faction.checkKeys()
                if faction.nKeys > 0:
                    print("[command.faction.update] faction {}: update logs".format(faction))
                    faction.updateLog()
                    print("[command.faction.update] faction {}: update upgrades".format(faction))
                    faction.updateUpgrades()
                    print("[command.faction.update] faction {}: update crimes".format(faction))
                    faction.updateCrimes()
                    # faction.resetSimuUpgrades(update=True)
                    # faction.getFactionTree()
                else:
                    print("[command.faction.update] faction {}: no more keys".format(faction))
            except BaseException as e:
                print("[command.faction.update] {}".format(e))

        print("[command.faction.update] end")
