source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "use_case_utils.py"))

# This test makes sure we can start and stop DAWN
def main():
    # Start or attach runs (or attaches) to DAWN and then 
    # makes sure the workbench window exists and finally
    # will close the Welcome screen 
    startOrAttachToDAWN()
    
    # On a test you may add test code here 
    #Open data browsing perspective
    openPerspective("Data Browsing (default)") 
    openExample("001.img")
    snooze(1) 
    doubleClick(waitForObject(":Image tools used to profile and inspect images._ToolItem"), 25, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Line Profile"))
    clickTab(waitForObject(":Line Profile_CTabItem"), 64, 11, 0, Button.Button1)
    
    proxy = waitForObject(":ref-testscale_1_001.img_CTabItem")
    widget = proxy.control
    b = widget.bounds

    mouseDrag(widget, b.x+b.width/8, b.y+b.height/8, int(b.width/3),b.height/3, 0, Button.Button1)
    snooze(2) # While fit...
    
    mouseClick(waitForObject(":Configure Settings..._ToolItem_3"), 9, 11, 0, Button.Button1)
    clickTab(waitForObject(":Configure Graph Settings.Regions_TabItem"))
    mouseClick(waitForObjectItem(":Regions.Region Location_Table", "0/1"), 37, 9, 0, Button.Button1)
    type(waitForObject(":Regions_Spinner"), "500")
    mouseClick(waitForObjectItem(":Regions.Region Location_Table", "0/2"), 49, 9, 0, Button.Button1)
    type(waitForObject(":Regions_Spinner"), "10")
    mouseClick(waitForObjectItem(":Regions.Region Location_Table", "1/1"), 27, 13, 0, Button.Button1)
    type(waitForObject(":Regions_Spinner"), "500")
    mouseClick(waitForObjectItem(":Regions.Region Location_Table", "1/2"), 31, 13, 0, Button.Button1)
    type(waitForObject(":Regions_Spinner"), "1000")
    clickButton(waitForObject(":Configure Graph Settings.Apply_Button"))
    mouseClick(waitForObjectItem(":Regions.Region Location_Table", "1/0"), 135, 16, 0, Button.Button1)
    clickButton(waitForObject(":Configure Graph Settings.OK_Button"))
    snooze(1) 
    
    system = getPlottingSystem("Line Profile")
    data   = system.getTraces().iterator().next().getData()
    size   = data.getSize()

    test.verify(size==991, "Data size check, size is "+str(size))
    # Exit (or disconnect) DAWN
    closeOrDetachFromDAWN()