# -*- coding: utf-8 -*-
from PRANKBOTS import *
from PB.ttypes import Message
from PB.ttypes import ContentType as Type
from datetime import datetime, timedelta
from time import sleep
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz
botStart = time.time()
#===========
WARRIOR = []
#================
settingsOpen = codecs.open("prankBots.json","r","utf-8")
settings = json.load(settingsOpen)
#===========
line = LINE("")
line.log("Auth Token : " + str(line.authToken))
channelToken = line.getChannelResult()
#===========
pb1 = LINE("")
pb1.log("Auth Token : " + str(pb1.authToken))
#===========
pb2 = LINE("")
pb2.log("Auth Token : " + str(pb2.authToken))
#================
oepoll = OEPoll(line)
lineProfile = line.getProfile()
lineSettings = line.getSettings()
lineMID = line.profile.mid
pb1MID = pb1.getProfile().mid
pb2MID = pb2.getProfile().mid
#================
Bots = [lineMID,pb1MID,pb2MID]
OWNER = ["u961be7189409ffd9138c7206e35003b0"]
#================
wait={
    "lang":"JP",
    "myProfile": {
        "displayName": "",
        "pictureStatus": "",
        "statusMessage": ""
    }
}
wait["myProfile"]["displayName"] = lineProfile.displayName
wait["myProfile"]["statusMessage"] = lineProfile.statusMessage
wait["myProfile"]["pictureStatus"] = lineProfile.pictureStatus
def backupData():
    try:
        backup = settings
        f = codecs.open('prankBots.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
            
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
    time.sleep(5)
    python = sys.executable
    os.execl(python, python, *sys.argv)

def logError(text):
    line.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("dataBug_eror.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
        
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyPrankBots"]):
            prankbot = pesan.replace(settings["keyPrankBots"],"")
        else:
            prankbot = "Undefined command"
    else:
        prankbot = text.lower()
    return prankbot

def myhelp():
    if settings['setKey'] == True:
        key = settings['keyPrankBots']
    else:
        key = ''
    helpMessage = "╭━━╦℘̰̰̈́ґ̰̰̈́∂̰̰̈́η̰̰̈́к̰̰̈́╦в̰̰̈́❍̰̰̈́т̰̰̈́ѕ̰̰̈́╦━━╮\n┣╦━━━━╩━━━╩━━━━━" + "\n" + \
                  "┣╦" + key + "Key" + "\n" + \
                  "┣╦" + key + "setbots" + "\n" + \
                  "┣╣━━━╦кї¢к℮ґ╦━━━━" + "\n" + \
                  "┣╣━━━╩━━━━╩━━━━" + "\n" + \
                  "┣╦" + key + "Crotin @" + "\n" + \
                  "┣╦" + key + "Crotinall *kickall" + "\n" + \
                  "┣╦" + key + "Kikuk *kickall blcklist" + "\n" + \
                  "┣╦" + key + "Botname *txt" + "\n" + \
                  "┣╦" + key + "Allbots" + "\n" + \
                  "┣╦" + key + "Botinvite @" + "\n" + \
                  "┣╦" + key + "Cekmek" + "\n" + \
                  "┣╦" + key + "Creat0r" + "\n" + \
                  "┣╦" + key + "botbye *bot leave all group" + "\n" + \
                  "┣╦" + key + "Kuy *mid *nama*jumlah" + "\n" + \
                  "┣╦" + key + "Blist" + "\n" + \
                  "┣╦" + key + "Deleteban" + "\n" + \
                  "┣╦" + key + "Warrior:0n|0ff" + "\n" + \
                  "┣╣━━╦αк̰̰̈́υяαѕι╦━━━" + "\n" + \
                  "┣╣━━╩━━━━━╩━━━" + "\n" + \
                  "┣╦" + key + "Restarter" + "\n" + \
                  "┣╦" + key + "Runtime" + "\n" + \
                  "┣╦" + key + "Spong" + "\n" + \
                  "┣╦" + key + "Deletehat" + "\n" + \
                  "┣━━━━━╩━━━╩━━━━━\n┣━╦🇮🇩CREATOR INDONESIA🇮🇩╦━╣"
    return helpMessage
def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoAdd"] == True:
                line.findAndAddContactsByMid(op.param1)
            sendMention(op.param1, op.param1, "","")
            pb1.sendMessage(op.param1, settings["message"])
            pb2.sendMessage(op.param1, settings["message"])
            line.sendMessage(op.param1, settings["message"])
            line.sendContact(op.param1, 'u5818cb4404411c2e2e6e6937d172cca8')
        if op.type == 13:
          if lineMID in op.param3:
                if op.param2 in OWNER or op.param2 in Bots:
                    line.acceptGroupInvitation(op.param1)
                else:
                    if op.param2 not in OWNER or op.param2 not in Bots:
                        try:
                            line.acceptGroupInvitation(op.param1)
                            line.leaveRoom(op.param1)
                        except:
                            pass
          if pb1MID in op.param3:
                if op.param2 in OWNER or op.param2 in Bots:
                    pb1.acceptGroupInvitation(op.param1)
                else:
                    if op.param2 not in OWNER or op.param2 not in Bots:
                        try:
                            pb1.acceptGroupInvitation(op.param1)
                            pb1.leaveRoom(op.param1)
                        except:
                            pass
          if pb2MID in op.param3:
                if op.param2 in OWNER or op.param2 in Bots:
                    pb2.acceptGroupInvitation(op.param1)
                else:
                    if op.param2 not in OWNER or op.param2 not in Bots:
                        try:
                            pb2.acceptGroupInvitation(op.param1)
                            pb2.leaveRoom(op.param1)
                        except:
                            pass
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != line.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        prankbot = command(text)
                        if prankbot == "key":
                          if msg._from in OWNER:
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["\n┣╦Minggu", "\n┣╦Senin", "\n┣╦Selasa", "\n┣╦Rabu", "\n┣╦Kamis", "\n┣╦Jumat", "\n┣╦Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n┣╦Jam━━╦ " + timeNow.strftime('%H:%M:%S') + " ╦━━"
                            helpMessage = myhelp()
                            line.sendMessage(to, str(helpMessage) + readTime + "\n╰━━╩℘̰̰̈́ґ̰̰̈́∂̰̰̈́η̰̰̈́к╩̰̰̈́в̰̰̈́❍̰̰̈́т̰̰̈́ѕ̰̰̈́╩━━╯")
                        elif prankbot == "cekmek":
                          if msg._from in OWNER:
                            profile = line.getProfile()
                            text = profile.displayName + "􀜁􀅔􏿿"
                            line.sendMessage(to, text)
                            profile = pb1.getProfile()
                            text = profile.displayName + "􀜁􀅔􏿿"
                            pb1.sendMessage(to, text)
                            profile = pb2.getProfile()
                            text = profile.displayName + "􀜁􀅔􏿿"
                            pb2.sendMessage(to, text)
                        elif prankbot == "crotinall": #KICKALL
                            if msg._from in OWNER:
                                if msg.toType == 2:
                                    gs = line.getGroup(msg.to)
                                    gs = pb1.getGroup(msg.to)
                                    gs = pb2.getGroup(msg.to)
                                    time.sleep(0.0002)
                                    targets = []
                                    for g in gs.members:
                                        if _name in g.displayName:
                                            targets.append(g.mid)
                                    if targets == []:
                                        line.sendMessage(to,"LIMIT.!!!")
                                    else:
                                        for target in targets:
                                            if not target in OWNER or not target in Bots:
                                              try:
                                                  klist=[line,pb1,pb2]
                                                  kicker=random.choice(klist)
                                                  kicker.kickoutFromGroup(to,[target])
                                                  print (to,[g.mid])
                                              except:
                                                  pass
                        elif prankbot.startswith("crotin "): #KICK VIA TAG
                          if msg._from in OWNER:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        settings["blacklist"][ls] = True
                                        line.kickoutFromGroup(to,[ls])
                                        print (to,[ls])
                                    except:
                                        pass
                        elif prankbot == "kikuk":
                          if msg._from in OWNER:
                            group = line.getGroup(msg.to)
                            gMembMids = [contact.mid for contact in group.members]
                            matched_list = []
                            for tag in settings["blacklist"]:
                                matched_list+=filter(lambda str: str == tag, gMembMids)
                            if matched_list == []:
                                random.choice(PRANK).sendMessage(to,"Noting blacklist in group..")
                                return
                            for jj in matched_list:
                                try:
                                    klist=[line,pb1,pb2]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(to,[jj])
                                    print((to,[jj]))
                                except:
                                    pass
#======================================
                        elif prankbot == "restarter":
                          if msg._from in OWNER:
                            line.sendMessage(to, "Sebentar...")
                            line.sendMessage(to, "Selesai.!!\n\nSilahkan command 1x ktik me\ntunggu beberapa saat skitar 1-2 mnt\njika respon command me lagi 1x\ntunggu respon (DONE NORMAL)")
                            settings["restartPoint"] = to
                            restartBot()
                        elif prankbot == "botbye":
                          if msg._from in OWNER:
                            gid = pb1.getGroupIdsJoined()
                            gid = pb2.getGroupIdsJoined()
                            gid = line.getGroupIdsJoined()
                            for i in gid:
                                pb1.leaveGroup(i)
                                pb2.leaveGroup(i)
                                line.leaveGroup(i)
                            else:
                            	pass
                        elif prankbot == "runtime":
                          if msg._from in OWNER:
                            timeNow = time.time()
                            runtime = timeNow - botStart
                            runtime = format_timespan(runtime)
                            line.sendMessage(to, "┣━━━╦RUNTIME BOTS╦━━━╣\n ┣━╦{}╦━╣".format(str(runtime)))
                        elif prankbot == "spong":
                          if msg._from in OWNER:
                            start = time.time()
                            elapsed_time = time.time() - start
                            line.sendMessage(to,format(str(elapsed_time)))
                            pb1.sendMessage(to,format(str(elapsed_time)))
                            pb2.sendMessage(to,format(str(elapsed_time)))
#==============================================================================#
                        elif prankbot.startswith("botname "):
                          if msg._from in OWNER:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 20:
                                profile = line.getProfile()
                                profile.displayName = string
                                line.updateProfile(profile)
                                line.sendMessage(to,"{}".format(str(string)))
                            if len(string) <= 20:
                                profile = pb2.getProfile()
                                profile.displayName = string
                                pb2.updateProfile(profile)
                            if len(string) <= 20:
                                profile = pb1.getProfile()
                                profile.displayName = string
                                pb1.updateProfile(profile)
                                pb1.sendMessage(to,"{}".format(str(string)))
                                pb2.sendMessage(to,"{}".format(str(string)))
                        elif prankbot == "allbots":
                          if msg._from in OWNER:
                            line.sendContact(to, lineMID)
                            pb1.sendContact(to, pb1MID)
                            pb2.sendContact(to, pb2MID)
                        elif prankbot == "creator":
                          if msg._from in OWNER:
                            line.sendContact(to, 'u961be7189409ffd9138c7206e35003b0')

                        elif prankbot == "deleteban":
                          if msg._from in OWNER:
                            settings["blacklist"] = {}
                            line.sendMessage(to,"done all deleted blacklist")
                            pb1.sendMessage(to,"succes.!!")
                            pb2.sendMessage(to,"succes.!!")
                        elif prankbot == "deletechat":
                          if msg._from in OWNER:
                            line.removeAllMessages(op.param2)
                            pb1.removeAllMessages(op.param2)
                            pb2.removeAllMessages(op.param2)
                            line.sendMessage(to, "Berhasil hapus semua chat")
                        elif prankbot == "blist":
                            if msg._from in OWNER:
                              if settings["blacklist"] == {}:
                                line.sendMessage(to,"Noting")
                              else:
                                ma = ""
                                a = 0
                                for m_id in settings["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +line.getContact(m_id).displayName + "\n"
                                line.sendMessage(to,"╭━━━══[ Daftar Blacklist ]══━━━╮\n"+ma+"\n━━━━━══[ Total|%s|Blacklist]══━━━━━" %(str(len(settings["blacklist"]))))
                        elif prankbot == "setbots":
                          if msg._from in OWNER:
                            try:
                                ret_ = "╭━╦℘̰̰̈́ґ̰̰̈́∂̰̰̈́η̰̰̈́к̰̰̈́в̰̰̈́❍̰̰̈́т̰̰̈́ѕ̰̰̈́╦━╮\n┣━╣━━╦SETTINGS╦━━━\n┣━╦━━╩━━━╩━━━"
                                if msg.to in settings["WARRIOR"]: ret_ += "\n┣━╣ 『  WARRIOR 』  Ξ 『ON』"
                                else: ret_ += "\n┣━╣ 『  WARRIOR 』  Ξ 『OFF』"
                                ret_ += "\n┣━━━╩━━━╩━━━━\n╰━╩℘̰̰̈́ґ̰̰̈́∂̰̰̈́η̰̰̈́кв̰̰̈́❍̰̰̈́т̰̰̈́ѕ̰̰̈́╩━╯"
                                line.sendMessage(to, str(ret_))
                            except Exception as e:
                                line.sendMessage(to, str(e))
                        elif prankbot == "warrior:on":
                          if msg._from in OWNER:
                            if msg.to in settings["WARRIOR"]:
                                line.sendMessage(to, "Zzz")
                                pb1.sendMessage(to, "Molor")
                                pb2.sendMessage(to, "Meler")
                            else:
                                line.sendMessage(to, "Bulsit")
                                pb1.sendMessage(to, "Jancok")
                                pb2.sendMessage(to, "Mulut tidak di skolahin pada")
                                settings["WARRIOR"][msg.to] = True
                        elif prankbot == "warrior:off":
                          if msg._from in OWNER:
                            if msg.to in settings["WARRIOR"]:
                                line.sendMessage(to, "Zzzz")
                                pb1.sendMessage(to, "zzz")
                                pb2.sendMessage(to, "zzz")
                                del settings["WARRIOR"][msg.to]
                            else:
                                line.sendMessage(to, "zzz")
                                pb1.sendMessage(to, "zzz")
                                pb2.sendMessage(to, "zzz")
        if op.type == 19:
          if op.param1 in settings['WARRIOR']:
            if lineMID in op.param3:
                if op.param2 in OWNER or op.param2 in Bots:
                    pb1.findAndAddContactsByMid(op.param3)
                    pb1.inviteIntoGroup(op.param1,[op.param3])
                    line.acceptGroupInvitation(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        pb2.findAndAddContactsByMid(op.param3)
                        pb1.kickoutFromGroup(op.param1,[op.param2])
                        pb2.inviteIntoGroup(op.param1,[op.param3])
                        line.acceptGroupInvitation(op.param1)
                    except:
                        pass
                                
            if pb1MID in op.param3:
                if op.param2 in OWNER or op.param2 in Bots:
                    line.findAndAddContactsByMid(op.param3)
                    line.inviteIntoGroup(op.param1,[op.param3])
                    pb1.acceptGroupInvitation(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        pb2.findAndAddContactsByMid(op.param3)
                        line.kickoutFromGroup(op.param1,[op.param2])
                        pb2.inviteIntoGroup(op.param1,[op.param3])
                        pb1.acceptGroupInvitation(op.param1)
                    except:
                        pass
            if pb2MID in op.param3:
                if op.param2 in OWNER or op.param2 in Bots:
                    pb1.findAndAddContactsByMid(op.param3)
                    pb1.inviteIntoGroup(op.param1,[op.param3])
                    pb2.acceptGroupInvitation(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        pb1.findAndAddContactsByMid(op.param3)
                        line.kickoutFromGroup(op.param1,[op.param2])
                        pb1.inviteIntoGroup(op.param1,[op.param3])
                        pb2.acceptGroupInvitation(op.param1)
                    except:
                        pass
            if op.param3 in OWNER:
                if op.param2 in OWNER or op.param2 in Bots:
                    line.findAndAddContactsByMid(op.param3)
                    line.inviteIntoGroup(op.param1,[op.param3])
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        line.findAndAddContactsByMid(op.param3)
                        pb1.kickoutFromGroup(op.param1,[op.param2])
                        line.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        pass
#==========================================#
        if op.type == 17: #MODE WAR
            if op.param2 in OWNER or op.param2 in Bots:
            	pass
            else:
              try:
                if op.param1 in settings['WARRIOR']:
                    settings["blacklist"][op.param2] = True
                    try:
                          pb1.kickoutFromGroup(op.param1,[op.param2])
                          G = pb2.getGroup(op.param1)
                          G.preventJoinByTicket = True
                          pb2.updateGroup(G)
                    except:
                          try:
                              pb2.kickoutFromGroup(op.param1,[op.param2])
                              G = line.getGroup(op.param1)
                              G.preventJoinByTicket = True
                              line.updateGroup(G)
                          except:
                              try:
                                  line.kickoutFromGroup(op.param1,[op.param2])
                                  G = pb1.getGroup(op.param1)
                                  G.preventJoinByTicket = True
                                  pb1.updateGroup(G)
                              except:
                                  pass
              except:
                  pass
        if op.type == 17:
            if op.param2 in settings["blacklist"]:
               try:
                   pb2.kickoutFromGroup(op.param1,[op.param2])
               except:
                   try:
                       pb1.kickoutFromGroup(op.param1,[op.param2])
                   except:
                       try:
                           line.kickoutFromGroup(op.param1,[op.param2])
                       except:
                           pass
    except Exception as error:
        logError(error)
        
        if op.type == 59:
            print (op)
        
#==============================================================================#
while True:
    try:
      ops=oepoll.singleTrace(count=50)
      if ops != None:
        for op in ops: 
          bot(op)
          oepoll.setRevision(op.revision)
        
    except Exception as e:
        line.log("[SINGLE_TRACE] ERROR : " + str(e))
