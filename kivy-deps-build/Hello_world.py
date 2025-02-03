# Importando o módulo Kivy, que é uma biblioteca para a criação de interfaces gráficas
import kivy

# Importando a classe App do módulo kivy.app. Ela é a base para a criação do aplicativo
from kivy.app import App

# Importando a classe Label do módulo kivy.uix.label. A classe Label é usada para criar rótulos de texto na interface
from kivy.uix.label import Label


# Definindo uma classe MyApp que herda de App, a qual representa o aplicativo
class MyApp(App):

    # Método build: define a interface gráfica do aplicativo
    def build(self):
        # Retorna um Label com o texto 'Hello world' como widget principal
        return Label(text='Hello world')


# A condição if __name__ == '__main__' verifica se o script está sendo executado diretamente
# Isso garante que o aplicativo será executado somente se o arquivo for rodado diretamente (e não se for importado)
if __name__ == '__main__':
    # Cria uma instância de MyApp e executa o método run(), que inicia o loop do aplicativo
    MyApp().run()
