import flet as ft
import random
import pandas as pd


def preguntaDefaultView(
    page,
    goFunc: callable,
    ft=ft,
    pregunta="",
    respuestas=[],
    word="",
    meaning="",
    current_index=0,
    total_questions=10,  # Número total de preguntas
    words=None,  # Recibir palabras desde el Router
    meanings=None,  # Recibir significados desde el Router
):
    total_questions = len(words) if words is not None else 10
    # Usa los parámetros word y meaning para personalizar la vista
    pregunta = pregunta or f"¿Cuál es el significado de '{word}'?"
    respuestas = respuestas or [meaning, "Opción 2", "Opción 3", "Opción 4"]

    # Asegurarse de que las respuestas tengan exactamente 4 elementos
    while len(respuestas) < 4:
        respuestas.append(f"Opción {len(respuestas) + 1}")

    print("Respuestas recibidas:", respuestas)  # Registro de depuración

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

    def next_question():
        if current_index + 1 < total_questions:
            word, options, correct_position = generate_question(current_index + 1)
            goFunc(
                "/preguntaDefault",
                current_index=current_index + 1,
                total_questions=total_questions,
                word=word,
                meaning=options[correct_position],
                respuestas=options,
                words=words,
                meanings=meanings,
            )
        else:
            goFunc("/Nahuatl")

    def calculate_text_size(text, base_size=30, max_length=10):
        """
        Calcula el tamaño del texto basado en su longitud.
        Si el texto tiene más de max_length caracteres, reduce el tamaño proporcionalmente.
        """
        if len(text) > max_length:
            return base_size * (max_length / len(text))
        return base_size

    # Modificar el botón "Saltar" y las respuestas para llamar a next_question
    content = ft.Container(
        content=ft.Column(
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
                            margin=ft.margin.only(right=10, top=10),
                        ),
                        ft.Container(
                            content=ft.Text(
                                "Saltar",
                                font_family="Monserrat Alternates",
                                size=24,
                                color=page.theme.color_scheme.on_background,
                            ),
                            margin=ft.margin.only(left=10, right=10, top=30),
                            on_click=lambda e: next_question(),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Container(
                    content=ft.Text(
                        pregunta,
                        font_family="Monserrat Alternates",
                        size=30,
                        color=page.theme.color_scheme.on_background,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    alignment=ft.alignment.center,
                    width=page.width * 4,
                    margin=ft.margin.only(top=20, bottom=20),
                ),
                ft.Column(
                    [
                        ft.Container(
                            content=ft.Text(
                                respuestas[0] if respuestas else "1",
                                size=calculate_text_size(
                                    respuestas[0] if respuestas else "1"
                                ),
                                color=page.theme.color_scheme.on_primary_container,
                                font_family="Monserrat Alternates",
                            ),
                            width=page.width * 4 * 0.7,
                            height=page.width * 4 * 0.055,
                            bgcolor=page.theme.color_scheme.primary_container,
                            border_radius=ft.border_radius.all(25),
                            alignment=ft.alignment.center,
                            margin=ft.margin.only(bottom=page.height * 0.01),
                            ink=True,
                            ink_color=page.theme.color_scheme.tertiary,
                            on_click=lambda e: next_question(),
                        ),
                        ft.Container(
                            content=ft.Text(
                                respuestas[1] if len(respuestas) > 1 else "4",
                                size=calculate_text_size(
                                    respuestas[1] if len(respuestas) > 1 else "4"
                                ),
                                color=page.theme.color_scheme.on_primary_container,
                                font_family="Monserrat Alternates",
                            ),
                            width=page.width * 4 * 0.7,
                            height=page.width * 4 * 0.055,
                            bgcolor=page.theme.color_scheme.primary_container,
                            border_radius=ft.border_radius.all(25),
                            alignment=ft.alignment.center,
                            margin=ft.margin.only(bottom=page.height * 0.01),
                            ink=True,
                            ink_color=page.theme.color_scheme.tertiary,
                            on_click=lambda e: next_question(),
                        ),
                        ft.Container(
                            content=ft.Text(
                                respuestas[2] if len(respuestas) > 2 else "3",
                                size=calculate_text_size(
                                    respuestas[2] if len(respuestas) > 2 else "3"
                                ),
                                color=page.theme.color_scheme.on_primary_container,
                                font_family="Monserrat Alternates",
                            ),
                            width=page.width * 4 * 0.7,
                            height=page.width * 4 * 0.055,
                            bgcolor=page.theme.color_scheme.primary_container,
                            border_radius=ft.border_radius.all(25),
                            alignment=ft.alignment.center,
                            margin=ft.margin.only(bottom=page.height * 0.01),
                            ink=True,
                            ink_color=page.theme.color_scheme.tertiary,
                            on_click=lambda e: next_question(),
                        ),
                        ft.Container(
                            content=ft.Text(
                                respuestas[3] if len(respuestas) > 3 else "2",
                                size=calculate_text_size(
                                    respuestas[3] if len(respuestas) > 3 else "2"
                                ),
                                color=page.theme.color_scheme.on_primary_container,
                                font_family="Monserrat Alternates",
                            ),
                            width=page.width * 4 * 0.7,
                            height=page.width * 4 * 0.055,
                            bgcolor=page.theme.color_scheme.primary_container,
                            border_radius=ft.border_radius.all(25),
                            alignment=ft.alignment.center,
                            margin=ft.margin.only(bottom=page.height * 0.01),
                            ink=True,
                            ink_color=page.theme.color_scheme.tertiary,
                            on_click=lambda e: next_question(),
                        ),
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Container(
                    content=ft.Text(
                        f"{current_index + 1}/{total_questions}",
                        font_family="Monserrat Alternates",
                        size=30,
                        color=page.theme.color_scheme.on_background,
                    ),
                    margin=ft.margin.only(right=10, top=5),
                    alignment=ft.alignment.center_right,
                    width=page.width * 4,
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
        ),
        padding=ft.padding.all(20),
    )
    return content
