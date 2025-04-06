import flet
from flet import IconButton, Page, Row, TextField, icons

def main(page: Page):

    page.adaptive = True
    #page.bgcolor = "#f0f0f0"
    page.title = "Counter"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.window.width = 300
    page.window.height = 200
    

    txt_number = TextField(value="0", text_align="center", width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        Row(
            [
                IconButton(icons.REMOVE, on_click=minus_click),
                txt_number,
                IconButton(icons.ADD, on_click=plus_click),
            ],
            alignment="center",
        )
    )

flet.app(target=main)