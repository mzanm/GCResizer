import shutil
import os
import PyInstaller.__main__ as pm


def cleanup(dist):
    shutil.rmtree("build", True)
    if dist:
        shutil.rmtree("dist", True)
    try:
        os.remove("GCResizer.spec")
    except FileNotFoundError:
        pass
    shutil.rmtree("__pycache__", True)


cleanup(True)

pm.run(
    [
        "--windowed",
        "--clean",
        "GCResizer.py",
        "--exclude-module=_ssl",
        "--exclude-module=_socket",
        "--exclude-module=socket",
        "--exclude-module=wx.html",
        "--exclude-module=wx.html2",
        "--exclude-module=pyreadline",
        "--exclude-module=difflib",
        "--exclude-module=tcl",
        "--exclude-module=optparse",
        "--exclude-module=pickle",
        "--exclude-module=pdb",
        "--exclude-module=unittest",
        "--exclude-module=test",
        "--exclude-module=doctest",
        "--exclude-module=tkinter",
        "--name=GCResizer",
    ]
)

shutil.copyfile("LICENSE", "dist\\LICENSE")
