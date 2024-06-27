import flet as ft

def main(page: ft.Page):
    # Установка фона синего цвета
    page.bgcolor = ft.colors.BLUE
    page.hide_app_bar = True  # Скрытие логотипа Flet

    # Создание текста и кнопки
    text = ft.Text(value="Эй Кей Тест", color=ft.colors.WHITE, size=30)
    button = ft.ElevatedButton(
        text="Перейти в Telegram",
        on_click=lambda _: page.launch_url("https://t.me/pakkkharev"),
        color=ft.colors.WHITE,
        bgcolor=ft.colors.BLUE_ACCENT
    )

    # Добавление элементов на страницу
    page.add(
        ft.Column(
            [
                text,
                button
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main, port=8000, view=None)
