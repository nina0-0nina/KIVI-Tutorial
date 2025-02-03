# Importando a função `random` para gerar cores aleatórias
from random import random

# Importando as classes necessárias do Kivy
from kivy.app import App  # Classe base para criar o aplicativo
from kivy.uix.widget import Widget  # Widget base para desenho
from kivy.uix.button import Button  # Botão para limpar o canvas
from kivy.graphics import Color, Ellipse, Line  # Elementos gráficos para desenhar na tela


# Criando um widget personalizado para desenho
class MyPaintWidget(Widget):

    # Método chamado quando o usuário toca na tela
    def on_touch_down(self, touch):
        # Gera uma cor aleatória no espaço HSV (matiz aleatória, saturação e brilho máximos)
        color = (random(), 1, 1)
        with self.canvas:  # Manipula o canvas para desenhar
            Color(*color, mode='hsv')  # Define a cor com base na matiz aleatória
            d = 30.  # Diâmetro do círculo
            # Desenha um pequeno círculo na posição onde o toque ocorreu
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            # Cria uma linha e armazena no dicionário de dados do toque
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    # Método chamado quando o usuário arrasta o dedo na tela
    def on_touch_move(self, touch):
        # Adiciona os novos pontos ao final da linha, estendendo o desenho
        touch.ud['line'].points += [touch.x, touch.y]


# Criando a classe principal do aplicativo
class MyPaintApp(App):

    # Método responsável por construir a interface do aplicativo
    def build(self):
        parent = Widget()  # Cria um widget que será o contêiner principal
        self.painter = MyPaintWidget()  # Instancia o widget de desenho
        clearbtn = Button(text='Clear')  # Cria um botão para limpar o canvas
        clearbtn.bind(on_release=self.clear_canvas)  # Associa a ação do botão ao método `clear_canvas`
        
        # Adiciona os widgets ao contêiner principal
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        
        return parent  # Retorna o layout com os componentes

    # Método para limpar o canvas de desenho
    def clear_canvas(self, obj):
        self.painter.canvas.clear()  # Remove todos os elementos gráficos do canvas


# Executa o aplicativo se o script for rodado diretamente
if __name__ == '__main__':
    MyPaintApp().run()
