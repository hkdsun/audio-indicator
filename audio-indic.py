#!/usr/bin/env python
#
# Copyright 2009-2012 Canonical Ltd.
#
# Authors: Neil Jagdish Patel <neil.patel@canonical.com>
#          Jono Bacon <jono@ubuntu.com>
#          David Planella <david.planella@ubuntu.com>
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of either or both of the following licenses:
#
# 1) the GNU Lesser General Public License version 3, as published by the 
# Free Software Foundation; and/or
# 2) the GNU Lesser General Public License version 2.1, as published by 
# the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranties of 
# MERCHANTABILITY, SATISFACTORY QUALITY or FITNESS FOR A PARTICULAR 
# PURPOSE.  See the applicable version of the GNU Lesser General Public 
# License for more details.
#
# You should have received a copy of both the GNU Lesser General Public 
# License version 3 and version 2.1 along with this program.  If not, see 
# <http://www.gnu.org/licenses/>
#
import os
from gi.repository import Gtk
from gi.repository import AppIndicator3 as appindicator


def run_rear(w):
  os.system("gksudo -u root ./.audio-rear.py")

def run_front(w):
  os.system("gksudo -u root ./.audio-front.py")

if __name__ == "__main__":
    ind = appindicator.Indicator.new (
                            "audio-jack-selector",
                            "multimedia-volume-control",
                            appindicator.IndicatorCategory.HARDWARE)
    ind.set_status (appindicator.IndicatorStatus.ACTIVE)
    ind.set_attention_icon ("indicator-messages-new")

    # create a menu
    menu = Gtk.Menu()

    # create some 
    rear_port_menuitem = Gtk.MenuItem("Use Rear Jack")
    front_port_menuitem = Gtk.MenuItem("Use Front Jack")

    menu.append(front_port_menuitem)
    menu.append(rear_port_menuitem)

    # this is where you would connect your menu item up with a function:

    rear_port_menuitem.connect("activate", run_rear)
    front_port_menuitem.connect("activate", run_front)

    # show the items
    front_port_menuitem.show()
    rear_port_menuitem.show()
    
    ind.set_menu(menu)

    Gtk.main()
