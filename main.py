import flet as ft

def main(page: ft.Page):
    text_hello = ft.Text(value='hello bekzhan')
    page.title = 'my first app'
    page.theme_mode = ft.ThemeMode.SYSTEM
    # text_hello.value = 'Bekzhan'
    # text_hello.color = ft.Colors.GREEN_800


    # text_button = ft.TextButton('send')
    # icon_button = ft.IconButton(icon=ft.Icons.SEND)
    def text(e):
        # print(name_input.value)
        name = name_input.value
        if name:
            text_hello.value = f'Hello {name}'
            text_hello.color = None
            name_input.value = None
        else:
            text_hello.value = 'write your name:'
            text_hello.color = ft.Colors.RED_ACCENT


    def back_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            

    elevatod_button = ft.ElevatedButton('send', on_click=text, icon=ft.Icons.SEND, icon_color=ft.Colors.BLACK)
    icon_button = ft.IconButton(icon=ft.Icons.SETTINGS_APPLICATIONS_SHARP, on_click=back_theme)

    name_input = ft.TextField(label='write something:', on_submit=text)



# добавление на страницу
    page.add(text_hello, name_input, elevatod_button, icon_button)
ft.app(target=main)