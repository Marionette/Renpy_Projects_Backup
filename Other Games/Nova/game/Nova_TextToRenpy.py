# coding: utf-8
import sys

file_name_in = sys.argv[1]
file_name_out = sys.argv[2]
#fin = open('CPath.txt')
#fout = open('nova_story_CPath.rpy', 'w+')
fin = open(file_name_in)
fout = open(file_name_out, 'w+')

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
  line = line.replace("\"The dashed line separates", "#The dashed line separates")
  line = line.replace("\">=3", "#>=3")
  
  
  
  
  
  
  
  
  #Replace any character bits
  line = line.replace("\"[M]   	\"", "mk \"") #merona external
  line = line.replace("\"[M]	\"", "mk \"") #merona external
  line = line.replace("\"[M] 	\"", "mk \"") #merona external
  line = line.replace("\"[M]       \"", "mk \"") #merona external
  line = line.replace("\"        	", "mi \"") #for merona internal
  line = line.replace("\"      	", "mi \"") #for merona internal
  line = line.replace("\"\t", "mi \"") #for merona internal
  line = line.replace("mi \"\"", "mk \"") #if ' mi "" ' actually a continuation of mk
  
  line = line.replace("\"[?]    	\"", "qq \"") #unknown person
  line = line.replace("\"[??]    	\"", "qq \"") #unknown person
  line = line.replace("\"[??]  	\"", "qq \"") #unknown person
  line = line.replace("\"[??]	\"", "qq \"") #unknown person
  line = line.replace("\"[?]	", "qq ") #unknown person
  line = line.replace("\"[R]   \t", "rt ") #rett
  line = line.replace("\"[R]	", "rt ") #rett
  line = line.replace("\"[R]    	", "rt ") #rett
  line = line.replace("\"[K]    	", "kh ") #krieta
  line = line.replace("\"[K]	", "kh ") #krieta
  line = line.replace("\"[W]   	", "hw ") # Wriene
  line = line.replace("\"[W]  	", "hw ") # Wriene
  line = line.replace("\"[W]	", "hw ") # Wriene
  line = line.replace("\"[W] 	", "hw ") # Wriene
  line = line.replace("\"[C]   	", "ck ") #Cimaria
  line = line.replace("\"[C]  	", "ck ") #Cimaria
  line = line.replace("\"[C]	", "ck ") #Cimaria
  line = line.replace("\"[D]	", "dt ") #Duran
  line = line.replace("\"[D]   	", "dt ") #Duran
  line = line.replace("\"[D] 	", "dt ") #Duran
  line = line.replace("\"[L]   	", "ln ") #Lexan
  line = line.replace("\"[L]    	", "ln ") #Lexan
  line = line.replace("\"[L]	", "ln ") #Lexan
  line = line.replace("\"[L]  	", "ln ") #Lexan
  line = line.replace("\"[B]    	", "bg ") #Boyen
  line = line.replace("\"[B]	", "bg ") #Boyen
  line = line.replace("\"[P]	", "pm ") #Prowen
  line = line.replace("\"[P]    	", "pm ") #Prowen
  line = line.replace("\"[P]       	", "pm ") #Prowen
  line = line.replace("\"[V]   	", "qv ") # Voya
  line = line.replace("\"[V]  	", "qv ") # Voya
  line = line.replace("\"[V]	", "qv ") # Voya
  line = line.replace("\"[V] 	", "qv ") # Voya
  line = line.replace("\"[RA]	", "ra ") # Ranan
  line = line.replace("\"[DR]	", "dr ") # Drae
  line = line.replace("\"[Monster]     	", "mo ") #Monster
  line = line.replace("", "")
  line = line.replace("", "")
  
  
  #Replace any image defines
  line = line.replace("\"[CG ", "scene cg ")
  line = line.replace("\"[CS ", "show ")
  line = line.replace("\" [CS ", "show ")
  line = line.replace("\"  [CS ", "show ")
  
  line = line.replace("\"[fade to white", "scene bg white with fade")
  line = line.replace("\"[fade to black please~ T^T", "scene bg black with fade ")  
  line = line.replace("\"[fade to black please", "scene bg black with fade")
  line = line.replace("\"[fade to black", "scene bg black with fade")
  line = line.replace("\"[Fade to black", "scene bg black with fade")
  line = line.replace("\"[face to black", "scene bg black with fade")
  line = line.replace("\"scene bg black with fade please", "scene bg black with fade ")
  line = line.replace("\"[fade to CG CandlesWBlur", "scene cg CandlesWBlur with fade")
  
  #Comment out Extra image instrucitons  
  line = line.replace("- keep in front", "#- keep in front")  
  
  #Replace sprite defines  
  line = line.replace("\"[M_u_", "show merona ")
  line = line.replace("\"[M_t_", "show merona t ")
  line = line.replace("\"[K_", "show kreita ")
  line = line.replace("\"[R_", "show rett ")
  line = line.replace("\"[B_", "show boyen ")
  line = line.replace("\"[RA_", "show ranan ")
  line = line.replace("\"[L_", "show lexan ")
  line = line.replace("\"[C_", "show cimaria ")
  line = line.replace("\"[D_", "show duran ")
  line = line.replace("\"[D_t_", "show duran t ")
  line = line.replace("\"[W_", "show wriane ")
  line = line.replace("\"[P_", "show prowen ")
  
  line = line.replace("M_u_", "merona ")
  line = line.replace("M_t_", "merona t ")
  line = line.replace("M_", "merona ")
  line = line.replace("DR_", "drae ")
  line = line.replace("RA_", "ranan ")
  line = line.replace("K_", "kreita ")
  line = line.replace("R_", "rett ")
  line = line.replace("B_", "boyen ")
  line = line.replace("L_", "lexan ")
  line = line.replace("C_", "cimaria ")
  line = line.replace("D_", "duran ")
  line = line.replace("D_t_", "duran t ")
  line = line.replace("W_", "wriane ")
  line = line.replace("P_", "prowen ")
  line = line.replace("V_", "voya ")
  
  line = line.replace("NF", "nightFire")
  line = line.replace("Omerona", "OM")
  
  line = line.replace("_", " ") #swap _ for spaces
  
  
  #Replace any sound defines
  line = line.replace("\"[Music: ", "play music ")
  line = line.replace("\" [Music: ", "play music ")
  line = line.replace("\"[Sound (no loop): ", "play sound ")
  line = line.replace("\"[Sound: ", "play sound ")
  line = line.replace("\"[Sound ", "play sound ")
  line = line.replace("\"Sound: ", "play sound ")
  line = line.replace("\"[Silence", "stop music")
  line = line.replace("\"[Stop any music please!\"", "stop music")  
  line = line.replace("\"[fade to silence please", "stop music fadeout 1.0")
  line = line.replace("\"[Fade to silence", "stop music fadeout 1.0")
  line = line.replace("\"[fade to silence", "stop music fadeout 1.0")
  line = line.replace("\"[fade to Silence", "stop music fadeout 1.0")
  line = line.replace("\"[Fade to Silence", "stop music fadeout 1.0")
  line = line.replace("\"[stop music fadeout 1.0 please~ T^T", "stop music fadeout 1.0")
  line = line.replace("\"[stop music fadeout 1.0 please~", "stop music fadeout 1.0")
  line = line.replace("\"[stop music fadeout 1.0 please", "stop music fadeout 1.0")
  line = line.replace("\"from before]", "#from before")
  line = line.replace("\"(from before)", "#from before")
    
  #Replace specific music files
  line = line.replace("play music Ambient Sound", "play music music_ambient")
  line = line.replace("play music Ambient Sound", "play music music_ambient")
  line = line.replace("play music New Beginnings", "play music music_newBegin")
  line = line.replace("play music Piano", "play music music_piano")
  line = line.replace("play music piano", "play music music_piano")
  line = line.replace("play music Potent Happiness", "play music music_potHappy")
  line = line.replace("play music Romance", "play music music_romance")
  line = line.replace("play music Society of Trees (Short)","play music music_SoTsh")
  line = line.replace("play music Society of Trees", "play music music_SoT")
  line = line.replace("play music Society of trees", "play music music_SoT")
  line = line.replace("play music Title Theme", "play music music_title")
  line = line.replace("play music Uplifting",  "play music music_uplifting")
  line = line.replace("play music battle", "play music music_movement")
  line = line.replace("play music Battle", "play music music_movement")
  line = line.replace("play music Merona's Theme", "play music music_meronatheme")
  line = line.replace("play music Life", "play music music_life")
  line = line.replace("play music Eerie", "play music music_eerie")
  line = line.replace("play music Recollection", "play music music_recollection")
  
  line = line.replace("play music Aces High", "play music music_Aces_High")
  line = line.replace("play music Aces high", "play music music_Aces_High")
  line = line.replace("play music Afterglow", "play music music_Afterglow")
  line = line.replace("play music A_Moments Reflection", "play music music_A_Moments_Reflection")
  line = line.replace("play music A Moments Reflection", "play music music_A_Moments_Reflection")
  line = line.replace("play music A Moment's Reflection", "play music music_A_Moments_Reflection")
  line = line.replace("play music A thousand Skins Pt2", "play music music_A_thousand_Skins_Pt2")
  line = line.replace("play music Black Vortex", "play music music_Black_Vortex")
  line = line.replace("play music Cool Steel Breeze", "play music music_Cool_Steel_Breeze")
  line = line.replace("play music Dark Red Wine", "play music music_Dark_Red_Wine")
  line = line.replace("play music Delightful D", "play music music_Delightful_D")
  line = line.replace("play music Ecstasy X", "play music music_Ecstasy_X")
  line = line.replace("play music Ecxtasy X", "play music music_Ecstasy_X")
  line = line.replace("play music Exctasy X", "play music music_Ecstasy_X")
  line = line.replace("play music Epilogue", "play music music_Epilogue")
  line = line.replace("play music Future Gladiator", "play music music_Future_Gladiator")
  line = line.replace("play music Gallows Hill", "play music music_Gallows_Hill")
  line = line.replace("play music Greek Dance", "play music music_Greek_Dance")
  line = line.replace("play music Green Leaves", "play music music_Green_Leaves")
  line = line.replace("play music Heart of Nowhere", "play music music_Heart_of_Nowhere")
  line = line.replace("play music Heroic Age", "play music music_Heroic_Age")
  line = line.replace("play music Ill be right behind you Josephine", "play music music_Ill_be_right_behind_you_Josephine")
  line = line.replace("play music Incoherent", "play music music_Incoherent")
  line = line.replace("play music Infinite Horizon", "play music music_Infinite_Horizon")
  line = line.replace("play music Infinite Perspective", "play music music_Infinite_Perspective")
  line = line.replace("play music Inner Journey", "play music music_Inner_Journey")
  line = line.replace("play music I want to destroy something beautiful", "play music music_I_want_to_destroy_something_beautiful")
  line = line.replace("play music Lafayette", "play music music_Lafayette")
  line = line.replace("play music Last Kiss Good Night", "play music music_Last_Kiss_Good_Night")
  line = line.replace("play music Main Theme", "play music music_Main_Theme")
  line = line.replace("play music Nincompoop", "play music music_Nincompoop")
  line = line.replace("play music Oh Mallory", "play music music_Oh_Mallory")
  line = line.replace("play music Pilot Error", "play music music_Pilot_Error")
  line = line.replace("play music Pompeii", "play music music_Pompeii")
  line = line.replace("play music Pride", "play music music_Pride")
  line = line.replace("play music Radio Martini", "play music music_Radio_Martini")
  line = line.replace("play music Renaissance", "play music music_Renaissance")
  line = line.replace("play music Revolution Now", "play music music_Revolution_Now")
  line = line.replace("play music River Meditation", "play music music_River_Meditation")
  line = line.replace("play music Roll away the Stone", "play music music_Roll_away_the_Stone")
  line = line.replace("play music Roll away the stone", "play music music_Roll_away_the_Stone")
  line = line.replace("play music Sailors Lament", "play music music_Sailors_Lament")
  line = line.replace("play music Shes on my Mind", "play music music_Shes_on_my_Mind")
  line = line.replace("play music She's on my Mind", "play music music_Shes_on_my_Mind")
  line = line.replace("play music Shes on my mind", "play music music_Shes_on_my_Mind")
  line = line.replace("play music She's on my mind", "play music music_Shes_on_my_Mind")
  line = line.replace("play music She dreams in blue", "play music music_She_dreams_in_blue")
  line = line.replace("play music She Dreams in Blue", "play music music_She_dreams_in_blue")
  line = line.replace("play music Soporific", "play music music_Soporific")
  line = line.replace("play music Sovereign", "play music music_Sovereign")
  line = line.replace("play music Sugar On My Tongue", "play music music_Sugar_On_My_Tongue")
  line = line.replace("play music Sugar on my Tongue", "play music music_Sugar_On_My_Tongue")
  line = line.replace("play music Sugar on my tongue", "play music music_Sugar_On_My_Tongue")
  line = line.replace("play music Summer Day", "play music music_Summer_Day")
  line = line.replace("play music Swimming To Cambodia", "play music music_Swimming_To_Cambodia")
  line = line.replace("play music Swimming to Cambodia", "play music music_Swimming_To_Cambodia")
  line = line.replace("play music Travel Light", "play music music_Travel_Light")
  line = line.replace("play music Under the Stairs", "play music music_Under_the_Stairs")
  line = line.replace("play music Up Kilkenny", "play music music_Up_Kilkenny")
  line = line.replace("play music White", "play music music_White")
  line = line.replace("play music Words Fall Apart", "play music music_Words_Fall_Apart")
  line = line.replace("play music Words fall apart", "play music music_Words_Fall_Apart")
  line = line.replace("play music Words", "play music music_Words")
  
  
  line = line.replace("play sound djhalleu  stavanger-nightingale1", "play sound sound_birds")     
  line = line.replace("play sound inchadney  cuckoo_short", "play sound sound_cukoo")         
  line = line.replace("play sound inchadney  cuckoo short", "play sound sound_cukoo")     
  
  line = line.replace("play sound kaonaya  bell-at-daitokuji-temple-kyoto","play sound sound_bell")       
  line = line.replace("play sound Monster Snarling", "play sound sound_snarl")     
  line = line.replace("play sound Nature Ambiance", "play sound sound_ambiance")  
  line = line.replace("play sound Nature Ambience", "play sound sound_ambiance")  
  line = line.replace("play sound weldonsmith  cricket2dopecho", "play sound sound_cricket")   
  line = line.replace("play sound Footsteps", "play sound sound_footsteps")   
  line = line.replace("play sound Knock", "play sound sound_knock")   
  line = line.replace("play sound knock", "play sound sound_knock")   
  line = line.replace("play sound BreatheOut", "play sound sound_breatheOut")   
  line = line.replace("play sound Falling In Dirt", "play sound sound_fallInDirt")   
  line = line.replace("play sound fallInDirt", "play sound sound_fallInDirt")   
  line = line.replace("play sound night time ambient sound", "play sound sound_nighttimeAmbience")   
  line = line.replace("play sound lionRoar", "play sound sound_lionRoar")    
  line = line.replace("play sound rustling", "play sound sound_rustling")   
  line = line.replace("play sound Punch", "play sound sound_punch") 
  line = line.replace("play sound Water", "play sound sound_water")    
  line = line.replace("play sound Bump", "play sound sound_bump")    
  
  line = line.replace("play sound airAttack", "play sound sound_airAttack")
  line = line.replace("play sound ambiance", "play sound sound_ambiance")
  line = line.replace("play sound arrow", "play sound sound_arrow")
  line = line.replace("play sound Arrow", "play sound sound_arrow")
  line = line.replace("play sound bell", "play sound sound_bell")
  line = line.replace("play sound birds", "play sound sound_birds")
  line = line.replace("play sound breatheOut", "play sound sound_breatheOut")
  line = line.replace("play sound bump", "play sound sound_bump")
  line = line.replace("play sound clap", "play sound sound_clap")
  line = line.replace("play sound crash", "play sound sound_crash")
  line = line.replace("play sound cricket", "play sound sound_cricket")
  line = line.replace("play sound cukoo", "play sound sound_cukoo")
  line = line.replace("play sound fallInDirt", "play sound sound_fallInDirt")
  line = line.replace("play sound fallInDirt_short", "play sound sound_fallInDirt_short")
  line = line.replace("play sound fireAttack", "play sound sound_fireAttack")
  line = line.replace("play sound fluttering", "play sound sound_fluttering")
  line = line.replace("play sound footsteps", "play sound sound_footsteps")
  line = line.replace("play sound harshFootsteps", "play sound sound_harshFootsteps")
  line = line.replace("play sound knock", "play sound sound_knock")
  line = line.replace("play sound lionRoar", "play sound sound_lionRoar")
  line = line.replace("play sound lionRoar2", "play sound sound_lionRoar2")
  line = line.replace("play sound nighttimeAmbience", "play sound sound_nighttimeAmbience")
  line = line.replace("play sound night time ambience", "play sound sound_nighttimeAmbience")
  line = line.replace("play sound punch", "play sound sound_punch")
  line = line.replace("play sound rain", "play sound sound_rain")
  line = line.replace("play sound rustling", "play sound sound_rustling")
  line = line.replace("play sound snarl", "play sound sound_snarl")
  line = line.replace("play sound swordAttack", "play sound sound_swordAttack")
  line = line.replace("play sound swordDraw", "play sound sound_swordDraw")
  line = line.replace("play sound thunder", "play sound sound_thunder")
  line = line.replace("play sound water", "play sound sound_water")
  line = line.replace("play sound whistle", "play sound sound_whistle")
  line = line.replace("play sound wind", "play sound sound_wind")
  
  
  
  #removed unneeded/empty lines
  
  line = line.replace("\"\"", "") #remove empty quotes
  line = line.replace("  \" \"\n", "") #remove empty quotes
  line = line.replace("  \n", "") #remove empty lines
  line = line.replace("  \"\n", "\n") #remove empty lines
  line = line.replace("]\"", "") #remove unneeded ]
  line = line.replace("] \"", "")#remove unneeded ]
  line = line.replace("]	\"", "")#remove unneeded ]
  line = line.replace("]	\"", "")#remove unneeded ]
  line = line.replace("]     \"", "")#remove unneeded ]
  line = line.replace("]   \"", "")#remove unneeded ]
  line = line.replace("] #", " #")#remove unneeded ]
  line = line.replace("]#", " #")#remove unneeded ]
  line = line.replace("]", " ")#remove unneeded ]
  line = line.replace("  \"\n", "\n") #remove lines that only have "
  line = line.replace("\" \"", "\"") #remove accidental " "  
  line = line.replace("\t", "  ")
  line = line.replace(";", "#;") #normally means theres an extra instruction
  
  
  line = line.replace("\"[", "#TODO [")#Replace unchanged [ as these need replaced manually
  line = line.replace("- Needs to be prepared first", "#TODO [ Needs to be prepared first")
  line = line.replace("- to be prepared", "#TODO [to be prepared")
  
  
  print(line)
  fout.write(line)
  