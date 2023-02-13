import PySimpleGUI as sg
import parkingLot
import parkingLot
import handle_events as events
import logger_parking_lot as lg
import enums as enm 

@lg.logger_func
def reports_window() -> sg.Window:
    """
    create the window of reports

    Returns:
        sg.Window: window
    """
   
    list_of_reports = [
        "current capacity",
        "number of entries per each entry points",
        "vehicles that parked more than 24 hours",
    ]
    layout = [[sg.TabGroup([[ sg.Tab("Reports", [[sg.Listbox(list_of_reports,font=(10,10), size=(40, 3), key="list of reports")],
              [sg.Text(size=(5,5))],
              [sg.Button("Submit report", size=(6,4)),sg.Button("Exit", size=(6,4))]] ),
                   sg.Tab("Queries",[[sg.Text("vehicles by company",size=(40,1)),sg.InputText(key="VEHICLE COMPANY")],
                                    [sg.Text("vehicles of a certain color",size=(40,1)),sg.InputText(key="VEHICLE COLOR")],
                                    [sg.Text("vehicles of a certain type",size=(40,1)),sg.InputText(key="VEHICLE TYPE")],
                                    [sg.Text("slot of vehicle by plate num",size=(40,1)),sg.InputText(key="VEHICLE NUM")],
                                    [sg.Text("vehicles parked during a period of time",size=(40,1)),sg.InputText(key="VEHICLE TIME")],
                                    [sg.Text("income during a certain period of time",size=(40,1)),sg.InputText(key="INCOME TIME")],
                                    [sg.Button("Submit queries", size=(6,4)),sg.Button("Exit", size=(6,4))]
                                     ])     ]]) ]]
   
              

    return sg.Window(
        title="Parking system", layout=layout, size=(700, 270), finalize=True
    )  # return window


def log_in_window() -> sg.Window:
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
    return sg.Window(
        title="Parking system", layout=layout, size=(600, 250), finalize=True
    )  # return window


def initialization_window() -> sg.Window:
    """The system settings. (the amount of parking spaces and their types)"""
    sg.theme("BluePurple")  # Add a touch of color
    # All the stuff inside your window.
    layout = [
        [sg.Text("Welcome to the smart parking system!", font=(any, 20))],
        [
            sg.Text(
                "How many Bus parking spaces do you have?", font=(any, 15), size=40
            ),
            sg.InputText(size=10, key="BUS"),
        ],
        [
            sg.Text(
                "How many Car parking spaces do you have?", font=(any, 15), size=40
            ),
            sg.InputText(size=10, key="CAR"),
        ],
        [
            sg.Text(
                "How many Motorcycle parking spaces do you have?",
                font=(any, 15),
                size=40,
            ),
            sg.InputText(size=10, key="BIKE"),
        ],
        [sg.Text("")],
        [sg.Button("start", size=(6, 2)), sg.Exit(size=(6, 2))],
    ]
    # Create the Window
    return sg.Window(
        title="Parking system", layout=layout, size=(650, 250), finalize=True
    )  # return window

def main_window():
    """
    control main window

    Returns:
        sg.Window: gui window
    """
    
    sg.theme("BlueMono")
    colum1 = sg.Column(
        [
            [
                sg.Frame(
                    "parking lot",
                    [
                        [
                            sg.Text("GATE A",background_color="white",font =(10,10),size=(5, 3)),
                            sg.Push(),
                            
                            sg.Text("GATE B",background_color="white",font =(10,10),size=(5, 3)),
                            sg.Push(),
                            sg.Text("GATE C",background_color="white",font =(10,10),size=(5, 3)),
                            sg.Text("     ")

                        ],
                        [
                            sg.Text(f"S{str(slot)}",
                               size=(6, 5),
                                background_color="white",
                                key=f"S{str(slot)}",
                            )
                            for slot in range(10)
                        ],
                        [
                            sg.Text(f"S{str(slot)}",
                               size=(6, 5),
                                background_color="white",
                                key=f"S{str(slot)}",
                            )
                            for slot in range(10, 20)
                        ],
                        [
                            sg.Text(f"M{str(slot)}",
                                size=(6, 5),
                                background_color="white",
                                key=f"M{str(slot)}",
                            )
                            for slot in range(10)
                        ],
                        [
                            sg.Text(f"M{str(slot)}",
                                size=(6, 5),
                                background_color="white",
                                key=f"M{str(slot)}",
                            )
                            for slot in range(10, 20)
                        ],
                        [
                            sg.Text(f"L{str(slot)}",
                                size=(6, 5),
                                background_color="white",
                                key=f"L{str(slot)}",
                            )
                            for slot in range(10)
                        ],
                        [
                            sg.Text(f"L{str(slot)}",
                                size=(6, 5),
                                background_color="white",
                                key=f"L{str(slot)}",
                            )
                            for slot in range(10, 20)
                        ],
                    ],
                    size=(600, 600),)]])
  

    colum2 = sg.Column(
        [
            [
                sg.Frame(
                    "buttons",
                    [
                        [sg.Button("Add car", size=(7, 4))],
                        [sg.Button("Remove car", size=(7, 4))],
                        [sg.Button("Add gate", size=(7, 4))],
                        [sg.Button("Check capacity", size=(7, 4))],
                        [sg.Button("Reports", size=(7, 4))],
                        [sg.Button("Exit", size=(7, 4))],
                    ],
                    size=(90, 650),
                )
            ]
        ]
    )

    layout = [[colum1, colum2]]

    return sg.Window("My new window", layout, finalize=True)
@lg.logger_func
def window_add_car() -> sg.Window:
    """
    enter the car details
    Returns:
        sg.Window : gui window
    """
    layout = [
        [sg.Text("choose color of car", size=(20, 1)),sg.DropDown(["red","green", "yellow","purple","cyan","pink","blue","orange"], key ="COLOR")],
        [sg.Text("Enter company name", size=(20, 1)), sg.InputText(key="COMPANY")],
        [sg.Text("Enter plate number ", size=(20, 1)), sg.InputText(key="ID")],
        [sg.Text("Enter type of vehicle", size=(20, 1)), sg.DropDown(["Bike", "Car", "Bus"], key="TYPE")],
        [sg.Text("Choose gate", size=(20, 1)), sg.InputOptionMenu("ABC", key="GATE")],
        [sg.Button("Exit"), sg.Button("Submit")],
    ]

    return sg.Window("Second Window", layout, finalize=True)  # return window

@lg.logger_func
def window_remove_car() -> sg.Window:
    """
    enter the car you want to remove
    Returns:
        sg.Window: gui window
    """
    layout = [
        [sg.Text("enter id of car"), sg.InputText(key="ID REMOVE")],
        [sg.Button("Delete")],
    ]

    return sg.Window("Remove car", layout, finalize=True)  # return window


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


def mark_windows_as_None(window: sg.Window, windows_list: list[sg.Window]) -> None:
    """
    check what window have been closed and mark the window as None

    Args:
        window (sg.Window): gui window
        windows_list (sg.Window): list of all the windows
    """

  
    if window == windows_list[enm.Windows.LOG_IN.value]:
        windows_list[enm.Windows.LOG_IN.value] = None
        lg.logger.debug(f'window: {enm.Windows.LOG_IN.name} is closed and mark as None')

    elif window == windows_list[enm.Windows.CAPACITY.value]:
        windows_list[enm.Windows.CAPACITY.value] = None
        lg.logger.debug(f'window: {enm.Windows.CAPACITY.name} is closed and mark as None')

    elif window == windows_list[enm.Windows.MAIN.value]:
        windows_list[enm.Windows.MAIN.value] = None
        lg.logger.debug(f'window: {enm.Windows.MAIN.name} is closed and mark as None')

    elif window == windows_list[enm.Windows.ADD_CAR.value]:
        windows_list[enm.Windows.ADD_CAR.value] = None
        lg.logger.debug(f'window: {enm.Windows.ADD_CAR.name} is closed and mark as None')

    elif window == windows_list[enm.Windows.REMOVE_CAR.value]:
        windows_list[enm.Windows.REMOVE_CAR.value] = None
        lg.logger.debug(f'window: {enm.Windows.REMOVE_CAR.name} is closed and mark as None')

    elif window == windows_list[enm.Windows.REPORTS.value]:
        windows_list[enm.Windows.REPORTS.value] = None
        lg.logger.debug(f'window: {enm.Windows.REPORTS.name} is closed an mark as None')


@lg.logger_func
def validate_status_of_windows(windows_list: sg.Window) -> bool:
    """
    check if all the windows are equals to None

    Args:
        windows_list (sg.Window): list of all windows

    Returns:
        bool: if all the windows equals to None return True
    """
    return (
        not windows_list[0]
        and not windows_list[1]
        and not windows_list[2]
        and not windows_list[3]
        and not windows_list[4]
        and not windows_list[5]
    )







def add_window(window_list: list[sg.Window], number_window: int, function) -> None:
    """
    add new window
    Args:
        window_list (list[sg.Window]): window
        number_window (int): type of window
        function (_type_): create window 
    """
    if number_window == 3:
        lg.logger.debug("\"ADD CAR\" window's opened")
    elif number_window == 4:
        lg.logger.debug("\"REMOVE CAR\" window's opened")
    elif number_window == 5:
        lg.logger.debug("\"REPORT\" window's opened")

    window_list[number_window] = function()


def create_widows_list() -> list[sg.Window,None]:
    """
    create all the windows by assignment them to None except the first window
    Returns:
        list[sg.Window,None]: list of windows
    """
    lg.logger.debug("create all the windows by assignment them to None except the first window")
    log_window,init_window,control_window, add_car_window, remove_car_window, report_window = log_in_window(), None ,None, None ,None ,None
    return [log_window,init_window,control_window, add_car_window, remove_car_window,report_window]
    