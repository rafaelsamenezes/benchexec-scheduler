import scheduler.view.base as B

class Jobs(B.Base):

    def __init__(self):
        super().__init__("Jobs")

    def _template_path(self):
        return "web/jobs.html"

    def _generate_template_args(self):
        d = super().generate_template_args()
        return d