from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from pytube import YouTube
import os
import urllib


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.label = Label(text="Insira o link no campo abaixo", font_size=50, font_name='Arial')
        layout.add_widget(self.label)

        self.Text_Input = TextInput(text='', multiline=False)
        layout.add_widget(self.Text_Input)

        btn = Button(text="Download", font_size=50, font_name='Calibri')
        btn.background_color = (2, 0, 0, 1)
        btn.bind(on_press=self.download)
        layout.add_widget(btn)

        return layout

    def download(self, instance):
        try:
            link = self.Text_Input.text
            if not link:
                self.label.text = "Insira um link válido"
                return

            if not urllib.request.urlopen(link).getcode() == 200:
                self.label.text = "Link inválido ou sem conexão à internet"
                return

            self.label.text = "Baixando..."

            diretorio = os.path.join(os.path.expanduser('~'), 'Downloads')
            youtube_video = YouTube(link)
            video = youtube_video.streams.filter(only_audio=True).first()
            out_file = video.download(output_path=diretorio)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            self.label.text = "ARQUIVO BAIXADO COM SUCESSO!"
            popup = Popup(title="Conversor Do Youtube", content=Label(text="ARQUIVO BAIXADO COM SUCESSO!"))
            popup.open()
        except Exception as e:
            erro = Popup(title="Conversor Do Youtube", content=Label(text=f"Erro, Ocorreu um erro: {str(e)}"))
            erro.open()


if __name__ == '__main__':
    MyApp().run()