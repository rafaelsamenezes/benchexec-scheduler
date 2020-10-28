from enum import Enum


class SideBarItem:

    def __init__(self, name: str, icon: str, is_active: bool):
        self.name = name
        self.icon = icon
        self.is_active = is_active

    def __repr__(self):
        return "<SideBarItem (name='%s', icon='%s', is_active='%s')" % (
            self.name,
            self.icon,
            self.is_active)


MENU = [("Dashboard", "home"),
        ("Machines", "hard-drive"),
        ("Jobs", "clock"),
        ("Results", "book")]

ITEMS = {name: SideBarItem(name, icon, False) for (name, icon) in MENU}
