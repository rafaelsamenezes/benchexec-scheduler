import scheduler.view.base as B


class ListItem:
    def __init__(self, label, badge_type, badge_content, badge_icon=''):
        self.label = label
        self.badge_type = badge_type
        self.badge_content = badge_content
        self.badge_icon = badge_icon

    def __repr__(self):
        return "<DashboardListItem (label='%s', badge_type='%s', badge_content='%s')>" % (
            self.label,
            self.badge_type,
            self.badge_content)

    @staticmethod
    def generate_check_item(item, check):
        badge_type = "badge-success" if check else "badge-danger"
        badge_content = 'Success' if check else 'Failed'
        badge_icon = 'check-circle' if check else 'alert-circle'
        return ListItem(item,
                        badge_type,
                        badge_content,
                        badge_icon)

    @staticmethod
    def generate_value_item(item, value):
        return ListItem(item, "badge-light", value)


class Dashboard(B.Base):

    def _generate_list_items(self):
        result = list()
        result.append(ListItem.generate_check_item("System Check:", self.values["system_check"]))
        result.append(ListItem.generate_check_item("Database Integrity:", self.values["database_check"]))
        result.append(ListItem.generate_value_item("Active Machines:", self.values["machines"]))

        job_per_machine = f'{self.values["active_jobs"]}/{self.values["jobs"]}'
        result.append(ListItem.generate_value_item("Active Jobs:", job_per_machine))

        result.append(ListItem.generate_value_item("Scheduling Algorithm:", self.values["algorithm"]))
        result.append(ListItem.generate_value_item("Version:", self.values["version"]))

        return result

    def __init__(self, checks):
        super().__init__("Dashboard")
        self.values = checks

    def _template_path(self):
        return "web/index.html"

    def generate_template_args(self):
        d = super().generate_template_args()
        d['system_items'] = self._generate_list_items()
        return d
