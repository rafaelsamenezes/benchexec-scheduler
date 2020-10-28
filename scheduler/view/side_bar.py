from enum import Enum


class SideBarItem:

    def __init__(self, name: str, icon: str, is_active: bool, href: str):
        self.name = name
        self.icon = icon
        self.is_active = is_active
        self.href = href

    def __repr__(self):
        return "<SideBarItem (name='%s', icon='%s', is_active='%s', href='%s')" % (
            self.name,
            self.icon,
            self.is_active,
            self.href)


MENU = [("Dashboard", "home", "/"),
        ("Machines", "hard-drive", "/machines"),
        ("Jobs", "clock", "/jobs"),
        ("Results", "book", "/results")]

ITEMS = {name: SideBarItem(name, icon, False, href) for (name, icon, href) in MENU}
