import pygame
import psycopg2 as p

pygame.init()

con = p.connect("dbname='python_game_data' user='postgres' host='192.168.99.100' password='postgres'")
cur = con.cursor()
cur.execute("select * from game_text")
rows = cur.fetchall()

walkRight = [pygame.image.load('images/human/R1.png'), pygame.image.load('images/human/R2.png'),
             pygame.image.load('images/human/R3.png'), pygame.image.load('images/human/R4.png'),
             pygame.image.load('images/human/R5.png'), pygame.image.load('images/human/R6.png'),
             pygame.image.load('images/human/R7.png'), pygame.image.load('images/human/R8.png'),
             pygame.image.load('images/human/R9.png')]
walkLeft = [pygame.image.load('images/human/L1.png'), pygame.image.load('images/human/L2.png'),
            pygame.image.load('images/human/L3.png'), pygame.image.load('images/human/L4.png'),
            pygame.image.load('images/human/L5.png'), pygame.image.load('images/human/L6.png'),
            pygame.image.load('images/human/L7.png'), pygame.image.load('images/human/L8.png'),
            pygame.image.load('images/human/L9.png')]

looseSound = pygame.mixer.Sound("sounds/loose_zelda.wav")

font = pygame.font.SysFont('comicsans', 30, True)


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = True
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        self.lives = 5
        self.score = 0

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not self.standing:
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    # pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

    def hit(self, win):
        self.isJump = False
        self.jumpCount = 10
        self.x = 60
        self.y = 410
        self.walkCount = 0
        self.lives -= 1
        self.score -= 5
        if self.lives <= 0:
            font1 = pygame.font.SysFont('comicsans', 28, True)
            text = font1.render(rows[1][2], 1, (255, 0, 0))
            win.blit(text, (250 - (text.get_width() / 2), 200))
            pygame.display.update()
            pygame.mixer.music.stop()
            pygame.mixer.music.set_volume(0.8)
            looseSound.play()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = 301
                        cur.execute("INSERT INTO scores (score) VALUES (%s);", (self.score,))
                        con.commit()
                        pygame.quit()

        text = font.render('-5', 1, (255, 0, 0))
        win.blit(text, (250 - (text.get_width() / 2), 200))
        pygame.display.update()
        i = 0
        while i < 200:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
