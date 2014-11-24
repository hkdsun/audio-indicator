#!/usr/bin/env python
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
