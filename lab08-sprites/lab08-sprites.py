import random
import arcade

# --- Constantes ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.25
SPRITE_SCALING_ROCK = 0.3
COIN_COUNT = 20
ROCK_COUNT = 10

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Esquiva las piedras y recoge las monedas"
SPEED = 4  # Velocidad de desplazamiento de los objetos
PLAYER_SPEED = 5  # Velocidad del jugador


class MyGame(arcade.Window):
    """ Nuestra clase personalizada de juego """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Listas de sprites
        self.player_list = None
        self.coin_list = None
        self.rock_list = None

        # Configuración del jugador
        self.player_sprite = None
        self.score = 0

        # Variables de movimiento del jugador
        self.player_dx = 0
        self.player_dy = 0

        # Esconder el cursor del mouse
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Configurar el juego e inicializar variables. """

        # Inicializar listas de sprites
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.rock_list = arcade.SpriteList()

        # Reiniciar puntuación
        self.score = 0

        # Crear el jugador
        img = ":resources:images/animated_characters/female_person/femalePerson_idle.png"
        self.player_sprite = arcade.Sprite(img, SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = SCREEN_HEIGHT // 2
        self.player_list.append(self.player_sprite)

        # Crear monedas
        for _ in range(COIN_COUNT):
            coin = arcade.Sprite(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)
            coin.center_x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 300)
            coin.center_y = random.randint(50, SCREEN_HEIGHT - 50)
            coin.change_x = -SPEED  # Moverse hacia la izquierda
            self.coin_list.append(coin)

        # Crear piedras
        for _ in range(ROCK_COUNT):
            rock = arcade.Sprite(":resources:images/tiles/rock.png", SPRITE_SCALING_ROCK)
            rock.center_x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 300)
            rock.center_y = random.randint(50, SCREEN_HEIGHT - 50)
            rock.change_x = -SPEED  # Moverse hacia la izquierda
            self.rock_list.append(rock)

    def on_draw(self):
        """ Dibujar todo en la pantalla """
        self.clear()
        self.coin_list.draw()
        self.rock_list.draw()
        self.player_list.draw()

        # Mostrar puntuación
        score_text = f"Puntuación: {self.score}"
        arcade.draw_text(score_text, 10, 20, arcade.color.WHITE, 14)

    def on_update(self, delta_time):
        """ Lógica del juego y movimiento """
        self.coin_list.update()
        self.rock_list.update()

        # Mover al jugador
        self.player_sprite.center_x += self.player_dx
        self.player_sprite.center_y += self.player_dy

        # Mantener al jugador dentro de los límites de la pantalla
        if self.player_sprite.center_y < 0:
            self.player_sprite.center_y = 0
        if self.player_sprite.center_y > SCREEN_HEIGHT:
            self.player_sprite.center_y = SCREEN_HEIGHT
        if self.player_sprite.center_x < 0:
            self.player_sprite.center_x = 0
        if self.player_sprite.center_x > SCREEN_WIDTH:
            self.player_sprite.center_x = SCREEN_WIDTH

        # Eliminar monedas y piedras fuera de la pantalla
        for coin in self.coin_list:
            if coin.center_x < 0:
                coin.center_x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 300)
                coin.center_y = random.randint(50, SCREEN_HEIGHT - 50)

        for rock in self.rock_list:
            if rock.center_x < 0:
                rock.center_x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 300)
                rock.center_y = random.randint(50, SCREEN_HEIGHT - 50)

        # Verificar colisiones con monedas
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1

        # Verificar colisiones con piedras
        if arcade.check_for_collision_with_list(self.player_sprite, self.rock_list):
            print("¡Has chocado con una piedra! Fin del juego.")
            arcade.close_window()

    def on_key_press(self, key, modifiers):
        """ Manejar teclas presionadas """
        if key == arcade.key.W:
            self.player_dy = PLAYER_SPEED
        elif key == arcade.key.S:
            self.player_dy = -PLAYER_SPEED
        elif key == arcade.key.A:
            self.player_dx = -PLAYER_SPEED
        elif key == arcade.key.D:
            self.player_dx = PLAYER_SPEED

    def on_key_release(self, key, modifiers):
        """ Manejar teclas liberadas """
        if key in (arcade.key.W, arcade.key.S):
            self.player_dy = 0
        if key in (arcade.key.A, arcade.key.D):
            self.player_dx = 0


def main():
    """ Función principal """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
