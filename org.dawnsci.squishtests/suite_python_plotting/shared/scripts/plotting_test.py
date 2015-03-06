def getFirstDataset(system):
    trcs = system.getTraces()
    
    if (trcs.size() == 0): return None
    
    tarray = trcs.toArray()
    
    return tarray.at(0).getData()

def createConsoleSpace(perspective="Python"):
    
    if perspective == "Python":
        consoleName = ":Console_CTabItem_2"
        sashName = ":_Sash_5"
        steps = 15
    elif perspective == "Data Browsing (default)":
        consoleName = ":Console_CTabItem"
        sashName = ":_Sash_3"
        steps = 40
    
    clickTab(waitForObject(consoleName), 49, 4, 0, Button.Button3)
    activateItem(waitForObjectItem(":Pop Up Menu", "Size"))
    activateItem(waitForObjectItem(":Size_Menu", "Top"))
    
    #For compactness, put dragging sash into loop
    a = 0
    while a < steps:
        type(waitForObject(sashName), "<Up>")
        a += 1
    clickTab(waitForObject(consoleName), 27, 12, 0, Button.Button1)

def plotting_script_test(system):
    
    type(waitForObject(":Console_ScriptConsoleViewer$ScriptConsoleStyledText"), "dnp.plot.image(dnp.random.rand(100,200))")
    type(waitForObject(":Console_ScriptConsoleViewer$ScriptConsoleStyledText"), "<Return>")
    snooze(1)
    
    trcs = system.getTraces()
    test.verify(trcs.size() == 1, "test image")
    
    data = getFirstDataset(system)
    
    if (data != None):
        test.verify(data.getShape().at(0) == 100, "test shape")
        test.verify(data.getShape().at(1) == 200, "test shape")
    else:
        test.fail("data is none")
    
    
    type(waitForObject(":Console_ScriptConsoleViewer$ScriptConsoleStyledText"), "dnp.plot.clear()")
    type(waitForObject(":Console_ScriptConsoleViewer$ScriptConsoleStyledText"), "<Return>")
    snooze(1)
    
    trcs = system.getTraces()
    test.verify(trcs.size() == 0, "test clear")
    
    type(waitForObject(":Console_ScriptConsoleViewer$ScriptConsoleStyledText"), "dnp.plot.line(dnp.arange(100),dnp.random.rand(100))")
    type(waitForObject(":Console_ScriptConsoleViewer$ScriptConsoleStyledText"), "<Return>")
    snooze(1)
    trcs = system.getTraces()
    test.verify(trcs.size() == 1, "test trace")
    data = getFirstDataset(system)
    if (data != None):
        test.verify(data.getShape().at(0) == 100, "test shape")
    else:
        test.fail("data is none")
    
    
    type(waitForObject(":Console_ScriptConsoleViewer$ScriptConsoleStyledText"), "dnp.plot.clear()")
    type(waitForObject(":Console_ScriptConsoleViewer$ScriptConsoleStyledText"), "<Return>")
    snooze(1)
    
    type(waitForObject(":Console_ScriptConsoleViewer$ScriptConsoleStyledText"), "dnp.plot.line(dnp.arange(100),(dnp.random.rand(100),dnp.random.rand(100)))")
    type(waitForObject(":Console_ScriptConsoleViewer$ScriptConsoleStyledText"), "<Return>")
    snooze(1)
    trcs = system.getTraces()
    test.verify(trcs.size() == 2, "test traces")
    data = getFirstDataset(system)
    if (data != None):
        test.verify(data.getShape().at(0) == 100, "test shape")
    else:
        test.fail("data is none")
    
    
    type(waitForObject(":Console_ScriptConsoleViewer$ScriptConsoleStyledText"), "dnp.plot.clear()")
    type(waitForObject(":Console_ScriptConsoleViewer$ScriptConsoleStyledText"), "<Return>")
    snooze(1)
    
    trcs = system.getTraces()
    test.verify(trcs.size() == 0, "test clear")
    
    openExternalFile("test_plot.py")
    
    snooze(1)
    
    clickTab(waitForObject(":test_plot_CTabItem"), 54, 11, 0, Button.Button1)
    snooze(1)
    mouseClick(waitForObject(":Activates the interactive console. (Ctrl+Alt+Enter)_ToolItem"), 18, 16, 0, Button.Button1)
    snooze(1)
    
    regs = system.getRegions()
    test.verify(regs.size() == 2, "test plotted")
    
    trcs = system.getTraces()
    test.verify(trcs.size() == 1, "test plotted")
