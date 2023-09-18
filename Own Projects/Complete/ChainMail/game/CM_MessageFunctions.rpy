init python:
  #email addresses
  
  Robert_email = "Robert Forrest <r.forrest@bvu.edu>"  
  David_email = "Dave Hudson <d.hudson@bvu.edu>"  
  
  #Extras
  Belle_email = "Belle Franks <b.franks@bvu.edu>"  
  Anne_email = "Anne Forrest <annabanana99@gmail.com>" 
  Derek_email = "Derek Rath <d.rath@bvu.edu>" 
  
  #Teachers
  Bannister_email = "Dr. Laith Bannister <l.bannister@bvu.edu>" 
  Marshall_email = "Dr. Anisa Marshall <a.marshall@bvu.edu>" 
  
  #IT dept
  Erin_email = "Erin Haines <a.marshall@bvu.edu>" 
  IT_email = "IT DEPARTMENT <no.reply@bvu.edu>" 
  Everyone_email = "All Students <students@bvu.edu>" 
  
  
  Simone_email = "Simone West <swest@fspub.com>"  
  Solomon_email = "Solomon Fox <sfox@fspub.com>"
  Milo_email = "Milo Matthews <mmathews@fspub.com>"
  Joel_email = "Joel Cabrera <jcabrera@fspub.com>"  
  Trina_email = "Trina Luong <trinabee@pmail.com>"
  
  ######################################################################

  ######################################################################
  #---------------------------------------------------------------------
  def GetAddressFromSender(sender):
    #address = "noreply@fspub.com"
    address = sender
    
    if sender == "Bob" or sender == "Robert":
      address = Robert_email
    if sender == "Dave" or sender == "David":
      address = David_email
    if sender == "Belle":
      address = Belle_email
    if sender == "Anne":
      address = Anne_email
    if sender == "Derek":
      address = Derek_email
      
    if sender == "Bannister":
      address = Bannister_email
    if sender == "Marshall":
      address = Marshall_email
    if sender == "Erin":
      address = Erin_email
    if sender == "IT":
      address = IT_email
    if sender == "Everyone":
      address = Everyone_email
    
    if sender == "Simone":
      address = Simone_email
    if sender == "Solomon":
      address = Solomon_email
    if sender == "Milo":
      address = Milo_email
    if sender == "Joel":
      address = Joel_email
    if sender == "Trina":
      address = Trina_email
      
    return address  
      
  #---------------------------------------------------------------------
  