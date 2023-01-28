from pathlib import Path

import bpy

from .register_class import _get_cls, operator


def execfile(file, globals_=None, locals_=None):
    pth = Path(file)
    if not pth.is_file():
        return False
    if txt := bpy.data.texts.get(pth.name):
        bpy.data.texts.remove(txt)
    txt = bpy.data.texts.load(str(pth))
    if scr := bpy.data.screens.get("Scripting"):
        areas = [a for a in scr.areas if a.type == "TEXT_EDITOR"]
        if areas:
            areas[0].spaces[0].text = txt
    exec(pth.read_text(), globals_, locals_)
    return True


class CDO_OT_run_script(bpy.types.Operator):
    """2つのオブジェクトの異なる点を選択"""

    bl_idname = "object.run_script"
    bl_label = "Run Script"
    bl_description = "Execute the specified script file."

    file: bpy.props.StringProperty() = bpy.props.StringProperty()  # type: ignore
    use_global: bpy.props.BoolProperty() = bpy.props.BoolProperty()  # type: ignore

    def execute(self, context):
        globals_ = globals() if self.use_global else None
        if not execfile(self.file, globals_):
            self.report({"WARNING"}, "Set file name.")
            return {"CANCELLED"}
        return {"FINISHED"}


class CDO_PT_bit(bpy.types.Panel):
    bl_label = "RunScript"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Edit"

    def draw(self, context):
        self.layout.prop(context.scene, "file", text="File")
        self.layout.prop(context.scene, "use_global", text="UseGlobal")
        prop = operator(self.layout, CDO_OT_run_script)
        prop.file = context.scene.file
        prop.use_global = context.scene.use_global


# core.py内のOperatorクラスとPanelクラス
ui_classes = _get_cls(__name__)
