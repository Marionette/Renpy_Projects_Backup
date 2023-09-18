
init python:
    class NonUniformRandom(object):
        def __init__(self, list_of_values_and_probabilities):
            """
            expects a list of [ (value, probability), (value, probability),...]
            """
            self.the_list = list_of_values_and_probabilities
            self.the_sum = sum([ v[1] for v in list_of_values_and_probabilities])

        def pick(self):
            """
            return a random value taking into account the probabilities
            """
            import random
            r = random.uniform(0, self.the_sum)
            s = 0.0
            for k, w in self.the_list:
                s += w
                if r < s: return k
            return k
            
    items = [   ["Common Item", 9],
                ["Uncommon Item", 7],
                ["Rare Item", 5],
                ["Epic Item", 3],
                ["Legendary Item", 1]]
         
         
init:
    # initialize our random picker with the options and their likelyhood of being selected:
    define n = NonUniformRandom( items )
    
       
label lbl_itemPickingTest: 
    $c=0
    $u=0
    $r=0
    $e=0
    $l=0

label lbl_itemPickingTest_1:
    "Let me find something..."
    $itemFound = n.pick()
    if itemFound == "Common Item":
        $c=c+1
    if itemFound == "Uncommon Item":
        $u=u+1
    if itemFound == "Rare Item":
        $r=r+1
    if itemFound == "Epic Item":
        $e=e+1
    if itemFound == "Legendary Item":
        $l=l+1
    
    "So far i have I found [c] Common, [u] uncommon, [r] Rare, [e] Epic and [l] Legendary items"
    menu:
      "Keep Looking":        
        jump lbl_itemPickingTest_1
      "Stop Looking":
        pass
        
    return