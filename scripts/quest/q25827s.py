# 25825 - [Job Advancement] Agent of Justige (AB 2nd job adv)
from net.swordie.ms.loaders import ItemData

status = -1
ESKALADE_NPC_ID = 3000132

def init():
    sm.setSpeakerID(ESKALADE_NPC_ID)
    if chr.getLevel() >= 100 and chr.getJob() == 6511:
        sm.sendNext("You've been working up quite a sweat, #h #.")
    else:
        sm.dispose()

def action(response, answer):
    sm.setSpeakerID(ESKALADE_NPC_ID)
    global status
    status += 1
    if status % 2 == 0:
        sm.setPlayerAsSpeaker()
    if status == 0:
        sm.sendNext("I want to be the hero of the people! I gotta work my butt off! Angelic Savior!")
    elif status == 1:
        sm.sendNext("I like it when you talk like that. I have a little proposition for you...")
    elif status == 2:
        sm.sendNext("I hate it when you use big words like that. You sound so serious.")
    elif status == 3:
        sm.sendNext("I'm always serious.")
    elif status == 4:
        sm.sendNext("That's... kinda scary.")
    elif status == 5:
        sm.sendNext("...We need a new contract.")
    elif status == 6:
        sm.sendNext("Aww, another one?!")
    elif status == 7:
        sm.sendNext("Our first contract was guided by fate! This one has to come from the heart! It's all about consensual bonding.")
    elif status == 8:
        sm.sendNext("That sounds weird. Is it gonna make everything more pink again?")
    elif status == 9:
        sm.sendAskYesNo("Probably, but you can deal! Now focus on my exceedingly attractive voice, okay? Just really "
                        "listen to the timbre.")
    elif status == 10:
        if response == 1:
            sm.sendSayOkay("I'm tougher than all the rest!")
        else:
            sm.dispose()
    else:
        sm.setJob(6512)
        sm.addSP(5)
        sm.addAP(5)
        equippedInv = chr.getEquippedInventory()
        oldSecondary = equippedInv.getItemBySlot(10)
        chr.consumeItem(oldSecondary)
        secondary = ItemData.getItemDeepCopy(1352604)
        secondary.setBagIndex(10)
        chr.getAvatarData().getAvatarLook().getHairEquips().add(secondary.getItemId())
        chr.setSpToCurrentJob(5)
        chr.getEquippedInventory().addItem(secondary)
        secondary.updateToChar(chr)
        sm.dispose()