import flet as ft


def profesoresView(page, goFunc: callable, ft=ft):
    onHoverContainer = ft.Row(
        [
            ft.Container(
                content=ft.Column(
                    [
                        ft.Image(
                            src="Icons/Book.png",
                            width=0.03 * page.width * 4,
                            height=0.03 * page.width * 4,
                        ),
                        ft.Text(
                            "Lecciones",
                            font_family="Monserrat Alternates",
                            size=0.007 * page.width * 4,
                            color=page.theme.color_scheme.surface,
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                height=0.05 * page.width * 4,
                padding=0,
                ink=True,
                on_click=lambda e: goFunc("/Lecciones"),
            ),
            ft.Container(
                width=0.001 * page.width * 4,
                height=0.1 * page.width * 4,
                bgcolor=page.theme.color_scheme.surface,
                padding=0,
            ),
            ft.Container(
                content=ft.Column(
                    [
                        ft.Image(
                            src="Icons/User minus.png",
                            width=0.03 * page.width * 4,
                            height=0.03 * page.width * 4,
                        ),
                        ft.Text(
                            "Eliminar",
                            font_family="Monserrat Alternates",
                            size=0.007 * page.width * 4,
                            color=page.theme.color_scheme.surface,
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                height=0.05 * page.width * 4,
                padding=0,
                ink=True,
                on_click=lambda e: goFunc("/Lecciones"),
            ),
            ft.Container(
                width=0.001 * page.width * 4,
                height=0.1 * page.width * 4,
                bgcolor=page.theme.color_scheme.surface,
                padding=0,
            ),
            ft.Container(
                content=ft.Column(
                    [
                        ft.Image(
                            src="Icons/Link.png",
                            width=0.03 * page.width * 4,
                            height=0.03 * page.width * 4,
                        ),
                        ft.Text(
                            "Comunicarse",
                            font_family="Monserrat Alternates",
                            size=0.007 * page.width * 4,
                            color=page.theme.color_scheme.surface,
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                height=0.05 * page.width * 4,
                padding=0,
                ink=True,
                on_click=lambda e: goFunc("/Lecciones"),
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        width=0.22 * page.width * 4,
        height=0.085 * page.width * 4,
    )
    defaultContent = ft.Row(
        [
            ft.Image(
                src="Icons/FotoDocentePrueba.png",
                width=0.075 * page.width * 4,
                height=0.05 * page.width * 4,
            ),
            ft.Column(
                [
                    ft.Text(
                        "Nombre del Docente",
                        font_family="Monserrat Alternates",
                        size=0.01 * page.width * 4,
                        color=page.theme.color_scheme.on_background,
                    ),
                    ft.Text(
                        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
                        font_family="Monserrat Alternates",
                        size=0.005 * page.width * 4,
                        color=page.theme.color_scheme.on_background,
                        width=0.12 * page.width * 4,
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                height=0.07 * page.width * 4,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        width=0.22 * page.width * 4,
        height=0.085 * page.width * 4,
    )

    def onHover(e):
        e.control.bgcolor = (
            page.theme.color_scheme.on_primary_container
            if e.data == "true"
            else page.theme.color_scheme.primary_container
        )
        e.control.content = onHoverContainer if e.data == "true" else defaultContent

        e.control.update()

    content = ft.Container(
        content=ft.Column(
            [
                ft.Container(
                    content=ft.Row(
                        [
                            ft.Text(
                                "Tus docentes",
                                font_family="Monserrat Alternates",
                                size=0.02 * page.width * 4,
                                color=page.theme.color_scheme.on_background,
                            ),
                            ft.Container(
                                content=ft.Image(
                                    src="Icons/User plus.png",
                                    width=0.05 * page.width * 4,
                                    height=0.05 * page.width * 4,
                                ),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    width=page.width * 4,
                    padding=ft.padding.only(
                        0.01 * page.width * 4,
                        0.02 * page.width * 4,
                        0.01 * page.width * 4,
                        0.015 * page.width * 4,
                    ),
                ),
                ft.Container(
                    content=defaultContent,
                    width=0.22 * page.width * 4,
                    height=0.085 * page.width * 4,
                    padding=ft.padding.only(
                        0.01 * page.width * 4,
                        0.02 * page.width * 4,
                        0.01 * page.width * 4,
                        0.015 * page.width * 4,
                    ),
                    bgcolor=page.theme.color_scheme.primary_container,
                    border_radius=20,
                    alignment=ft.alignment.center,
                    margin=0,
                    on_hover=onHover,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    return content
