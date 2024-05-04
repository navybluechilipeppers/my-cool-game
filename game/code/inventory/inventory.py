import pygame
from pygame.locals import *
from PIL import Image, ImageEnhance
#from item_data import Seeds


screen = pygame.display.set_mode((1920, 1080))
#itemData = Seeds()

class Inventory():
    def __init__(self):
        self.inventory = []
        self.inventoryBoxRect = []
        self.slotSpacing = 82
        self.inventoryTileOffset = 128
        self.inventorybox_general = pygame.Rect(128,768,778-125,64)
        self.savedCoords = (0,0)
        self.savedCoordsHover = (0,0)

        self.slotSelected = -1

        self.inventoryTile = pygame.image.load("inventory pictures\inventory tile.png")
        self.inventoryTileHover = pygame.image.load("inventory pictures\inventory tile hover.png")

        self.invSlot1 = self.inventoryTile.get_rect(bottomleft = (128,768+72))
        self.invSlot2 = self.inventoryTile.get_rect(bottomleft = (210,768+72))
        self.invSlot3 = self.inventoryTile.get_rect(bottomleft = (292,768+72))
        self.invSlot4 = self.inventoryTile.get_rect(bottomleft = (374,768+72))
        self.invSlot5 = self.inventoryTile.get_rect(bottomleft = (456,768+72))
        self.invSlot6 = self.inventoryTile.get_rect(bottomleft = (538,768+72))
        self.invSlot7 = self.inventoryTile.get_rect(bottomleft = (620,768+72))
        self.invSlot8 = self.inventoryTile.get_rect(bottomleft = (702,768+72))


        self.inventoryBoxRect.append(self.invSlot1)
        self.inventoryBoxRect.append(self.invSlot2)
        self.inventoryBoxRect.append(self.invSlot3)
        self.inventoryBoxRect.append(self.invSlot4)
        self.inventoryBoxRect.append(self.invSlot5)
        self.inventoryBoxRect.append(self.invSlot6)
        self.inventoryBoxRect.append(self.invSlot7)
        self.inventoryBoxRect.append(self.invSlot8)

        self.seedsImg = pygame.image.load("item icons\seed packet.png")



    def drawInventory(self):
        mouseX,mouseY = pygame.mouse.get_pos()
        #the general box drawing to check if its drawn correctly
        #pygame.draw.rect(screen, (0,0,255), self.inventorybox_general)
        

        for i in range(8):
           
            if (i == self.slotSelected):
                screen.blit(self.inventoryTile,(self.inventoryTileOffset+self.slotSpacing*i,758))
            else:
                screen.blit(self.inventoryTile,(self.inventoryTileOffset+self.slotSpacing*i,768))
            
            
            #print(self.slotSelected)
            # pygame.draw.rect(screen,(0,0,255),self.invSlot1)
            # pygame.draw.rect(screen,(0,0,255),self.invSlot2)
            # pygame.draw.rect(screen,(0,0,255),self.invSlot3)
            # pygame.draw.rect(screen,(0,0,255),self.invSlot4)
            # pygame.draw.rect(screen,(0,0,255),self.invSlot5)
            # pygame.draw.rect(screen,(0,0,255),self.invSlot6)
            # pygame.draw.rect(screen,(0,0,255),self.invSlot7)
            # pygame.draw.rect(screen,(0,0,255),self.invSlot8)

        
        
            # if (self.inventoryBoxRect[i].collidepoint(mouseX,mouseY)):
                
            #     screen.blit(self.inventoryTileHover,(self.inventoryTileOffset+self.slotSpacing*i,768))
            # else:
            #     screen.blit(self.inventoryTile,(self.inventoryTileOffset+self.slotSpacing*i,768))

                # for event in pygame.event.get():
                #     if event.type == pygame.MOUSEBUTTONDOWN:
                #         self.slotSelected= i

        if (self.inventorybox_general.collidepoint(mouseX,mouseY)):
            for event in pygame.event.get():
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print(self.savedCoords)
                        print(self.slotSelected)
                        self.savedCoords = (mouseX,mouseY)
                            
                        if(128 < self.savedCoords[0] < 210):
                            self.slotSelected = 0
                        elif(210< self.savedCoords[0] <292):
                            self.slotSelected = 1
                        elif(292< self.savedCoords[0] <374):
                            self.slotSelected = 2
                        elif(374< self.savedCoords[0] <456):
                            self.slotSelected = 3
                        elif(456< self.savedCoords[0] <538):
                            self.slotSelected = 4
                        elif(538< self.savedCoords[0] <620):
                            self.slotSelected = 5
                        elif(620< self.savedCoords[0] <702):
                            self.slotSelected = 6
                        elif(702< self.savedCoords[0] <702+82):
                            self.slotSelected = 7

            

            

    def drawIcons(self):
        for i in range(len(self.inventory)):
           
            screen.blit(self.inventory[i][0],(self.inventoryTileOffset+self.slotSpacing*i,760))




       