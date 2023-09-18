
# Call this label to start the minigame
label trading_start():
    $current_buyer = 0
    $soldPrice = 0
    $totalMade = 0
    $CustomerCount = 3
    $CUSTOMER_LIST = GenerateCharacters(CustomerCount)
    $cust = CUSTOMER_LIST[0]
    #scene trading_bg
    show jonah bored at left
    show mallory panic at right
    jon "Looks like I'm all set up to start trading."
    #show screen minigame_trade_status
    while current_buyer < len(CUSTOMER_LIST):
        call start_trade()
        #if minigame_trades >= 5:
        #    #minigame_player "Oh, I'm out of things to trade..."
        #    #jump minigame_finished
        #    return
        $current_buyer = current_buyer+1
        $totalMade = totalMade + soldPrice;
    #minigame_player "No one else seems to be coming. I guess that was everyone I could trade with..."
    #jump minigame_finished
    jon "Well looks like i made [totalMade] gold."
    jon "Not too shabby."
    return


#label trading_finished():
    #return


label start_trade():

    $cust = CUSTOMER_LIST[current_buyer]
    $Customer_Name = CUSTOMER_LIST[current_buyer].Name
    customer "My name is [cust.Name]. I am a [cust.Gender] [cust.Type]. I have [cust.Funds] gold to spend. I like [cust.Likes] and i dislike [cust.Dislikes]."
    jon "Welcome! Does anything I have here catch your eye?" 
    
label trade_setPrice():
    call screen sale_screen()
    $offer = int(_return)
    jon "How does [offer] sound?"
    
    if offer > cust.Funds:    
      customer "I cant afford that. [cust.Funds]"
      menu:
        "The customer says they can't afford that price."
        "Best i can do is...":
          jump trade_setPrice
        "You're wasting my time here.":
          $soldPrice = 0
          customer "How rude."
          "The customer leaves without buying anything."
          return
    
    if cust.Mood == "V.Unhappy":
      customer "Theres no way I'd pay that." 
      "The customer leaves without buying anything."
      return

    if cust.Mood == "V.Happy" or offer < cust.Funds/3:
      customer "I'll Take it!"
      $soldPrice = offer    
      e "Sold for [soldPrice] gold!"
      return

    
    if offer > cust.Funds/2:
      customer "Hmm... can you go a little lower?"    
      menu:
        "Best i can do is...":
          jump trade_setPrice
        "You're wasting my time here.":
          $soldPrice = 0
          customer "How rude."
          "The customer leaves without buying anything."
    
    if offer > cust.Funds/1.7:
      $counter_offer = int(cust.Funds/1.7)
      customer "Hmm... How about [counter_offer] instead?"
    
      menu:
        "Sell for [counter_offer]?"
        "Sold!":
          $soldPrice = counter_offer
          e "Sold for [soldPrice] gold!"
          return
        "Best i can do is...":
          jump trade_setPrice
        "You're wasting my time here.":
          $soldPrice = 0
          customer "How rude."
          "The customer leaves without buying anything."
    
    return