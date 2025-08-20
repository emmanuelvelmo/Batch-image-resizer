from cx_Freeze import setup, Executable

setup(name="Batch image resizer", executables=[Executable("Batch image resizer script.py")], options={"build_exe": {"excludes": ["tkinter"]}})
