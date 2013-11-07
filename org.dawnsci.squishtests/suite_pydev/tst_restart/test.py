source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_python_setup.py"))

def main():
    startOrAttachToDAWN()
    setupEPDPython()

    waitForObject(":Workbench Window")
    
    snooze(1.0)
    closeOrDetachFromDAWN()
    
    # Don't clean the WS this time
    startOrAttachToDAWNOnly(clean_workspace=False)

    # Make sure that EPD Free is setup    
    activateItem(waitForObjectItem(":_Menu", "Window"))
    activateItem(waitForObjectItem(":Window_Menu", "Preferences"))
    expand(waitForObjectItem(":Preferences_Tree", "PyDev"))
    expand(waitForObjectItem(":Preferences_Tree", "Interpreters"))
    mouseClick(waitForObjectItem(":Preferences_Tree", "Python Interpreter"))
    waitFor("object.exists(':Python interpreters (e.g.: python.exe).Enthought EPD Free_TreeItem')", 20000)
    test.compare(findObject(":Python interpreters (e.g.: python.exe).Enthought EPD Free_TreeItem").text, "Enthought EPD Free")
    clickButton(waitForObject(":Preferences.OK_Button"))
    snooze(1.0)
    closeWindow(":Workbench Window")
    clickButton(waitForObject(":Confirm Exit.OK_Button"))
