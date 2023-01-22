import bpy

from .register_class import _get_cls, operator


class CDO_OT_run_script(bpy.types.Operator):
    """2つのオブジェクトの異なる点を選択"""

    bl_idname = "object.run_script"
    bl_label = "Run Script"
    bl_description = "Execute the specified script file."

    file: bpy.props.StringProperty() = bpy.props.StringProperty()  # type: ignore

    def execute(self, context):
        return {"FINISHED"}


class CDO_PT_bit(bpy.types.Panel):
    bl_label = "RunScript"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Edit"

    def draw(self, context):
        self.layout.prop(context.scene, "file", text="File")
        prop = operator(self.layout, CDO_OT_run_script)
        prop.file = context.scene.file


# core.py内のOperatorクラスとPanelクラス
ui_classes = _get_cls(__name__)
