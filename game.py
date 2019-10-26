import sys, pygame
pygame.init()
pygame.mixer.init(44100, 16, 2, 4096)

show_coffin = False
#used for framerate
clock = pygame.time.Clock()
#loading ball image with rectangular size
sprite = pygame.image.load("walk1.png")
dest = (0, 270)
#loads walk right animation
WalkRight = [pygame.image.load("walk1.png"), pygame.image.load("walk2.png"), pygame.image.load("walk3.png"),
             pygame.image.load("walk4.png"), pygame.image.load("walk5.png"), pygame.image.load("walk6.png"),
             pygame.image.load("walk7.png"), pygame.image.load("walk8.png")]
#for loop takes images from WaLk Right and flips the x, y and adds it to Walk Left
WalkLeft = []
for img in WalkRight:
    WalkLeft.append(pygame.transform.flip(img,True, False))
#sets a background and rectangle for it
bg = pygame.image.load("background.png")
bg_rect = bg.get_rect()
pygame.display.set_caption("Vampire's Rest ")
#defining screen
screenwidth = 438
screenheight = 438
screen = pygame.display.set_mode((screenwidth, screenheight))
speed = [1, 1]
shootLoop = 0
#background music
pygame.mixer.music.load("vampiretheme.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)
black = 0, 0, 0
# creation of coffin class
# class coffin1(object):
#     coffinimg = pygame.image.load("coffin.png")
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self. height = height
#
#     def draw(self, screen):
#         self.coffinimg


#creation of player class
class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = WalkRight[0]
        self.rect = self.image.get_rect()
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.WalkCount = 0
        self.standing = True
        self.hitbox = (self.x + 10,self.y, 25, 80)
#method that draws character
    def draw(self,screen):
        # if character is moving left or right walk count will increase showing different animations
        if not (self.standing):
            if self.right:
                screen.blit(WalkRight[self.WalkCount // 5], (self.x, self.y))
                self.WalkCount += 1
                if self.WalkCount + 1 >= 40:
                    self.WalkCount = 0
            elif self.left:
                screen.blit(WalkLeft[self.WalkCount // 5], (self.x, self.y))
                self.WalkCount += 1
                if self.WalkCount + 1 >= 40:
                    self.WalkCount = 0
        else:
            if self.right:
                screen.blit(WalkRight[0], (self.x, self.y))
            else:
                screen.blit(WalkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 10, self.y, 25, 80)

#creation of projectile class
class projectile (object):
    def __init__(self, x, y, facing, radius, color):
        self.x = x
        self.y = y
        self.facing = facing
        self.radius = radius
        self.color = color
        self.image = pygame.image.load("vampireshot.png")
        self.velocity = 2 * facing
        #method that draws projectile
    def drawProjectile(self,screen):
        #makes the projectile
        screen.blit(self.image,(self.x, self.y))
        #creation of enemy class
class enemy1(object):
    #Change this to actual enemy
    WalkLeft = [pygame.image.load("hunter.png"), pygame.image.load("hunter1.png"), pygame.image.load("hunter2.png"),
                 pygame.image.load("hunter3.png"), pygame.image.load("hunter4.png"), pygame.image.load("hunter5.png"),
                 pygame.image.load("hunter6.png"), pygame.image.load("hunter7.png")]
    # for loop takes images from WaLk Right and flips the x, y and adds it to Walk Left
    WalkRight = []
    for img in WalkLeft:
        WalkRight.append(pygame.transform.flip(img, True, False))
    def __init__(self, x, y, width,height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.WalkCount = 0
        self.velocity = 1
        #makes character go from end to x
        self.path = [self.end, self.x]
        self.hitbox = (self.x + 10, self.y, 25, 80)
        self.health = 10
        self.visibile = True
        #draws enemy on the screen
    def drawenemy(self, screen):
        self.move()
        if self.visibile:
            self.hitbox = (self.x + 10, self.y, 25, 80)

        else:
            self.hitbox = (9999, 9999, 9999, 9999)

    #allows character to move a certain distance back and forth
    def move(self):
        if self.visibile:
            if self.WalkCount + 1 >= 40:
                self.WalkCount = 0
            if self.velocity > 0:
                screen.blit(self.WalkRight[self.WalkCount // 5], (self.x, self.y))
                self.WalkCount += 1
            else:
                screen.blit(self.WalkLeft[self.WalkCount // 5], (self.x, self.y))
                self.WalkCount += 1
            if self.velocity > 0:
                if self.x + self.velocity < self.path[1]:
                    self.x += self.velocity
                else:
                    self.velocity = self.velocity * -1
                    self.WalkCount = 0
            else:
                if self.x - self.velocity > self.path[0]:
                    self.x += self.velocity
                else:
                    self.velocity = self.velocity * -1
                    self.WalkCount = 0
#allows us to do certain things on collision
    def hit(self):
        if self.health > 0 :
            self.health -= 5
        else:
            self.visibile = False
        print("Oww")

class enemy2(object):
    #Change this to actual enemy
    WalkLeft = [pygame.image.load("skeleton.png"), pygame.image.load("skeleton1.png"), pygame.image.load("skeleton2.png")]
    # for loop takes images from WaLk Right and flips the x, y and adds it to Walk Left
    WalkRight = []
    for img in WalkLeft:
        WalkRight.append(pygame.transform.flip(img, True, False))
    def __init__(self, x, y, width,height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.WalkCount = 0
        self.velocity = 1
        #makes character go from end to x
        self.path = [self.end, self.x]
        self.hitbox = (self.x + 15, self.y, 50, 80)
        self.health = 10
        self.visibile = True
        #draws enemy on the screen
    def drawenemy(self, screen):
        self.move()
        if self.visibile:
            self.hitbox = (self.x + 10, self.y, 25, 80)
        else: self.hitbox = (9999, 9999, 9999, 9999)

    #allows character to move a certain distance back and forth
    def move(self):
        if self.visibile:
            if self.WalkCount + 1 >= 15:
                self.WalkCount = 0
            if self.velocity > 0:
                screen.blit(self.WalkRight[self.WalkCount // 5], (self.x, self.y))
                self.WalkCount += 1
            else:
                screen.blit(self.WalkLeft[self.WalkCount // 5], (self.x, self.y))
                self.WalkCount += 1
            if self.velocity > 0:
                if self.x + self.velocity < self.path[1]:
                    self.x += self.velocity
                else:
                    self.velocity = self.velocity * -1
                    self.WalkCount = 0
            else:
                if self.x - self.velocity > self.path[0]:
                    self.x += self.velocity
                else:
                    self.velocity = self.velocity * -1
                    self.WalkCount = 0
#allows us to do certain things on collision
    def hit(self):
        if self.health > 0 :
            self.health -= 5
        else:
            self.visibile = False
        print("Oww")

class enemy3(object):
    #Change this to actual enemy
    WalkLeft = [pygame.image.load("zombie.png"), pygame.image.load("zombie1.png"), pygame.image.load("zombie2.png")]
    # for loop takes images from WaLk Right and flips the x, y and adds it to Walk Left
    WalkRight = []
    for img in WalkLeft:
        WalkRight.append(pygame.transform.flip(img, True, False))
    def __init__(self, x, y, width,height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.WalkCount = 0
        self.velocity = 1
        #makes character go from end to x
        self.path = [self.end, self.x]
        self.hitbox = (self.x + 10, self.y, 25, 80)
        self.health = 10
        self.visibile = True
        #draws enemy on the screen
    def drawenemy(self, screen):
        self.move()
        if self.visibile:
            self.hitbox = (self.x + 10, self.y, 25, 80)

        else:
            self.hitbox = (9999, 9999, 9999, 9999)
    #allows character to move a certain distance back and forth
    def move(self):
        if self.visibile:
            if self.WalkCount + 1 >= 15:
                self.WalkCount = 0
            if self.velocity > 0:
                screen.blit(self.WalkRight[self.WalkCount // 5], (self.x, self.y))
                self.WalkCount += 1
            else:
                screen.blit(self.WalkLeft[self.WalkCount // 5], (self.x, self.y))
                self.WalkCount += 1
            if self.velocity > 0:
                if self.x + self.velocity < self.path[1]:
                    self.x += self.velocity
                else:
                    self.velocity = self.velocity * -1
                    self.WalkCount = 0
            else:
                if self.x - self.velocity > self.path[0]:
                    self.x += self.velocity
                else:
                    self.velocity = self.velocity * -1
                    self.WalkCount = 0
#allows us to do certain things on collision
    def hit(self):
        if self.health > 0 :
            self.health -= 5
        else:
            self.visibile = False
        print("Oww")
run = True
x = 200
y = 270
vel = 2
coffin2 = pygame.image.load("coffin.png")
coffin_rect = coffin2.get_rect()
class coffin(object):

    def __init__(self, x, y, width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 1
        self.hitbox = (self.x + 20, self.y, 25, 80)
        self.show_coffin = False
        self.image = coffin2
        self.coffin_rect = coffin_rect

    def showcoffin(self):
        if self.show_coffin == True and vampireMc.right == True :
            self.x -= self.velocity
            screen.blit(coffin2,(self.x, self.y))
            self.hitbox = (self.x , self.y, 50, 80)
            pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)
            if self.coffin_rect.colliderect(vampireMc.rect) == True and endcoffin.x == 0:
               global run, textRect,delay
               font = pygame.font.SysFont('comicsansms', 32)
               text = font.render('You Got Sleep ', True, (0, 255, 0), (0, 0, 128))
               textRect = text.get_rect()
               textRect.center = (200, 200)
               screen.blit(text, [200, 200])
               pygame.display.flip()
               print('yo')
               run = False
               delay = 0
        if self.show_coffin == True and vampireMc.left == True:
            self.x += self.velocity
            screen.blit(coffin2, (self.x, self.y), self.coffin_rect)
            self.hitbox = (self.x , self.y, 50, 80)
            pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)







    # A function that redraws the window
def redrawWindow():
    global WalkCount
    # repaints screen
    screen.fill(black)
    screen.blit(bg,bg_rect)
    vampireMc.draw(screen)
    enemy.drawenemy(screen)
    hunter.drawenemy(screen)
    skeleton.drawenemy(screen)
    zombie.drawenemy(screen)
    endcoffin.showcoffin()






    #hunter.drawenemy(screen)
    for bullet in bullets:
        bullet.drawProjectile(screen)
    pygame.display.update()


#instances of different classes
vampireMc = player(0, 270, 87, 50)
bullets = []
enemy = enemy1(800, 270, 87, 50, 100)
hunter = enemy1(500, 270, 87, 50, 100)
skeleton = enemy2(1000, 270, 42, 88, 100)
zombie = enemy3(1200, 270, 44, 75, 100)
endcoffin = coffin(500, 270, 54, 86)
#coffin = coffin1(200, 270, 54, 89)
delay = 0
#Main Loop
while run == True :
    #sets frame rate
    delay += clock.tick(60)
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0
    #Listens for events
    for event in pygame.event.get():
        #terminates game on exit
        if event.type == pygame.QUIT:
            sys.exit()

        #creates bullets
    # for bullet in bullets:
    #    if bullet.y < enemy.hitbox[1] + enemy.hitbox[3] and bullet.y  > enemy.hitbox[1]:
    #        if bullet.x  > enemy.hitbox[0] and bullet.x < enemy.hitbox[0] + enemy.hitbox[2]:
    #         enemy.hit()  # calls enemy hit method
    #         bullets.pop(bullets.index(bullet))
    #    if bullet.y < hunter.hitbox[1] + hunter.hitbox[3] and bullet.y > hunter.hitbox[1]:
    #         if bullet.x > hunter.hitbox[0] and bullet.x < hunter.hitbox[0] + hunter.hitbox[2]:
    #              hunter.hit()  # calls enemy hit method
    #              bullets.pop(bullets.index(bullet))
    #
    #    if bullet.x < 500 and bullet.x > 0:
    #         bullet.x += bullet.velocity  # Moves the bullet by its vel
    #    else:
    #         bullets.pop(bullets.index(bullet))
# listens for actions with keys
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] and shootLoop == 0:

            if vampireMc.left:
                #allows us to determine where character is facing
                facing = -1
            else:
                facing = 1

            if len(bullets) < 1:
                bullets.append(
                    projectile(round(vampireMc.x + vampireMc.width // 2), round(vampireMc.y + vampireMc.height // 2),
                               6, (0, 0, 0), facing))
            shootLoop = 1

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.velocity  # Moves the bullet by its vel
        else:
            bullets.pop(bullets.index(bullet))

        if bullet.y < enemy.hitbox[1] + enemy.hitbox[3] and bullet.y > enemy.hitbox[1]:
            if bullet.x > enemy.hitbox[0] and bullet.x < enemy.hitbox[0] + enemy.hitbox[2]:
                enemy.hit()  # calls enemy hit method
                bullets.pop(bullets.index(bullet))
        if bullet.y < hunter.hitbox[1] + hunter.hitbox[3] and bullet.y > hunter.hitbox[1]:
            if bullet.x > hunter.hitbox[0] and bullet.x < hunter.hitbox[0] + hunter.hitbox[2]:
                hunter.hit()  # calls enemy hit method
                bullets.pop(bullets.index(bullet))
        if bullet.y < skeleton.hitbox[1] + skeleton.hitbox[3] and bullet.y > skeleton.hitbox[1]:
            if bullet.x > skeleton.hitbox[0] and bullet.x < skeleton.hitbox[0] + skeleton.hitbox[2]:
                skeleton.hit()  # calls enemy hit method
                bullets.pop(bullets.index(bullet))
        if bullet.y < zombie.hitbox[1] + zombie.hitbox[3] and bullet.y > zombie.hitbox[1]:
            if bullet.x > zombie.hitbox[0] and bullet.x < zombie.hitbox[0] + zombie.hitbox[2]:
                zombie.hit()  # calls enemy hit method
                bullets.pop(bullets.index(bullet))



        #moves background for side scrolling effect
    if key[pygame.K_LEFT] :
        if(bg_rect.left < 0):
            bg_rect = bg_rect.move([3, 0])

        vampireMc.left = True
        vampireMc.right = False
        vampireMc.standing = False
        #Moves character right

    #moves background for side scroll
    elif key[pygame.K_RIGHT]:
        bg_rect = bg_rect.move([-3, 0])
        print(bg_rect.right)
        if(bg_rect.right <=4500):
            endcoffin.show_coffin = True
        vampireMc.right = True
        vampireMc.left = False
        vampireMc.standing = False
#when character stands still
    else:
        vampireMc.standing = True
        vampireMc.WalkCount = 0
        #jump
    if not vampireMc.isJump:

        if key[pygame.K_UP]:
            vampireMc.y = 270
            vampireMc.isJump = True
#Sets up the physics of the jump
    else:
         if vampireMc.jumpCount >= - 10:
             neg = 1
             if vampireMc.jumpCount < 0:
              neg = -1
             vampireMc.y -=(vampireMc.jumpCount ** 2) * 0.5 * neg
             vampireMc.jumpCount -=1
         else:
             vampireMc.isJump = False
             vampireMc.jumpCount = 10
#calls redraw window function
    redrawWindow()
    if run == False:
        font = pygame.font.SysFont('comicsansms', 32)
        text = font.render('You Got Sleep ', True, (0, 255, 0), (0, 0, 128))
        textRect = text.get_rect()
        textRect.center = (200, 200)
        screen.blit(text, [200, 200])
        pygame.display.flip()
        pygame.time.wait(2000)
        sys.exit()

