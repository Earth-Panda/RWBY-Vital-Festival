import pygame
from time import sleep
pygame.init()

win = pygame.display.set_mode((1244,700))
                              #, pygame.FULLSCREEN)
#name of the window
pygame.display.set_caption("RWBY: waifu wars")

#Dont write pygame.image.load 20000000 times
pil = pygame.image.load

#Player controls
print('welcome to RWBY: Vital Festival this game is the clash between the best huntsmen and huntresses in all of reminant:\nThe contols are:\nRuby: \n\tJump=W \n\tRight=A \n\tLeft=D \n\tRanged=E \n\tAttack=SPACE\n\nWiess: \n\tJump=U \n\tRight=H \n\tLeft=K \n\tRanged=I \n\tAttack=LEFTALT') 

#Animations in lists
RubyWalkR = [pil('RubyWalkRight0.png'), pil('RubyWalkRight1.png'), pil('RubyWalkRight2.png'), pil('RubyWalkRight3.png'), pil('RubyWalkRight4.png'), pil('RubyWalkRight5.png'), pil('RubyWalkRight6.png'), pil('RubyWalkRight7.png')]

RubyWalkL = [pil('RubyWalkLeft0.png'), pil('RubyWalkLeft1.png'), pil('RubyWalkLeft2.png'), pil('RubyWalkLeft3.png'), pil('RubyWalkLeft4.png'), pil('RubyWalkLeft5.png'), pil('RubyWalkLeft6.png'), pil('RubyWalkLeft7.png')]

RubyJumpR = [pil('RubyJump00.png'), pil('RubyJump01.png'), pil('RubyJump02.png'), pil('RubyJump03.png'), pil('RubyJump04.png'), pil('RubyJump05.png'), pil('RubyJump06.png'), pil('RubyJump07.png'), pil('RubyJump08.png'), pil('RubyJump09.png')]

RubyJumpL = [pil('RubyJumpL00.png'), pil('RubyJumpL01.png'), pil('RubyJumpL02.png'), pil('RubyJumpL03.png'), pil('RubyJumpL04.png'), pil('RubyJumpL05.png'), pil('RubyJumpL06.png'), pil('RubyJumpL07.png'), pil('RubyJumpL08.png'), pil('RubyJumpL09.png')]

RubyRangedR = [pil('ShootingRuby0.png'), pil('ShootingRuby1.png'), pil('ShootingRuby2.png'), pil('ShootingRuby3.png'), pil('ShootingRuby4.png'), pil('ShootingRuby5.png')]

RubyRangedL = [pil('ShootingRubyL0.png'), pil('ShootingRubyL1.png'), pil('ShootingRubyL2.png'), pil('ShootingRubyL3.png'), pil('ShootingRubyL4.png'), pil('ShootingRubyL5.png')]

RubyAttackR = [pil('RubyAttack0.png'),pil('RubyAttack1.png'),pil('RubyAttack2.png'),pil('RubyAttack3.png'), pil('RubyAttack4.png'),pil('RubyAttack5.png')]

RubyAttackL = [pil('RubyAttackL0.png'),pil('RubyAttackL1.png'),pil('RubyAttackL2.png'),pil('RubyAttackL3.png'), pil('RubyAttackL4.png'),pil('RubyAttackL5.png')]

RubyAirAttackR = [pil('AirSpin0.png'),pil('AirSpin1.png'),pil('AirSpin2.png'),pil('AirSpin3.png')]

RubyAirAttackL = [pil('AirSpinL0.png'),pil('AirSpinL1.png'),pil('AirSpinL2.png'),pil('AirSpinL3.png')]

RubyStandingR = pil('standing.png')

RubyStandingL = pil('standing2.png')

RubyDeathR = [pil('Damage00.png'), pil('Damage01.png'), pil('Damage02.png'), pil('Damage03.png'), pil('Damage04.png'), pil('Damage05.png'), pil('Damage06.png')]

RubyDeathL = [pil('DamageL00.png'), pil('DamageL01.png'), pil('DamageL02.png'), pil('DamageL03.png'), pil('DamageL04.png'), pil('DamageL05.png'), pil('DamageL06.png')]

RubyHitR = [pil('Damage00.png'), pil('Damage01.png')]

RubyHitL = [pil('DamageL00.png'), pil('DamageL01.png')]


WiessWalkR= [pil('Wiesswalk0.png'), pil('Wiesswalk1.png'), pil('Wiesswalk2.png'), pil('Wiesswalk3.png'), pil('Wiesswalk4.png'), pil('Wiesswalk5.png')]

WiessWalkL = [pil('WiesswalkLeft0.png'), pil('WiesswalkLeft1.png'), pil('WiesswalkLeft2.png'), pil('WiesswalkLeft3.png'), pil('WiesswalkLeft4.png'), pil('WiesswalkLeft5.png')]

WiessJumpR = [pil('wiessjump0.png'), pil('wiessjump1.png'), pil('wiessjump2.png'), pil('wiessjump3.png'), pil('wiessjump4.png'), pil('wiessjump5.png'), pil('wiessjump6.png'), pil('wiessjump7.png')]

WiessJumpL = [pil('WiessJumpL0.png'), pil('WiessJumpL1.png'), pil('WiessJumpL2.png'), pil('WiessJumpL3.png'), pil('WiessJumpL4.png'), pil('WiessJumpL5.png'), pil('WiessJumpL6.png'), pil('WiessJumpL7.png')]

WiessRangedR = [pil('Counter0.png'), pil('Counter1.png'), pil('Counter1.png'), pil('Counter1.png'), pil('Counter0.png')]

WiessRangedL = [pil('CounterL0.png'), pil('CounterL1.png'), pil('CounterL1.png'), pil('CounterL1.png'), pil('CounterL0.png')]

WiessAttackR = [pil('Wiessattack0.png'), pil('Wiessattack1.png'), pil('Wiessattack2.png'), pil('Wiessattack3.png')]

WiessAttackL = [pil('WiessAttackLeft0.png'), pil('WiessAttackLeft1.png'), pil('WiessAttackLeft2.png'), pil('WiessAttackLeft3.png')]

WiessAirAttackR = [pil('wiessairattack0.png'), pil('wiessairattack1.png'), pil('wiessairattack2.png'), pil('wiessairattack3.png'), pil('wiessairattack4.png'), pil('wiessairattack5.png')]

WiessAirAttackL = [pil('WiessAirAttackL0.png'), pil('WiessAirAttackL1.png'), pil('WiessAirAttackL2.png'), pil('WiessAirAttackL3.png'), pil('WiessAirAttackL4.png'), pil('WiessAirAttackL5.png')]

WiessDeathR = [pil('WiessHit0.png'), pil('WiessHit1.png'), pil('WiessHit2.png'), pil('WiessHit3.png'), pil('WiessHit4.png'), pil('WiessHit5.png')] 

WiessDeathL = [pil('WiessHitL0.png'), pil('WiessHitL1.png'), pil('WiessHitL2.png'), pil('WiessHitL3.png'), pil('WiessHitL4.png'), pil('WiessHitL5.png')]

WiessHitR = [pil('WiessHit0.png'), pil('WiessHit1.png')]

WiessHitL = [pil('WiessHitL0.png'), pil('WiessHitL1.png')]

WiessStandingR = pil('wiessStandR.png')

WiessStandingL = pil('wiessStandL.png')

WiessCounteredR = [pil('wiessattack(2-3)0.png'), pil('wiessattack(2-3)1.png'), pil('wiessattack(2-3)2.png'), pil('wiessattack(2-3)3.png'),pil('wiessattack(2-3)4.png'),pil('wiessattack(2-3)5.png'),pil('wiessattack(2-3)6.png'),pil('wiessattack(2-3)7.png')]     

#Images
bg = pil('bg.jpg')
charscr = pil('title.jpg')
title = pil('Title screen.png')

#Login screen
enter = pil('enter.png')

num1 = pil('num0.png')
num2 = pil('num1.png')
num3 = pil('num2.png')
num4 = pil('num3.png')

numL1 = pil('numlight0.png')
numL2 = pil('numlight1.png')
numL3 = pil('numlight2.png')
numL4 = pil('numlight3.png')

#Win pics
Rwin = pil('Rubywin.png')
Wwin = pil('Wiesswin.png')
Bwin = pil('Blakewin.png')
Ywin = pil('Yangwin.png')

#Healthbars
RubyHealthbar = pil('Healthbar.png')
WiessHealthbar = pil('Wiessbar.png')

#Timer
clock = pygame.time.Clock()

#Backround Music
Backroundmusic = pygame.mixer.music.load('This Will Be The Day.mp3')
pygame.mixer.music.play(-1)

#this is the player class
class player(object):
    def __init__(self, x, y, width, height, wR, wL, jR, jL, rR, rL, a1R, a1L, aaR, aaL, stR, stL, dR, dL, hR, hL):
    #all of the nessisary varibles for the labeled player
        #basic info for character creation
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        #True/False
        self.isJump = False
        self.left = False
        self.right = False
        self.shooting = False
        self.standing = True
        self.finished = False
        self.finishedattack = False
        self.attacking = False
        self.invincible = False
        self.shootable = True
        self.finJump = True
        self.hitt = False
        self.counter = False
         
        #animations
        self.walkRight = wR  
        self.walkLeft = wL  
        self.jumpRight = jR
        self.jumpLeft = jL
        self.attack1Right = a1R 
        self.attack1Left = a1L 
        self.airAttackRight = aaR 
        self.airAttackLeft = aaL
        self.rangeRight = rR 
        self.rangeLeft = rL
        self.standingRight = stR
        self.standingLeft = stL
        self.DeathR = dR
        self.DeathL = dL
        self.hitR = hR
        self.hitL = hL

        #animation frame counters
        self.walkCount = 0
        self.jumpCount = 10
        self.airCount = 0
        self.shotcount = 0
        self.attackcount = 0
        self.attackcount = 0
        self.hitcount = 0
        self.DeathCount = 0
        
        #Numbers      
        self.shottime = 0
        self.attacktime = 0
        self.health = 10
        self.hittime = 0
        self.vel = 7
        self.Dead = 1

        #Hitbox
        self.hitbox = (self.x + 12, self.y + 10, 76,30)
        
    #this draws all of the anmiations
    def draw(self, win):
        #if you are killed
        if self.Dead == 2:
            self.invincible == True
            
            #if you are dieing
            if self.DeathCount == len(self.DeathR)-1:
                self.Dead = 3
            else:
                if self.right:
                    win.blit(self.DeathR[int(self.DeathCount)], (self.x,self.y))
                if self.left:
                    win.blit(self.DeathL[int(self.DeathCount)], (self.x,self.y))
                self.DeathCount += .5
            self.hitbox = (0, 0, 0, 0)
            
        #if you are dead
        if self.Dead == 3:
            win.blit(self.DeathL[-1], (self.x, self.y))

        #if you are not dead
        if self.Dead == 1:
            if self.hitt == True: #had to have 2 t becuase there is a fuction called hit to
                self.invincible = True
                    
                if self.hitcount == len(self.hitR)-1: #to not go outside the list
                    self.hitcount = 0
                    self.hitt = False                    
                    self.invincible = False
                    
                if self.counter == True:
                    print('2')
                    aniplayer(WiessCounteredR, WiessCounteredR, self.hitcount, self.x, self.y, self.right, self.left)
                    self.hitcount += .5
                else:
                    aniplayer(self.hitR, self.hitL, self.hitcount, self.x, self.y, self.right, self.left)
                    self.hitcount += .5

                    
                            
            #everything that happens when you are not hit
            if self.hitt == False:
                #shooting checker
                if self.shooting == True and self.isJump == False: 
                    if self.shotcount == len(self.rangeRight)-1: #to not go outside the list
                        self.shotcount = 0
                        self.finished = True
                        self.shooting = False
                        self.invincible = False
                    else:
                        aniplayer(self.rangeRight, self.rangeLeft, self.shotcount, self.x, self.y, self.right, self.left)
                        self.shotcount += .5

                #attcking on the ground    
                if self.attacking == True and self.isJump == False: 
                    if self.attackcount == len(self.attack1Right)-1: #to not go outside the list
                        self.attackcount = 0
                        self.attacking = False
                        self.attacktime = 0
                        self.finishedattack = True
                    else:
                        aniplayer(self.attack1Right, self.attack1Left, self.attackcount, self.x, self.y, self.right, self.left)
                        self.attackcount += .5 
                
                #Attcking in the air
                if self.attacking == True and self.isJump == True:
                    if self.airCount == len(self.airAttackRight)-1:
                        self.airCount = 0
                        self.attacking = False
                    
                    else:
                        aniplayer(self.airAttackRight, self.airAttackLeft, self.airCount, self.x, self.y, self.right, self.left)
                        self.airCount += .5
                
                #if you are not shooting or attcking    
                if self.finished == False and self.shooting == False and self.attacking == False:
                    #Jump animation
                    if self.isJump and self.right:
                        win.blit(self.jumpRight[self.jumpCount//4], (self.x,self.y))

                    elif self.isJump and self.left:
                        win.blit(self.jumpLeft[self.jumpCount//4], (self.x,self.y))
                        
                    #walk animation
                    if not self.isJump:    
                        if not(self.standing):
                            if self.walkCount == len(self.walkLeft):
                                self.walkCount = 1
                            else:
                                if self.left:
                                    win.blit(self.walkLeft[int(self.walkCount)], (self.x,self.y))
                                    
                                if self.right:
                                    win.blit(self.walkRight[int(self.walkCount)], (self.x,self.y))
                                self.walkCount += .5
                                    
                        else:
                            #standing animation
                            if self.right:
                                win.blit(self.standingRight, (self.x, self.y))
                            else:
                                win.blit(self.standingLeft, (self.x, self.y))
                        
                self.hitbox = (self.x + 12, self.y + 10, 76,75) #hitbox
                pygame.draw.rect(win, (0,0,255), self.hitbox,2) #hitbox display
        
        
    def hit(self):
        self.hitt = True
        if self.counter:
            self.invincible = True
        if self.health > 0 and self.invincible == False: #reduces your heath when hit
            self.health -= 1

        if self.health <= 0:
            self.Dead = 2
        
#for the bullets
class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        #projectile varibles
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 30 * facing
        
    #draws itself
    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

class Melee(object):
    def __init__(self,x,y,radius,color,facing):
        #projectile varibles
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        
    #draws itself
    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

def Healthbars(self, y1, healthbar, R, G, B):
    pygame.draw.rect(win, (0,0,0), (56, y1+9, 218, 26))             #the 10 is the total health
    pygame.draw.rect(win, (R, G, B), (56, y1+9, 218- (21.8 * (10 - self.health)), 26))
    win.blit(healthbar, (0, y1))

def aniplayer(aniR, aniL, frame, x, y, right, left):
    if right:
        win.blit(aniR[int(frame)], (x, y))
    if left:
        win.blit(aniL[int(frame)], (x, y))

def Victory(char1, char2,):
    if char1 == 2:
        win.blit(Rwin, (0,0))
        message_display('Victory!', 255, 0, 0, 40, 40, 60)
    if char2 == 2:
        win.blit(Wwin, (0,0))
        message_display('Victory!', 165, 242, 243, 350, 40, 60)
    pygame.display.update()
    
#redraws over what was on the screen privoiuly so we don't have a mess
def redrawGameWindow(char1, char2):
    win.blit(bg,(0,0))
    
    Healthbars(Ruby, 0,  RubyHealthbar, 255, 0, 0)
    Healthbars(Wiess, 79, WiessHealthbar, 255, 255, 255)
        
    for bullet in bullets:
        bullet.draw(win)

    #Only draws selected characters
    if char1 == 2:
        Ruby.draw(win)
    if char2 == 2 :
        Wiess.draw(win)
        
    #update
    pygame.display.update()

def redrawTitleWindow(screen1, screen2, char1, char2):
    entercounter = 0
    if screen1:
        win.blit(title,(0,0))
        win.blit(enter, (0,0))
        
    if screen2:
        win.blit(charscr,(0,0))
        win.blit(num1,(150,80))
        win.blit(num2,(430,80))
        win.blit(num3,(710,80))
        win.blit(num4,(980,80))
    
        if char1 == 2:
            win.blit(numL1,(150,80))
        if char2 == 2:
            win.blit(numL2,(430,80))
        message_display('Who is fighting?', 255, 255, 255, 20, 10, 85)
    pygame.display.update()

def message_display(text, R, G, B, x, y, size):
    font = pygame.font.Font('freesansbold.ttf', size)
    win.blit(font.render(text, True, (R,G,B)), (x,y))
    pygame.display.update()

def col_obj_player(enemy, Object):
    if Object.y - Object.radius < enemy.hitbox[1] + enemy.hitbox[3] and Object.y + Object.radius > enemy.hitbox[1]:
                    if Object.x + Object.radius > enemy.hitbox[0] and Object.x - Object.radius < enemy.hitbox[0] + enemy.hitbox[2]:
                        return True


Ruby = player(600, 550, 100, 100, RubyWalkR, RubyWalkL, RubyJumpR, RubyJumpL, RubyRangedR, RubyRangedL, RubyAttackR, RubyAttackL, RubyAirAttackR, RubyAirAttackL, RubyStandingR, RubyStandingL, RubyDeathR, RubyDeathL, RubyHitR, RubyHitL)#main sprite
Wiess = player(800, 550, 100, 100, WiessWalkR, WiessWalkL, WiessJumpR, WiessJumpL, WiessRangedR, WiessRangedL, WiessAttackR, WiessAttackL, WiessAirAttackR, WiessAirAttackL, WiessStandingR, WiessStandingL, WiessDeathR, WiessDeathL, WiessHitR, WiessHitL)
bullets = [] #Bullet list
blades = [] #blade list (basically bullets)
spins = []
run = True
dustcount = 3000000000000000000000000000000
playing = False
charselect = False
titlescreen = True
R___ = 1
_W__ = 1
__B_ = 1
___Y = 1
players = 0


#mainloop
while run == True:
    clock.tick(27) 
    if playing == False:
        keys = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            #Checks if you hit exit
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                run = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:

                    if titlescreen == True:
                        titlescreen = False
                        charselect = True
                    
                    if charselect == True and players > 1:
                        charselect = False
                        playing = True

                if charselect == True:
                    if event.key == pygame.K_1:
                        if R___ == 2:
                            R___ = 1
                            players -= 1
                            
                        else:
                            R___ = 2
                            players += 1
                        
                    if event.key == pygame.K_2:
                        if _W__ == 2:
                            _W__ = 1
                            players -= 1
                            
                        else:
                            _W__ = 2
                            players += 1
                            
            
        redrawTitleWindow(titlescreen, charselect, R___, _W__)

    if playing == True:
        
        keys = pygame.key.get_pressed()
        
        #Checks if you hit exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                run = False

        #Ruby's Loop
        if R___ == 2 or R___ == 3:    
        
            for bullet in bullets:
                #is the bullet inside the enimy's hitbox
                if  col_obj_player(Wiess, bullet): 
                        Wiess.hit()
                        bullets.pop(bullets.index(bullet))

                if dustcount >= 0:
                    Ruby.shootable = True
                    if bullet.x < 1244 and bullet.x > 0:
                        bullet.x += bullet.vel
                    else:
                        bullets.pop(bullets.index(bullet))
                if dustcount == 0:
                    Ruby.shootable = False       
                           
            #attacking
            if keys[pygame.K_SPACE]:
                Ruby.attacking = True
                
                if Ruby.left:
                    facing = -1
                if Ruby.right:
                    facing = 1
            
            if Ruby.attacking == True and Ruby.finishedattack == True:
                if len(blades) < 1:
                    if Ruby.right:
                        blades.append(Melee(round(Ruby.x + Ruby.width), round(Ruby.y + Ruby.height//3), 6, (0,0,0), facing))
                        
                    if Ruby.left:
                        blades.append(Melee(round(Ruby.x), round(Ruby.y + Ruby.height//3), 6, (0,0,0), facing))
                Ruby.attcking = False
                
            for blade in blades:     
                #is the blade inside the enimeys hitbox
                if  col_obj_player(Wiess, blade): 
                        Wiess.hit() #Calls the hit function
                        blades.pop(blades.index(blade)) #removes the hit box
                        Ruby.finishedattack = False  #this is so that we don't pop the blade 2 times
                        
                
                if Ruby.finishedattack == True and len(blades) > 0:
                    blades.pop(blades.index(blade)) #removes the hit box


            if Ruby.attacking == True and Ruby.isJump == True:
                spins.append(Melee(round(Ruby.x + Ruby.width/2), round(Ruby.y + Ruby.height/2), 35, (0,0,0), facing))

            for spin in spins:
                if  col_obj_player(Wiess, spin): 
                #is the spin inside the enimeys hitbox 
                        Wiess.hit() #Calls the hit function
                        spins.pop(spins.index(spin)) #removes the hit box
                        Ruby.finishedattack = False  #this is so that we don't pop the spin 2 times
                        
                else:
                    spins.pop(spins.index(spin))
            
            #shooting
            if keys[pygame.K_e] == True and  Ruby.isJump == False:
                Ruby.shooting = True
                if Ruby.left:
                    facing = -1
                if Ruby.right:
                    facing = 1

            if Ruby.finished == True and Ruby.shootable == True:
                if len(bullets) < 3:
                    if Ruby.right:
                        bullets.append(projectile(round(Ruby.x + Ruby.width), round(Ruby.y + Ruby.height//3), 6, (255,223,0), facing))
                            
                    if Ruby.left:
                        bullets.append(projectile(round(Ruby.x), round(Ruby.y + Ruby.height//3), 6, (255,223,0), facing))    
                Ruby.finished = False
                dustcount -= 1

            if Ruby.shootable == False:
                Ruby.finished = False

             #walking 
            if Ruby.shooting == False and Ruby.finished == False:
                
                if keys[pygame.K_a] and Ruby.x > Ruby.vel and Ruby.hitt == False:
                    Ruby.x -= Ruby.vel
                    Ruby.left = True
                    Ruby.right = False
                    Ruby.standing = False
                    
                elif keys[pygame.K_d] and Ruby.x < 1244 - Ruby.width - Ruby.vel and Ruby.hitt == False:
                    Ruby.x += Ruby.vel
                    Ruby.right = True
                    Ruby.left = False
                    Ruby.standing = False
                else:
                    Ruby.standing = True
                    Ruby.walkCount = 0

                #jumping   
                if not(Ruby.isJump):
                    if keys[pygame.K_w] and Ruby.hitt == False:
                        Ruby.isJump = True
                        Ruby.walkCount = 0
                else:
                    if Ruby.jumpCount >= -10:
                        neg = 1
                        if Ruby.jumpCount < 0:
                            neg = -1
                        Ruby.y -= (Ruby.jumpCount ** 2) * 0.5 * neg
                        Ruby.jumpCount -= 1
                        
                    else:
                        Ruby.isJump = False
                        Ruby.attacking = False
                        Ruby.jumpCount = 10

        #Wiess' Loop
        if _W__ == 2 or _W__ == 3:
    
            for bullet in bullets:
                #is the bullet inside the enimy's hitbox
                if  col_obj_player(Ruby, bullet): 
                        Ruby.hit()
                        bullets.pop(bullets.index(bullet))

                if dustcount >= 0:
                    Wiess.shootable = True
                    if bullet.x < 1244 and bullet.x > 0:
                        bullet.x += bullet.vel
                    else:
                        bullets.pop(bullets.index(bullet))
                if dustcount == 0:
                    Wiess.shootable = False       
                           
            #attacking
            if keys[pygame.K_PERIOD]:
                Wiess.attacking = True
                
                if Wiess.left:
                    facing = -1
                if Wiess.right:
                    facing = 1
            
            if Wiess.attacking == True and Wiess.finishedattack == True:
                if len(blades) < 1:
                    if Wiess.right:
                        blades.append(Melee(round(Wiess.x + Wiess.width), round(Wiess.y + Wiess.height//3), 6, (0,0,0), facing))
                        
                    if Wiess.left:
                        blades.append(Melee(round(Wiess.x), round(Wiess.y + Wiess.height//3), 6, (0,0,0), facing))
                Wiess.attcking = False
                
            for blade in blades:
                if  col_obj_player(Ruby, blade): 
                        Ruby.hit() #Calls the hit function
                        blades.pop(blades.index(blade)) #removes the item
                        Wiess.finishedattack = False  #this is so that we don't pop the blade 2 times
                        
                if Wiess.finishedattack == True and len(blades) > 0:
                    blades.pop(blades.index(blade)) #removes the hit box


            if Wiess.attacking == True and Wiess.isJump == True:
                spins.append(Melee(round(Wiess.x + Wiess.width/2), round(Wiess.y + Wiess.height/2), 35, (0,0,0), facing))

            for spin in spins:
                if  col_obj_player(Ruby, spin): 
                        Ruby.hit() 
                        spins.pop(spins.index(spin)) 
                        Wiess.finishedattack = False 
                else:
                    spins.pop(spins.index(spin))
            
            #i is shootingz
            if keys[pygame.K_i] == True and  Wiess.isJump == False and Wiess.counter == False:
                Wiess.shooting = True
                Wiess.counter = True
                print('1')
                    
            if Wiess.finished == True and Wiess.shootable == True:
                Wiess.counter = False
                Wiess.finished = False
                dustcount -= 1

            if Wiess.shootable == False:
                Wiess.finished = False
                
             #walking 
            if Wiess.shooting == False and Wiess.finished == False:           
                if keys[pygame.K_h] and Wiess.x > Wiess.vel and Wiess.hitt == False:
                    Wiess.x -= Wiess.vel
                    Wiess.left = True
                    Wiess.right = False
                    Wiess.standing = False

                elif keys[pygame.K_k] and Wiess.x < 1244 - Wiess.width - Wiess.vel and Wiess.hitt == False:
                    Wiess.x += Wiess.vel
                    Wiess.right = True
                    Wiess.left = False
                    Wiess.standing = False

                else:
                    Wiess.standing = True
                    Wiess.walkCount = 0
                #jumping    
                if not(Wiess.isJump):
                    if keys[pygame.K_u] and Wiess.hitt == False:
                        Wiess.isJump = True
                        Wiess.walkCount = 0
                else:
                    if Wiess.jumpCount >= -10:
                        neg = 1
                        if Wiess.jumpCount < 0:
                            neg = -1
                        Wiess.y -= (Wiess.jumpCount ** 2) * 0.5 * neg
                        Wiess.jumpCount -= 1
                        
                    else:
                        Wiess.isJump = False
                        Wiess.attacking = False
                        Wiess.jumpCount = 10
                        
        #Game counts the players left               
        if Ruby.Dead == 3 and R___ == 2:
            players -= 1
            R___ = 3

        if Wiess.Dead == 3 and _W__ == 2:
            players -= 1
            _W__ = 3

        if players == 1:
            Victory(R___, _W__)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    #resets everything
                    if event.key == pygame.K_RETURN:
                        Ruby = player(600, 550, 100, 100, RubyWalkR, RubyWalkL, RubyJumpR, RubyJumpL, RubyRangedR, RubyRangedL, RubyAttackR, RubyAttackL, RubyAirAttackR, RubyAirAttackL, RubyStandingR, RubyStandingL, RubyDeathR, RubyDeathL, RubyHitR, RubyHitL)#main sprite
                        Wiess = player(800, 550, 100, 100, WiessWalkR, WiessWalkL, WiessJumpR, WiessJumpL, WiessRangedR, WiessRangedL, WiessAttackR, WiessAttackL, WiessAirAttackR, WiessAirAttackL, WiessStandingR, WiessStandingL, WiessDeathR, WiessDeathL, WiessHitR, WiessHitL)
                        bullets = [] #Bullet list
                        blades = [] #blade list (basically bullets)
                        spins = []
                        run = True
                        dustcount = 30
                        playing = False
                        charselect = False
                        titlescreen = True
                        R___ = 1
                        _W__ = 1
                        __B_ = 1
                        ___Y = 1
                        selected = False
                        players = 0

        # if no one has won 
        if players > 1:
            redrawGameWindow(R___, _W__)

#if the game has ended
if not run:
    pygame.quit()


