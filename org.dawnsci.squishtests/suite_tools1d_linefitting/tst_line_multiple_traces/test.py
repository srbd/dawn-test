source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))

def main():
    
    #Start using clean workspace
    startOrAttachToDAWN()
    
    # Open data browsing perspective 
    openPerspective("Data Browsing (default)")
    
    #expand data tree and open metal mix
    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    children = object.children(waitForObjectItem(":Project Explorer_Tree", "examples"))
    
    for child in children:
        if "metalmix.mca" in child.text:
            doubleClick(child, 5, 5, 0, Button.Button1)
            continue
    
    mouseClick(waitForObject(":Plot data as separate plots_ToolItem"), 18, 11, 0, Button.Button1)
    
    for i in range(16):
        mouseClick(waitForObjectItem(":Data_Table", str(i) + "/0"), 9, 7, 0, Button.Button1)
    
    mouseClick(waitForObject(":XY plotting tools_ToolItem_2"), 31, 7, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Line Fitting"))
    
    c = waitForObject(":Plot_Composite_2")
    b = c.bounds

    test.log("Image at (%d, %d) is %d x %d" % (b.x,b.y, b.width, b.height))
    mouseDrag(c, b.x+b.width/3, b.y+b.height/3, int(b.width/1.7),b.height/3, 0, Button.Button1)
    snooze(1)
    
    tab = waitForObject(":Line Fitting_Table")
    
    test.verify(tab.getItemCount()==1,"one line in table")
    
    mouseClick(waitForObject(":Choose trace for fit._ToolItem"), 29, 8, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Select all"))
    
    snooze(10)
    
    test.verify(tab.getItemCount()==16,"16 line in table")
    
    for i in range(16):
        wid =  waitForObjectItem(":Line Fitting_Table",  str(i) + "/1")
        test.verify(wid.text == "Fit " + str(i+1),"line present")


    closeOrDetachFromDAWN()