from Views.HomeView import homeView
from Views.NahuatlView import nahuatlView
from Views.ProfesoresView import profesoresView
from Views.LeccionesView import leccionesView
from Views.PreguntaDefaultView import preguntaDefaultView
from Views.VocabularyView import vocabularyView
from Views.HablaView import hablaView
import pandas as pd
import flet as ft

# from Views.MazahuatlView import mazahuatlView
# from Views.MayaView import mayaView


class Router:

    def __init__(self, page, ft):
        dfVocabulary = pd.read_csv("database/vocabulary/unit1.csv")
        dfListen = pd.read_csv("database/listening/unit1.csv")
        self.page = page
        self.ft = ft
        self.page_width = page.width
        self.page_height = page.height
        self.routes = {
            "/": homeView(page, goFunc=self.go, ft=ft),
            "/Nahuatl": nahuatlView(
                page, goFunc=self.go, ft=ft
            ),  # Example route, can be replaced with actual views
            # "/Mazahuatl": mazahuatlView(page, ft),
            # "/Maya": mayaView(page, ft),
            "/Profesores": profesoresView(page, goFunc=self.go, ft=ft),
            "/Lecciones": leccionesView(page, goFunc=self.go, ft=ft),
            "/preguntaDefault": preguntaDefaultView(page, goFunc=self.go, ft=ft),
            "/VocabularyView/Alphabet": vocabularyView(
                page,
                goFunc=self.go,
                words=[dfVocabulary.columns[0]] + dfVocabulary.iloc[:, 0].tolist(),
                meanings=[dfVocabulary.columns[1]] + dfVocabulary.iloc[:, 1].tolist(),
                ft=ft,
            ),
            "/HablaView/Alphabet": hablaView(
                page,
                goFunc=self.go,
                words=[dfListen.columns[0]] + dfListen.iloc[:, 0].tolist(),
                meanings=[dfListen.columns[1]] + dfListen.iloc[:, 1].tolist(),
                ft=ft,
            ),
        }
        self.body = ft.Container(content=self.routes["/"])
        self.appBar = ft.Container()

    def go(self, route):
        if route in self.routes:
            print(f"Navigating to {route}")
            self.page.route = route
            self.page.update()
            self.routeChange(route)
        else:
            print(f"Route {route} not found")

    def routeChange(self, route):
        ft = self.ft

        self.body.content = self.routes[route]
        if (
            route != "/"
            and route != "/Lecciones"
            and route != "/preguntaDefault"
            and route != "/VocabularyView/Alphabet"
            and route != "/HablaView/Alphabet"
        ):
            self.appBar.content = ft.Container(
                content=ft.Row(
                    [
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Image(
                                        src="Icons/Home.png",
                                        width=0.017 * self.page_width,
                                        height=0.017 * self.page_width,
                                    ),
                                    ft.Text(
                                        "Inicio",
                                        size=0.008 * self.page_width,
                                        color=self.page.theme.color_scheme.on_background,
                                        font_family="Monserrat Alternates",
                                    ),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                height=0.05 * self.page_width,
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            on_click=lambda e: self.go("/"),
                            ink=True,
                        ),
                        ft.Container(
                            ft.Column(
                                [
                                    ft.Image(
                                        src="Icons/Trending up.png",
                                        width=0.017 * self.page_width,
                                        height=0.017 * self.page_width,
                                    ),
                                    ft.Text(
                                        "Progreso",
                                        size=0.008 * self.page_width,
                                        color=self.page.theme.color_scheme.on_background,
                                        font_family="Monserrat Alternates",
                                    ),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                height=0.05 * self.page_width,
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            on_click=lambda e: self.go("/"),
                            ink=True,
                        ),
                        ft.Container(
                            ft.Column(
                                [
                                    ft.Container(
                                        content=ft.Image(
                                            src="Icons/Book open.png",
                                            width=0.017 * self.page_width,
                                            height=0.017 * self.page_width,
                                        ),
                                        bgcolor=self.page.theme.color_scheme.tertiary_container,
                                        width=0.05 * self.page_width,
                                        height=0.02 * self.page_width,
                                        border_radius=15,
                                    ),
                                    ft.Text(
                                        "Biblioteca",
                                        size=0.008 * self.page_width,
                                        color=self.page.theme.color_scheme.on_background,
                                        font_family="Monserrat Alternates",
                                    ),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                height=0.05 * self.page_width,
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            on_click=lambda e: self.go("/Nahuatl"),
                            ink=True,
                        ),
                        ft.Container(
                            ft.Column(
                                [
                                    ft.Image(
                                        src="Icons/User.png",
                                        width=0.017 * self.page_width,
                                        height=0.017 * self.page_width,
                                    ),
                                    ft.Text(
                                        "Docente",
                                        size=0.008 * self.page_width,
                                        color=self.page.theme.color_scheme.on_background,
                                        font_family="Monserrat Alternates",
                                    ),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                height=0.05 * self.page_width,
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            on_click=lambda e: self.go("/Profesores"),
                            ink=True,
                        ),
                        ft.Container(
                            ft.Column(
                                [
                                    ft.Image(
                                        src="Icons/GenericAvatar.png",
                                        width=0.017 * self.page_width,
                                        height=0.017 * self.page_width,
                                    ),
                                    ft.Text(
                                        "User Name",
                                        size=0.008 * self.page_width,
                                        color=self.page.theme.color_scheme.on_background,
                                        font_family="Monserrat Alternates",
                                    ),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                height=0.05 * self.page_width,
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            on_click=lambda e: self.go("/"),
                            ink=True,
                        ),
                    ],
                    width=self.page_width,
                    height=0.05 * self.page_width,
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                ),
                width=self.page_width,
                height=0.05 * self.page_width,
                bgcolor=self.page.theme.color_scheme.surface,
            )
            print(self.page_width, self.page_height)
        else:
            self.appBar.content = ft.Container()

        self.appBar.update()
        self.body.update()

        print("Ruta cambiada", route)

    def onPageResize(self):
        self.page_width = self.page.width
        self.page_height = self.page.height
        self.routes = {
            "/": homeView(self.page, self.page_width, self.page_height),
        }
        self.body = self.routes["/"]
