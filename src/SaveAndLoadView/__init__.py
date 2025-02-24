from ovito.gui import UtilityInterface
from ovito.traits import action_handler
from traits.api import Button
from ovito import scene
from ovito.vis import Viewport


class SaveAndLoadView(UtilityInterface):

    reset_view = Button(ovito_label="Reset view")
    save_view = Button(ovito_label="Save view")
    load_view = Button(ovito_label="Load View")
    cache = {}

    @action_handler("reset_view")
    def reset_view_button(self):
        scene.viewports.active_vp.type = Viewport.Type.Perspective
        scene.viewports.active_vp.fov = 0.610865238198
        scene.viewports.active_vp.camera_dir = (
            -0.49923017660270624,
            0.665640235470275,
            -0.5547001962252291,
        )
        scene.viewports.active_vp.camera_pos = (
            14.000942985459858,
            -18.667923980613143,
            15.55660331717762,
        )
        scene.viewports.active_vp.zoom_all()

    @action_handler("save_view")
    def save_view_button(self):
        self.cache.clear()
        self.cache["type"] = scene.viewports.active_vp.type.value
        self.cache["fov"] = scene.viewports.active_vp.fov
        self.cache["camera_dir"] = scene.viewports.active_vp.camera_dir
        self.cache["camera_pos"] = scene.viewports.active_vp.camera_pos

    @action_handler("load_view")
    def load_view_button(self):
        if not self.cache:
            raise RuntimeError(
                "There is currently no view stored. Please store a view using the 'Save view' button."
            )
        scene.viewports.active_vp.type = Viewport.Type(self.cache["type"])
        scene.viewports.active_vp.fov = self.cache["fov"]
        scene.viewports.active_vp.camera_dir = self.cache["camera_dir"]
        scene.viewports.active_vp.camera_pos = self.cache["camera_pos"]
