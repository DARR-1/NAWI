import flet as ft


def preguntaDefaultView(page, goFunc: callable, ft=ft):
    content = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Image(
                                src="Icons/Arrow right.png",
                                width=0.026 * page.width,
                                height=0.026 * page.width,
                            ),
                            on_click=lambda e: goFunc("/Nahuatl"),
                            width=0.026 * page.width,
                            margin=ft.margin.only(right=10, top=30),
                        ),
                        ft.Container(
                            content=ft.Text(
                                "Saltar",
                                font_family="Monserrat Alternates",
                                size=24,
                                color=page.theme.color_scheme.on_background,
                            ),
                            margin=ft.margin.only(left=10, right=10, top=30),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Container(
                    content=ft.Text(
                        "¿Cuanto es dos mas dos?",
                        font_family="Monserrat Alternates",
                        size=30,
                        color=page.theme.color_scheme.on_background,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    alignment=ft.alignment.center,
                    width=page.width,
                    margin=ft.margin.only(top=20, bottom=20),
                ),
                ft.Column(
                    [
                        ft.Container(
                            content=ft.Text(
                                "5",
                                size=30,
                                color=page.theme.color_scheme.on_primary_container,
                                font_family="Monserrat Alternates",
                            ),
                            width=page.width * 0.7,
                            height=page.width * 0.055,
                            bgcolor=page.theme.color_scheme.primary_container,
                            border_radius=ft.border_radius.all(25),
                            alignment=ft.alignment.center,
                            margin=ft.margin.only(bottom=18),
                            ink=True,
                            ink_color=page.theme.color_scheme.tertiary,
                            on_click=lambda e: print("Respuesta seleccionada: 5"),
                        ),
                        ft.Container(
                            content=ft.Text(
                                "4",
                                size=30,
                                color=page.theme.color_scheme.on_primary_container,
                                font_family="Monserrat Alternates",
                            ),
                            width=page.width * 0.7,
                            height=page.width * 0.055,
                            bgcolor=page.theme.color_scheme.primary_container,
                            border_radius=ft.border_radius.all(25),
                            alignment=ft.alignment.center,
                            margin=ft.margin.only(bottom=18),
                            ink=True,
                            ink_color=page.theme.color_scheme.tertiary,
                            on_click=lambda e: print("Respuesta seleccionada: 4"),
                        ),
                        ft.Container(
                            content=ft.Text(
                                "3",
                                size=30,
                                color=page.theme.color_scheme.on_primary_container,
                                font_family="Monserrat Alternates",
                            ),
                            width=page.width * 0.7,
                            height=page.width * 0.055,
                            bgcolor=page.theme.color_scheme.primary_container,
                            border_radius=ft.border_radius.all(25),
                            alignment=ft.alignment.center,
                            margin=ft.margin.only(bottom=18),
                            ink=True,
                            ink_color=page.theme.color_scheme.tertiary,
                            on_click=lambda e: print("Respuesta seleccionada: 3"),
                        ),
                        ft.Container(
                            content=ft.Text(
                                "2",
                                size=30,
                                color=page.theme.color_scheme.on_primary_container,
                                font_family="Monserrat Alternates",
                            ),
                            width=page.width * 0.7,
                            height=page.width * 0.055,
                            bgcolor=page.theme.color_scheme.primary_container,
                            border_radius=ft.border_radius.all(25),
                            alignment=ft.alignment.center,
                            margin=ft.margin.only(bottom=18),
                            ink=True,
                            ink_color=page.theme.color_scheme.tertiary,
                            on_click=lambda e: print("Respuesta seleccionada: 2"),
                        ),
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Container(
                    content=ft.Text(
                        "8/24",
                        font_family="Monserrat Alternates",
                        size=30,
                        color=page.theme.color_scheme.on_background,
                    ),
                    margin=ft.margin.only(right=10, top=5),
                    alignment=ft.alignment.center_right,
                    width=page.width,
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
        ),
        padding=ft.padding.all(20),
    )
    return content
