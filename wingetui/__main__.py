if __name__ == "__main__":
    # WingetUI cannot be run directly from this file, it must be run by importing the wingetui module 
    import subprocess, os, sys
    if not __file__ in sys.argv:
        sys.exit(subprocess.run(["cmd", "/C", "python", "-m", "wingetui"], shell=True, cwd=os.path.dirname(__file__).split("wingetui")[0]).returncode)
        

def CheckProgramIntegrity():
    # BEGIN AUTOGENERATED HASH DICTIONARY
    HASHES: dict[str:str] = {
        ".\\data\\contributors.py": "097a4b7afd25f8f37ffa8b233c411e7d72e7e8e4cb0084d27bb18553e73e9714",
        ".\\data\\translations.py": "2083baf6d0bda89312d3e24c0226abf9f986c26a929e7e83e54d3bd0c81f2282",
        ".\\data\\versions.py": "d0dec5bc2768381952dc1b8093b47da9421e88505442aeab6631d0851ad08cf2",
        ".\\external\\blurwindow.py": "d68947ee90f5cbdb3d91a9bea04b7478db47082c0483bd32bd38c12cd9e8e152",
        ".\\lang\\languages.py": "30effb2fd0e6576c3332fe2bf90762cb2f225583aacc4396cca6cc5e74ce9db0",
        ".\\lang\\lang_tools.py": "1bfa049c763475e5970a6e3898996b24b62c9a3513dda415897509d8386a46c8",
        ".\\PackageManagers\\choco.py": "a2eb7595a5af854988a19f9f487a4031f46023f3d845076d987ae70f21e7a0de",
        ".\\PackageManagers\\npm.py": "da4da3281132d65fa181a008beeb10d79bc0529741302ce757d3db021d36ee73",
        ".\\PackageManagers\\PackageClasses.py": "cc5d68202719f0f88271a8924c48a6f5fe80e3950effe3a20aabfd585e6b0fcb",
        ".\\PackageManagers\\pip.py": "b6676a5b32265a81429897d8d8bae536720473afc305c9c0eee108864688d603",
        ".\\PackageManagers\\sampleHelper.py": "6261824e44b9b425b1b2d6cb3156019cab17e7f0d2101034e653143aacb2d60c",
        ".\\PackageManagers\\scoop.py": "9e99528aa204af1e24042964ffa6a90534ac8873ed58152f5d83f63c327bd867",
        ".\\PackageManagers\\winget.py": "2ff447f8184b363bb31a077b98cd557b9f3f1a74989b88856c190493413b4e3a",
        ".\\apiBackend.py": "f14c96e72e2b9a672667e317853a4a3e391c30391c2cf70972203cad8168d23b",
        ".\\customWidgets.py": "1497d464b0c13b889e6b1e64cef3f90b177e245acf5082b91480380db57db8c1",
        ".\\genericCustomWidgets.py": "86e04bc2ba58fbd7a0cf878ceacdf5061079459fcf735f7f4316f4cd3c0d88dc",
        ".\\globals.py": "6d501b019b2c1d40c6a7e7d141375f5462b08848e0ba9e26f6789c2c7c6e09c7",
        ".\\mainWindow.py": "9ca58cf20341f033e33fef67cf25ce8f2ffa83fe3ca58f9c0c7949c320f81ddc",
        ".\\storeEngine.py": "a5082fd7fdf6f7a0b82371bacc0e210c9a2d903f8619c6a78190c602308eb057",
        ".\\tools.py": "5fc12c2a0f63379e2159ae1b8e85d9d44d58250665d3f2309d25285674a1076c",
        ".\\uiSections.py": "7990a03740e61de5920ba907abe232052a8c37cd0e459970ad473f2deb33e46a",
        ".\\upgradeAssistant.py": "ae4dd250376517c72bc8737cb0adfdc79cfa7b6236bea4b06117b15a2aae316d",
        ".\\welcome.py": "74c0bc9532aa28d0220cb34a0e7bce831c05361716a8af22df130d93575b62bf",
        "./components\\gsudo.exe": "1acd324cf636c53012b57467fd7a356520d4199e45acda4a0876cb52c03091a1"
    }
    # END AUTOGENERATED HASH DICTIONARY
    import glob
    import hashlib
    import os
    import sys

    root_dir = os.path.dirname(__file__)
    os.chdir(root_dir)

    for file in glob.glob("./**/**.py") + glob.glob("./**.py") + glob.glob("./components/**.exe") + glob.glob("./**/**.pyc") + glob.glob("./**.pyc"):
        if file in HASHES.keys():
            with open(file, "rb") as f:
                bytes = f.read()  # read entire file as bytes
                HASH = hashlib.sha256(bytes).hexdigest()
                if HASH != HASHES[file]:
                    if (getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')):
                        print(f"🔴 File {file} HASH does not coincide!")
                        raise ModuleNotFoundError(f"The file {file} has an invalid hash, meaning that it has been likely modified. Please reinstall WingetUI")
                    else:
                        print(f"🔵 File {file} HASH does not coincide, but running unfrozen")
        else:
            print(f"🔵 File {file} not in hashing list")

    print("🟢 Hash check passed, coninuing execution...")


try:
    import sys
    if "--debugcrash" in sys.argv:
        import faulthandler
        faulthandler.enable()

    pathIsValid = True
    specialCharacter = ""
    for char in sys.executable:
        if char not in "\\/:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSRTUVWXYZ1234567890_+()-., ":
            specialCharacter = char
            pathIsValid = False
            break

    if not pathIsValid:
        import ctypes
        ctypes.windll.user32.MessageBoxW(None, "WingetUI can't be installed in a path containing special characters. Please reinstall WingetUI on a valid location\n\n\nCurrent path: " + os.path.dirname(sys.executable) + "\nInvalid character detected: " + specialCharacter + "\n\n\nPlease run the WingetUI installer and select a different install location. A possible valid path could be C:\\Program Files\\WingetUI", "WingetUI Crash handler", 0x00000010)
        sys.exit(1)

    _globals = globals
    
    CheckProgramIntegrity()
    
    import os
    import sys

    from PySide6.QtCore import *
    from PySide6.QtGui import *
    from PySide6.QtWidgets import *
    
    import wingetui.Core.Globals as Globals
    from wingetui.Interface.Application import RunMainApplication
    from wingetui.Interface.Tools import *
    from wingetui.Interface.Tools import _
    from wingetui.PackageManagers.PackageClasses import Package 

    if "--daemon" in sys.argv:
        if getSettings("DisableAutostart"):
            sys.exit(0)

    print("---------------------------------------------------------------------------------------------------")
    print("")
    print(f"   WingetUI version {versionName} (version number {version}) log")
    print("   All modules loaded successfully and sys.stdout patched correctly, starting main script")
    print(f"   Translator function language set to \"{langName}\"")
    print("")
    print("---------------------------------------------------------------------------------------------------")
    print("")
    print(" Log legend:")
    print(" 🔵: Verbose")
    print(" 🟢: Information")
    print(" 🟡: Warning")
    print(" 🟠: Handled unexpected exception")
    print(" 🔴: Unhandled unexpected exception")
    print("")
    
    # Migrator from legacy settings
    legacy_ignored_updates = GetIgnoredPackageUpdates_Permanent()
    legacy_ignored_updates_version = GetIgnoredPackageUpdates_SpecificVersion()
    
    try:
        for pkglist in legacy_ignored_updates_version:
            if len(pkglist) == 3:
                package = Package(pkglist[0], pkglist[0], pkglist[1], pkglist[2], None)
                package.AddToIgnoredUpdates(package.Version)
        setSettings("SingleVersionIgnoredPackageUpdates", False)
        
        for pkglist in legacy_ignored_updates:
            if len(pkglist) == 2:
                package = Package(pkglist[0], pkglist[0], "", pkglist[1], None)
                package.AddToIgnoredUpdates()
        setSettings("PermanentlyIgnoredPackageUpdates", False)    
    except Exception as e:
        report(e)

    sys.exit(RunMainApplication())
    
except (ModuleNotFoundError, ImportError, FileNotFoundError):
    import traceback
    tb = traceback.format_exception(*sys.exc_info())
    tracebacc = ""
    for line in tb:
        tracebacc += line + "\n"
    import ctypes
    ctypes.windll.user32.MessageBoxW(None, "Your WingetUI installation appears to have missing or corrupt components. Please reinstall WingetUI.\n\n" + tracebacc, "WingetUI Crash handler", 0x00000010)

except Exception as e:
    import platform
    import traceback
    import webbrowser
    if "langName" not in globals() and "langName" not in locals():
        langName = "Unknown"
    try:
        from wingetui.tools import version as appversion
    except Exception:
        appversion = "Unknown"
    os_info = "" + \
        f"                        OS: {platform.system()}\n" + \
        f"                   Version: {platform.win32_ver()}\n" + \
        f"           OS Architecture: {platform.machine()}\n" + \
        f"          APP Architecture: {platform.architecture()[0]}\n" + \
        f"                  Language: {langName}\n" + \
        f"               APP Version: {appversion}\n" + \
        f"                Executable: {sys.executable}\n" + \
        "                   Program: WingetUI\n" + \
        "           Program section: Main script" + \
        "\n\n-----------------------------------------------------------------------------------------"
    traceback_info = "Traceback (most recent call last):\n"
    try:
        for line in traceback.extract_tb(e.__traceback__).format():
            traceback_info += line
        traceback_info += f"\n{type(e).__name__}: {str(e)}"
    except Exception:
        traceback_info += "\nUnable to get traceback"
    webbrowser.open(("https://www.marticliment.com/error-report/?appName=WingetUI&errorBody=" + os_info.replace('\n', '{l}').replace(' ', '{s}') + "{l}{l}{l}{l}WingetUI Log:{l}" + str("\n\n\n\n" + traceback_info).replace('\n', '{l}').replace(' ', '{s}')).replace("#", "|=|"))
    print(traceback_info)