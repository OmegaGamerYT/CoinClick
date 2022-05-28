import sys
import time
import math
#Settings
#important will break game if changed
creator = 'Omega'
loop = 1
#defining variable
Bitches = 0
Coins = 0
Gain = 1
Saving = 0
Rebirth = 0
shop = 'null'
Rebirth_ = Rebirth + 1
URebirth = 0
URebirth_ = URebirth + 1
file = open('Settings.txt')
content = file.readlines()
ShowGain = int(content[0])
ShowTotal = int(content[1])
time.sleep(1)
Buy1 = 5 + Gain - 1
Buy2 = Gain * 500
#-------------------------------------
print('Made by: ' + str(creator))
print('Version 1.1')

if creator == 'Omega':
  time.sleep(2)
else:
  print('You tryna steal my game? Yeah look at you bozo. You showed your mom this and said "LoOk I cAn CoDe" after changing the creator? Goofy. Im gonna close this game now.')
  time.sleep(15)
  sys.exit()
  time.sleep(1)
print ('Type "controls" to view controls')
while loop == 1:
  Buy2 = int(Gain) * 500
  Buy1 = int(Gain) - 1 + 5
  BuyURebirth = URebirth_ * 1000000
  BuyRebirth = Rebirth_ * 10000
  #Game Starts
  click1 = input()
  #Click for coins
  if click1 == '':
    Coins = URebirth_ * Rebirth_ * (Coins + Gain)
    if ShowGain == '1':
      print('+' + str(Gain))
    if ShowTotal == '1':
      print('Coins:')
  else:
    #controls
    if click1 == 'controls':
                print('')
                print('Type ENTER to get coins. Type "Shop" to open shop. Type "Rebirth" to open Rebirth menu. Type "Save" to save your progress or type "Load" if you have saved before.')
    else:       
#load
        if click1 == 'load':
              print('Loaded!') 
              file = open('game.save')
              content = file.readlines()
              Coins = int(content[0])
              Gain = int(content[1])
        else:   
#save 
            if click1 == 'save':
              print('Save!')
              with open('game.save', 'w') as f:
                f.write(str(Coins) + '\n' + str(Gain))
            else:

              if click1 == 'shop':
                print('')
                print('Shop: (Type the number next to the item to purchase or 0 to exit!)')     
                print('')
                print('Coins: ' + str(Coins))     
                print('')
                print('(1) Increase coin gain by 1 | Cost: ' + str(Buy1)) 
                print('')
                print('(2) Multiply coin gain by 2 | Cost: ' + str(Buy2)) 
                print('')
                shop1 = input('What do you want to by? ')
                if shop1 == '0':
                  print('')
                else:
                  if shop1 == '':
                    print('')
                  else: 
                    if shop1 == '1':
                      if Coins < 5:
                        print('Not enough coins')
                      else:
                        Gain = Gain + 1
                        Coins = Coins - Buy1
                      if shop1 == '2':
                        if Coins < Buy2 - 1:
                          print('Not enough coins')
                        else:
                          Gain = Gain + Gain
                          Coins = Coins - Buy2 
              else:  

                  print('')
                  