import copy
import scheduler.view.side_bar as SB

class Base():

    def __init__(self, default_item):
        self.default_item = default_item
   

    def _template_path(self):
        raise NotImplementedError

    def _get_menu_items(self):
        items = copy.deepcopy(SB.ITEMS)
        items[self.default_item].is_active = True
        return list(items.values())

    def generate_template_args(self):
        d = dict(side_bar_items=self._get_menu_items())
        return d