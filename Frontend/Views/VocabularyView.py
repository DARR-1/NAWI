import flet as ft
from .PreguntaDefaultView import preguntaDefaultView
import random


def vocabularyView(page, goFunc: callable, words, meanings, ft=ft):

    def generate_question(index):
        correct_word = words[index]
        correct_meaning = meanings[index]

        # Generar opciones incorrectas
        incorrect_options = meanings[:index] + meanings[index + 1 :]
        incorrect_options = random.sample(
            incorrect_options, min(3, len(incorrect_options))
        )

        # Insertar la opción correcta en una posición aleatoria
        correct_position = random.randint(0, len(incorrect_options))
        options = (
            incorrect_options[:correct_position]
            + [correct_meaning]
            + incorrect_options[correct_position:]
        )

        return correct_word, options, correct_position

    word, options, correct_position = generate_question(0)
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
                        on_click=lambda e: goFunc(
                            "/preguntaDefault",
                            word=word,
                            meaning=options[correct_position],
                            respuestas=options,
                            words=words,  # Pasar palabras
                            meanings=meanings,  # Pasar significados
                        ),
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
        ],
        width=page.width * 4,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    for index in range(len(words)):
        word, options, correct_position = generate_question(index)
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
                        width=0.1 * page.width * 4,
                        alignment=ft.alignment.center,
                    ),
                    ft.Container(
                        bgcolor=page.theme.color_scheme.primary_container,
                        width=0.002 * page.width * 4,
                        height=0.04 * page.width * 4,
                        border_radius=ft.border_radius.all(10),
                        margin=ft.margin.only(top=10, bottom=10),
                    ),
                    ft.Container(
                        content=ft.Text(
                            options[correct_position],
                            size=(
                                220 / len(options[correct_position])
                                if len(options[correct_position]) > 11
                                else 20
                            ),
                            color=page.theme.color_scheme.on_background,
                            font_family="Monserrat Alternates",
                        ),
                        width=0.1 * page.width * 4,
                        alignment=ft.alignment.center,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                width=page.width * 4,
            )
        )

    table = ft.ListView(
        controls=table.controls,
        width=page.width * 4,
        height=page.height,  # Ajusta la altura según sea necesario
    )

    print("Opciones generadas:", options)

    return table
