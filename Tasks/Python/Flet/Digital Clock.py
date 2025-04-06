import flet as ft

#COLORS
COLOR_BG = "#1E1E1E"
COLOR_WHITE = "#E0E0E0"
COLOR_PRIMARY = "#4CAF50"
COLOR_SECONDARY = "#757575"

def main(page: ft.Page):
    page.title = "PWD Digital Clock"
    page.window.width = 400
    page.window.height = 500
    page.window.bgcolor = COLOR_WHITE
    page.window.resizable = False
    page.window.icon = "../Banco de Imagenes/int exp.png"

    title_label = ft.Text("Digital Clock", color=COLOR_PRIMARY, size=30, weight="bold")
    label_time = ft.Text("00:00:00", color=COLOR_WHITE, size=45, weight="bold")
    label_info = ft.Text("", size=20, color= COLOR_SECONDARY)

    city_input = ft.TextField("Enter City Name", text_align="center", bgcolor="#333333", color=COLOR_WHITE, width=200, border_radius=8)
    weather_label = ft.Text("", color=COLOR_WHITE, size=16)

    update_button = ft.ElevatedButton(
        "Update Weather", 
        icon=ft.icons.SEARCH,
        color=COLOR_WHITE, 
        bgcolor=COLOR_PRIMARY, 
        style=ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=10))
        )


    container = ft.Container(
        ft.Column(
            [
                ft.Icon(name=ft.icons.ACCESS_TIME, size=50, color=COLOR_PRIMARY, shadows=ft.BoxShadow(color="#ffffff")),
                title_label,
                label_time,
                label_info,
                city_input,
                update_button,
                weather_label,

            ],
            alignment= ft.MainAxisAlignment.CENTER,
            ),
            padding=15,
            border_radius=10,
            bgcolor="#2C2C2C",
    )
    page.add(container)


ft.app(main)