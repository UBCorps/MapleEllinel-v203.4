# Frozen Fairy Forest : Royal Chamber (910150004)  |  Used for the Mercedes In Ice Scene

def init():
    sm.lockInGameUI(True)
    sm.showScene("Effect.wz/Direction5", "mersedesTutorial", "Scene0") # Shows the Mercedes in Ice  scene
    sm.invokeAfterDelay(14000, "showFadeTransition", 0, 500, 500)