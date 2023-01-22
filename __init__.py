from .core import execfile  # noqa: F401
from .register_class import register, ui_classes, unregister  # noqa: F401

bl_info = {
    "name": "RunScript",
    "author": "tsutomu",
    "version": (0, 1),
    "blender": (3, 4, 0),
    "support": "TESTING",
    "category": "Object",
    "description": "",
    "location": "View3D > Object",
    "warning": "",
    "doc_url": "https://github.com/SaitoTsutomu/RunScript",
}
