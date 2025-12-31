# from datetime import date
# pip install flet[all]
import flet as ft 

def main(page: ft.Page):
    text_hello = ft.Text(value='Hello world')

    text_button = ft.TextButton('SEND')
    elevated_button = ft.ElevatedButton('SEND')

    page.add(text_hello, text_button, elevated_button)


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
