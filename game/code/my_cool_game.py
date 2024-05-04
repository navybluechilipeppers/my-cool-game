# Example file showing a circle moving on screen
import pygame
from pygame.locals import *
import os, sys
from inventory.inventory import Inventory


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
pygame. display. toggle_fullscreen()
pygame.display.set_caption('My super cool game')
running = True 
dt = 0
orientation = "left"

#default background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

#define some basic info
tile = 64
font = pygame.font.Font( "font.ttf", 24)
speed =20

textboxes = []
#lumi's textbox
textboxes.append(pygame.image.load(r"C:\Users\thecu\Desktop\game\textbox\lumi.png"))
textboxes.append(pygame.image.load(r"C:\Users\thecu\Desktop\game\textbox\merchant.png"))

#create the player to later add variables and animations too
class Player (pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.moving =True
        self.x = 0
        self.y = 0

        self.img = pygame.image.load( "player\playerR.png")
        self.rect = pygame.Rect(self.x,self.y,64,64)
        self.walkL = []
        self.walkL.append(pygame.image.load( "player\walkR\walk1.png"))
        self.walkL.append(pygame.image.load( "player\walkR\walk2.png"))
        self.walkL.append(pygame.image.load( "player\walkR\walk3.png"))
        self.walkL.append(pygame.image.load( "player\walkR\walk4.png"))

        self.walkF = []
        self.walkF.append(pygame.image.load( "player\walkF\walk1.png"))
        self.walkF.append(pygame.image.load( "player\walkF\walk2.png"))
        self.walkF.append(pygame.image.load( "player\walkF\walk3.png"))
        self.walkF.append(pygame.image.load( "player\walkF\walk4.png"))

        self.walkB = []
        self.walkB.append(pygame.image.load( "player\walkB\walk1.png"))
        self.walkB.append(pygame.image.load( "player\walkB\walk2.png"))
        self.walkB.append(pygame.image.load( "player\walkB\walk3.png"))
        self.walkB.append(pygame.image.load( "player\walkB\walk4.png"))     
        
        self.isAnimating = False
        self.orientation = "forward"
        self.frameCountWalkF = 0
        self.frameCountWalkB = 0
        self.frameCountWalkL = 0
        self.frameCountWalkR = 0



    def walk (self):
        #keeping track of the frames of the walking animation while going left
        # self.frameCountWalkL = 0
        # self.frameCountWalkR = 0
        # self.frameCountWalkF = 0
        # self.frameCountWalkB = 0

        #tracking if an animation is playing in order for the idle to work
        self.isAnimating = False
        #the player can't run into the npcs
        # for npc in npcs:
        #     npcRect = npc.img.get_rect(topleft = (npc.x,npc.y))
        #     pygame.draw.rect(screen,(0,0,255),npcRect)
        #     # if player.rect.colliderect(npcRect):
        #     #     self.moving = False
        #     print(npcRect)


        if keys[pygame.K_s]:
            self.img = player.walkF[int(self.frameCountWalkF)]
            self.orientation = "forward"
                  
            new_rect = self.rect.move(0, speed)
            if not any(new_rect.colliderect(npc.rect) for npc in npcs):
                self.y += speed  

            self.isAnimating = True
            self.frameCountWalkF += 0.1
            if self.frameCountWalkF > 4:
                self.frameCountWalkF = 0
            
        if keys[pygame.K_w]:
            self.img = self.walkB[int(self.frameCountWalkB)]
            self.orientation = "backward"

            new_rect = self.rect.move(0, -speed)
            if not any(new_rect.colliderect(npc.rect) for npc in npcs):
                self.y -= speed

            self.isAnimating = True
            self.frameCountWalkB += 0.1
            if self.frameCountWalkB > 4:
                self.frameCountWalkB = 0

        if keys[pygame.K_d]:
            #change the image to the left facing one
            self.img = self.walkL[int(self.frameCountWalkL)]
            self.orientation = "right"
            # if self.moving == True:
            #     self.x += speed
            self.isAnimating = True

            new_rect = self.rect.move(speed, 0)
            if not any(new_rect.colliderect(npc.rect) for npc in npcs):
                self.x += speed

            #pygame.draw.rect(screen,(0,0,255),lumi.rect)


            self.frameCountWalkL += 0.1
            if self.frameCountWalkL > 3:
                self.frameCountWalkL = 0

        if keys[pygame.K_a]:
            #change the image to the right facing one
            
            new_rect = self.rect.move(-speed,0)
            if not any(new_rect.colliderect(npc.rect) for npc in npcs):
                self.x -= speed

            self.orientation = "left"
            self.isAnimating = True
            self.img = pygame.image.load( "player\playerR.png")
            self.img = pygame.transform.flip(self.walkL[int(self.frameCountWalkR)], True, False)
            self.frameCountWalkR += 0.1
        
            if self.frameCountWalkR > 4:
                self.frameCountWalkR = 0

        if(self.isAnimating == False):
            if(self.orientation == "left"):        
                self.img = pygame.image.load( "player\playerL.png")
            if(self.orientation == "right"):
                self.img = pygame.image.load( "player\playerR.png")
            if(self.orientation == "forward"):
                self.img = pygame.image.load( "player\playerF.png")
            if(self.orientation == "backward"):
                self.img = pygame.image.load( "player\playerB.png")
        

        # player cant exit the boundary of the side of the game
        if player.x>1468:
            player.x = 1468
        if player.x<0:
            player.x = 0
        if player.y>800:
            player.y = 800
        if player.y< 0:
            player.y = 0

        self.moving = True
            
                



    def update(self):
        # update the player's rect (used for collisions )
        self.rect = pygame.Rect(self.x,self.y,64,92)

class Lumi(pygame.sprite.Sprite):
    def __init__(self):
        #variables regarding the sprite
        global speed 
        self.img = pygame.image.load( "lumi\lumi.png")
        
        self.y = 300
        self.x = 400

        self.rect = self.img.get_rect(topleft = (self.x,self.y))


        self.talkIndicator = pygame.image.load("talk indicator.png")


        #variables regarding the textbox
        #self.textboximg = pygame.image.load(r"C:\Users\thecu\Desktop\game\textbox\textbox.png")

        #textbox loader animation
        self.textboxLoader = []
        self.textboxLoader.append(pygame.image.load( r"C:\Users\thecu\Desktop\game\textbox\spinner animation\0.png"))
        self.textboxLoader.append(pygame.image.load( r"C:\Users\thecu\Desktop\game\textbox\spinner animation\1.png"))
        self.textboxLoader.append(pygame.image.load( r"C:\Users\thecu\Desktop\game\textbox\spinner animation\2.png"))
        self.textboxLoader.append(pygame.image.load( r"C:\Users\thecu\Desktop\game\textbox\spinner animation\3.png"))
        self.textboxLoader.append(pygame.image.load( r"C:\Users\thecu\Desktop\game\textbox\spinner animation\4.png"))
        self.textboxLoader.append(pygame.image.load( r"C:\Users\thecu\Desktop\game\textbox\spinner animation\5.png"))
        self.textboxLoader.append(pygame.image.load( r"C:\Users\thecu\Desktop\game\textbox\spinner animation\6.png"))
        self.textboxLoader.append(pygame.image.load( r"C:\Users\thecu\Desktop\game\textbox\spinner animation\7.png"))
        self.textboxLoader.append(pygame.image.load( r"C:\Users\thecu\Desktop\game\textbox\spinner animation\8.png"))
        self.textboxLoader.append(pygame.image.load( r"C:\Users\thecu\Desktop\game\textbox\spinner animation\9.png"))
        self.textboxLoader.append(pygame.image.load( r"C:\Users\thecu\Desktop\game\textbox\spinner animation\10.png"))
        self.textboxLoader.append(pygame.image.load( r"C:\Users\thecu\Desktop\game\textbox\spinner animation\11.png"))
        self.textboxLoaderCount = 0
        self.textboxLoaderIsAnimating = True
        self.textboxLoaderIdle = 0

        self.inputbox = pygame.image.load("textbox\inputbox.png")
        self.inputboxHover = pygame.image.load("textbox\inputbox_hover.png")

        #all variabbles related to the textbox and bliting the portrait sprites
        
        self.name = "lumi"
        self.textboxIndex = 0

    
        self.talkRangeRect = pygame.Rect(self.x-128,self.y-128,256,256)
        self.talkE = False
        self.currentDialouge = ""
        # self.script = ["shkdfd your civilization is coming to an end. sdjkhs dfkjha akshdjkhasd kjsadjnasdkahsd k jksdf jkdshf jkhsdf kjhsdfn kjhdf jashdkjn askjdh sakhdn sakdj kjasd",
        #                "It’s really a shame, truly, but such is the ways of the universe.",
        #                "It seems you have escaped.",
        #                "Would you like to work for me?"]
        self.script = [
                               ["neutral.png","it."],
                               ["wink.png", "Would you like to work for me?",[["Yes","No"],[[1,1],[0,1]]] ],
                               ["neutral.png","Great. Welcome to the team."],
                               ["neutral.png","Oh. That's a shame."]]
                                
        
        self.scriptAllWords = []
        self.messageCount = 0
        self.dialougeRect = font.render(self.currentDialouge, True, (255, 248, 189)).get_rect(bottomleft=(232, 672))
        self.isPrinting = True
        self.wordCount = 0
        self.messageCount = 0
        self.lineCounter= 0
        self.lineCounter2 = 0
    
        self.dialouge = font.render(self.script[self.messageCount][1], True, (255, 248, 189))
        self.line = 0
        self.counter = 0
        self.dialougeOutside = pygame.Rect(1131,594,74,190)

        self.k = 0

        


    def talk(self):
        #creat e the range for being close enough to lumi to talk to her
        #write the dialouge
        if player.rect.colliderect(self.talkRangeRect):
            
#265
            #if E is true continue everything
            if keys[pygame.K_e]:
                self.talkE = True
                # the player can't move while talking, no animations either
                global speed
                speed = 0
                
            if self.talkE == True:
                #if the current message isn't over,
                
                if self.counter <= len(self.script[self.messageCount][1])-1:
                    # print(self.script[self.messageCount][1])
                    # print(self.currentDialouge)
                    # print(self.counter)
                    # print(len(self.script[self.messageCount][1])-1)
                    # print(self.scriptAllWords)

                   # print(self.script[self.messageCount])
                    print(self.messageCount)
                     
                    #setup for printing
                    self.textboxLoaderIsAnimating = True
                    self.isPrinting = True
                    self.scriptAllWords = self.script[self.messageCount][1].split(' ')
                    if self.talkE == True:
                        screen.blit(pygame.image.load(self.name+"/portraits/"+self.script[self.messageCount][0]), (64, 430))
                        screen.blit(textboxes[self.textboxIndex], (64, 430))

                        #write code for the little animation

                        screen.blit(self.textboxLoader[int(self.textboxLoaderCount)],(1088,704))
                        self.textboxLoaderCount += 0.1
                        if self.textboxLoaderCount > 10:
                            self.textboxLoaderCount = 0

                        #checking if the entire string has been iterated
                        
                        #concatenate the new string
                        self.currentDialouge = (self.currentDialouge + self.script[self.messageCount][1][self.counter])
                        #screen.blit(font.render(lumi.currentDialouge, True, (255, 248, 189)),(232, 636))
                        self.counter = self.counter+1

                        #checking if the line is too long for the textbox.
                        self.dialougeRect = font.render(self.currentDialouge, True, (255, 248, 189)).get_rect(bottomleft=(232, 672))
                        #pygame.draw.rect(screen,(0,0,0),self.dialougeRect)
                        if self.wordCount >= len(self.scriptAllWords)-1:
                                #self.line = 0
                                self.isPrinting = False

                        #handling checking for the new worsd
                        if self.script[self.messageCount][1][self.counter-1] == ' ':
                            if self.line == 0:
                                #pygame.draw.rect(screen,(0,0,0),(font.render(self.scriptAllWords[self.wordCount], True, (255, 248, 189)).get_rect(bottomleft=((232+font.size(self.currentDialouge)[0]), 672))))
                                if self.dialougeOutside.colliderect(font.render(self.scriptAllWords[self.wordCount], True, (255, 248, 189)).get_rect(bottomleft=((232+font.size(self.currentDialouge)[0]), 672))) and  self.wordCount < len(self.scriptAllWords):
                                    self.lineCounter = len(self.currentDialouge)
                                    self.line += 1
                            if self.line == 1:
                                if self.dialougeOutside.colliderect(font.render(self.scriptAllWords[self.wordCount], True, (255, 248, 189)).get_rect(bottomleft=((232+font.size(self.currentDialouge[self.lineCounter:])[0]), 708))):
                                    self.lineCounter2 = len(self.currentDialouge)
                                    self.line += 1
                            self.wordCount += 1
                            
                    # render the text based on the line
                        if self.line == 0:
                            screen.blit(font.render(self.currentDialouge, True, (255, 248, 189)),(232, 636))

                        elif self.line == 1:
                            screen.blit(font.render(self.currentDialouge[:self.lineCounter], True, (255, 248, 189)),(232, 636))
                            screen.blit(font.render(self.currentDialouge[self.lineCounter:], True, (255, 248, 189)),(232, 672))
                            
                        elif self.line == 2:
                            screen.blit(font.render(self.currentDialouge[:self.lineCounter], True, (255, 248, 189)),(232, 636))
                            screen.blit(font.render(self.currentDialouge[self.lineCounter:self.lineCounter2], True, (255, 248, 189)),(232, 672))
                            screen.blit(font.render(self.currentDialouge[self.lineCounter2:], True, (255, 248, 189)),(232, 708))

                    

                if self.isPrinting == False:
                    screen.blit(pygame.image.load(self.name+"/portraits/"+self.script[self.messageCount][0]), (64, 430))
                    screen.blit(textboxes[self.textboxIndex], (64, 430))

                    #allow the previous animation to finish
                    if self.textboxLoaderCount < 11:
                        self.textboxLoaderCount += 0.09
                        screen.blit(self.textboxLoader[int(self.textboxLoaderCount)],(1088,704))
                    if self.textboxLoaderCount >= 11:
                        self.textboxLoaderIsAnimating = False
                    
                    #when it's done, play the waiting animation
                    if self.textboxLoaderIsAnimating== False:
                         self.textboxLoaderIdle += 0.06
                         if int(self.textboxLoaderIdle) == 0:
                             screen.blit(self.textboxLoader[0],(1088,704))
                         if int(self.textboxLoaderIdle) == 1:
                             screen.blit(self.textboxLoader[0],(1088,694))
                         if int(self.textboxLoaderIdle) == 2:
                             self.textboxLoaderIdle = 0
                        

                    #one bilt for each line of code
                    if self.line == 0:
                            screen.blit(font.render(self.currentDialouge, True, (255, 248, 189)),(232, 636))

                    elif self.line == 1:
                            screen.blit(font.render(self.currentDialouge[:self.lineCounter], True, (255, 248, 189)),(232, 636))
                            screen.blit(font.render(self.currentDialouge[self.lineCounter:], True, (255, 248, 189)),(232, 672))
                            
                    elif self.line == 2:
                            screen.blit(font.render(self.currentDialouge[:self.lineCounter], True, (255, 248, 189)),(232, 636))
                            screen.blit(font.render(self.currentDialouge[self.lineCounter:self.lineCounter2], True, (255, 248, 189)),(232, 672))
                            screen.blit(font.render(self.currentDialouge[self.lineCounter2:], True, (255, 248, 189)),(232, 708))

                    #function used for resetting everything
                    def resetAll():
                        #start the next message
                        self.textboxLoaderIsAnimating = True
                        self.messageCount += 1
                                #reset everything
                        self.counter = 0
                        self.currentDialouge = ""
                        self.wordCount = 0
                        self.line = 0


                    if len(self.script[self.messageCount]) < 3:

                        if event.type == pygame.MOUSEBUTTONDOWN:
                                print("hellooooo")
                                resetAll()

                                #if it's the last message in the interaction, close everything
                                if self.messageCount==len(self.script):
                                    print(self.messageCount)
                                    self.talkE = False       
                                    self.messageCount = 0   

                                #reset the script for talking to her again
                                    ## REDO THIS CODE LATER - WONT WORK IN THE FUTURE... -------------------------------------------------
                                    if self.name == "lumi":
                                        self.script = [
                                        ["neutral.png","it seems you have escaped."],
                                        ["wink.png", "Would you like to work for me?",[["Yes","No"],[[1,1],[0,1]]] ],
                                        ["wink.png","Great. Welcome to the team."],
                                        ["neutral.png","Oh. Cool. ksjdfkjsdf ksjdfjnsdf jsdhfsdf"]]
                
                    #EVERYTHING IN HERE IS RELATED TO THE INPUT FUNCTION
                    else:
                        self.input1 = font.render(self.script[self.messageCount][2][0][0],True,(255, 248, 189))
                        self.input2 = font.render(self.script[self.messageCount][2][0][1],True,(255, 248, 189))
                        self.inputBox1 = pygame.Rect(550,758,268, 84)
                        self.inputBox2 = pygame.Rect(828,758,268, 84)

                        mouseX,mouseY = pygame.mouse.get_pos()


                        #hovering for the first input box
                        if self.inputBox1.collidepoint(mouseX, mouseY):
                            #change the colour of the first input box
                            screen.blit(self.inputboxHover, (550,758))
                            screen.blit(self.input1,(655, 762))
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                self.k= self.k+ 1
                               
                                for i in range(self.script[self.messageCount][2][1][0][1]):
                                    del self.script[self.messageCount+self.script[self.messageCount][2][1][0][0]+1]
                                

                                resetAll()

                                    #self.messageCount+self.script[self.messageCount][2][1][0][0]+1
                        else:
                            #otherwise leave it
                            screen.blit(self.inputbox, (550,758))
                            screen.blit(self.input1,(655, 762))

                        #govering for the second input box
                        if self.inputBox2.collidepoint(mouseX, mouseY):
                            screen.blit(self.inputboxHover, (828,758))
                            screen.blit(self.input2,(88, 762))

                            if event.type == pygame.MOUSEBUTTONDOWN:
                                self.k= self.k+ 1
                            
                                for i in range(self.script[self.messageCount][2][1][1][1]):
                                    del self.script[self.messageCount+self.script[self.messageCount][2][1][1][0]+1]

                                resetAll()
                            #["wink.png", "Would you like to work for me?",[["Yes","No"],[[1,2],[0,1]]]],
                        
                        else:
                            screen.blit(self.inputbox, (828,758))
                            screen.blit(self.input2,(828, 762))




                        

            if self.talkE ==False:
                    #if the user is not pressing e, tell them they can to talk to lumi
                screen.blit(self.talkIndicator,(self.x+50,self.y+20))
                speed = 20
        
    def update(self):
        pass

#the merchant has the same code as lumi, but all that is different is defined as an overwritten variable in the init
class Merchant(Lumi):
    def __init__(self):
        super().__init__()
        self.x = 892
        self.y = 138
        self.img = pygame.image.load( "merchant\merchantSprite.png")
        self.rect = self.img.get_rect(topleft = (self.x,self.y))

        self.talkRangeRect = pygame.Rect(self.x-128,self.y-128,256,256)

        self.name = "merchant"
        self.textboxIndex = 1


        self.script = [["neutral.png","heyyyyy its the merchant i have my ownnnn dialouge :3"],
                       ["happy.png","WHATS UPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP PPPPPPPPPPPPp"],
                       ["neutral.png","THREE LINES KSJDFKJDSFNKDSJFN DSKJFNKDSNF THREE LINES KJDSFDDSKJFHDSF KSDJFNKJDSNF kSJdnfjnsdf kjsnfka aoawiwj asjsd skjdhfjsdf sdjfhhjsdfjkad"]]

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super(Coin, self).__init__()
        self.x = 500
        self.y = 200
        self.img = pygame.image.load( "coin.png")
        self.rect = pygame.Rect(self.x,self.y,64,64)
        self.collectSound =  pygame.mixer.Sound( "coin noise.wav")
        self.moneyCount = 0
    def update(self):
        self.moneyCount = self.moneyCount
        pass

class Seed(pygame.sprite.Sprite):
    def __init__(self):
        super(Seed, self).__init__()
        self.x = 200
        self.y = 300
        self.img = pygame.image.load( "item icons\seed packet.png")
        self.rect = pygame.Rect(self.x,self.y,64,64)
    def update(self):
        for seed in seeds:
            screen.blit(self.img, (self.x,self.y))
            if player.rect.colliderect(self.rect):
                seeds.remove(seed)
                inventory.inventory.append([self.img,1])
        
        


#keeping track of the frames of the walking animation while going left
frameCountWalkL = 0
frameCountWalkR = 0
frameCountWalkF = 0
frameCountWalkB = 0

#tracking if an animation is playing in order for the idle to work
isAnimating = False


#create object isntances for the classes
player = Player()
coin = Coin()
seed = Seed()


lumi = Lumi()
merchant = Merchant()
inventory = Inventory()

npcs = []
npcs.append(lumi)
npcs.append(merchant)

#sprite coin group to keep them all together
coins = pygame.sprite.Group()
coins.add(coin)

seeds = pygame.sprite.Group()
seeds.add(seed)

allSprites = pygame.sprite.Group()
allSprites.add(coins,player)
#Keep the npcs together
#add code later

#code will run this when a coin and the player collide 
# def coinCollect():
#     coll = pygame.sprite.spritecollide(player.playerRect,coins,True)
#     print(player.rect)
#     if coll:
#         print("coin crash!")
#         sys.exit()

while running:
    #put the background on screen

    screen.blit(background, (0, 0))
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
            mouseX, mouseY = pygame.mouse.get_pos()

        
    #define controls

    #set default so that it resets
    isAnimating = False

    keys = pygame.key.get_pressed()
    general_event_list = pygame.event.get()

    player.walk()
    
    coin.update()
    player.update()
    seed.update()


    #check if the player and the coin has touched
    # coinCollect()
    #put the objects on screen
    for coin in coins:
        screen.blit(coin.img, (coin.x, coin.y))
    # screen.blit(coin.img, (coin.x,coin.y))
    screen.blit(player.img, (player.x,player.y))
    screen.blit(font.render('Coins: '+ str(coin.moneyCount), True, (0,0,0)),(1100,500))
    screen.blit(lumi.img, (lumi.x,lumi.y))
    screen.blit(merchant.img,(merchant.x,merchant.y))
    #pygame.draw.rect(screen, (0,0,0), pygame.Rect(128, 576, 1280, 256))

   #check if coins are on screen
    for coin in coins:
        if player.rect.colliderect(coin.rect):
            coins.remove(coin)
            coin.moneyCount = coin.moneyCount + 1
            pygame.mixer.Sound.play(coin.collectSound)
            pygame.mixer.music.stop()
    
    #check if player can talk to lumi & run that script
    lumi.talk()
    merchant.talk()

    if (lumi.talkE & merchant.talkE) == False:
        inventory.drawInventory()
        inventory.drawIcons()
    else:
        pass

    

    # -------------------------------- DEBUGGING ZONE! WEAR PERSONAL EQUIPMENT! :3-------------------------------------------------------------------
    #pygame.draw.rect(screen,(0,0,0),lumi.dialougeOutside)
    #print(merchant.talkRangeRect)
    #print(player.rect.colliderect(merchant.talkRangeRect))
    # pygame.draw.rect(screen,(0,0,255),merchant.talkRangeRect)
    # pygame.draw.rect(screen,(255,0,0),lumi.talkRangeRect)


    # show everything] andupdate the screen
    pygame.display.flip()
    clock.tick(60)