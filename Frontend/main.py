import flet as ft

from Router import Router

i = 0


def main(page: ft.Page):
    global i

    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary="#D97D54",
            secondary="#5C3A21",
            tertiary="#3B6B4D",
            background="#EFE8D8",
            on_background="#221A16",
            primary_container="#E8895F",
            on_primary_container="#2C0B00",
            surface="#FFFFFF",
            secondary_container="#6D492F",
        )
    )

    page.fonts = {
        "Monserrat Alternates": "Fonts/MontserratAlternates-Regular.ttf",
        "Monserrat Alternates(black)": "Fonts/MontserratAlternates-Black.ttf",
    }

    page.padding = ft.Padding(0, 0, 0, 0)
    page.bgcolor = page.theme.color_scheme.background
    page.scroll = ft.ScrollMode.HIDDEN
    page.padding = ft.Padding(0, 0, 0, 0)
    page.bgcolor = page.theme.color_scheme.background
    page.scroll = ft.ScrollMode.HIDDEN

    if i == 0:
        my_router = Router(page, ft)
        i += 1

    page.add(
        ft.Column(
            [my_router.body, my_router.appBar],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            height=page.height * 0.9,
        )
    )

    my_router.go("/")

    def onResize(e):
        print("resized")
        my_router.onPageResize()
        page.controls[0] = my_router.body
        page.update()

    # page.on_rute_change = my_router.routeChange
    page.on_resize = onResize

    # my_router.go("/Lecciones")  # Navigate to Lecciones view on startup
    print("Page initialized with width:", page.width, "and height:", page.height)
    page.update()


ft.app(target=main, assets_dir="Assets", view=ft.AppView.WEB_BROWSER, port=8080)
