# Importações do Kivy para criação da aplicação
from kivy.app           import App  # Classe base para o aplicativo
from kivy.uix.widget    import Widget  # Base para criação de widgets
from kivy.vector        import Vector  # Usado para cálculos vetoriais (movimentação da bola)
from kivy.clock         import Clock  # Controla a atualização do jogo em intervalos regulares

# Importação de propriedades reativas do Kivy
from kivy.properties    import (
    NumericProperty,  # Propriedade numérica que pode ser reativa na interface
    ReferenceListProperty,  # Agrupa múltiplas propriedades em uma só
    ObjectProperty  # Referência a um objeto Kivy
)


# Classe que representa as raquetes do jogo
class PongPaddle(Widget):
    # Propriedade para armazenar a pontuação do jogador
    score = NumericProperty(0)
    
    # Método para detectar colisão entre a bola e a raquete
    def bounce_ball(self, ball):
        if self.collide_widget(ball):  # Verifica se a bola tocou na raquete
            vx, vy = ball.velocity  # Obtém a velocidade da bola
            offset = (ball.center_y - self.center_y) / (self.height / 2)  # Calcula um desvio baseado no ponto de contato
            bounced = Vector(-1 * vx, vy)  # Inverte a direção da bola horizontalmente
            vel = bounced * 1.1  # Aumenta a velocidade para tornar o jogo mais difícil com o tempo
            ball.velocity = vel.x, vel.y + offset  # Aplica o novo vetor de velocidade à bola


# Classe que representa a bola do jogo
class PongBall(Widget):
    # Propriedades numéricas da velocidade da bola
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    # Criação de uma propriedade que agrupa as velocidades x e y em uma só
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    
    # Método responsável por atualizar a posição da bola com base na sua velocidade
    def move(self): 
        self.pos = Vector(*self.velocity) + self.pos  # Move a bola conforme sua velocidade atual


# Classe principal que representa o jogo Pong
class PongGame(Widget):
    # Referências aos objetos do jogo (bola e jogadores)
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    
    # Método para iniciar a bola na posição central com uma velocidade inicial
    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center  # Coloca a bola no centro do jogo
        self.ball.velocity = vel  # Define a velocidade inicial da bola
    
    # Método chamado repetidamente para atualizar o jogo
    def update(self, dt):
        self.ball.move()  # Move a bola
        
        # Verifica colisões com as raquetes
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)
        
        # Se a bola tocar na parte superior ou inferior da tela, inverte sua direção vertical
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

        # Se a bola sair pela esquerda, o jogador 2 pontua e o jogo reinicia a bola
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(4, 0))  # Bola reinicia indo para a direita
            
        # Se a bola sair pela direita, o jogador 1 pontua e o jogo reinicia a bola
        if self.ball.right > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4, 0))  # Bola reinicia indo para a esquerda
            
    # Método para movimentar as raquetes com base no toque do jogador
    def on_touch_move(self, touch):
        if touch.x < self.width / 3:  # Se o toque estiver no terço esquerdo da tela, move a raquete do jogador 1
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:  # Se estiver no terço direito, move a raquete do jogador 2
            self.player2.center_y = touch.y


# Classe principal do aplicativo Pong
class PongApp(App):
    
    # Método responsável por construir a interface do jogo
    def build(self):
        game = PongGame()  # Cria uma instância do jogo
        game.serve_ball()  # Inicia a bola na posição inicial
        Clock.schedule_interval(game.update, 1.0 / 60.0)  # Atualiza o jogo a cada 1/60 de segundo
        return game  # Retorna o jogo como interface principal do app


# Executa o jogo se o script for rodado diretamente
if __name__ == '__main__':
    PongApp().run()
