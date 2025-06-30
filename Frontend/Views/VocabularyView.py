import flet as ft


def vocabularyView(page, goFunc: callable, words, meanings, ft=ft):
    table = ft.Column(
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
                            "Practicar",
                            font_family="Monserrat Alternates",
                            size=24,
                            color=page.theme.color_scheme.on_background,
                        ),
                        margin=ft.margin.only(left=10, right=10, top=30),
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
        ],
        width=page.width,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    for word, meaning in zip(words, meanings):
        table.controls.append(
            ft.Row(
                [
                    ft.Container(
                        content=ft.Text(
                            word,
                            size=120 / len(word) if len(word) > 6 else 20,
                            color=page.theme.color_scheme.on_background,
                            font_family="Monserrat Alternates",
                        ),
                        width=0.1 * page.width,
                        alignment=ft.alignment.center,
                    ),
                    ft.Container(
                        bgcolor=page.theme.color_scheme.primary_container,
                        width=0.002 * page.width,
                        height=0.04 * page.width,
                        border_radius=ft.border_radius.all(10),
                        margin=ft.margin.only(top=10, bottom=10),
                    ),
                    ft.Container(
                        content=ft.Text(
                            meaning,
                            size=220 / len(meaning) if len(meaning) > 11 else 20,
                            color=page.theme.color_scheme.on_background,
                            font_family="Monserrat Alternates",
                        ),
                        width=0.1 * page.width,
                        alignment=ft.alignment.center,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                width=page.width,
            )
        )

    table = ft.ListView(
        controls=table.controls,
        width=page.width,
        height=page.height - 0.026 * page.width,  # Ajusta la altura según sea necesario
    )

    return table
