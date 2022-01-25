import math
import pygame
pygame.init()


TILES = (32, 32)
TILE_SIZE = (512/TILES[0], 512/TILES[1])
SCREEN = pygame.display.set_mode((512, 512))
FOV = math.radians(60)
RES = 128
DEBUG = False
FPS = 60


class Map:
    def __init__(self):
        self.map2D = [
            #[1, 1, 1, 1, 1, 1, 1, 1],
            #[1, 0, 0, 1, 0, 0, 0, 1],
            #[1, 0, 0, 1, 0, 0, 0, 1],
            #[1, 0, 0, 1, 1, 0, 0, 1],
            #[1, 0, 0, 0, 0, 0, 0, 1],
            #[1, 0, 1, 0, 0, 0, 1, 1],
            #[1, 0, 1, 0, 0, 0, 0, 1],
            #[1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1],
            [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1],
            [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]


        self.blocks = []
        for y in range(len(self.map2D)):
            for x in range(len(self.map2D[0])):
                if self.map2D[y][x] == 1:
                    self.blocks.append(pygame.Rect(x*TILE_SIZE[0] + 512, y*TILE_SIZE[1], TILE_SIZE[0], TILE_SIZE[1]))


    def update(self):
        for tile in self.blocks:
            pygame.draw.rect(SCREEN, (0, 0, 0), tile)
            


class Player:
    def __init__(self, map):
        self.map = map
        self.pos = [732, 220]
        self.facing = 0


    def rays(self):
        self.start = self.facing - (FOV/2)
        pygame.draw.rect(SCREEN, (150, 150, 150), (0, 256, 512, 256))
        pygame.draw.rect(SCREEN, (135, 206, 235), (0, 0, 512, 256))

        for ray in range(round(RES)):
            for length in range(512):
                test_x = self.pos[0] - math.cos(self.start) * length
                test_y = self.pos[1] + math.sin(self.start) * length
                col = math.floor(test_x / TILE_SIZE[0]) - TILES[0]
                row = math.floor(test_y / TILE_SIZE[1]) - TILES[1]
                
                if self.map.map2D[row][col] == 1:
                    pygame.draw.line(SCREEN, (0, 255, 0), (self.pos[0], self.pos[1]), (test_x, test_y))
                    pygame.draw.circle(SCREEN, (255, 0, 0), (test_x, test_y), 1)


                    colour = 50 / (1 + length * length * 0.0001)
                    length *= math.cos(self.facing - self.start)
                    rectSelect = pygame.Rect((ray*(512/RES)), 0, 512/RES, 21000 / length)
                    rectSelect.centery = 256
                    pygame.draw.rect(SCREEN, (colour, colour, colour), rectSelect)

                    break
            self.start+=FOV/RES


    def move(self):
        if pygame.key.get_pressed()[pygame.K_a]:
            self.facing -= 0.1

        if pygame.key.get_pressed()[pygame.K_d]:
            self.facing += 0.1

        if pygame.key.get_pressed()[pygame.K_w]:
            self.dPos[0] -= (math.cos(self.facing)*1)
            self.dPos[1] += (math.sin(self.facing)*1)

        if pygame.key.get_pressed()[pygame.K_s]:
            self.dPos[0] += (math.cos(self.facing)*1)
            self.dPos[1] -= (math.sin(self.facing)*1)

        if pygame.key.get_pressed()[pygame.K_q]:
            self.dPos[0] += (math.cos(self.facing+math.radians(90))*1)
            self.dPos[1] -= (math.sin(self.facing+math.radians(90))*1)

        if pygame.key.get_pressed()[pygame.K_e]:
            self.dPos[0] -= (math.cos(self.facing+math.radians(90))*1)
            self.dPos[1] += (math.sin(self.facing+math.radians(90))*1)


    def collide(self):
        for tile in self.map.blocks:
            if tile.collidepoint((self.pos[0] + self.dPos[0], self.pos[1])):
                self.dPos[0] = 0
                
            if tile.collidepoint((self.pos[0], self.pos[1] + self.dPos[1])):
                self.dPos[1] = 0


    def update(self):
        self.dPos = [0, 0]

        self.move()
        self.rays()
        self.collide()

        self.pos[0] += self.dPos[0]
        self.pos[1] += self.dPos[1]
        pygame.draw.circle(SCREEN, (255, 0, 0), self.pos, 5)


class Main:
    def __init__(self):
        self.run = True
        self.clock = pygame.time.Clock()
        self.map = Map()
        self.player = Player(self.map)

        

        self.game_loop()

    def events(self):
        global RES
        global FOV
        global DEBUG
        for event in pygame.event.get():
            if event.type == pygame.QUIT: self.run = False
            if event.type == pygame.KEYDOWN:
                if event.scancode == 82:
                    RES *= 2
                if event.scancode == 81:
                    RES /= 2

                if event.scancode == 80:
                    FOV -= 0.1
                if event.scancode == 79:
                    FOV += 0.1
                
                if event.scancode == 5:
                    if DEBUG:
                        SCREEN = pygame.display.set_mode((512, 512))
                        DEBUG = False
                    else:
                        SCREEN = pygame.display.set_mode((1024, 512))
                        DEBUG = True
    

    def draw(self):
        pygame.display.set_caption("FPS: "+str(round(self.clock.get_fps()))+", FOV: "+str(round(math.degrees(FOV)))+", Resolution: "+str(round(RES)))


        SCREEN.fill((255, 255, 255))

        self.map.update()

        self.player.update()

        pygame.display.flip()

    def game_loop(self):
        while self.run:
            self.clock.tick(FPS)
            self.events()



            self.draw()






if __name__ == "__main__":
    main = Main()

pygame.quit()