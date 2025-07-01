import flet as ft


def hablaView(page, goFunc: callable, words, meanings, ft=ft):
    table = ft.Column(
        [
            ft.Row(
                [
                    ft.Container(
                        content=ft.Image(
                            src="Icons/Arrow right.png",
                            width=0.026 * page.width * 4,
                            height=0.026 * page.width * 4,
                        ),
                        on_click=lambda e: goFunc("/Nahuatl"),
                        width=0.026 * page.width * 4,
                        margin=ft.margin.only(right=10, top=30, bottom=20),
                    ),
                    ft.Container(
                        content=ft.Text(
                            "Practicar",
                            font_family="Monserrat Alternates",
                            size=24,
                            color=page.theme.color_scheme.on_background,
                        ),
                        margin=ft.margin.only(left=10, right=10, top=30, bottom=20),
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
        ],
        width=page.width * 4,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    for word, meaning in zip(words, meanings):
        table.controls.append(
            ft.Column(
                [
                    ft.Row(
                        [
                            ft.Container(
                                content=ft.Text(
                                    word,
                                    size=120 / len(word) if len(word) > 6 else 20,
                                    color=page.theme.color_scheme.on_background,
                                    font_family="Monserrat Alternates",
                                ),
                                width=0.1 * page.width * 4,
                                alignment=ft.alignment.center,
                            ),
                            ft.Container(
                                content=ft.Text(
                                    meaning,
                                    size=(
                                        210 / len(meaning)
                                        if 11 < len(meaning) < 20
                                        else 13
                                    ),
                                    color=page.theme.color_scheme.on_background,
                                    font_family="Monserrat Alternates",
                                    max_lines=None,  # Permite múltiples líneas
                                    text_align=ft.TextAlign.CENTER,  # Centra el texto
                                ),
                                width=0.1 * page.width * 4,
                                alignment=ft.alignment.center,  # Centra el contenedor horizontalmente
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        width=page.width * 4,
                    ),
                    ft.Container(
                        bgcolor=page.theme.color_scheme.primary_container,
                        width=0.24 * page.width * 4,
                        height=0.002 * page.width * 4,
                        border_radius=ft.border_radius.all(10),
                        margin=ft.margin.only(top=10, bottom=10),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

    table = ft.ListView(
        controls=table.controls,
        width=page.width * 4,
        height=page.height,  # Ajusta la altura según sea necesario
    )

    return table
