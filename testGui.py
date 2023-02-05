import PySimpleGUI as sg

def log_in_window() -> None:
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
    return sg.Window(title="Parking system", layout=layout, size=(600, 250),finalize=True)
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
    return sg.Window(title="Parking system", layout=layout, size=(650, 250),finalize=True)
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

def main_window():
    sg.theme("BlueMono")
    layout = [
        [
            sg.Button("Add_car", size=(6, 4)),
            sg.Button("Remove_car", size=(6, 4)),
            sg.Button("Reports", size=(6, 4), pad=((350, 50), 50)),
        ],
        
        [sg.Button("check_capacity", size=(6, 4))],
        [sg.Button("add_gate", size=(6, 4))],
        [sg.Button("Exit")],
    ]

    return sg.Window("My new window", layout, size=(900, 700), finalize=True)


def make_win_add_car():
    layout = [[sg.Text("enter_color",size=(20,1)), sg.InputText(key='-COLOR-')], 
              
              [sg.Text("enter_company_name",size=(20,1)), sg.InputText(key='-COMPANY-')],
              [sg.Text("enter_id_of car",size=(20,1)), sg.InputText(key='-ID-')],
              [sg.Text("enter_type_of_car",size=(20,1)), sg.InputText(key='-TYPE-')],
                [sg.Text("choose_gate",size=(20,1)),sg.InputOptionMenu('ABC',key= '-GATE-')],
                
              [sg.Button("Exit"),sg.Button('Submit_Car')]]
    
    return sg.Window("Second Window", layout, finalize=True)

def make_window_remove_car():
    layout =[[sg.Text("enter_id_of_car"),sg.InputText(key='-ID_REMOVE-')],
             sg.Button('Submit_exit_car')]
    return sg.Window("Remove car", layout, finalize=True)


# def check_which_window_closed(window: object,  )
def run_gui():
    log_window,init_window,control_window, add_car_window, remove_car_window = log_in_window(), None ,None, None ,None
    while True:  # Event Loop
        window, event, values = sg.read_all_windows()

        if event in [sg.WIN_CLOSED, "Exit"]:
            window.close()
            if window == control_window:  # if closing win 2, mark as closed
                control_window = None
            elif window == add_car_window:
                add_car_window = None
            elif window == remove_car_window:
                remove_car_window =None
            elif window == log_window:
                log_window = None
            elif window == init_window:
                init_window = None

            if not log_window and not init_window and not control_window and not add_car_window and not remove_car_window:  # if closing win 1, exit program
                break
        if window == log_window and is_valid_input(event, values):
            window.close()
            log_window = None
            initialization()
        if  event == "start":
             window.close()
             init_window = None
             main_window()
        if event == "Add_car" and not add_car_window:
            add_car_window = make_win_add_car()

        if event == "Remove_car" and not remove_car_window:
            make_window_remove_car()

        if event == "Submit_Car":
            add_car_window.close()
            add_car_window = None
            sg.popup(f"time of entrance\n slot number...\n color:{values['-COLOR-']}" )
        if event == "Submit_exit_car":
            window.close()
            remove_car_window = None
            sg.popup("you pay is.. ")






    window.close()


def main():
    run_gui()


if __name__ == "__main__":
    main()
