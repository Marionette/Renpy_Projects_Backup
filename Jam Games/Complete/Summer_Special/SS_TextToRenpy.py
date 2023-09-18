# coding: utf-8

fin = open('dayScript.txt')
fout = open('dayScript.rpy', 'w+')

fin.seek(0)

for line in fin:
  #line.translate(u"'", u"‘’")
  #line.translate(u"\"", u"“”")
  #line.translate(u"...", u"…")
  #line.translate(u"-", u"—")
  #line.translate("  ", "\t")
  
  #Replace any Invalid Characters
  line = line.replace("‘", "'")
  line = line.replace("’", "'")
  line = line.replace("“", "\"")
  line = line.replace("”", "\"")
  line = line.replace("…", "...")
  line = line.replace("—", "-")
  #line = line.replace("\t", "  ")
  
  #Add quotes to all lines
  line = "  \"%s\"" % line
  line = line.replace("\n\"", "\"\n")
  
  line = line.replace("\"\"", "\"") # Remove duplicate "
  
  line = line.replace("(", "#(")
  line = line.replace("\"#", "#")
  line = line.replace(")\"", ")")
  line = line.replace("\"\t[", "# [")
  line = line.replace("\"-----------------------------------------------------------\"", "#\"-----------------------------------------------------------\"")
  line = line.replace("\"----------------------------------------------------------\"", "#\"-----------------------------------------------------------\"")
  line = line.replace("\"-----------------------\"", "#\"-----------------------\"")
  line = line.replace("\"-----------------------------------------------\"", "#\"-----------------------------------------------\"")
  line = line.replace("\"------------------------------------------------------\"", "#\"------------------------------------------------------\"")
  line = line.replace("\"-------------------------------------------------------\"", "#\"-------------------------------------------------------\"")
  line = line.replace("\"-------------------------------------\"", "#\"-------------------------------------\"")
  line = line.replace("\"--------------------------------\"", "#\"--------------------------------\"")
  line = line.replace("\"--------------------------\"", "#\"--------------------------------\"")
  line = line.replace("\"---------------------------------\"", "#\"--------------------------------\"")
  line = line.replace("\"---------------------------------------------------------------------\"", "#\"--------------------------------\"")
  line = line.replace("\"--------------------------------------------------------------------\"", "#\"--------------------------------\"")
  
  
  
  
  
  
  #Replace any character bits
  line = line.replace("\"MC \"", "ce \"") 
  line = line.replace("\"MC  \"", "ce \"")
  line = line.replace("\" MC \"", "ce \"") 
  line = line.replace("\"JJ \"", "ju \"") 
  line = line.replace("\"JJ  \"", "ju \"") 
  line = line.replace("\"K \"", "ka \"") 
  line = line.replace("\"K  \"", "ka \"") 
  line = line.replace("\"N \"", "ka \"") 
  line = line.replace("\"N  \"", "ka \"")
  line = line.replace("\"G \"", "gr \"") 
  line = line.replace("\"G  \"", "gr \"") 



  line = line.replace("\">JJ leaves\"", "hide june ")
  line = line.replace("\"-- JJ leaves\"", "hide june ")
  line = line.replace("\">K leaves\"", "hide kameron ")
  line = line.replace("\">N leaves\"", "hide kameron ")
  line = line.replace("\">N leaves.\"", "hide kameron ")
  line = line.replace("\">JJ enters\"", "show june ")
  line = line.replace("\">K enters\"", "show kameron ")
  line = line.replace("\">N enters\"", "show kameron ")
  line = line.replace("\"> N enters\"", "show kameron ")

  #line = line.replace("\"[M] 	\"", "mk \"") #merona external
  #line = line.replace("\"[M]       \"", "mk \"") #merona external
  #line = line.replace("\"        	", "mi \"") #for merona internal
  #line = line.replace("\"      	", "mi \"") #for merona internal
  #line = line.replace("\"\t", "mi \"") #for merona internal
  #line = line.replace("mi \"\"", "mk \"") #if ' mi "" ' actually a continuation of mk
  #
  #line = line.replace("\"[?]    	\"", "qq \"") #unknown person
  #line = line.replace("\"[??]    	\"", "qq \"") #unknown person
  #line = line.replace("\"[??]  	\"", "qq \"") #unknown person
  #line = line.replace("\"[??]	\"", "qq \"") #unknown person
  #line = line.replace("\"[?]	", "qq ") #unknown person
  #line = line.replace("\"[R]   \t", "rt ") #rett
  #line = line.replace("\"[R]	", "rt ") #rett
  #line = line.replace("\"[R]    	", "rt ") #rett
  #line = line.replace("\"[K]    	", "kh ") #krieta
  #line = line.replace("\"[K]	", "kh ") #krieta
  #line = line.replace("\"[W]   	", "hw ") # Wriene
  #line = line.replace("\"[W]  	", "hw ") # Wriene
  #line = line.replace("\"[W]	", "hw ") # Wriene
  #line = line.replace("\"[C]   	", "ck ") #Cimaria
  #line = line.replace("\"[C]  	", "ck ") #Cimaria
  #line = line.replace("\"[C]	", "ck ") #Cimaria
  #line = line.replace("\"[D]	", "dt ") #Duran
  #line = line.replace("\"[D]   	", "dt ") #Duran
  #line = line.replace("\"[D] 	", "dt ") #Duran
  #line = line.replace("\"[L]   	", "ln ") #Lexan
  #line = line.replace("\"[L]    	", "ln ") #Lexan
  #line = line.replace("\"[L]	", "ln ") #Lexan
  #line = line.replace("\"[L]  	", "ln ") #Lexan
  #line = line.replace("\"[B]    	", "bg ") #Boyen
  #line = line.replace("\"[B]	", "bg ") #Boyen
  #line = line.replace("\"[P]	", "pm ") #Prowen
  #line = line.replace("\"[P]    	", "pm ") #Prowen
  #line = line.replace("\"[Monster]     	", "mo ") #Prowen
  #line = line.replace("", "")
  #line = line.replace("", "")
  #
  #
  ##Replace any image defines

  #image bg grandmaHouse = "images/bg/bg_grandmaHouse.jpg"
  #image bg storeFront = "images/bg/bg_storeFront.jpg"
  #image bg storeInside_Register = "images/bg/bg_storeInside_Register.jpg"
  #image bg storeOutside back1 = "images/bg/bg_storeOutside1_Back.jpg"
  #image bg storeOutside back2 = "images/bg/bg_storeOutside2_Back.jpg"
  #image bg storeRegister = "images/bg/bg_storeRegister.png"
  #image bg storeRoof1 = "images/bg/bg_storeRoof1.jpg"
  #image bg storeRoof2 = "images/bg/bg_storeRoof2.jpg"
  line = line.replace("\"[BG STORAGE ROOM]\"", "show bg storage room")
  line = line.replace("\"[BG STORE FRONT]\"", "show bg storeFront")
  line = line.replace("\"[BG STORE INSIDE]\"", "show bg storeInside_Register")
  #line = line.replace("\"[CG ", "scene cg ")
  #line = line.replace("\"[CS ", "show ")
  #line = line.replace("\" [CS ", "show ")
  #line = line.replace("\"  [CS ", "show ")
  #line = line.replace("\"[fade to white", "scene bg white with fade")
  #line = line.replace("\"[fade to black", "scene bg black with fade")
  #line = line.replace("\"[Fade to black", "scene bg black with fade")
  #line = line.replace("\"scene bg black with fade please", "scene bg black with fade ")
  #
  #
  ##Replace sprite defines  
  #line = line.replace("\"[M_u_", "show merona ")
  #line = line.replace("\"[M_t_", "show merona t ")
  #line = line.replace("\"[K_", "show kreita ")
  #line = line.replace("\"[R_", "show rett ")
  #line = line.replace("\"[B_", "show boyen ")
  #line = line.replace("\"[RA_", "show ranan ")
  #line = line.replace("\"[L_", "show lexan ")
  #line = line.replace("\"[C_", "show cimaria ")
  #line = line.replace("\"[D_", "show duran ")
  #line = line.replace("\"[D_t_", "show duran t ")
  #line = line.replace("\"[W_", "show wriane ")
  #line = line.replace("\"[P_", "show prowen ")
  #
  #line = line.replace("M_u_", "merona ")
  #line = line.replace("M_t_", "merona t ")
  #line = line.replace("M_", "merona ")
  #line = line.replace("K_", "kreita ")
  #line = line.replace("R_", "rett ")
  #line = line.replace("B_", "boyen ")
  #line = line.replace("RA_", "ranan ")
  #line = line.replace("L_", "lexan ")
  #line = line.replace("C_", "cimaria ")
  #line = line.replace("D_", "duran ")
  #line = line.replace("D_t_", "duran t ")
  #line = line.replace("W_", "wriane ")
  #line = line.replace("P_", "prowen ")
  #
  #line = line.replace("NF", "nightFire")
  #line = line.replace("Omerona", "OM")
  #
  #line = line.replace("_", " ") #swap _ for spaces
  #
  #
  ##Replace any sound defines
  #line = line.replace("\"[Music: ", "play music ")
  #line = line.replace("\" [Music: ", "play music ")
  #line = line.replace("\"[Sound: ", "play sound ")
  #line = line.replace("\"[Sound ", "play sound ")
  #line = line.replace("\"Sound: ", "play sound ")
  #line = line.replace("\"[Silence", "stop music")
  #line = line.replace("\"[Stop any music please!\"", "stop music")  
  #line = line.replace("\"[Fade to silence", "stop music fadeout 1.0")
  #line = line.replace("\"[fade to silence", "stop music fadeout 1.0")
  #line = line.replace("\"[fade to Silence", "stop music fadeout 1.0")
  #line = line.replace("\"[stop music fadeout 1.0 please~ T^T", "stop music fadeout 1.0")
  #line = line.replace("\"[stop music fadeout 1.0 please~", "stop music fadeout 1.0")
  #line = line.replace("\"[stop music fadeout 1.0 please", "stop music fadeout 1.0")
  #line = line.replace("\"from before]", "#from before]")
  #
  ##Replace specific music files
  #line = line.replace("play music Ambient Sound", "play music music_ambient")
  #line = line.replace("play music Ambient Sound", "play music music_ambient")
  #line = line.replace("play music New Beginnings", "play music music_newBegin")
  #line = line.replace("play music Piano", "play music music_piano")
  #line = line.replace("play music Potent Happiness", "play music music_potHappy")
  #line = line.replace("play music Romance", "play music music_romance")
  #line = line.replace("play music Society of Trees (Short)","play music music_SoTsh")
  #line = line.replace("play music Society of Trees", "play music music_SoT")
  #line = line.replace("play music Society of trees", "play music music_SoT")
  #line = line.replace("play music Title Theme", "play music music_title")
  #line = line.replace("play music Uplifting",  "play music music_uplifting")
  #line = line.replace("play music battle", "play music music_movement")
  #line = line.replace("play music Merona's Theme", "play music music_meronatheme")
  #line = line.replace("play music Life", "play music music_life")
  #line = line.replace("play music Eerie", "play music music_eerie")
  #line = line.replace("play music Recollection", "play music music_recollection")
  #
  #line = line.replace("play sound djhalleu  stavanger-nightingale1", "play sound sound_birds")     
  #line = line.replace("play sound inchadney  cuckoo_short", "play sound sound_cukoo")         
  #line = line.replace("play sound inchadney  cuckoo short", "play sound sound_cukoo")     
  #
  #line = line.replace("play sound kaonaya  bell-at-daitokuji-temple-kyoto","play sound sound_bell")       
  #line = line.replace("play sound Monster Snarling", "play sound sound_snarl")     
  #line = line.replace("play sound Nature Ambiance", "play sound sound_ambiance")  
  #line = line.replace("play sound Nature Ambience", "play sound sound_ambiance")  
  #line = line.replace("play sound weldonsmith  cricket2dopecho", "play sound sound_cricket")   
  #line = line.replace("play sound Footsteps", "play sound sound_footsteps")   
  #line = line.replace("play sound Knock", "play sound sound_knock")   
  #line = line.replace("play sound knock", "play sound sound_knock")   
  #line = line.replace("play sound BreatheOut", "play sound sound_breatheOut")   
  #line = line.replace("play sound Falling In Dirt", "play sound sound_fallInDirt")   
  #line = line.replace("play sound fallInDirt", "play sound sound_fallInDirt")   
  #line = line.replace("play sound night time ambient sound", "play sound sound_nighttimeAmbience")   
  #line = line.replace("play sound lionRoar", "play sound sound_lionRoar")    
  #line = line.replace("play sound rustling", "play sound sound_rustling")   
  #line = line.replace("play sound Punch", "play sound sound_punch") 
  #line = line.replace("play sound Water", "play sound sound_water")    
  #line = line.replace("play sound Bump", "play sound sound_bump")    
  
  
  
  
  #removed unneeded/empty lines
  
  line = line.replace("\"\"", "") #remove empty quotes
  line = line.replace("  \" \"\n", "") #remove empty quotes
  line = line.replace("  \n", "") #remove empty lines
  line = line.replace("  \"\n", "\n") #remove empty lines
  #line = line.replace("]\"", "") #remove unneeded ]
  #line = line.replace("] \"", "")#remove unneeded ]
  #line = line.replace("]	\"", "")#remove unneeded ]
  #line = line.replace("]	\"", "")#remove unneeded ]
  #line = line.replace("]     \"", "")#remove unneeded ]
  #line = line.replace("]   \"", "")#remove unneeded ]
  #line = line.replace("] #", " #")#remove unneeded ]
  #line = line.replace("]#", " #")#remove unneeded ]
  #line = line.replace("]", " ")#remove unneeded ]
  line = line.replace("  \"\n", "\n") #remove lines that only have "
  line = line.replace("\" \"", "\"") #remove accidental " "  
  line = line.replace("\t", "  ")
  line = line.replace(";", "#;") #normally means theres an extra instruction
  
  
  line = line.replace("\"[", "#TODO [")#Replace unchanged [ as these need replaced manually
  line = line.replace("\" [", "#TODO [")#Replace unchanged [ as these need replaced manually
  line = line.replace("\">", "#TODO >")#Replace unchanged [ as these need replaced manually
  line = line.replace("\"<", "#TODO <")#Replace unchanged [ as these need replaced manually
  #line = line.replace("- Needs to be prepared first", "#TODO [ Needs to be prepared first")
  #line = line.replace("- to be prepared", "#TODO [to be prepared")
  
  
  print(line)
  fout.write(line)
  