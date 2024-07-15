import flomo.helpers as helpers


class Config:
    def __init__(self):
        self.path = helpers.get_path("config.json", in_data=True)

    def create_config(self):
        pass
