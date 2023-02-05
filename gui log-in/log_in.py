import PySimpleGUI as sg


def log_in() -> None:
    """log in to system parking lot"""
    sg.theme("BluePurple")  # Add a touch of color
    # All the stuff inside your window.
    layout = [
        [sg.Text("Welcome to the Smart parking lot system!", font=(any, 20))],
        [sg.Text("User Name", size=(10, 1), font=(any, 15)), sg.InputText(size=20)],
        [sg.Text("password", size=(10, 1), font=(any, 15)), sg.InputText(size=20)],
        [sg.Text("")],
        [sg.Button("log-in", size=(6, 2)), sg.Cancel(size=(6, 2))],
    ]
    # Create the Window
    window = sg.Window(title="Parking system", layout=layout, size=(600, 250))
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in [
            sg.WIN_CLOSED,
            "Cancel",
        ]:  # if user closes window or clicks cancel
            break
        if is_valid_input(event, values):
            window.close()
            initialization()
    window.close()


def is_valid_input(event: object, values: dict) -> bool:
    """Checks validity of username and password

    Args:
        event (object): event from Button
        values (dict): Values from Buttons

    Returns:
        bool: True if the username and password are correct
    """
    if event == "log-in":
        if values[0] and values[1]:
            if values[0] == "king" and values[1] == "1234":
                return True
            else:
                sg.popup(
                    "You must specify a valid username and password",
                    title="ERROR",
                    font=10,
                )
        else:
            sg.popup("Fill all the fields", title="ERROR", font=10)


def initialization():
    """The system settings. (the amount of parking spaces and their types)"""
    sg.theme("BluePurple")  # Add a touch of color
    # All the stuff inside your window.
    layout = [
        [sg.Text("Welcome to the Smart parking system!", font=(any, 20))],
        [
            sg.Text(
                "How many Bus parking spaces do you have?", font=(any, 15), size=40
            ),
            sg.InputText(size=10),
        ],
        [
            sg.Text(
                "How many Car parking spaces do you have?", font=(any, 15), size=40
            ),
            sg.InputText(size=10),
        ],
        [
            sg.Text(
                "How many Motorcycle parking spaces do you have?",
                font=(any, 15),
                size=40,
            ),
            sg.InputText(size=10),
        ],
        [sg.Text("")],
        [sg.Button("start", size=(6, 2)), sg.Exit(size=(6, 2))],
    ]
    # Create the Window
    window = sg.Window(title="Parking system", layout=layout, size=(650, 250))
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in [
            sg.WIN_CLOSED,
            "Exit",
        ]:  # if user closes window or clicks cancel
            break
        if event == "start":

            break
    window.close()
