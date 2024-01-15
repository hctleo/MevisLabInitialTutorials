from mevis import *

# global variables
listCSOs = []
idxCSO = -1

def colorizeCSO():
    if ctx.field("CSOManager.numCSOs") == 0:
        pass
    else:
        global listCSOs
        global idxCSO
        if listCSOs == []:
            listCSOs = ctx.field("CSOManager.outCSOList").object()
        
        # COLORIZATION OF CSO
        # Changing back color of previously selected CSO to default value
        if idxCSO >= 0:
            oldCSO = listCSOs.getCSOAt(idxCSO)
            oldCSO.setPathPointColor((1.0, 1.0, 0.0)) # Color change of CSO
            oldCSO.setPathPointWidth(1)               # Line width change
        
        # Changing color and width of selected CSO
        idxCSO = ctx.field("SoView2DCSOExtensibleEditor.csoIdUnderMouseCursor").value - 1 # -1 because CSOs are indexed starting at 1
        if idxCSO >= 0:
            currentCSO = listCSOs.getCSOAt(idxCSO)
            currentCSO.setPathPointColor((1.0, 0.0, 1.0))
            currentCSO.setPathPointWidth(5)

def enableFunctionalities():
    ctx.field("SoView2DCSOExtensibleEditor.updateCSOIdUnderMouseCursor").value = True

def fileDialog():
    exp = ctx.expandFilename(ctx.field("LocalImage.name").stringValue())
    filename = MLABFileDialog.getOpenFileName(exp, "", "Open file")
    if filename:
        ctx.field("LocalImage.name").value = ctx.unexpandFilename(filename)
      
#def resetCSO():
#  ctx.field("CSOManager.removeAllCSOsAndGroups"). = True

  
  