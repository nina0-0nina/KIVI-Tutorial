# Importando as classes necessárias do Kivy
from kivy.app import App  # A classe App é a base para a criação de um aplicativo no Kivy
from kivy.uix.gridlayout import GridLayout  # GridLayout permite organizar widgets em uma grade
from kivy.uix.label import Label  # O widget Label é usado para exibir texto na interface
from kivy.uix.textinput import TextInput  # TextInput é um widget para inserir texto

# Definindo a classe LoginScreen, que herda de GridLayout
class LoginScreen(GridLayout):

    # Inicializador da classe LoginScreen. Recebe parâmetros adicionais (**kwargs) se necessário
    def __init__(self, **kwargs):
        # Chama o inicializador da classe pai (GridLayout) para configurar corretamente o layout
        super(LoginScreen, self).__init__(**kwargs)
        
        # Define o número de colunas na grade (layout 2x2, com dois widgets por linha)
        self.cols = 2
        
        # Adiciona um widget Label para o campo "User Name"
        self.add_widget(Label(text='User Name'))
        
        # Cria um TextInput para o campo de entrada do nome de usuário. A opção multiline=False garante que o campo seja de uma linha.
        self.username = TextInput(multiline=False)
        # Adiciona o widget de entrada de texto à grade
        self.add_widget(self.username)
        
        # Adiciona um widget Label para o campo "password"
        self.add_widget(Label(text='Password'))
        
        # Cria um TextInput para a senha. A opção password=True oculta os caracteres digitados.
        self.password = TextInput(password=True, multiline=False)
        # Adiciona o widget de entrada de senha à grade
        self.add_widget(self.password)


# Definindo a classe MyApp, que herda de App. Esta classe cria o aplicativo Kivy.
class MyApp(App):

    # Método build, que define a interface gráfica do aplicativo
    def build(self):
        # Retorna a instância da tela de login (LoginScreen) como widget principal da interface
        return LoginScreen()


# Verifica se o script está sendo executado diretamente
if __name__ == '__main__':
    # Se o script estiver sendo executado diretamente, cria uma instância de MyApp e executa o método run(), que inicia o aplicativo
    MyApp().run()
