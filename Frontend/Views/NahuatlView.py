import flet as ft


def getContainer(page, goFunc: callable, route, topic: str, ft=ft):
    return ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    topic,
                    font_family="Monserrat Alternates",
                    size=24,
                    color=page.theme.color_scheme.on_primary_container,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.ProgressRing(
                    value=0.15,
                    stroke_width=5 * 0.6,
                    bgcolor=page.theme.color_scheme.surface,
                    color=page.theme.color_scheme.on_primary_container,
                    stroke_cap=ft.StrokeCap.ROUND,
                    width=page.width * 4 * 0.113 * 0.6,
                    height=page.width * 4 * 0.113 * 0.6,
                    stroke_align=0,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        width=page.width * 4 * 0.2,
        height=page.width * 4 * 0.13,
        bgcolor=page.theme.color_scheme.primary_container,
        border_radius=ft.border_radius.all(29),
        alignment=ft.alignment.center,
        ink=True,
        ink_color=page.theme.color_scheme.tertiary,
        on_click=lambda e: goFunc(route),
        margin=ft.margin.only(bottom=10, left=10),
    )


def nahuatlView(page, goFunc: callable, ft=ft):
    content = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Container(
                            content=ft.ProgressBar(
                                width=page.width * 4 * 0.18,
                                height=page.width * 4 * 0.003,
                                color=page.theme.color_scheme.primary,
                                bgcolor=page.theme.color_scheme.secondary_container,
                                value=0.1,
                                border_radius=ft.border_radius.all(10),
                            ),
                            margin=ft.margin.only(left=10, right=0, top=75, bottom=0),
                        ),
                        ft.Container(
                            content=ft.Text(
                                "Unit 1",
                                font_family="Monserrat Alternates",
                                size=15,
                                color=page.theme.color_scheme.on_background,
                            ),
                            alignment=ft.alignment.center,
                            width=page.width * 4 * 0.05,
                            margin=ft.margin.only(left=10, right=0, top=75, bottom=0),
                        ),
                    ]
                ),
                ft.Container(
                    content=ft.Text(
                        "¿Qué vamos a aprender hoy?",
                        font_family="Monserrat Alternates(black)",
                        size=20,
                        color=page.theme.color_scheme.on_background,
                    ),
                    alignment=ft.alignment.center,
                    width=page.width * 4,
                ),
                ft.Container(
                    content=ft.Text(
                        "Vocabulario",
                        font_family="Monserrat Alternates",
                        size=20,
                        color=page.theme.color_scheme.on_background,
                    ),
                    margin=ft.margin.only(left=10),
                ),
                ft.Row(
                    [
                        getContainer(
                            page, goFunc, "/VocabularyView/Alphabet", "El Alfabeto", ft
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=10,
                    height=page.width * 4 * 0.15,
                    width=page.width * 4 * 2,
                ),
                ft.Container(
                    content=ft.Text(
                        "Habla",
                        font_family="Monserrat Alternates",
                        size=20,
                        color=page.theme.color_scheme.on_background,
                    ),
                    margin=ft.margin.only(left=10),
                ),
                ft.Row(
                    [
                        getContainer(
                            page, goFunc, "/HablaView/Alphabet", "El Alfabeto", ft
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=10,
                    height=page.width * 4 * 0.15,
                    width=page.width * 4 * 2,
                ),
                ft.Container(
                    content=ft.Text(
                        "Escucha",
                        font_family="Monserrat Alternates",
                        size=20,
                        color=page.theme.color_scheme.on_background,
                    ),
                    margin=ft.margin.only(left=10),
                ),
                ft.Row(
                    [
                        getContainer(
                            page, goFunc, "/HablaView/Alphabet", "El Alfabeto", ft
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=10,
                    height=page.width * 4 * 0.15,
                    width=page.width * 4 * 2,
                ),
            ]
        )
    )
    return content
