# from datetime import date
# pip install flet[all]
import flet as ft 

def main(page: ft.Page):
    page.title = "Мое первое приложение!"
    page.theme_mode = ft.ThemeMode.LIGHT

    text_hello = ft.Text(value='Hello world')

    def on_button_click(_):
        name = name_input.value.strip()
        print(name)

        if name:
            text_hello.color = None
            text_hello.value = f"Hello {name}"
            name_input.value = None
        else:
            text_hello.value = 'Введите корректное имя'
            text_hello.color = ft.Colors.RED
            
        # page.update() 

    elevated_button = ft.ElevatedButton('SEND', icon=ft.Icons.SEND, on_click=on_button_click)

    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click)

    page.add(text_hello, name_input, elevated_button)


ft.app(target=main)
