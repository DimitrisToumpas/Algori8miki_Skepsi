import sys
import pygame


#---------- UI -----------



# ---------- Ρυθμίσεις ----------
WIDTH, HEIGHT = 480, 720
FPS = 60

ROAD_LEFT = 60          # αριστερό όριο του δρόμου
ROAD_RIGHT = WIDTH - 60  # δεξί όριο του δρόμου

GRASS = (60, 140, 60)
ASPHALT = (60, 60, 60)
WHITE = (240, 240, 240)
YELLOW = (250, 200, 0)


# ---------- Ταξί ----------
class Taxi(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = self.make_image()
        self.rect = self.image.get_rect(midbottom=(WIDTH // 2, HEIGHT - 30))
        self.speed = 6

    @staticmethod
    def make_image():
        """Ζωγραφίζει ένα απλό ταξί. Αργότερα αντικαταστήστε το με PNG:
        return pygame.image.load("assets/images/taxi.png").convert_alpha()
        """
        img = pygame.Surface((50, 90), pygame.SRCALPHA)
        pygame.draw.rect(img, YELLOW, (0, 0, 50, 90), border_radius=10)       # αμάξωμα
        pygame.draw.rect(img, (30, 30, 30), (6, 20, 38, 18), border_radius=4)  # παρμπρίζ
        pygame.draw.rect(img, (30, 30, 30), (6, 58, 38, 14), border_radius=4)  # πίσω τζάμι
        pygame.draw.rect(img, WHITE, (15, 42, 20, 10))                         # πινακίδα TAXI
        #return img
        return pygame.image.load("assets/images/car_yellow_1.png")


    def update(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed

        # Κρατάμε το ταξί μέσα στο δρόμο και στην οθόνη
        self.rect.left = max(self.rect.left, ROAD_LEFT)
        self.rect.right = min(self.rect.right, ROAD_RIGHT)
        self.rect.top = max(self.rect.top, 0)
        self.rect.bottom = min(self.rect.bottom, HEIGHT)


# ---------- Σχεδίαση δρόμου (προσωρινά στατικός) ----------
def draw_road(screen):
    screen.fill(GRASS)
    pygame.draw.rect(screen, ASPHALT, (ROAD_LEFT, 0, ROAD_RIGHT - ROAD_LEFT, HEIGHT))
    for y in range(0, HEIGHT, 60):
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 3, y, 6, 30))


# ---------- Κύριο πρόγραμμα ----------
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Crazy Taxi 2D")
    clock = pygame.time.Clock()

    taxi = Taxi()
    all_sprites = pygame.sprite.Group(taxi)

    running = True
    while running:
        # 1. Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        # 2. Update
        keys = pygame.key.get_pressed()
        taxi.update(keys)

        # 3. Draw
        draw_road(screen)
        all_sprites.draw(screen)
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()