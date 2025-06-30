import flet as ft


def leccionesView(page, goFunc: callable, ft=ft):
    content = ft.Column(
        [
            ft.Container(
                content=ft.Image(
                    src="Icons/Arrow right.png",
                    width=0.026 * page.width,
                    height=0.026 * page.width,
                ),
                on_click=lambda e: goFunc("/Profesores"),
                width=0.026 * page.width,
                height=0.026 * page.width,
                margin=ft.margin.only(
                    0.005 * page.width,
                    0.015 * page.width,
                    0 * page.width,
                    0.004 * page.width,
                ),
            ),
            ft.Container(
                content=ft.Text(
                    "Tus Lecciones",
                    font_family="Monserrat Alternates",
                    size=24,
                    color=page.theme.color_scheme.on_background,
                ),
                margin=ft.margin.only(
                    0.014 * page.width,
                    0.0 * page.width,
                    0.0 * page.width,
                    0.0 * page.width,
                ),
            ),
            ft.Container(
                content=ft.Column(
                    [
                        ft.Column(
                            [
                                ft.Row(
                                    [
                                        ft.Container(
                                            width=0.085 * page.width,
                                            height=0.001 * page.width,
                                            bgcolor=page.theme.color_scheme.tertiary,
                                        ),
                                        ft.Text(
                                            "Hoy",
                                            font_family="Monserrat Alternates",
                                            size=24,
                                            color=page.theme.color_scheme.on_background,
                                        ),
                                        ft.Container(
                                            width=0.085 * page.width,
                                            height=0.001 * page.width,
                                            bgcolor=page.theme.color_scheme.tertiary,
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                                ft.Text(
                                    "Ningún docente ha asignado tareas para este día.",
                                    font_family="Monserrat Alternates",
                                    size=16,
                                    color=page.theme.color_scheme.on_background,
                                    text_align=ft.TextAlign.CENTER,
                                ),
                            ],
                            width=1 * page.width,
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ],
                    width=1 * page.width,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                margin=ft.margin.only(
                    0.014 * page.width,
                    0.015 * page.width,
                    0.014 * page.width,
                    0.014 * page.width,
                ),
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.START,
        alignment=ft.MainAxisAlignment.START,
        width=1 * page.width,
    )
    return content
