import PySimpleGUI as sg
import parkingLot
import parkingLot
import handle_events as events
import logger_parking_lot as lg
import enums as enm 

def reports_window() -> sg.Window:
   
    list_of_reports = [
        "current capacity",
        "vehicles by company",
        "vehicles of a certain color",
        "vehicles of a certain type",
        "slot of vehicle by plate no",
        "vehicles parked during a period of time",
        "income during a certain period of time",
        "number of entries per each entry points",
        "vehicles that parked more than 24 hours"
    ]
    layout = [[sg.Listbox(list_of_reports,font=(10,10), size=(40, 10), key="list of reports")],
              
              [sg.Button("Submit report", size=(10,20)),sg.Button("Exit", size=(10,20))]]
              

    return sg.Window(
        title="Parking system", layout=layout, size=(400, 250), finalize=True
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
                            sg.Text(f"slotS{str(slot)}",
                               size=(6, 5),
                                background_color="white",
                                key=f"S{str(slot)}",
                            )
                            for slot in range(10)
                        ],
                        [
                            sg.Text(f"slotS{str(slot)}",
                               size=(6, 5),
                                background_color="white",
                                key=f"S{str(slot)}",
                            )
                            for slot in range(10, 20)
                        ],
                        [
                            sg.Text(f"slotM{str(slot)}",
                                size=(6, 5),
                                background_color="white",
                                key=f"M{str(slot)}",
                            )
                            for slot in range(10)
                        ],
                        [
                            sg.Text(f"slotM{str(slot)}",
                                size=(6, 5),
                                background_color="white",
                                key=f"M{str(slot)}",
                            )
                            for slot in range(10, 20)
                        ],
                        [
                            sg.Text(f"slotL{str(slot)}",
                                size=(6, 5),
                                background_color="white",
                                key=f"L{str(slot)}",
                            )
                            for slot in range(10)
                        ],
                        [
                            sg.Text(f"slotL{str(slot)}",
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
                        [sg.Button("Check_capacity", size=(7, 4))],
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

    
def initialize_parking_lot(number_bikes: str, number_cars: str,number_buses: str)-> parkingLot.AutomatedParkingLot:
    """
    initialize object of parking lot

    Args:
        number_bikes (int): number of bikes slot
        number_cars (int): number of cars slot
        number_buses (int): number of buses slot

    Returns:
        parkingLot.AutomatedParkingLot: object of AutomatedParkingLot
    """
    lg.logger.debug("initialize object of parking lot")
    lg.logger.debug("main window is opened")
    parking_lot_obj = parkingLot.AutomatedParkingLot(number_bikes,number_cars,number_buses) 
    parking_lot_obj.allocate_n_slots()
    return parking_lot_obj
   

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
        [sg.Text("Enter type of vehicle", size=(20, 1)), sg.InputText(key="TYPE")],
        [sg.Text("Choose gate", size=(20, 1)), sg.InputOptionMenu("ABC", key="GATE")],
        [sg.Button("Exit"), sg.Button("Submit_Car")],
    ]

    return sg.Window("Second Window", layout, finalize=True)  # return window


def window_remove_car() -> sg.Window:
    """
    enter the car you want to remove
    Returns:
        sg.Window: gui window
    """
    layout = [
        [sg.Text("enter_id_of_car"), sg.InputText(key="ID_REMOVE")],
        [sg.Button("Submit_exit_car")],
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
    if number_window == 3:
        lg.logger.debug("\"ADD CAR\" window's opened")
    elif number_window == 4:
        lg.logger.debug("\"REMOVE CAR\" window's opened")
    elif number_window == 5:
        lg.logger.debug("\"REPORT\" window's opened")

    window_list[number_window] = function()


def create_widows_list() -> list[sg.Window,None]:
    lg.logger.debug("create all the windows by assignment them to None except the first window")
    log_window,init_window,control_window, add_car_window, remove_car_window, report_window = log_in_window(), None ,None, None ,None ,None
    return [log_window,init_window,control_window, add_car_window, remove_car_window,report_window]
    