import arcade
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Bouncing Balls"

class Ball:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        self.size = 0



def make_ball():
    ball = Ball()
    ball.size = random.randrange(10, 30)

    ball.x = random.randrange(ball.size, SCREEN_WIDTH - ball.size)
    ball.y = random.randrange(ball.size, SCREEN_HEIGHT - ball.size)

    ball.change_x = random.randrange(-2, 3)
    ball.change_y = random.randrange(-2, 3)

    ball.color = (random.randrange(256), random.randrange(256), random.randrange(256))

    return ball


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.ball_list = []
        ball = make_ball()
        self.ball_list.append(ball)

    def on_draw(self):

        arcade.start_render()

        for ball in self.ball_list:
            arcade.draw_circle_filled(ball.x, ball.y, ball.size, ball.color)

        output = "Balls: {}".format(len(self.ball_list))
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def update(self, delta_time):

        for ball in self.ball_list:
            ball.x += ball.change_x
            ball.y += ball.change_y

            if ball.x < ball.size:
                ball.change_x *= -1

            if ball.y < ball.size:
                ball.change_y *= -1

            if ball.x > SCREEN_WIDTH - ball.size:
                ball.change_x *= -1

            if ball.y > SCREEN_HEIGHT - ball.size:
                ball.change_y *= -1

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked.
        """
        ball = make_ball()
        self.ball_list.append(ball)


def main():
    MyGame()
    arcade.run()


if __name__ == "__main__":
    main()