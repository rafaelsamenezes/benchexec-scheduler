import scheduler.view.base as B

class Machines(B.Base):

    def __init__(self):
        super().__init__("Machines")

    def _template_path(self):
        return "web/machines.html"

    def _generate_template_args(self):
        d = super().generate_template_args()
        return d