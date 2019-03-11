# Created by MechAviv
# Map ID :: 402090000
# Sandstorm Zone : Sandstorm Desert

sm.curNodeEventEnd(True)
sm.setTemporarySkillSet(0)
sm.setInGameDirectionMode(True, False, False, False)
sm.removeAdditionalEffect()
sm.blind(1, 255, 0, 0, 0, 0, 0)
sm.levelUntil(10)
sm.giveSkill(150010079, 1, 1)
sm.giveItem(2001502, 350)
sm.giveItem(2001506, 350)
sm.setMapTaggedObjectVisible("core0", False, 0, 0)
sm.setMapTaggedObjectVisible("core1", False, 0, 0)
sm.setMapTaggedObjectAnimation("sand", 0)
sm.forcedFlip(True)
sm.spawnNpc(3001508, -2680, 263)
sm.showNpcSpecialActionByTemplateId(3001508, "summon", 0)
sm.spawnNpc(3001509, -2750, 263)
sm.showNpcSpecialActionByTemplateId(3001509, "summon", 0)
sm.spawnNpc(3001510, -2400, 263)
sm.showNpcSpecialActionByTemplateId(3001510, "summon", 0)
sm.sendDelay(1000)


sm.changeBGM("Bgm48.img/Doomsday_FULL", 0, 0)
sm.OnOffLayer_On(500, "2", 0, -10, 0, "Effect/Direction17.img/effect/ark/noise/1366/2", 4, 1, -1, 1)
sm.OnOffLayer_On(500, "3", 0, -10, 0, "Effect/Direction17.img/effect/ark/noise/1366/3", 4, 1, -1, 1)
sm.sendDelay(2500)


sm.OnOffLayer_On(1500, "d0", 0, -80, 1, "Effect/Direction17.img/effect/ark/illust/6/0", 4, 1, -1, 0)
sm.sendDelay(2000)


sm.sendDelay(7850)
sm.playExclSoundWithDownBGM("Voice4.img/GLAdd/Mono/AA/1")
sm.createFieldTextEffect("#fn???????? ExtraBold##fs35#For too long, we endured war for the sake of war.", 50, 7350, 7, 0, -50, 0, 4, 300, 3, 300)


sm.sendDelay(8150)
sm.playExclSoundWithDownBGM("Voice4.img/GLAdd/Mono/AA/2")
sm.createFieldTextEffect("#fn???????? ExtraBold##fs35#We championed selfish causes for misguided leaders.", 50, 7650, 7, 0, -50, 0, 4, 300, 3, 300)


sm.sendDelay(6200)
sm.playExclSoundWithDownBGM("Voice4.img/GLAdd/Mono/AA/3")
sm.createFieldTextEffect("#fn???????? ExtraBold##fs35#We wasted countless lives for nothing.", 50, 5700, 7, 0, -50, 0, 4, 300, 3, 300)


sm.sendDelay(9500)
sm.playExclSoundWithDownBGM("Voice4.img/GLAdd/Mono/AA/4")
sm.createFieldTextEffect("#fn???????? ExtraBold##fs35#But now, we must rise together as one for a greater purpose.", 50, 9000, 7, 0, -50, 0, 4, 300, 3, 300)


sm.sendDelay(7100)
sm.playExclSoundWithDownBGM("Voice4.img/GLAdd/Mono/AA/5")
sm.createFieldTextEffect("#fn???????? ExtraBold##fs35#By fighting together, we can end this chaos.", 50, 6600, 7, 0, -50, 0, 4, 300, 3, 300)


sm.sendDelay(2500)


sm.playExclSoundWithDownBGM("Voice4.img/GLAdd/Mono/AA/6")
sm.createFieldTextEffect("#fn???????? ExtraBold##fs35#Join me!", 50, 2000, 7, 0, -50, 0, 4, 300, 3, 300)
sm.sendDelay(7250)
sm.playExclSoundWithDownBGM("Voice4.img/GLAdd/Mono/AA/7")
sm.createFieldTextEffect("#fn???????? ExtraBold##fs35#Dedicate your lives to the glory of our race.", 50, 6750, 7, 0, -50, 0, 4, 300, 3, 300)


sm.sendDelay(10550)
sm.playExclSoundWithDownBGM("Voice4.img/GLAdd/Mono/AA/8")
sm.createFieldTextEffect("#fn???????? ExtraBold##fs35#It is time for the noble High Flora to lead Grandis into a new age!", 50, 10050, 7, 0, -50, 0, 4, 300, 3, 300)


sm.OnOffLayer_Off(300, "d0", 0)
sm.OnOffLayer_Off(300, "2", 0)
sm.OnOffLayer_Off(300, "3", 0)
sm.sendDelay(1500)


sm.sendDelay(2300)


sm.spineScreen(False, True, True, 0, "Effect/Direction17.img/effect/ark/fire/0/front_particle", "animation", "00")
sm.spineScreen(False, True, True, 0, "Effect/Direction17.img/effect/ark/fire/1/fire_particle_01", "animation", "01")
sm.spineScreen(False, True, True, 0, "Effect/Direction17.img/effect/ark/fire/2/fire_particle_02", "animation", "02")
sm.sendDelay(2000)


sm.sayMonologue("#fs22##fnArial#I thought I was fighting for something greater than myself, for peace.", False)
sm.playExclSoundWithDownBGM("Voice4.img/Ark/Mono/A/Male/1")


sm.sayMonologue("#fs22##fnArial#\r\nBut I soon discovered it was just more greed and hate.", False)
sm.playExclSoundWithDownBGM("Voice4.img/Ark/Mono/A/Male/2")


sm.sayMonologue("#fs22##fnArial#No longer would I blindly obey the whims of a corrupt leader.", False)


sm.playExclSoundWithDownBGM("Voice4.img/Ark/Mono/A/Male/3")
sm.sayMonologue("#fs22##fnArial#\r\nInstead, I would fight alongside the weak and defend them.", False)
sm.playExclSoundWithDownBGM("Voice4.img/Ark/Mono/A/Male/4")


sm.sayMonologue("#fs22#\r\n\r\n\r\n#fnArial#I thought if enough of us stood together, we could make a difference.", True)
sm.playExclSoundWithDownBGM("Voice4.img/Ark/Mono/A/Male/5")


sm.sayMonologue("#fs22##fnArial#It may have been treason, but I knew it was the right choice.", False)
sm.playExclSoundWithDownBGM("Voice4.img/Ark/Mono/A/Male/6")


sm.sayMonologue("#fs22##fnArial#If I could help stop the madness, it would be worth it.", False)


sm.playExclSoundWithDownBGM("Voice4.img/Ark/Mono/A/Male/7")
sm.sayMonologue("#fs22##fnArial#\r\n\r\nIf there were ever a time to put my life on the line for a cause, it was then.", False)
sm.playExclSoundWithDownBGM("Voice4.img/Ark/Mono/A/Male/8")


sm.sayMonologue("#fs22##fnArial#If I fell in battle fighting for something I truly believed in...", False)
sm.playExclSoundWithDownBGM("Voice4.img/Ark/Mono/A/Male/9")


sm.sayMonologue("#fs22##fnArial#Even if no one knew my name or what I did for them...", False)


sm.playExclSoundWithDownBGM("Voice4.img/Ark/Mono/A/Male/10")
sm.sayMonologue("#fs22##fnArial#\r\nI would be satisfied. After all, it was never about the glory.", True)
sm.playExclSoundWithDownBGM("Voice4.img/Ark/Mono/A/Male/11")


sm.sendDelay(1000)


sm.sendDelay(5300)
sm.playExclSoundWithDownBGM("Voice4.img/Ark/Mono/A/Male/12")
sm.createFieldTextEffect("#fn???????? ExtraBold##fs45#But fate had other plans for me.", 50, 4800, 4, 0, 0, 0, 4, 300, 3, 300)


sm.sendDelay(1000)


sm.offSpineScreenImmediate("00")
sm.offSpineScreenImmediate("01")
sm.offSpineScreenImmediate("02")
sm.playSound("Sound/SoundEff.img/radionoise", 100)
sm.OnOffLayer_On(500, "0", 0, -10, 0, "Effect/Direction17.img/effect/ark/noise/1366/0", 4, 1, -1, 1)
sm.blind(1, 255, 0, 0, 0, 500, 0)
sm.sendDelay(500)


sm.sendDelay(300)


sm.OnOffLayer_On(500, "2", 0, -10, 0, "Effect/Direction17.img/effect/ark/noise/1366/2", 4, 1, -1, 1)
sm.OnOffLayer_On(500, "3", 0, -10, 0, "Effect/Direction17.img/effect/ark/noise/1366/3", 4, 1, -1, 1)
sm.OnOffLayer_Off(300, "0", 0)
sm.sendDelay(2500)


sm.OnOffLayer_On(1500, "d1", 0, -80, -1, "Effect/Direction17.img/effect/ark/illust/0/0", 4, 1, -1, 0)
sm.sendDelay(1000)


sm.sendDelay(6500)
sm.playExclSoundWithDownBGM("Voice4.img/Ark/Back/A/Male/1")
sm.createFieldTextEffect("#fn???????? ExtraBold##fs35#I did all I could, but it wasn't enough.", 50, 6000, 7, 0, -50, 0, 4, 300, 3, 300)


sm.sendDelay(6800)
sm.playExclSoundWithDownBGM("Voice4.img/Ark/Back/A/Male/2")
sm.createFieldTextEffect("#fn???????? ExtraBold##fs35#Maybe it was always meant to end this way.", 50, 6300, 7, 0, -50, 0, 4, 300, 3, 300)


sm.sendDelay(4400)


sm.playExclSoundWithDownBGM("Voice4.img/Ark/Back/A/Male/3")
sm.createFieldTextEffect("#fn???????? ExtraBold##fs35#Or maybe it was just me...", 50, 3900, 7, 0, -50, 0, 4, 300, 3, 300)
sm.sendDelay(3500)
sm.playExclSoundWithDownBGM("Voice4.img/Ark/Back/A/Male/4")
sm.createFieldTextEffect("#fn???????? ExtraBold##fs35#Is this how it ends?", 50, 3000, 7, 0, -50, 0, 4, 300, 3, 300)


sm.sendDelay(1000)


sm.OnOffLayer_Off(300, "d1", 0)
sm.sendDelay(1000)


sm.sendDelay(2500)
sm.playExclSoundWithDownBGM("Voice4.img/ArkNpc/Back/A/7")
sm.createFieldTextEffect("#fn???????? ExtraBold##fs65#Ark!", 50, 2000, 4, 0, 0, 0, 4, 300, 3, 300)


sm.spineScreen(True, False, True, 0, "Map/Effect2.img/HofM/ACT1_bye/whiteback2/skeleton", "animation", None)
sm.sendDelay(2000)


sm.OnOffLayer_On(300, "d2", 0, -80, -1, "Effect/Direction17.img/effect/ark/illust/0/1", 4, 1, -1, 0)
sm.sendDelay(3000)


sm.playSound("Sound/Voice4.img/Ark/Now/A/Male/3", 100)
sm.sendDelay(2000)


sm.OnOffLayer_Off(300, "d2", 0)
sm.OnOffLayer_Off(300, "2", 0)
sm.OnOffLayer_Off(300, "3", 0)
sm.playSound("Sound/SoundEff.img/radionoise", 100)
sm.OnOffLayer_On(500, "0", 0, -10, 0, "Effect/Direction17.img/effect/ark/noise/1366/0", 4, 1, -1, 1)
sm.blind(1, 255, 240, 240, 240, 1300, 0)
sm.sendDelay(1600)


sm.setBGMVolume(0, 2000)
sm.sendDelay(2300)


sm.changeBGM("Bgm00.img/Silence", 0, 0)
sm.setBGMVolume(-1, 1000)
sm.OnOffLayer_Off(300, "0", 0)
sm.sendDelay(1000)


sm.zoomCamera(0, 1000, 0, 2, 180)


sm.localEmotion(1, 999999, False)
sm.forcedAction(25, 999999)
sm.showEffect("Effect/Direction17.img/effect/ark/sand/back", 9999999, 0, 0, -120, -2, False, 0)
sm.showEffect("Effect/Direction17.img/effect/ark/sand/front_0", 9999999, 0, 0, 1, -2, False, 0)
sm.showEffect("Effect/Direction17.img/effect/ark/sand/wind", 10000, 0, 0, 2, -2, False, 0)
sm.blind(1, 255, 240, 240, 240, 0, 0)
sm.sendDelay(1200)


sm.blind(0, 0, 0, 0, 0, 1000, 0)
sm.sendDelay(1400)


sm.zoomCamera(0, 1000, 0, 2, 180)


sm.sendDelay(500)


sm.setSpeakerID(3001500)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialogue()
sm.setBoxChat()
sm.boxChatPlayerAsSpeaker()
sm.setBoxOverrideSpeaker()
sm.flipBoxChat()
sm.flipBoxChatPlayerAsSpeaker()
sm.setColor(1)
sm.sendNext("#face1#What happened?")
sm.playExclSoundWithDownBGM("Voice4.img/Ark/Back/A/Male/9")


sm.sendDelay(6000)


sm.playSound("Sound/SoundEff.img/ark/wind", 100)
sm.showEffect("Effect/Direction17.img/effect/ark/sand/wind", 0, 0, 0, 2, -2, False, 0)
sm.sendDelay(500)


sm.showEffect("Effect/Direction17.img/effect/ark/sand/front_1", 0, 0, 0, 1, -2, False, 0)
sm.showEffect("Effect/Direction17.img/effect/ark/sand/wind", 0, 0, 0, 2, -2, False, 0)
sm.sendDelay(1000)


sm.showEffect("Effect/Direction17.img/effect/ark/sand/front_2", 9999, 0, 0, 1, -2, False, 0)
sm.showEffect("Effect/Direction17.img/effect/ark/sand/wind", 0, 0, 0, 2, -2, False, 0)
sm.sendDelay(500)


sm.zoomCamera(3000, 1500, 3000, 250, -50)


sm.sendDelay(4000)


sm.showFadeTransition(0, 300, 300)
sm.sendDelay(300)


sm.removeOverlapScreen(300)
sm.zoomCamera(0, 1500, 0, -2350, -50)


sm.teleportInField(-1200, 200)
sm.setMapTaggedObjectAnimation("sand", 512)
sm.moveNpcByTemplateId(3001508, False, 1200, 80)
sm.moveNpcByTemplateId(3001509, False, 1050, 80)
sm.moveNpcByTemplateId(3001510, False, 1200, 80)
sm.sendDelay(1000)


sm.playSound("Sound/SoundEff.img/cadena/energy_running2", 150)
sm.zoomCamera(3000, 1000, 3000, -2300, 180)


sm.playSound("Sound/SoundEff.img/ark/flare_ready", 100)
sm.sendDelay(3000)


sm.zoomCamera(17000, 1000, 17000, -1050, 180)


sm.playSound("Sound/SoundEff.img/ark/flare_ready", 100)
sm.sendDelay(2000)


sm.playSound("Sound/SoundEff.img/cadena/energy_running2", 150)
sm.setSpeakerID(3001509)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialogue()
sm.setBoxChat()
sm.boxChatPlayerAsSpeaker()
sm.setBoxOverrideSpeaker()
sm.flipBoxChat()
sm.flipBoxChatPlayerAsSpeaker()
sm.setColor(1)
sm.sendNext("#face3#Searching today! Searching forever!\r\nAlways searching! Always together!")


sm.setSpeakerID(3001509)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialogue()
sm.setBoxChat()
sm.boxChatPlayerAsSpeaker()
sm.setBoxOverrideSpeaker()
sm.flipBoxChat()
sm.flipBoxChatPlayerAsSpeaker()
sm.setColor(1)
sm.sendSay("#face4#Keep on searching!")


sm.playSound("Sound/SoundEff.img/ark/flare_ready", 100)
sm.setSpeakerID(3001509)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialogue()
sm.setBoxChat()
sm.boxChatPlayerAsSpeaker()
sm.setBoxOverrideSpeaker()
sm.flipBoxChat()
sm.flipBoxChatPlayerAsSpeaker()
sm.setColor(1)
sm.sendSay("#face3#North! South! East! West! Always searching for the best!\r\nUp! Down! Left! Right! Search all day! Search all night!")


sm.setSpeakerID(3001509)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialogue()
sm.setBoxChat()
sm.boxChatPlayerAsSpeaker()
sm.setBoxOverrideSpeaker()
sm.flipBoxChat()
sm.flipBoxChatPlayerAsSpeaker()
sm.setColor(1)
sm.sendSay("#face4#Keep on searching!")


sm.playSound("Sound/SoundEff.img/ark/flare_ready", 100)
sm.setSpeakerID(3001509)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialogue()
sm.setBoxChat()
sm.boxChatPlayerAsSpeaker()
sm.setBoxOverrideSpeaker()
sm.flipBoxChat()
sm.flipBoxChatPlayerAsSpeaker()
sm.setColor(1)
sm.sendSay("#face3#No, no, nowhere at all!\r\nFate has brought us to a crawl!")


sm.setSpeakerID(3001509)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialogue()
sm.setBoxChat()
sm.boxChatPlayerAsSpeaker()
sm.setBoxOverrideSpeaker()
sm.flipBoxChat()
sm.flipBoxChatPlayerAsSpeaker()
sm.setColor(1)
sm.sendSay("#face4#Searching today! Searching forever!\r\nI'll search the skies for this endeavor!")


sm.playSound("Sound/SoundEff.img/cadena/energy_running2", 150)
sm.setSpeakerID(3001509)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialogue()
sm.setBoxChat()
sm.boxChatPlayerAsSpeaker()
sm.setBoxOverrideSpeaker()
sm.flipBoxChat()
sm.flipBoxChatPlayerAsSpeaker()
sm.setColor(1)
sm.sendSay("#face0#Ack! Cough!")


sm.playSound("Sound/SoundEff.img/ark/flare_ready", 100)
sm.sendDelay(500)


sm.playSound("Sound/SoundEff.img/ark/flare_ready", 100)
sm.setSpeakerID(3001510)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialogue()
sm.setBoxChat()
sm.boxChatPlayerAsSpeaker()
sm.setBoxOverrideSpeaker()
sm.flipBoxChat()
sm.flipBoxChatPlayerAsSpeaker()
sm.setColor(1)
sm.sendNext("#face0#Oh! Are you finally done? I couldn't hear myself think over all that racket! Now I can focus on getting a good signal.")


sm.moveNpcByTemplateId(3001509, False, 50, 90)
sm.zoomCamera(1000, 1000, 1000, -1200, 180)


sm.setSpeakerID(3001509)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialogue()
sm.setBoxChat()
sm.boxChatPlayerAsSpeaker()
sm.setBoxOverrideSpeaker()
sm.flipBoxChat()
sm.flipBoxChatPlayerAsSpeaker()
sm.setColor(1)
sm.sendNext("#face1#Cough! Cough! Racket?\r\nHow could you NOT like my work song?")


sm.setSpeakerID(3001510)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialogue()
sm.setBoxChat()
sm.boxChatPlayerAsSpeaker()
sm.setBoxOverrideSpeaker()
sm.flipBoxChat()
sm.flipBoxChatPlayerAsSpeaker()
sm.setColor(1)
sm.sendSay("#face0#If it interferes with my work, then it's not a work song. It's just noise.")


sm.zoomCamera(1000, 2000, 1000, -1500, 320)


sm.setSpeakerID(3001509)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialogue()
sm.setBoxChat()
sm.boxChatPlayerAsSpeaker()
sm.setBoxOverrideSpeaker()
sm.flipBoxChat()
sm.flipBoxChatPlayerAsSpeaker()
sm.setColor(1)
sm.sendNext("#face1#How dare you! I don't have to take that! Prepare to be further annoyed!!")


sm.zoomCamera(1000, 2000, 1000, -1350, 320)


sm.moveNpcByTemplateId(3001510, True, 1, 80)
sm.sendDelay(1000)


sm.setSpeakerID(3001510)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialogue()
sm.setBoxChat()
sm.boxChatPlayerAsSpeaker()
sm.setBoxOverrideSpeaker()
sm.flipBoxChat()
sm.flipBoxChatPlayerAsSpeaker()
sm.setColor(1)
sm.sendNext("#face0#You sing like a box of mice at feeding time!")


sm.setSpeakerID(3001509)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialogue()
sm.setBoxChat()
sm.boxChatPlayerAsSpeaker()
sm.setBoxOverrideSpeaker()
sm.flipBoxChat()
sm.flipBoxChatPlayerAsSpeaker()
sm.setColor(1)
sm.sendSay("#face1#And you spend way too much time working and being a grump!")


sm.setSpeakerID(3001508)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialogue()
sm.setBoxChat()
sm.boxChatPlayerAsSpeaker()
sm.setBoxOverrideSpeaker()
sm.flipBoxChat()
sm.flipBoxChatPlayerAsSpeaker()
sm.setColor(1)
sm.sendSay("#face2#Stop it, you two!\r\nFriends don't fight!")


sm.setSpeakerID(3001508)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialogue()
sm.setBoxChat()
sm.boxChatPlayerAsSpeaker()
sm.setBoxOverrideSpeaker()
sm.flipBoxChat()
sm.flipBoxChatPlayerAsSpeaker()
sm.setColor(1)
sm.sendSay("#face3#Shake hands and apologize, or I'll- I'll make you hug each other!")


sm.sendDelay(300)


sm.flipNpcByTemplateId(3001508, False)
sm.sendDelay(500)


sm.flipNpcByTemplateId(3001508, True)
sm.sendDelay(500)


sm.flipNpcByTemplateId(3001508, False)
sm.sendDelay(500)


sm.flipNpcByTemplateId(3001508, True)
sm.sendDelay(500)


sm.flipNpcByTemplateId(3001508, False)
sm.setSpeakerID(3001510)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialogue()
sm.setBoxChat()
sm.boxChatPlayerAsSpeaker()
sm.setBoxOverrideSpeaker()
sm.flipBoxChat()
sm.flipBoxChatPlayerAsSpeaker()
sm.setColor(1)
sm.sendNext("#face3#Who cares if I'm a grump?! I do something useful!")


sm.setSpeakerID(3001509)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialogue()
sm.setBoxChat()
sm.boxChatPlayerAsSpeaker()
sm.setBoxOverrideSpeaker()
sm.flipBoxChat()
sm.flipBoxChatPlayerAsSpeaker()
sm.setColor(1)
sm.sendSay("#face1#Singing is useful too! ")


sm.setSpeakerID(3001508)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialogue()
sm.setBoxChat()
sm.boxChatPlayerAsSpeaker()
sm.setBoxOverrideSpeaker()
sm.flipBoxChat()
sm.flipBoxChatPlayerAsSpeaker()
sm.setColor(1)
sm.sendSay("#face3#Not again...")


sm.setSpeakerID(3001508)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialogue()
sm.setBoxChat()
sm.boxChatPlayerAsSpeaker()
sm.setBoxOverrideSpeaker()
sm.flipBoxChat()
sm.flipBoxChatPlayerAsSpeaker()
sm.setColor(1)
sm.sendSay("#face2#Please, you two. Just... get along for one day?!\r\nWe haven't gotten anything done!")


sm.setSpeakerID(3001510)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialogue()
sm.setBoxChat()
sm.boxChatPlayerAsSpeaker()
sm.setBoxOverrideSpeaker()
sm.flipBoxChat()
sm.flipBoxChatPlayerAsSpeaker()
sm.setColor(1)
sm.sendSay("#face0#Grrr...")


sm.setSpeakerID(3001509)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialogue()
sm.setBoxChat()
sm.boxChatPlayerAsSpeaker()
sm.setBoxOverrideSpeaker()
sm.flipBoxChat()
sm.flipBoxChatPlayerAsSpeaker()
sm.setColor(1)
sm.sendSay("#face0#...")


sm.setSpeakerID(3001510)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialogue()
sm.setBoxChat()
sm.boxChatPlayerAsSpeaker()
sm.setBoxOverrideSpeaker()
sm.flipBoxChat()
sm.flipBoxChatPlayerAsSpeaker()
sm.setColor(1)
sm.sendSay("#face0#Fine. I'm sorry.")


sm.setSpeakerID(3001509)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialogue()
sm.setBoxChat()
sm.boxChatPlayerAsSpeaker()
sm.setBoxOverrideSpeaker()
sm.flipBoxChat()
sm.flipBoxChatPlayerAsSpeaker()
sm.setColor(1)
sm.sendSay("#face3#I'm sorry too. You just don't understand my music.")


sm.setSpeakerID(3001508)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialogue()
sm.setBoxChat()
sm.boxChatPlayerAsSpeaker()
sm.setBoxOverrideSpeaker()
sm.flipBoxChat()
sm.flipBoxChatPlayerAsSpeaker()
sm.setColor(1)
sm.sendSay("#face3#It's no one's fault. Today just started out on the wrong foot.")


sm.moveNpcByTemplateId(3001508, False, 60, 120)
sm.sendDelay(1000)


sm.moveNpcByTemplateId(3001508, True, 30, 120)
sm.sendDelay(1000)


sm.flipNpcByTemplateId(3001508, False)
sm.sendDelay(500)


sm.flipNpcByTemplateId(3001508, True)
sm.sendDelay(500)


sm.flipNpcByTemplateId(3001508, False)
sm.sendDelay(500)


sm.flipNpcByTemplateId(3001508, True)
sm.sendDelay(500)


sm.flipNpcByTemplateId(3001508, False)
sm.sendDelay(500)


sm.showEffect("Effect/Direction17.img/effect/ark/sand/wind", 999999, 0, 0, 2, -2, False, 0)
sm.setMapTaggedObjectAnimation("sand", 0)
sm.sendDelay(300)


sm.moveNpcByTemplateId(3001508, True, 10, 100)
sm.setSpeakerID(3001508)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialogue()
sm.setBoxChat()
sm.boxChatPlayerAsSpeaker()
sm.setBoxOverrideSpeaker()
sm.flipBoxChat()
sm.flipBoxChatPlayerAsSpeaker()
sm.setColor(1)
sm.sendNext("#face2#Eh?!")


sm.sendDelay(2000)


sm.moveNpcByTemplateId(3001508, True, 50, 100)
sm.sendDelay(1000)


sm.setSpeakerID(3001508)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialogue()
sm.setBoxChat()
sm.boxChatPlayerAsSpeaker()
sm.setBoxOverrideSpeaker()
sm.flipBoxChat()
sm.flipBoxChatPlayerAsSpeaker()
sm.setColor(1)
sm.sendNext("#face3#Ahh!")


sm.zoomCamera(1000, 2000, 1000, -1350, -400)


sm.setSpeakerID(3001509)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialogue()
sm.setBoxChat()
sm.boxChatPlayerAsSpeaker()
sm.setBoxOverrideSpeaker()
sm.flipBoxChat()
sm.flipBoxChatPlayerAsSpeaker()
sm.setColor(1)
sm.sendNext("#face0#Whoa...")


sm.setSpeakerID(3001510)
sm.setSpeakerType(3)
sm.removeEscapeButton()
sm.flipDialogue()
sm.setBoxChat()
sm.boxChatPlayerAsSpeaker()
sm.setBoxOverrideSpeaker()
sm.flipBoxChat()
sm.flipBoxChatPlayerAsSpeaker()
sm.setColor(1)
sm.sendSay("#face2#This lifeform is from... somewhere else.")


sm.sendDelay(3000)


sm.showFadeTransition(0, 1000, 3000)
sm.zoomCamera(0, 1000, 2147483647, 2147483647, 2147483647)


sm.moveCamera(True, 0, 0, 0)


sm.sendDelay(300)


sm.removeOverlapScreen(1000)
sm.moveCamera(True, 0, 0, 0)


sm.setTemporarySkillSet(0)
sm.setInGameDirectionMode(False, True, False, False)
# Unhandled Message [47] Packet: 2F 01 00 00 00 40 9C 00 00 00 00 00 00 28 00 00 00 00 00 00 80 05 BB 46 E6 17 02 0C 00 75 73 65 72 5F 6C 76 75 70 3D 31 30
sm.removeNpc(3001508)
sm.removeNpc(3001509)
sm.removeNpc(3001510)
sm.warp(402090001, 0)
