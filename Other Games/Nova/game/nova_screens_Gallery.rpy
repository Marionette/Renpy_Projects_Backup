#python:    
    #FanArt = [imageName, thumbnailName, artist, galleryLink, tags]
    
init python:
    FontPath = "assets\BOLTON.TTF"
    ShowMerona = True
    ShowDuran = True
    ShowOthers = True
    ShowGroup = True
    #----------------------------------------------
    def ShouldShowImage(Fanart, Tag):
      shouldShow = False
      
      Tags = Fanart[4]
      
      if Tag in Tags:
        shouldShow = True
        
      if Tag == "Group" and len(Tags) > 1:
        shouldShow = True
      
      if "Everyone" in Tags:
        shouldShow = True
      
      if Tag == "None":
        shouldShow = False
        
      return shouldShow
    #----------------------------------------------
    
    #FanArt = [imageName, galleryPath, artist, galleryLink, tags]
    
    
    FanartMerona01 = [ "akkeyroomi.png", "img/fanart/FanartGallery_Merona",          "akkeyroomi",          "http://akkeyroomi.deviantart.com/gallery/",                                        ["Merona"] ]
    FanartMerona02 = [ "Animizuu.png", "img/fanart/FanartGallery_Merona",            "Animizuu",            "http://animizuu.deviantart.com/gallery/",                                          ["Merona"] ]
    FanartMerona03 = [ "Clovis-thecutestcat.png", "img/fanart/FanartGallery_Merona", "Clovis-thecutestcat", "http://clovis-thecutestcat.deviantart.com/gallery/44681617/My-personal-Favorites", ["Merona"] ]
    FanartMerona04 = [ "Danimi.png", "img/fanart/FanartGallery_Merona",             "Danimi",              "http://danimi.deviantart.com/gallery/",                                            ["Merona"] ]
    FanartMerona05 = [ "Iriho-chan.png", "img/fanart/FanartGallery_Merona",         "IridescentFlora",          "https://iridescentflora.deviantart.com/gallery",                                        ["Merona"] ]
    FanartMerona06 = [ "llenviash.png", "img/fanart/FanartGallery_Merona",          "llenviash",           "http://llenviash.deviantart.com/gallery/",                                         ["Merona"] ]
    FanartMerona07 = [ "MiLiica.png", "img/fanart/FanartGallery_Merona",            "MiLiica",             "http://miliica.deviantart.com/gallery",                                            ["Merona"] ]
    FanartMerona08 = [ "RuiCarmen.png", "img/fanart/FanartGallery_Merona",          "Rui/Carmen",          "http://rui09.deviantart.com/gallery/",                                             ["Merona"] ]
    FanartMerona09 = [ "Suika.png", "img/fanart/FanartGallery_Merona",              "Suika",               "http://www.facebook.com/little.suika",                                             ["Merona"] ]
    FanartMerona10 = [ "sweetsalad.png", "img/fanart/FanartGallery_Merona",         "sweetsalad",          "http://sweetsalad.deviantart.com/gallery/",                                        ["Merona"] ]
    FanartMerona11 = [ "Tai-chan104.png", "img/fanart/FanartGallery_Merona",        "Tai-Chan104",         "http://tai-chan104.deviantart.com/gallery/",                                       ["Merona"] ]
    FanartMerona12 = [ "tierEight.png", "img/fanart/FanartGallery_Merona",          "tierEight",           "http://tiereight.deviantart.com/gallery/",                                         ["Merona"] ]
    FanartMerona13 = [ "Tomoyo Ichijouji.png", "img/fanart/FanartGallery_Merona",   "Tomoyo Ichijouji",     "http://tomoyoichijouji.deviantart.com/gallery/",                                  ["Merona"] ]
    
    FanartGroup01 = [ "Duran and Merona_by_KuroDK.png", "img/fanart/FanartGallery_Group",   "KuroDK",     "https://kurodk.deviantart.com",                        ["Merona", "Duran"] ]
    FanartGroup02 = [ "merona_and_duran_by_KatouShinobu.png", "img/fanart/FanartGallery_Group",   "KatouShinobu",     "https://katoushinobu.deviantart.com/gallery/",            ["Merona", "Duran"] ]
    FanartGroup04 = [ "nova_by J-amesT.png", "img/fanart/FanartGallery_Group",   "J-amesT",     "https://j-amest.deviantart.com/gallery/",                                  ["Merona", "Cimaria", "Wriane"] ]
    FanartGroup05 = [ "nova_by_immortalblood0219.png", "img/fanart/FanartGallery_Group",   "immortalblood0219",     "https://immortalblood0219.deviantart.com/gallery/",          ["Everyone"] ]
    FanartGroup03 = [ "nova_by_TomoyoIchijouji.png", "img/fanart/FanartGallery_Group",   "Tomoyo Ichijouji",     "http://tomoyoichijouji.deviantart.com/gallery/",                     ["Merona", "Wriane", "Kreita", "Rett", "Ranan"] ]
    FanartGroup06 = [ "nova_synthesis_creaturum_contest_entry_by_willow-wishes-d986suk.png", "img/fanart/FanartGallery_Group",   "willow-wishes",     "https://willow-wishes.deviantart.com/gallery/", ["Everyone"] ]
    FanartGroup07 = [ "Prowen and Cimaria_by_pixelograph.png", "img/fanart/FanartGallery_Group",   "pixelograph",     "https://www.deviantart.com/",            ["Prowen", "Cimaria"] ]


    
    List_FanArt = [ FanartMerona01,
                    FanartMerona02,
                    FanartMerona03,
                    FanartMerona04,
                    FanartMerona05,
                    FanartMerona06,
                    FanartMerona07,
                    FanartMerona08,
                    FanartMerona09,
                    FanartMerona10,
                    FanartMerona11,
                    FanartMerona12,
                    FanartMerona13,
                    FanartGroup01,
                    FanartGroup02,
                    FanartGroup04,
                    FanartGroup05,
                    FanartGroup03,
                    FanartGroup06,
                    FanartGroup07]
                    
    #List_CG = [ FanartMerona01]

##############################################################################
# Galleries
#

init python:
    #Galleries settings - start
    #list the CG gallery images here:
    gallery_cg_items = ["cg intro1",
                        "cg intro2",
                        "cg intro3",
                        "cg intro4", 
                        "cg talkwithtree1",
                        #"cg talkwithtree2",
                        #"cg talkwithtree3",
                        #"cg talkwithtree4",
                        #"cg talkwithtree5",
                        #"cg talkwithtree6",
                        "cg handOnBranch1",
                        #"cg handOnBranch2",
                        #"cg handOnBranch3",
                        "cg monsterRoar",
                        "cg M_onGround1",
                        #"cg M_onGround2",
                        #"cg M_onGround3",
                        #"cg M_onGround4",
                        #"cg M_onGround5",
                        "cg M_zoomShadow1", 
                        #"cg M_zoomShadow2",
                        #"cg M_zoomShadow3",
                        "cg rabbit",
                        "cg sunsetScape1",
                        #"cg sunsetScape2",
                        #"cg sunsetScape2_cimaria1",
                        #"cg sunsetScape2_cimaria2",
                        #"cg sunsetScape2_cimaria_lexan",
                        #"cg sunsetScape3",
                        #"cg sunsetScape4",
                        #"cg sunsetScape5",
                        #"cg sunsetScape6",
                        #"cg sunsetScape7",
                        #"cg sunsetScape8",
                        #"cg sunsetScape9",
                        #"cg sunsetScape10",
                        "cg C_leaving1",
                        #"cg C_leaving2",
                        #"cg C_leaving3",
                        #"cg C_leaving4",
                        "cg_composite L_holding_M1",
                        #"cg L_holdingM1",
                        #"cg L_holdingM2",
                        #"cg L_holdingM3",
                        #"cg L_holdingM4",
                        #"cg L_holdingM5",
                        #"cg L_holdingM6",
                        #"cg L_holdingM7",
                        #"cg L_holdingM8",
                        #"cg L_holdingM9",
                        #"cg L_holdingM10",
                        #"cg L_holdingM11",
                        #"cg L_holdingM12",
                        #"cg L_holdingM13",
                        #"cg L_holdingM14",
                        #"cg L_holdingM15",
                        #"cg L_holdingM16",
                        #"cg L_holdingM17",
                        #"cg L_holdingM18",
                        #"cg L_holdingM19",
                        "cg candles",
                        #"cg candles blur",
                        "cg hangingPlant",
                        #"cg hangingPlant2",
                        "cg glowingPotCG",
                        "cg handInSoil",
                        #"cg handInSoil2",
                        "cg honey",
                        "cg examination",
                        #"cg examination1",
                        #"cg examination2",
                        #"cg examination3",
                        #"cg examination3b",
                        #"cg examination4",
                        #"cg examination4b",
                        #"cg examination5",
                        #"cg examination6",
                        #"cg examination7",
                        #"cg examination8",
                        #"cg examination9",
                        "cg RettOnFloor",
                        "cg Kreita_ArmsonMR",
                        "cg MeronaTreeHug",
                        "cg climb",
                        "cg duranSulk1",
                        #"cg duranSulk2",
                        #"cg duranSulk3",
                        #"cg duranSulk4",
                        #"cg duranSulk5",
                        "cg duranBurn1",
                        #"cg duranBurn2",
                        #"cg duranBurn3",
                        "cg raspberry",
                        "cg fallenTrunks",
                        "cg monsterCat",
                        "cg KreitaAttack",
                        #"cg Lexan handOnMsArm1",
                        #"cg Lexan handOnMsArm2",
                        "cg Lexan handOnMsArm3",
                        #"cg Lexan handOnMsArm4",
                        #"cg Lexan handOnMsArm5",
                        "cg bushRustle",
                        "cg KreitaGrab",
                        "cg ProwenAwakes",
                        "cg DuranPunch",
                        #"cg DuranPunch2",
                        #"cg DuranPunch3",
                        #"cg DuranPunch4",
                        #"cg DuranPunch5",
                        ##Nightfire here##
                        #"cg nightFire",
                        "cg_composite nightFire_full",
                        "cg danger",
                        "cg_composite RettAtTree_full1",
                        #"cg RettAtTree",
                        "cg fishMonster",
                        "cg FishmonsterEyes",
                        #"cg climb2",
                        ##Tailorshop here##
                        "cg_composite tailorShop_full1",
                        #"cg tailorshop back",
                        #"cg tailorshop door closed",
                        #"cg tailorshop door slightlyOpen",
                        #"cg tailorshop duran",
                        #"cg tailorshop duran OM",  
                        #"cg tailorshop duran SO",
                        #"cg tailorshop duran SO OM",
                        #"tailorshop front"
                        #"cg tailorDress",
                        #"cg tailorDoor closed",
                        #"cg tailorDoor open",
                        #"cg tailorDoor slightlyOpen",
                        #"cg tailorShopFront",
                        #"cg tailorShopWall",
                        "cg MeronaDuranCuddle",
                        "cg MeronaLexan_EyeCover",
                        #"cg MeronaLexan_EyeCover2",
                        "cg CimariaRettFlirting",
                        "cg LexanRainShield",
                        "cg MeronasMagic",
                        "cg antidote",
                        "cg MeronasLove_A",
                        "cg MeronasLove_B",
                        "cg grave",
                        "cg ProwensHouse3",
                        "cg ocean",
                        "cg ProwensGoodbye",
                        "cg MeronaDuranRomance1",
                        #"cg MeronaDuranRomance2",
                        #"cg MeronaDuranRomance3",
                        "cg MeronaLexanRomance1",
                        #"cg MeronaLexanRomance2",
                        #"cg MeronaLexanRomance3",                        
                        "cg ANewJourney",
                        ]
    
    #list the BG gallery images here:]
    gallery_bg_items = [
                        "cg forest1", 
                        #"cg_sky1",
                        #"cg forest1_5",
                        "cg forest2", 
                        "cg forest3", 
                        "cg forest4", 
                        "cg forest5", 
                        "cg_sky2",
                        "cg officeBack",
                        "cg office",
                        #"cg office2",
                        "cg_sky3",
                        "cg MeronasRoom",
                        #"cg MeronasRoom_dark",
                        "cg MeronasRoom_2",
                        "cg MeronasDoor",
                        #"cg MeronasDoor2",
                        "bg corridor",
                        "cg stairs",
                        "bg corridor2",
                        "cg dormOutside",
                        "cg laneo",
                        "bg laneoOutskirts",
                        "cg ground",
                        #"cg ground2",
                        "cg forest1_evening",
                        "bg laneoStreet",
                        "cg forest6",
                        "cg forest7", 
                        "cg forest8",
                        "cg forest9", 
                        "cg forest10",
                        "cg forest11", 
                        "cg forest12",
                        "cg forest13",
                        "cg forestHouse",
                        "cg forestHouse inside",
                        "cg forestHouse inside2",
                        "cg forest14",
                        "cg forest15",
                        "cg forest16",
                        #"cg forest16b",
                        "cg campingFire",
                        "cg nightSky",
                        "cg forest17",
                        "cg hillSide",
                        "cg riverSide",
                        "cg hillSide2",
                        "cg forest18",
                        "cg forestGround",
                        #"cg forestGroundNight",
                        "cg forest19",
                        "cg stream",
                        "cg streamGround",
                        "cg forestTop",
                        "cg forest20",
                        "cg forest20_5",
                        "cg forest20_75",
                        "cg forest21",
                        "cg forest22",
                        "cg forest23",
                        "cg town",
                        "cg townShops",
                        "cg townHerbShop",
                        "cg pharmacy",
                        "cg forest24",
                        "cg forest25", 
                        "cg forest26",
                        #"cg forest26b",
                        "cg forest27",
                        "cg forest28",
                        "cg forest29",
                        "cg forest30",
                        "cg forest31",
                        "cg forest32",
                        "cg forest33",
                        "cg ProwensHouse1",
                        #"cg ProwensHouse2",
                        "cg forest34",
                        #"cg forest34_2",
                        "cg forest35",
                        #"cg forest35_2",
                        "cg cave",
                        "cg Calil",
                        "cg RanansShopBack",
                        "cg InnRoom",
                        "cg InnLobby",
                        "cg RanansLair",
                        "cg RoyalGardens",
                        "cg castleRoom",
                        "cg castleGate",
                        #"academy",
                        #"cg ground3",
                        #"cg town skyVersion",
                        ]
                     

    #list the Music Room gallery images here:
    gallery_mr_items = [
                        "audio/music/Title Theme.ogg",
                        "audio/music/New Beginnings.ogg",
                        "audio/music/Cool Steel Breeze.ogg",
                        "audio/music/Dark Red Wine.ogg",
                        #"audio/music/Society of Trees (Short).ogg",
                        "audio/music/Society of Trees.ogg",
                        "audio/music/Merona's Theme.ogg",
                        "audio/music/battle.ogg",
                        "audio/music/Piano.ogg",
                        "audio/music/Lafayette.ogg",
                        "audio/music/Potent Happiness.ogg",
                        "audio/music/River Meditation.ogg",
                        "audio/music/Summer Day.ogg",
                        "audio/music/Sugar On My Tongue.ogg",
                        "audio/music/Heart of Nowhere.ogg",
                        "audio/music/Recollections.ogg",
                        "audio/music/Ill be right behind you Josephine.ogg",
                        "audio/music/Words.ogg",
                        "audio/music/Epilogue.ogg",
                        "audio/music/Life.ogg",
                        "audio/music/She dreams in blue.ogg",
                        "audio/music/Uplifting.ogg",
                        "audio/music/Up Kilkenny.ogg",
                        "audio/music/Nincompoop.ogg",
                        "audio/music/Travel Light.ogg",
                        "audio/music/Ecstasy X.ogg",
                        "audio/music/Delightful D.ogg",
                        "audio/music/Radio Martini.ogg",
                        "audio/music/Infinite Perspective.ogg",
                        "audio/music/White.ogg",
                        "audio/music/Words Fall Apart.ogg",
                        "audio/music/Eerie.ogg",
                        "audio/music/Aces High.ogg",
                        "audio/music/Afterglow.ogg",
                        "audio/music/Pilot Error.ogg",
                        "audio/music/Soporific.ogg",
                        "audio/music/I want to destroy something beautiful.ogg",
                        "audio/music/Green Leaves.ogg",
                        "audio/music/Swimming To Cambodia.ogg",
                        "audio/music/Revolution Now.ogg",
                        "audio/music/Incoherent.ogg",
                        "audio/music/Future Gladiator.ogg",
                        "audio/music/Pride.ogg",
                        "audio/music/Romance.ogg",
                        "audio/music/Greek Dance.ogg",
                        "audio/music/Under the Stairs.ogg",
                        "audio/music/Shes on my Mind.ogg",
                        "audio/music/Roll away the Stone.ogg",
                        "audio/music/Sovereign.ogg",
                        "audio/music/A Moments Reflection.ogg",
                        "audio/music/Inner Journey.ogg",
                        "audio/music/Gallows Hill.ogg",
                        "audio/music/Infinite Horizon.ogg",
                        "audio/music/Sailors Lament.ogg",
                        "audio/music/Oh Mallory.ogg",
                        "audio/music/A thousand Skins Pt2.ogg",
                        "audio/music/Pompeii.ogg",
                        "audio/music/Black Vortex.ogg",
                        "audio/music/Renaissance.ogg",                        
                        #"audio/music/Heroic Age.ogg",
                        #"audio/music/Last Kiss Good Night.ogg",
                        ]


    #Text to display for Music Box Items
    gallery_music_text = [
                          "Title Theme",
                          "New Beginnings",
                          "Cool Steel Breeze",
                          "Dark Red Wine",
                          #"Society of Trees (Short)",
                          "Society of Trees",
                          "Merona's Theme",
                          "Battle",
                          "Piano",
                          "Lafayette",
                          "Potent Happiness",
                          "River Meditation",
                          "Summer Day",
                          "Sugar On My Tongue",
                          "Heart of Nowhere",
                          "Recollections",
                          "Ill be right behind you Josephine",
                          "Words",
                          "Epilogue",
                          "Life",
                          "She dreams in blue",
                          "Uplifting",
                          "Up Kilkenny",
                          "Nincompoop",
                          "Travel Light",
                          "Ecstasy X",
                          "Delightful D",
                          "Radio Martini",
                          "Infinite Perspective",
                          "White",
                          "Words Fall Apart",
                          "Eerie",
                          "Aces High",
                          "Afterglow",
                          "Pilot Error",
                          "Soporific",
                          "I want to destroy something beautiful",
                          "Green Leaves",
                          "Swimming To Cambodia",
                          "Revolution Now",
                          "Incoherent",
                          "Future Gladiator",
                          "Pride",
                          "Romance",
                          "Greek Dance",
                          "Under the Stairs",
                          "Shes on my Mind",
                          "Roll away the Stone",
                          "Sovereign",
                          "A Moments Reflection",
                          "Inner Journey",
                          "Gallows Hill",
                          "Infinite Horizon",
                          "Sailors Lament",
                          "Oh Mallory",
                          "A Thousand Skins Pt2",
                          "Pompeii",
                          "Black Vortex",
                          "Renaissance",                          
                          #"Heroic Age",
                          #"Last Kiss Good Night",
                          ]
    

    artist = ["artist", "artist2"]
    gallery = ["gallery", "gallery2"]
    quote = ["quote", "quote2"]
    #how many rows and columns in the gallery screens?
    gal_rows = 10
    gal_cols = 1
    #thumbnail size in pixels:
    #thumbnail_x = 100
    #thumbnail_y = 100
    thumbnail_x = 267
    thumbnail_y = 150
    #the setting above (267x150) will work well with 16:9 screen ratio. Make sure to adjust it, if your are using 4:3 or something else.
    #Galleries settings - end
    
    gal_cells = gal_rows * gal_cols    
    g_cg = Gallery()
    
    for gal_item in gallery_cg_items:
        compositeImage = False
        
        #--- Composite Images ---
    
        if gal_item == "cg_composite L_holding_M1":
          g_cg.button(gal_item + " butt")
          g_cg.unlock_image("cg_composite L_holding_M1")
          g_cg.unlock_image("cg_composite L_holding_M2")
          g_cg.unlock_image("cg_composite L_holding_M3")
          #g_cg.unlock("cg_composite L_holding_M1")
          #g_cg.unlock("cg_composite L_holding_M2")
          #g_cg.unlock("cg_composite L_holding_M3")
          compositeImage = True
          
        #if gal_item == "cg nightFire":
        #  g_cg.button(gal_item + " butt")
        #  g_cg.transform(ScrollDown)
        #  g_cg.unlock_image("cg_composite nightFire_full")
        #  compositeImage = True
          
        if gal_item == "cg_composite nightFire_full":
          g_cg.button(gal_item + " butt")
          g_cg.unlock_image("cg_composite nightFire_full")
          g_cg.transform(ScrollDown)
          compositeImage = True
          
        if gal_item == "cg_composite tailorShop_full1":
          g_cg.button(gal_item + " butt")
          g_cg.unlock_image("cg_composite tailorShop_full1")
          g_cg.unlock_image("cg_composite tailorShop_full2")
          g_cg.unlock_image("cg_composite tailorShop_full3")
          compositeImage = True
          
        if gal_item == "cg_composite RettAtTree_full1":
          g_cg.button(gal_item + " butt")
          g_cg.unlock_image("cg_composite RettAtTree_full1")
          g_cg.unlock_image("cg_composite RettAtTree_full2")
          g_cg.unlock_image("cg_composite RettAtTree_full3")
          compositeImage = True
          
        #---
        
        if compositeImage == False:
          g_cg.button(gal_item + " butt")
          g_cg.image(gal_item)
          g_cg.unlock(gal_item)
        
        if gal_item == "cg handOnBranch1": 
          g_cg.image("cg handOnBranch2")
          g_cg.unlock("cg handOnBranch2")
          g_cg.image("cg handOnBranch3")
          g_cg.unlock("cg handOnBranch3")
          
        if gal_item == "cg M_onGround1": 
          g_cg.image("cg M_onGround2")
          g_cg.unlock("cg M_onGround2")
          g_cg.image("cg M_onGround3")
          g_cg.unlock("cg M_onGround3")
          g_cg.image("cg M_onGround4")
          g_cg.unlock("cg M_onGround4")
          g_cg.image("cg M_onGround5")
          g_cg.unlock("cg M_onGround5")
          
        if gal_item == "cg M_zoomShadow1": 
          g_cg.image("cg M_zoomShadow2")
          g_cg.unlock("cg M_zoomShadow2")
          g_cg.image("cg M_zoomShadow3")
          g_cg.unlock("cg M_zoomShadow3")
          
        if gal_item == "cg talkwithtree1":
          g_cg.image("cg talkwithtree2")
          g_cg.unlock("cg talkwithtree2")
          g_cg.image("cg talkwithtree3")
          g_cg.unlock("cg talkwithtree3")
          g_cg.image("cg talkwithtree4")
          g_cg.unlock("cg talkwithtree4")
          g_cg.image("cg talkwithtree5")
          g_cg.unlock("cg talkwithtree5")
          g_cg.image("cg talkwithtree6")
          g_cg.unlock("cg talkwithtree6")
        
        if gal_item == "cg C_leaving1":
          g_cg.image("cg C_leaving2")
          g_cg.unlock("cg C_leaving2")
          g_cg.image("cg C_leaving3")
          g_cg.unlock("cg C_leaving3")
          g_cg.image("cg C_leaving4")
          g_cg.unlock("cg C_leaving4")
        
        if gal_item == "cg sunsetScape1":
          # commented out cgs dont show up in story?
          g_cg.image("cg sunsetScape2")
          g_cg.unlock("cg sunsetScape2")
          #g_cg.image("cg sunsetScape2_cimaria1")
          #g_cg.unlock("cg sunsetScape2_cimaria1")
          #g_cg.image("cg sunsetScape2_cimaria2")
          #g_cg.unlock("cg sunsetScape2_cimaria2")
          #g_cg.image("cg sunsetScape2_cimaria_lexan")
          #g_cg.unlock("cg sunsetScape2_cimaria_lexan")
          g_cg.image("cg sunsetScape3")
          g_cg.unlock("cg sunsetScape3")
          g_cg.image("cg sunsetScape4")
          g_cg.unlock("cg sunsetScape4")
          g_cg.image("cg sunsetScape5")
          g_cg.unlock("cg sunsetScape5")
          g_cg.image("cg sunsetScape6")
          g_cg.unlock("cg sunsetScape6")
          g_cg.image("cg sunsetScape7")
          g_cg.unlock("cg sunsetScape7")
          g_cg.image("cg sunsetScape8")
          g_cg.unlock("cg sunsetScape8")
          #g_cg.image("cg sunsetScape9")
          #g_cg.unlock("cg sunsetScape9")
          g_cg.image("cg sunsetScape10")
          g_cg.unlock("cg sunsetScape10")
        
        if gal_item == "cg hangingPlant":
          g_cg.transform(ScrollDown)
          g_cg.image("cg hangingPlant2")
          g_cg.unlock("cg hangingPlant2")
          
        if gal_item == "cg handInSoil":
          g_cg.image("cg handInSoil2")
          g_cg.unlock("cg handInSoil2")
        
        if gal_item == "cg candles":
          g_cg.image("cg candles blur")
          g_cg.unlock("cg candles blur")
        
        if gal_item == "cg monsterCat":
          g_cg.transform(ScrollUp)
        if gal_item == "cg fishMonster":
          g_cg.transform(ZoomOut)
        #Separate
        if gal_item == "cg climb":
          g_cg.image("cg climb2")
          g_cg.unlock("cg climb2")
        
        if gal_item == "cg examination":
          g_cg.image("cg examination1")
          g_cg.unlock("cg examination1")
          g_cg.image("cg examination2")
          g_cg.unlock("cg examination2")
          g_cg.image("cg examination3")
          g_cg.unlock("cg examination3")
          g_cg.image("cg examination3b")
          g_cg.unlock("cg examination3b")
          g_cg.image("cg examination4")
          g_cg.unlock("cg examination4")
          g_cg.image("cg examination4b")
          g_cg.unlock("cg examination4b")
          g_cg.image("cg examination5")
          g_cg.unlock("cg examination5")
          g_cg.image("cg examination6")
          g_cg.unlock("cg examination6")
          g_cg.image("cg examination7")
          g_cg.unlock("cg examination7")
          g_cg.image("cg examination8")
          g_cg.unlock("cg examination8")
          g_cg.image("cg examination9")
          g_cg.unlock("cg examination9")
        
        if gal_item == "cg handInSoil":
          g_cg.image("cg handInSoil2")
          g_cg.unlock("cg handInSoil2")
        
        
        if gal_item == "cg duranBurn1":
          g_cg.image("cg duranBurn2")
          g_cg.unlock("cg duranBurn2")
          g_cg.image("cg duranBurn3")
          g_cg.unlock("cg duranBurn3")
        
        if gal_item == "cg duranSulk1":
          g_cg.image("cg duranSulk2")
          g_cg.unlock("cg duranSulk2")
          g_cg.image("cg duranSulk3")
          g_cg.unlock("cg duranSulk3")
          g_cg.image("cg duranSulk4")
          g_cg.unlock("cg duranSulk4")
          g_cg.image("cg duranSulk5")
          g_cg.unlock("cg duranSulk5")
        
        #if gal_item == "cg Lexan handOnMsArm1":
        #"cg Lexan handOnMsArm2")
        if gal_item == "cg Lexan handOnMsArm3":
          g_cg.image("cg Lexan handOnMsArm4")
          g_cg.unlock("cg Lexan handOnMsArm4")
          g_cg.image("cg Lexan handOnMsArm5")
          g_cg.unlock("cg Lexan handOnMsArm5")
        
        if gal_item == "cg DuranPunch":
          g_cg.image("cg DuranPunch2")
          g_cg.unlock("cg DuranPunch2")
          g_cg.image("cg DuranPunch3")
          g_cg.unlock("cg DuranPunch3")
          g_cg.image("cg DuranPunch4")
          g_cg.unlock("cg DuranPunch4")
          g_cg.image("cg DuranPunch5")
          g_cg.unlock("cg DuranPunch5")
        
        if gal_item == "cg MeronaDuranRomance1":
          g_cg.image("cg MeronaDuranRomance2")
          g_cg.unlock("cg MeronaDuranRomance2")
          g_cg.image("cg MeronaDuranRomance3")
          g_cg.unlock("cg MeronaDuranRomance3")
        
        if gal_item == "cg MeronaLexanRomance1":
          g_cg.image("cg MeronaLexanRomance2")
          g_cg.unlock("cg MeronaLexanRomance2")
          g_cg.image("cg MeronaLexanRomance3")
          g_cg.unlock("cg MeronaLexanRomance3")
        
        if gal_item == "cg MeronaLexan_EyeCover":
          g_cg.image("cg MeronaLexan_EyeCover2")
          g_cg.unlock("cg MeronaLexan_EyeCover2")
        
        #1 and 2 are in BGs instead
        #if gal_item == "cg ProwensHouse1":
        #  g_cg.image("cg ProwensHouse2")
        #  g_cg.image("cg ProwensHouse3")
        #  g_cg.unlock("cg ProwensHouse2")
        #  g_cg.unlock("cg ProwensHouse3")
          
    g_cg.transition = fade
    cg_page=0
    cg_piece = 0
    cg_MaxPiece = 0
    cg_MaxPage = 0

    g_bg = Gallery()
    for gal_item in gallery_bg_items:
    
        compositeImage = False
        
        #--- Composite Images ---
        if gal_item == "cg office":
          g_bg.button(gal_item + " butt")
          g_bg.unlock_image("cg_sky3", "cg office","desk")
          #g_bg.unlock_image("cg_composite Office")
          compositeImage = True
          
          #meronasroom2
        if gal_item == "cg MeronasRoom_2":
          g_bg.button(gal_item + " butt")
          g_bg.unlock_image("cg MeronasRoom_2", "Meronasdesk")
          compositeImage = True
          
        #town
        if gal_item == "cg town":
          g_bg.button(gal_item + " butt")
          g_bg.unlock_image("cg_sky1", "clouds","cg town")
          compositeImage = True
          
        #---
        
        if compositeImage == False:
          g_bg.button(gal_item + " butt")
          g_bg.image(gal_item)
          g_bg.unlock(gal_item)
        #if BGs have variations, such as night version, uncomment the lines below and copy paste them for each BG with variations
#        if gal_item == "bg kitchen":
#            g_bg.image("bg kitchen dining")
#            g_bg.unlock("bg kitchen dining")


                        
        if gal_item == "cg MeronasRoom":
          g_bg.image("cg MeronasRoom_dark")
          g_bg.unlock("cg MeronasRoom_dark")
          
        if gal_item == "cg MeronasDoor":
          g_bg.image("cg MeronasDoor2")
          g_bg.unlock("cg MeronasDoor2")
          
        if gal_item == "cg ground":
          g_bg.image("cg ground2")
          g_bg.unlock("cg ground2")
          
        if gal_item == "cg forest16":
          g_bg.image("cg forest16b")
          g_bg.unlock("cg forest16b")
          
        if gal_item == "cg forestGround":
          g_bg.image("cg forestGroundNight")
          g_bg.unlock("cg forestGroundNight")
          
        if gal_item == "cg forest26":
          g_bg.image("cg forest26b")
          g_bg.unlock("cg forest26b")
          
        if gal_item == "cg ProwensHouse1":
          g_bg.image("cg ProwensHouse2")
          g_bg.unlock("cg ProwensHouse2")
          
        if gal_item == "cg forest34":
          g_bg.image("cg forest34_2")
          g_bg.unlock("cg forest34_2")
          
        if gal_item == "cg forest35":
          g_bg.image("cg forest35_2")
          g_bg.unlock("cg forest35_2")
          
    g_bg.transition = fade
    bg_page=0
    bg_piece = 0
    bg_MaxPiece = 0
    bg_MaxPage = 0
    
    fa_page=0
    fa_piece = 0
    fa_MaxPiece = 0
    fa_MaxPage = 0
    
    g_mr = MusicRoom(fadeout=1.0)
    #add title screen music
    AlwaysUnlockedCount = 0
    i = 0
    for mr_item in gallery_mr_items:
      if (i < AlwaysUnlockedCount):
        g_mr.add(mr_item, always_unlocked=True)
        i+=1
      else:
        g_mr.add(mr_item)
    g_mr.transition = fade
    mr_page=0
    
    
init +1 python:
    #Here we create the thumbnails. We create a grayscale thumbnail image for BGs, but we use a special "locked" image for CGs to prevent spoilers.
    for gal_item in gallery_cg_items:
        _image = gal_item
        
        #if gal_item == "cg L_holdingM1":
        #  _image = "cg_composite L_holding_M1"
        #if gal_item == "cg RettAtTree":
        #  _image = "cg_composite RettAtTree_full1"
        #if gal_item == "cg tailorshop front":
        #  _image = "cg_composite tailorShop_full1"
        if gal_item == "cg nightFire":
          _image = "cg_composite nightFire_full"
          
        renpy.image (gal_item + " butt", im.Scale(ImageReference(_image), thumbnail_x, thumbnail_y))
        
        
    for gal_item in gallery_bg_items:
        _image = gal_item
        
        if gal_item == "cg office":
          _image = "cg_composite Office"
        if gal_item == "cg MeronasRoom_2":
          _image = "cg_composite MeronasRoom2_full"
        if gal_item == "cg town":
          _image = "cg_composite town_full"
          
        renpy.image (gal_item + " butt", im.Scale(ImageReference(_image), thumbnail_x, thumbnail_y))
        #renpy.image (gal_item + " butt dis", im.Grayscale(ImageReference(gal_item + " butt")))

        
        
    #image cg_composite L_holding_M1 = "cg/composites/L_holding_M1.png"
    #image cg_composite L_holding_M2 = "cg/composites/L_holding_M2.png"
    #image cg_composite L_holding_M3 = "cg/composites/L_holding_M3.png"
    #image cg_composite RettAtTree_full1 = "cg/composites/RettAtTree_full1.png"
    #image cg_composite RettAtTree_full2 = "cg/composites/RettAtTree_full2.png"
    #image cg_composite RettAtTree_full3 = "cg/composites/RettAtTree_full3.png"
    #image cg_composite tailorShop_full1 = "cg/composites/tailorShop_full1.png"
    #image cg_composite tailorShop_full2 = "cg/composites/tailorShop_full2.png"
    #image cg_composite tailorShop_full3 = "cg/composites/tailorShop_full3.png"
    #image cg_composite nightFire_full = "cg/composites/nightFire_full.png"
    
    #image cg_composite MeronasRoom2_full = "cg/composites/MeronasRoom2_full.png"
    #image cg_composite Office = "cg/composites/Office.png"
    #image cg_composite town_full = "cg/composites/town_full.png"

    ## ---
        
init -2:
  transform rot180:
      rotate 180
      
#############################################################################################################
screen customButton(buttonText, DoAction, Xpos, Ypos, fontsize=16, Ratio=1.5, TextColour='#966935', TextXOffset=0, TextYOffset=0):
    $imageSizeX = 233/Ratio
    $imageSizeY = 92/Ratio
    $ydiff = 25/Ratio
    $xdiff = 50/Ratio
    #imagebutton auto im.Scale("img/gui/extras/button_blank_%s.png", 116, 45) xpos Xpos ypos Ypos action DoAction
    imagebutton idle im.Scale(im.Grayscale("img/gui/extras/button_blank_idle.png"), imageSizeX, imageSizeY) hover im.Scale(im.Grayscale("img/gui/extras/button_blank_hover.png"), imageSizeX, imageSizeY) selected_idle im.Scale("img/gui/extras/button_blank_idle.png", imageSizeX, imageSizeY) selected_hover im.Scale("img/gui/extras/button_blank_hover.png", imageSizeX, imageSizeY) xpos Xpos ypos Ypos action DoAction
    #imagebutton  xpos Xpos ypos Ypos action DoAction
    #imagebutton ground im.Scale("img/gui/extras/button_blank_ground.png", 116, 45) xpos Xpos ypos Ypos action DoAction
    text "{size=[fontsize]}{color=[TextColour]}[buttonText]{/color}{/size}" xpos (int)(Xpos+xdiff+TextXOffset) ypos (int)(Ypos+ydiff+TextYOffset)
    
screen customButton2(buttonText, DoAction, Xpos, Ypos, fontsize=16, Ratio=1.5, TextColour='#966935', TextXOffset=0, TextYOffset=0):
    $imageSizeX = 233/Ratio
    $imageSizeY = 92/Ratio
    $ydiff = 25/Ratio
    $xdiff = 50/Ratio
    #imagebutton auto im.Scale("img/gui/extras/button_blank_%s.png", 116, 45) xpos Xpos ypos Ypos action DoAction
    imagebutton idle im.Scale("img/gui/extras/button_blank_idle.png", imageSizeX, imageSizeY) hover im.Scale("img/gui/extras/button_blank_hover.png", imageSizeX, imageSizeY) selected_idle im.Scale("img/gui/extras/button_blank_selected_idle.png", imageSizeX, imageSizeY) selected_hover im.Scale("img/gui/extras/button_blank_selected_idle.png", imageSizeX, imageSizeY) xpos Xpos ypos Ypos action DoAction
    #imagebutton  xpos Xpos ypos Ypos action DoAction
    #imagebutton ground im.Scale("img/gui/extras/button_blank_ground.png", 116, 45) xpos Xpos ypos Ypos action DoAction
    label "{size=[fontsize]}{color=[TextColour]}[buttonText]{/color}{/size}" xpos (int)(Xpos+xdiff+TextXOffset) ypos (int)(Ypos+ydiff+TextYOffset)
#--------------------------------------------------------------------------------------------------------
screen thumbnailButton(imagePath, DoAction, Xpos, Ypos):
    #imagebutton idle im.Scale("img/gui/blank.png",100,100) hover im.Scale("img/gui/blank.png",100,100) xpos Xpos ypos Ypos focus_mask None action DoAction
    #add imagePath xpos Xpos ypos Ypos 
    imagebutton idle imagePath hover imagePath xpos Xpos ypos Ypos focus_mask None action DoAction

    #FanArt = [imageName, galleryPath, artist, galleryLink, tags]
    
#--------------------------------------------------------------------------------------------------------
screen FanartThumbnailButton(_Fanart, DoAction, Xpos, Ypos):
    
    $FanartName = _Fanart[0]
    $FanartPath = _Fanart[1]
    $imagePath = FanartPath + "/Thumbs/" + FanartName
    imagebutton idle im.Scale(imagePath, 100, 100) hover im.Scale(imagePath, 100, 100) xpos Xpos ypos Ypos focus_mask None action DoAction
    
#--------------------------------------------------------------------------------------------------------
screen fa_gallery_custom:
    tag menu
    add "img/gui/extras/FAGalleryBG.png"
    add "img/gui/extras/FanartGallery_Font.png" xalign 0.55 ypos 27
    use extra_navigation
      
    $ next_fa_page = fa_page + 1
    $ prev_fa_page = fa_page - 1
    $ next_fa_piece = fa_piece + 1
    $ prev_fa_piece = fa_piece - 1
    
    if next_fa_page >= int(len(List_FanArt)/gal_cells)-1:
        $ next_fa_page = int(len(List_FanArt)/gal_cells)-1
    if prev_fa_page < 0:
        $ prev_fa_page = 0
        
    if next_fa_piece >= len(List_FanArt)-1:
        $ next_fa_piece = len(List_FanArt)-1
    if prev_fa_piece < 0:
        $ prev_fa_piece = 0
        
    $ next_fa_piecepage = fa_page
    $ prev_fa_piecepage = fa_page
    if int(next_fa_piece%gal_rows) == 0:
      $next_fa_piecepage = next_fa_page      
    if int(fa_piece%gal_rows) == 0:
      $prev_fa_piecepage = prev_fa_page
      

    #imagebutton auto "img/gui/options/OButtons_Return_%s.png" xpos 155 ypos 718 focus_mask True action Return()
    #imagebutton auto "img/gui/MainMenu_Exit_%s.png" xpos 1670 ypos 892 focus_mask True action Quit()
    imagebutton auto "img/gui/extras/ExtraMenu_Prev_%s.png" xpos 468 ypos 540  focus_mask True action [SetVariable('fa_page', prev_fa_piecepage), SetVariable('fa_piece', prev_fa_piece), ShowMenu("fa_gallery_custom")] 
    imagebutton auto "img/gui/extras/ExtraMenu_Next_%s.png" xpos 1391 ypos 520 focus_mask True action [SetVariable('fa_page', next_fa_piecepage), SetVariable('fa_piece', next_fa_piece), ShowMenu("fa_gallery_custom")] at rot180
    
    imagebutton auto "img/gui/extras/ExtraMenu_Prev_small_%s.png" xpos 250 ypos 120  focus_mask True action [SetVariable('fa_page', prev_fa_page), SetVariable('fa_piece', prev_fa_page*gal_rows), ShowMenu("fa_gallery_custom")] 
    imagebutton auto "img/gui/extras/ExtraMenu_Next_small_%s.png" xpos 1650 ypos 100 focus_mask True action [SetVariable('fa_page', next_fa_page), SetVariable('fa_piece', next_fa_page*gal_rows), ShowMenu("fa_gallery_custom")] at rot180
    
    
    use customButton("Merona", ToggleVariable('ShowMerona'), 50, 300, 25)
    use customButton("Duran", ToggleVariable('ShowDuran'), 50, 370, 25)
    use customButton("Others", ToggleVariable('ShowOthers'), 50, 440, 25)
    use customButton("Groups", ToggleVariable('ShowGroup'), 50, 510, 25)
    
    add "img/gui/extras/FAThumbBGb.png" xpos 376 ypos 100    
    
    frame background "img/gui/extras/FABorder.png":
            xpos 700 
            yalign 0.77
            $artist[0] = List_FanArt[fa_piece][2]
            $gallery[0] = List_FanArt[fa_piece][3]
            $imagePath = List_FanArt[fa_piece][1] + "/Images/" + List_FanArt[fa_piece][0]
            vbox:
                add LiveCrop((0, 0, 600, 600), imagePath) xpos 25 ypos 25 
                add Text(_("Artist: [artist[0]]") , drop_shadow = (2, 2), drop_shadow_color = "#000000") xalign 0.5 ypos 40
                add Text(_("{a=[gallery[0]]}{color=#832627}Click to visit my Gallery!{/color}{/a}")) xalign 0.5 ypos 40
                #add Text(_("Piece: [fa_piece]") , drop_shadow = (2, 2), drop_shadow_color = "#000000") xalign 0.5 ypos 40

    $pagedisplay = fa_page+1
    text "{size=25}{color=#966935}Page: [pagedisplay]{/color}{/size}" xalign 0.55 yalign 0.25 
    
    $ThumbsPerPage = 10
    $ThumbOffset = fa_page*ThumbsPerPage
    $shownImageCount = 0
    #for i in range(ThumbOffset, ThumbOffset+ThumbsPerPage):
    for i in range(ThumbOffset, len(List_FanArt)):
      $currentPos = shownImageCount
      #if currentPos >= 10:
      #  $currentPos = 0
      #if (i < len(gallery_fa_items)):
      if (i < len(List_FanArt) and currentPos < ThumbsPerPage):
        #use thumbnailButton(FanartThumbs[i] , SetVariable('fa_piece', i), 410+125*currentPos, 130)
        if (ShouldShowImage(List_FanArt[i], "Merona") and ShowMerona) or (ShouldShowImage(List_FanArt[i], "Duran") and ShowDuran) or (ShouldShowImage(List_FanArt[i], "Others") and ShowOthers) or (ShouldShowImage(List_FanArt[i], "Lexan") and ShowOthers) or (ShouldShowImage(List_FanArt[i], "Prowen") and ShowOthers) or (ShouldShowImage(List_FanArt[i], "Nony") and ShowOthers) or (ShouldShowImage(List_FanArt[i], "Ranan") and ShowOthers) or (ShouldShowImage(List_FanArt[i], "Cimaria") and ShowOthers) or (ShouldShowImage(List_FanArt[i], "Rett") and ShowOthers) or (ShouldShowImage(List_FanArt[i], "Kreita") and ShowOthers) or (ShouldShowImage(List_FanArt[i], "Boyen") and ShowOthers) or (ShouldShowImage(List_FanArt[i], "Wriane") and ShowOthers) or (ShouldShowImage(List_FanArt[i], "Voya IV") and ShowOthers) or (ShouldShowImage(List_FanArt[i], "Drae VI") and ShowOthers) or (ShouldShowImage(List_FanArt[i], "Father") and ShowOthers) or (ShouldShowImage(List_FanArt[i], "Mother") and ShowOthers) or (ShouldShowImage(List_FanArt[i], "Group") and ShowGroup) :
          if i == fa_piece:
            add "img/gui/extras/thumbBack.png" xpos 408+125*currentPos ypos 128
          use FanartThumbnailButton(List_FanArt[i] , SetVariable('fa_piece', i), 410+125*currentPos, 130)
          $shownImageCount = shownImageCount +1
          #text "{size=25}{color=#966935}[shownImageCount]{/color}{/size}" xpos 410+125*currentPos yalign 0.25 
    
#--------------------------------------------------------------------------------------------------------
screen extra_navigation:

    add "img/gui/extras/FAGalleryBG.png"
    imagebutton auto "img/gui/options/OButtons_Return_%s.png" xpos 155 ypos 718 focus_mask True action [SetVariable('cg_page', 0), SetVariable('bg_page', 0), SetVariable('fa_page', 0), SetVariable('mr_page', 0), ShowMenu("gallery_custom")]
    imagebutton auto "img/gui/MainMenu_Exit_%s.png" xpos 1670 ypos 892 focus_mask True action Quit()
    #use customButton("CG Gallery", [SetVariable('cg_page', 0), ShowMenu("cg_gallery_custom")], 400, 810, 20)
    #use customButton("BG Gallery", [SetVariable('bg_page', 0), ShowMenu("bg_gallery_custom")], 600, 812, 20)
    #use customButton("Fan Art Gallery", [SetVariable('fa_page', 0), ShowMenu("fa_gallery_custom")], 800, 812, 20)
    #use customButton("Music Box", [SetVariable('mr_page', 0), ShowMenu("mr_gallery_custom")], 1000, 812, 20)
    
#--------------------------------------------------------------------------------------------------------
screen cg_gallery_custom:

    tag menu
    #add "img/gui/extras/FAGalleryBG.png"
    use extra_navigation
    add "img/gui/saveload/SaveLoad_BG_topbar.png" 
    use base_gallery_custom("cg")
    
#--------------------------------------------------------------------------------------------------------
screen bg_gallery_custom:
    tag menu
    #add "img/gui/extras/FAGalleryBG.png"
    use extra_navigation
    add "img/gui/saveload/SaveLoad_BG_topbar.png" 
    use base_gallery_custom("bg")
    
#--------------------------------------------------------------------------------------------------------
screen mr_gallery_custom:
    tag menu
    #add "img/gui/extras/FAGalleryBG.png"
    use extra_navigation
    add "img/gui/saveload/SaveLoad_BG_topbar.png" 
    use base_gallery_custom("mr")

#--------------------------------------------------------------------------------------------------------
screen base_gallery_custom(_galleryType="cg"):
  
    $ columns = 4
    $ rows = 2
    $y_button_offset = 200
    $x_button_offset = 300
    
    $TextColour='#966935'
    $TextColourSelected='#84b3ae'
      
    $base_gallery = g_cg
    $base_gallery_items = gallery_cg_items
    $base_page = cg_page
    $current_gallery_page_name = "cg_page"
    $current_gallery_name = "cg_gallery_custom"
    $base_gallery_isMusic = False
    
    if _galleryType == "bg":
      $base_gallery = g_bg
      $base_gallery_items = gallery_bg_items
      $base_page = bg_page
      $current_gallery_page_name = "bg_page"
      $current_gallery_name = "bg_gallery_custom"
      
    if _galleryType == "mr":
      $base_gallery = g_mr
      $base_gallery_items = gallery_mr_items
      $base_page = mr_page
      $current_gallery_page_name = "mr_page"
      $current_gallery_name = "mr_gallery_custom"
      $base_gallery_isMusic = True
      $columns = 2
      $rows = 5
      $y_button_offset = 83
      $x_button_offset = 605
    
    $base_gal_cells = rows * columns
    
    $ j = 0
    $ next_base_page = base_page + 1     
    $ prev_base_page = base_page - 1      
    #$ test1 = len(base_gallery_items)
    #$ test2 = base_gal_cells
    #$ test3 = int(test1/base_gal_cells)
    #text "[test1]/[test2] = [test3] "    
    if next_base_page > int(len(base_gallery_items)/base_gal_cells):
        $ next_base_page = int(len(base_gallery_items)/base_gal_cells)       
    if prev_base_page < 0:
        $ prev_base_page = 0
        
    $display_base_page = base_page+1
    $lastPageItems = int(len(base_gallery_items)%base_gal_cells)
    #if (lastPageItems == 0):
    #  $display_last_page = int(len(base_gallery_items)/base_gal_cells)  
    #else:
    $display_last_page = int(len(base_gallery_items)/base_gal_cells)+1    
    #text " Page [display_base_page]/[display_last_page]" xpos 1500 ypos 900 color "#31677d"
    
    
    $pageButtonXOffset = (7-display_last_page)*111
    $page1ButtonXOffset = pageButtonXOffset
    $page7ButtonXOffset = pageButtonXOffset
    #text "[pageButtonXOffset]"
    $shiftNumbers = False
    if (pageButtonXOffset < 0):
      $pageButtonXOffset = -(111/2)
      $page1ButtonXOffset = pageButtonXOffset*2
      $page7ButtonXOffset = 0
      $shiftNumbers = True
    
    if (base_page > 0):
      use customButton("Previous", [SetVariable(current_gallery_page_name, prev_base_page), ShowMenu(current_gallery_name)], 400 + page1ButtonXOffset, 205, 25)
    else:
      use customButton("Previous", [], 400 + page1ButtonXOffset, 205, 25, 1.5, '#888888')
    if (base_page < next_base_page):
      use customButton("Next", [SetVariable(current_gallery_page_name, next_base_page), ShowMenu(current_gallery_name)], 1300+(11*7), 205, 25)
    else:
      use customButton("Next", [], 1300+(11*7), 205, 25, 1.5, '#888888')
        
    if not shiftNumbers:
      if (display_last_page >= 1):
        imagebutton auto "img/gui/saveload/Buttons_Save_1_%s.png" xpos (594+(111*(1-1))+page1ButtonXOffset) ypos 189 focus_mask True action [SetVariable(current_gallery_page_name, 0)]#, ShowMenu(current_gallery_name)]
      if (display_last_page >= 2):
        imagebutton auto "img/gui/saveload/Buttons_Save_2_%s.png" xpos (594+(111*(2-1))+pageButtonXOffset) ypos 189 focus_mask True action [SetVariable(current_gallery_page_name, 1)]#, ShowMenu(current_gallery_name)]
      if (display_last_page >= 3):
        imagebutton auto "img/gui/saveload/Buttons_Save_3_%s.png" xpos (594+(111*(3-1))+pageButtonXOffset) ypos 189 focus_mask True action [SetVariable(current_gallery_page_name, 2)]#, ShowMenu(current_gallery_name)]
      if (display_last_page >= 4):
        imagebutton auto "img/gui/saveload/Buttons_Save_4_%s.png" xpos (594+(111*(4-1))+pageButtonXOffset) ypos 189 focus_mask True action [SetVariable(current_gallery_page_name, 3)]#, ShowMenu(current_gallery_name)]
      if (display_last_page >= 5):
        imagebutton auto "img/gui/saveload/Buttons_Save_5_%s.png" xpos (594+(111*(5-1))+pageButtonXOffset) ypos 189 focus_mask True action [SetVariable(current_gallery_page_name, 4)]#, ShowMenu(current_gallery_name)]
      if (display_last_page >= 6):
        imagebutton auto "img/gui/saveload/Buttons_Save_6_%s.png" xpos (594+(111*(6-1))+pageButtonXOffset) ypos 189 focus_mask True action [SetVariable(current_gallery_page_name, 5)]#, ShowMenu(current_gallery_name)]
      if (display_last_page >= 7):
        imagebutton auto "img/gui/saveload/Buttons_Save_7_%s.png" xpos (594+(111*(7-1))+page7ButtonXOffset) ypos 189 focus_mask True action [SetVariable(current_gallery_page_name, 6)]#, ShowMenu(current_gallery_name)]
    else:
      $fontsize = 50
      $_textColour = TextColour
      if base_page == 0:
        $_textColour = TextColourSelected
      else:
        $_textColour = TextColour
        
      imagebutton auto "img/gui/saveload/Buttons_empty_%s.png" xpos (594+(111*(1-1))+page1ButtonXOffset) ypos 189 focus_mask True action [SetVariable(current_gallery_page_name, 0)]
      text "{size=[fontsize]}{color=[_textColour]}1{/color}{/size}" xpos (594-15+(111*(1-1))+pageButtonXOffset) ypos 189+25
      $x = 2
      for i in range(1,display_last_page-1):
        $displayMinPage = base_page -3
        $displayMaxPage = base_page + 3
        if displayMaxPage > display_last_page-1:
          $displayMaxPage = display_last_page-1
          $displayMinPage = displayMaxPage - 6
          
        if ((i > displayMinPage and i < displayMaxPage) or ((base_page < 3) and (i <= 5))):
          if base_page == i:
            $_textColour = TextColourSelected
          else:
            $_textColour = TextColour
          imagebutton auto "img/gui/saveload/Buttons_empty_%s.png" xpos (594+(111*(x-1))+pageButtonXOffset) ypos 189 focus_mask True action [SetVariable(current_gallery_page_name, i)]
          $pageText = i+1
          text "{size=[fontsize]}{color=[_textColour]}[pageText]{/color}{/size}" xpos (594+30+(111*(x-1))+pageButtonXOffset) ypos 189+25
          #text "[base_page]" xpos (594+25+(111*(x-1))+pageButtonXOffset) ypos 189+45
          $x+=1
        
      if base_page == display_last_page-1:
        $_textColour = TextColourSelected
      else:
        $_textColour = TextColour
      imagebutton auto "img/gui/saveload/Buttons_empty_%s.png" xpos (594+(111*(7-1))+page7ButtonXOffset) ypos 189 focus_mask True action [SetVariable(current_gallery_page_name, display_last_page-1)]
      text "{size=[fontsize]}{color=[_textColour]}[display_last_page]{/color}{/size}" xpos (594+85+(111*(7-1))+pageButtonXOffset) ypos 189+25
    for gal_item in base_gallery_items:      
      $ j += 1
      $index = j
      if (index > int(columns*rows)):
        $index = j - int(columns*rows*base_page)
      $ipos = y_button_offset*int((index-1)/columns)
      $index = ((j-1)%columns) + 1
      $jpos = x_button_offset*(index-1)
        
      if j <= (base_page+1)*base_gal_cells and j>base_page*base_gal_cells: 
        if (base_gallery_isMusic):
          imagebutton auto "img/gui/saveload/SaveSlot_%s.png" focus_mask None  xpos 310+jpos ypos (321+ipos) action base_gallery.Play(gal_item)
          if base_gallery.is_unlocked(base_gallery_items[j-1]):
            $SongNameLen = len(gallery_music_text[j-1])
            $TextCenteringOffset = 260 - (10 * SongNameLen)
            if TextCenteringOffset < 0:
              $TextCenteringOffset = 0
            
            
            if (len(gallery_music_text[j-1]) > 30):
              $ songName = gallery_music_text[j-1]
              text "{size=-5}{color=[TextColour]}[songName]{/color}{/size}" xpos 335+jpos ypos (345+ipos)
            
            else:
              $_songName = gallery_music_text[j-1]
              text "{color=[TextColour]}[_songName]{/color}" xpos 335+jpos+TextCenteringOffset ypos (345+ipos)
          else:
            text "{color=[TextColourSelected]}Locked{/color}" xpos 335+jpos+200 ypos (345+ipos)
            #$_songName = gallery_music_text[j-1]
            #$_songFileName = gal_item
            #text "{color=[TextColour]}[_songName]=[_songFileName]{/color}" xpos 335+jpos+TextCenteringOffset ypos (365+ipos)
        else:
          $ buttonname = gal_item + " butt"
          add base_gallery.make_button(gal_item + " butt", gal_item + " butt", "img/gui/extras/GalleryBox_insensitive.png",  xpos=385+jpos, ypos=(330+ipos),  background=None)
          #text gal_item xpos 495+jpos ypos (430+ipos)
          imagebutton auto "img/gui/extras/GalleryBox_%s.png" focus_mask None  xpos 398+jpos ypos (332+ipos) action base_gallery.Action(gal_item + " butt")
          #text "[buttonname]"   xpos 398+jpos ypos (332+ipos)
    
#--------------------------------------------------------------------------------------------------------
screen gallery_custom:
    tag menu
    add "img/gui/extras/FAGalleryBG.png"
    imagebutton auto "img/gui/options/OButtons_Return_%s.png" xpos 155 ypos 718 focus_mask True action Return()
    imagebutton auto "img/gui/MainMenu_Exit_%s.png" xpos 1670 ypos 892 focus_mask True action Quit()
    
    #use customButton("CG Gallery", [SetVariable('cg_page', 0), ShowMenu("cg_gallery_custom")], 800, 200, 20)
    #use customButton("BG Gallery", [SetVariable('bg_page', 0), ShowMenu("bg_gallery_custom")], 800, 300, 20)
    #use customButton("Fan Art", [SetVariable('fa_page', 0), ShowMenu("fa_gallery_custom")], 800, 400, 20)
    #use customButton("Music Box", [SetVariable('mr_page', 0), ShowMenu("mr_gallery_custom")], 800, 500, 20)
    
    $TextColour='#966935'
    
    imagebutton auto "img/gui/saveload/SaveSlot_%s.png" focus_mask None  xpos 750 ypos 200 action [SetVariable('cg_page', 0), ShowMenu("cg_gallery_custom")]
    text "{color=[TextColour]}Cutscene Gallery{/color}" xpos 900 ypos 225
    
    imagebutton auto "img/gui/saveload/SaveSlot_%s.png" focus_mask None  xpos 750 ypos 350 action [SetVariable('bg_page', 0), ShowMenu("bg_gallery_custom")]
    text "{color=[TextColour]}Background Gallery{/color}" xpos 890 ypos 375
    
    imagebutton auto "img/gui/saveload/SaveSlot_%s.png" focus_mask None  xpos 750 ypos 500 action [SetVariable('mr_page', 0), ShowMenu("mr_gallery_custom")]
    text "{color=[TextColour]}Music Room{/color}" xpos 930 ypos 525
    
    imagebutton auto "img/gui/saveload/SaveSlot_%s.png" focus_mask None  xpos 750 ypos 650 action [SetVariable('fa_page', 0), ShowMenu("fa_gallery_custom")]
    text "{color=[TextColour]}Fanart Gallery{/color}" xpos 920 ypos 675
  