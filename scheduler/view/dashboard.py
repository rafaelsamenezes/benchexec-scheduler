import scheduler.view.base as B

class Dashboard(B.Base):

    def __init__(self):
        super().__init__("Dashboard")

    def _template_path(self):
        return "web/index.html"

    def _generate_template_args(self):
        d = super().generate_template_args()
        return d

