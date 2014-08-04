# =============================================================================
#     Author: Kan!skA
#     Date:   Aug 05, 2014
#     File:   Setup.py
#     Description: This is the cx_Freeze setup file for creating an exe program
# =============================================================================
from cx_Freeze import setup, Executable
# NOTE: you can include any other necessary external imports here as well

includefiles = []  # include any files here that you wish
includes = []
excludes = []
packages = []

exe = Executable(
    # what to build
    script="TryThis.py",  # the name of your main python script goes here
    initScript=None,
    base="Win32GUI",  # if creating a GUI instead of a console app, type "Win32GUI"
    targetName="First.exe",  # this is the name of the executable file
    copyDependentFiles=True,
    compress=True,
    appendScriptToExe=True,
    appendScriptToLibrary=True,
    icon=None  # if you want to use an icon file, specify the file name here
)

setup(
    # the actual setup & the definition of other misc. info
    name="Try This",  # program name
    version="0.1",
    description='trial',
    author="Kan!skA",
    author_email="email@kaniska.in",
    options={"build_exe": {"excludes": excludes, "packages": packages,
                           "include_files": includefiles}},
    executables=[exe], requires=['cx_Freeze', 'selenium']
)