import pyglet
from pyglet.sprite import Sprite
from pyglet.window import key
import random
import time
jump_distance = 20
gravity = 50
WIDTH = 400
HEIGHT = 300

location = 20
backgroundmusic = pyglet.resource.media('music.wav')
deathsound = pyglet.resource.media('deathsound.wav')
endmusic = pyglet.resource.media('endmusic.wav')
score = 1
def center_image(im):
    im.anchor_x = im.width // 2
    im.anchor_y = im.height // 2
    return im
class Ship(Sprite):
    def __init__(self, img_fp, x, y):
        img = pyglet.image.load(img_fp)
        c_img = center_image(img)
        super().__init__(c_img, x, y)
        self.velocity_x = 0
        self.velocity_y = -10

    def update(self, dt):

       if self.y < 10:
           self.y = 20
       if self.y > 280:
           self.y = 280
       if self.x < 0:
           self.x = 0
       if self.x > 380:
           self.x = 380



    def control(self, symbol,):
        if symbol == key.W or symbol == key.UP:
            self.y += jump_distance
            print("up")
        if symbol == key.S or symbol == key.DOWN:
            self.y -= jump_distance
            print("down")
        if symbol == key.A or symbol == key.LEFT:
            self.x -= jump_distance
            print("left")
        if symbol == key.D or symbol == key.RIGHT :
            self.x += jump_distance
            print("right", )


class Astroid(Sprite):
    astroidmin = -50
    astroidmax = -100
    NUM_ASTEROIDS = 8
    def __init__(self, img_fp, x, y, batch):
        img = pyglet.image.load(img_fp)
        super().__init__(img, x, y, batch=batch)


        self.velocity_y = random.randint(Astroid.astroidmax, Astroid.astroidmin)

    def update(self, dt):

        self.y += self.velocity_y * dt
        if self.y < 0:
            self.x = random.randint(0, WIDTH)
            self.velocity_y = random.randint(Astroid.astroidmax, Astroid.astroidmin)
        self.y = self.y % HEIGHT               # Loop back to top


class Bullet(Sprite):

    def __init__(self, img_fp, x, y):
        img = pyglet.image.load(img_fp)
        c_img = center_image(img)
        super().__init__(c_img, x, y)
        self.velocity_y = 200


    def update(self, dt):
        self.y += self.velocity_y * dt

class Game(pyglet.window.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.death = False
        self.win = False
        self.projectile = Bullet('bullet.png', 1000, 1000)
        self.lander = Ship('ship.png', 170, 0)
        self.batch = pyglet.graphics.Batch()
        self.astroid_number_update = 0
        self.enemys = []
        self.score = 0 # Instance variable for score
        self.score_label = pyglet.text.Label(f"Score: {self.score}",font_name='Arial',font_size=16, x=10, y=HEIGHT - 20,anchor_x='left', anchor_y='top',color=(255, 255, 255, 255))
        self.death_label = pyglet.text.Label(f"You died your score was: {self.score} Press R to restart", font_name='Arial', font_size=13, x=WIDTH/2, y=HEIGHT/2, anchor_x='center', anchor_y='center', color=(255, 255, 255, 255))
        self.win_label = pyglet.text.Label(f"You have won, the password is: The Neon Dream", font_name='Arial', font_size=12,
                                             x=WIDTH / 2, y=HEIGHT / 2, anchor_x='center', anchor_y='center',
                                             color=(255, 255, 255, 255))

        for i in range(Astroid.NUM_ASTEROIDS):
            location = random.randint(0, WIDTH)
            rock = Astroid('asteroid.png', location, HEIGHT, batch=self.batch)
            self.enemys.append(rock)

    def check_collision(self, sprite1, sprite2):
        return (
            sprite1.x < sprite2.x + sprite2.width and
            sprite1.x + sprite1.width > sprite2.x and
            sprite1.y < sprite2.y + sprite2.height and
            sprite1.y + sprite1.height > sprite2.y
        )

    def update(self, dt):
        if not self.death or self.win:
            self.lander.update(dt)
            self.projectile.update(dt)
            for rock in self.enemys:
                rock.update(dt)
                if self.check_collision(self.lander, rock):
                    if self.win == False:
                        self.death = True
                        deathsound.play()
                if self.check_collision(self.projectile, rock):
                    rock.y = -50
                    self.score += 1
                    self.score_label.text = f"Score: {self.score}"
                    self.death_label.text = f"You died your score was: {self.score} Press R to restart"
                    self.astroid_number_update += 1
                    Astroid.astroidmin -= 2
                    Astroid.astroidmax -= 2
                    print(f"Score: {self.score}")
                if self.astroid_number_update == 10:
                    self.astroid_number_update = 0
                    Astroid.NUM_ASTEROIDS += 1
                if self.score == 100:
                    self.win = True
    def on_draw(self):
        self.clear()
        if not self.death and self.win == False:
            self.lander.draw()
            self.projectile.draw()
            for rock in self.enemys:
                rock.draw()
            self.batch.draw()
            self.score_label.draw()
        elif self.death == True:
            self.death_label.draw()  # Show the death message
        elif self.win == True:
            self.win_label.draw()
            player.pause()
            endmusic.play()






    def on_key_press(self, symbol, modifiers):
        if symbol in [key.W, key.A, key.S, key.D, key.LEFT, key.RIGHT, key.UP, key.DOWN]:
            self.lander.control(symbol)
            print(self.lander.x, self.lander.y)
        if symbol == key.SPACE:
            self.projectile = Bullet('bullet.png', self.lander.x, self.lander.y)
        if symbol == key.R:
            Astroid.astroidmin = -50
            Astroid.astroidmax = -100
            Astroid.NUM_ASTEROIDS = 8
            self.death = False
            self.projectile = Bullet('bullet.png', 1000, 1000)
            self.lander = Ship('ship.png', 170, 0)
            self.batch = pyglet.graphics.Batch()
            self.astroid_number_update = 0
            self.enemys = []
            self.score = 0  # Instance variable for score
            self.score_label = pyglet.text.Label(f"Score: {self.score}", font_name='Arial', font_size=16, x=10,
                                                 y=HEIGHT - 20, anchor_x='left', anchor_y='top',
                                                 color=(255, 255, 255, 255))
            for i in range(Astroid.NUM_ASTEROIDS):
                location = random.randint(0, WIDTH)
                rock = Astroid('asteroid.png', location, HEIGHT, batch=self.batch)
                self.enemys.append(rock)






player = pyglet.media.Player()
player.queue(backgroundmusic)
player.loop = True
player.play()
game = Game(WIDTH,HEIGHT)
game.set_caption("The Galactic quest")
pyglet.clock.schedule_interval(game.update, 1/120)
pyglet.app.run()

