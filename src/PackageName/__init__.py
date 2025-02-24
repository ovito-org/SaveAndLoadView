from ovito.gui import UtilityInterface
from ovito.traits import action_handler
from traits.api import Button


class MyUtilityApplet(UtilityInterface):
    btn = Button(ovito_label="Run action")

    @action_handler("btn")
    def run(self):
        print("Hello world!")
