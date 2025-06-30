import flet as ft


def homeView(page: ft.Page, goFunc: callable, ft=ft):
    content = ft.Container(
        content=ft.Column(
            [
                ft.Container(
                    content=ft.Row(
                        [
                            ft.Image(
                                src="Icons/GenericAvatar.png",
                                width=40 * page.width / 1500,
                                height=40 * page.width / 1500,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                            ft.Image(
                                src=f"Icons/Settings.png",
                                width=27 * page.width / 1500,
                                height=27 * page.width / 1500,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    margin=ft.margin.only(20, 80, 20, 10),
                ),
                ft.Row(
                    [
                        ft.Text(
                            "  Tus cursos",
                            font_family="Monserrat Alternates",
                            size=32 * 0.8,
                            color=page.theme.color_scheme.on_background,
                        )
                    ]
                ),
                ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.Text(
                                                "Nahuatl",
                                                font_family="Monserrat Alternates",
                                                size=24 * 0.6,
                                                color=page.theme.color_scheme.on_primary_container,
                                            ),
                                            ft.ProgressRing(
                                                value=0.15,
                                                stroke_width=5 * 0.6,
                                                bgcolor=page.theme.color_scheme.surface,
                                                color=page.theme.color_scheme.on_primary_container,
                                                stroke_cap=ft.StrokeCap.ROUND,
                                                width=page.width * 0.113 * 0.6,
                                                height=page.width * 0.113 * 0.6,
                                                stroke_align=0,
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    ),
                                    width=page.width * 0.21 * 0.6,
                                    height=page.width * 0.21 * 0.6,
                                    bgcolor=page.theme.color_scheme.primary_container,
                                    border_radius=ft.border_radius.all(29),
                                    alignment=ft.alignment.center,
                                    ink=True,
                                    ink_color=page.theme.color_scheme.tertiary,
                                    on_click=lambda e: goFunc("/Nahuatl"),
                                ),
                                ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.Text(
                                                "Mazahuatl",
                                                font_family="Monserrat Alternates",
                                                size=24 * 0.6,
                                                color=page.theme.color_scheme.on_primary_container,
                                            ),
                                            ft.ProgressRing(
                                                value=0.45,
                                                stroke_width=5 * 0.6,
                                                bgcolor=page.theme.color_scheme.surface,
                                                color=page.theme.color_scheme.on_primary_container,
                                                stroke_cap=ft.StrokeCap.ROUND,
                                                width=page.width * 0.113 * 0.6,
                                                height=page.width * 0.113 * 0.6,
                                                stroke_align=0,
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    ),
                                    width=page.width * 0.21 * 0.6,
                                    height=page.width * 0.21 * 0.6,
                                    bgcolor=page.theme.color_scheme.primary_container,
                                    border_radius=ft.border_radius.all(29),
                                    alignment=ft.alignment.center,
                                    ink=True,
                                    ink_color=page.theme.color_scheme.tertiary,
                                    on_click=lambda e: page.go("/mazahuatl"),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            [
                                ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.Text(
                                                "Maya",
                                                font_family="Monserrat Alternates",
                                                size=24 * 0.6,
                                                color=page.theme.color_scheme.on_primary_container,
                                            ),
                                            ft.ProgressRing(
                                                value=0.15,
                                                stroke_width=5 * 0.6,
                                                bgcolor=page.theme.color_scheme.surface,
                                                color=page.theme.color_scheme.on_primary_container,
                                                stroke_cap=ft.StrokeCap.ROUND,
                                                width=page.width * 0.113 * 0.6,
                                                height=page.width * 0.113 * 0.6,
                                                stroke_align=0,
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    ),
                                    width=page.width * 0.21 * 0.6,
                                    height=page.width * 0.21 * 0.6,
                                    bgcolor=page.theme.color_scheme.primary_container,
                                    border_radius=ft.border_radius.all(29),
                                    alignment=ft.alignment.center,
                                    ink=True,
                                    ink_color=page.theme.color_scheme.tertiary,
                                    on_click=lambda e: page.go("/maya"),
                                ),
                                ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.Image(
                                                src="Icons/Plus.png",
                                                width=100 * page.width / 1500,
                                                height=100 * page.width / 1500,
                                                fit=ft.ImageFit.CONTAIN,
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    ),
                                    width=page.width * 0.21 * 0.6,
                                    height=page.width * 0.21 * 0.6,
                                    border_radius=ft.border_radius.all(29),
                                    alignment=ft.alignment.center,
                                    ink=True,
                                    ink_color=page.theme.color_scheme.tertiary,
                                    on_click=lambda e: page.go("/mazahuatl"),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ]
                ),
            ]
        ),
        width=page.width,
        bgcolor=page.theme.color_scheme.background,
    )

    return content
