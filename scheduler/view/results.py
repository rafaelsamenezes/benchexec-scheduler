import scheduler.view.base as B

class Results(B.Base):

    def __init__(self):
        super().__init__("Results")

    def _template_path(self):
        return "web/results.html"

    def _generate_template_args(self):
        d = super().generate_template_args()
        return d