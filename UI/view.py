import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None

        # graphical elements
        self._title = None
        self.txt_name = None

        self.btn_graph = None
        self.btn_countedges = None
        self.btn_search = None

        self.txt_result = None
        self.txt_result2 = None
        self.txt_result3 = None

        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Esame 14-09-2022", color="blue", size=24)
        self._page.controls.append(self._title)

        self._txtDurata = ft.TextField(label="Durata")
        self.btn_graph = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handle_graph)

        row1 = ft.Row([ft.Container(self._txtDurata, width=400), ft.Container(self.btn_graph, width=300)],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self._ddAlbum = ft.Dropdown(label="Album", width=400, disabled=True)

        self._btnAnalisi = ft.ElevatedButton(text="Analisi componente", disabled=True, on_click=self._controller.handle_analisi)

        row2 = ft.Row([ft.Container(self._ddAlbum, width=400), ft.Container(self._btnAnalisi, width=300)], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        self.txt_result1 = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result1)

        self._txtSoglia = ft.TextField(label="Soglia", width=400, disabled=True)

        self._btnSetAlbum = ft.ElevatedButton(text="Set di Album",
                                              on_click=self._controller.handle_set_album, width=200, disabled=True)
        row3 = ft.Row([ft.Container(self._txtSoglia, width=400), ft.Container(self._btnSetAlbum, width=300)], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # List View where the reply is printed
        self.txt_result2 = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)
        self._page.controls.append(self.txt_result2)
        self._page.update()

        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
