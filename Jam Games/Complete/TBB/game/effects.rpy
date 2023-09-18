# Effects #
label splashscreen:
    if not persistent.Intro:
        scene bg black
        "A Fervent Game"
        $ persistent.intro = True
return

init:
    $ persistent.intro = False
    

#Switches Chapter 1 - Good Path #############################################################################################
########################################################################################################################
init:
    
#First Time Talking to Characters
    $ FirstTimeNue = False
    $ FirstTimeDeis = False
    $ FirstTimeMorco = False
    $ FirstTimeMary = False
    $ FirstTimeEdelia = False
    $ FirstTimeMogu = False
        
# Talking Switches
    $ talkedtonueDeis = False
    
    $ talkedtodeis = False
    $ talkedtomorco = False
    $ talkedtoMary = False
    
# Event Switches

# Event # 1 - Mogu's Food
    $ helpMogufindfood = False
    $ Moguhungry = False
    $ MoguhungryNue = False
    $ MoguhungryDeis = False
    $ Deishasfood = False
    $ DeishasfoodNue = False
    $ Deislikesbooks = False
    $ DeislikesbooksEdelia = False
    $ DeishasfoodMogu = False
    $ bookforDeis = False
    $ lookitsabookDeis = False
    $ lietoMogu = False
    $ mogulovesyou = False
    $ Deislikesyou = False
    
    $ foodforMoguNue = False
    $ foodforMoguMogu = False
    
# EdeliaTimer
init:
    $ ede_timer_range =  0
    $ ede_timer_jump = 0
    $ Edelialeft = False
    $ waitedforEdeliadone = False
    $ waitedforEdeliaseen = False
    $ Edeliaback = False
    
# Event 2 - Mary and the Horn
    $ Maryknowsweapon = False
    $ MaryknowsweaponMary = False
    $ Marygivesunicornhorn = False
    $ Marylikesyou = False
    $ bookforDeisMary = False
    
#Items Chapter 1 - Good Path    
    $ book = False
    $ foodforMogu = False
    $ unicornhorn = False

    $ librarypathclear = False
    $ chap1done = False
#Switches Chapter 1 - BAD Path ###########################################################################################
##################################################################################################################

init:
    $ ignoreMogu = False
    $ puzzlegameforhorn = False
    $ puzzlegameforhornMorco = False
    $ puzzlegameforhorndone = False
    
    $ answertohornpuzzle = False
    $ Maryhatesyou = False
    $ answertohornpuzzleMary = False
    $ liedtoMogu = False
    $ lietoMogu = False
    $ lietoMoguseen = False
    $ liedtoMoguseen = False
    
# Items
    $ ramhorn = False
    $ mcramhorns = False
    

#Chapter 2 - Good Path ###########################################################################################
##################################################################################################################


init:
# Event 1 - Nue's Tail / Mask   

    $ FirstTimeNuemask = False
    $ helpNuefindmask = False
    
    $ aboutNuetailDeis = False
    $ aboutNuetailMorco = False
    $ aboutNuetailMary = False
    $ aboutNuetailMogu = False
    
    $ aboutNuemaskDeis = False
    $ aboutNuemaskMorco = False
    $ aboutNuemaskMary = False
    $ aboutNuemaskMogu = False
    
    $ Nuecluefromthestars = False
    
    $ brokenmask = False
    $ brokenmaskNue = False
    $ brokenmaskDeis = False
    $ Nuetalkingtoyou = False
    $ Deistransmutingmask = False
    $ DeistransmutingmaskNue = False
    $ Nueisyourfriend = False
    $ Deistransmutingmaskdone = False
    
    $ Nuenewmask = False
    $ NuenewmaskNue = False
    $ Nueishappy = False
    
# Event 2 - Make the Stars laugh
    $ FirstTimestars = False
    $ starsaresmart = False
    $ starscanhelpyoufindstuff = False
    $ findstarjoke = False
    $ madestarslaugh = False
    
    $ starjokeNue = False
    $ Nuehasabadjoke = False
    $ Nuehasastarjoke = False
    $ Marygoodwithjokes = False
    $ NuehasastarjokeMogu = False
    $ starjokeDeis = False
    $ starjokeMary = False
    $ starjokeMorco = False
    $ starjokeDeisMogu = False
    
    $ Maryhasastarjoke = False
    $ starjokeMaryMogu = False
    
    $ starsarehappy = False
    $ starsaregoodmood = False
    $ starsareamused = False
    
    $ Nuecluefromstars = False
    
    $ Deishasajoke = False
    $ DeishasajokeMogu = False
    $ Deishasajoke_seen = False

# Event 3 - Mary's Memory
    $ Maryissad = False
    $ helpMaryfindstory = False
    
    $ MarystoryNue = False
    $ MarystoryDeis = False
    $ MarystoryMorco = False
    $ MarystoryMogu = False
    
    $ DeisknowsMarystory = False
    $ DeisasksMaryclue = False
    $ DeisasksMaryclueMary = False
    
    $ Maryclue = False
    $ MaryclueDeis = False
    $ Marycluefromstars = False
    $ MarycluefromstarsDeis = False

    $ foundMarystory = False
    $ foundMarystoryMary = False
    $ foundMarystoryMorco = False
    $ Marystorybook = False
    
    $ Maryishappy = False
    
    
# Random Event - Flower
    $ happystartears = 0
    $ happystartears_count = 0
    $ happystartears_c = False
    $ happystartears_enough = False
    
    $ wateredtheplant = 0
    $ wateredtheplanttwice = False
    
    $ keytoflowerroom = False
    $ FirstTimeflowerroom = False

    $ goodpathdone = False
    $ Morcotalkstoyou = False
    $ Manticoreawake = False
    $ Manticoreawakedone = False
    
    $ Ponchuiswhizzingabout = False
    
    
# Random Event - Book
    $ readabook = 0
    $ readabookcount = 0
    $ read2books = False
    $ read2books_seen = False
    
    # Random Event - Ponchu 
    $ Ponchuiswhizzingabout = False

# Deis Counter #############
init:
    $ deis_timer_range =  0
    $ deis_timer_jump = 0
    $ waitforDeis = False
    $ waitedforDeisdone = False
    $ waitedforDeisseen = False
    
#Chapter 2 - Bad Path ###########################################################################################

init:
    $ Nuetail = False
    $ Nueignoresyou = False
    $ aboutNuetailbook = False
    $ Nuetailcut = False
    $ NuetailcutDark = False
    $ Nuehatesyou = False
    
    $ Youwantatail = False
    $ YouwantatailDeis = False 
    $ YouwantatailMorco = False
    $ YouwantatailMary = False
    
    $ killedastar = False
    $ killedastarDark = False
    $ Moguhatesyou = False
    
    $ Nuesecret = False
    $ NuesecretNue = False
    $ badpathdone = False
    
    $ killedMorco = False
    $ Morcowingscut = False
    $ killedMorcoDark = False
    
    $ mctail = False
    $ mcwings = False
