import PySimpleGUI as sg
import gui_windows as wd
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
def mark_window_as_None(windows_list: list[sg.Window], number_window: int) -> None:
    """
    initialize window to None
    Args:
        windows_list (list[sg.Window]): list of all windows
        number_window (int): indicate what window to mark
    """
    windows_list[number_window] = None

def switch_window_by_closing_it(
    window: sg.Window, windows_list: list[sg.Window], number_window: int, function
) -> None:
    """
    change the window to next one

    Args:
        window (sg.Window): gui window
        windows_list (list[sg.Window]): list of all windows
        number_window (int): indicate what window to mark
    """
    window.close()
    mark_window_as_None(windows_list, number_window)
    windows_list[number_window + 1] = function()

def change_to_initializ_window(window: sg.Window, windows_list: list[sg.Window], event: object, values: object) -> bool:
    if window == windows_list[0] and is_valid_input(event, values):
        switch_window_by_closing_it(window, windows_list,0,wd.initialization_window)

def  is_change_to_main_window(window: sg.Window, windows_list: list[sg.Window], event: object) -> None:
    return window == windows_list[1] and event == "start"

def is_open_window_add_car( windows_list: list[sg.Window], event: object) -> bool:
    return event == "Add car" and not windows_list[3]

def is_open_window_remove_car( windows_list: list[sg.Window], event: object) -> bool:
    return event == "Remove car" and not windows_list[4]
def validate_input_car_details(values: sg) -> bool:
    if values['COLOR'] not in["red","green", "yellow","purple","cyan","pink","blue","orange"]:
        sg.popup("Enter valid color" ,title="Error input",font=(20,20))
        return False

    if not values['COMPANY']:
        sg.popup("Enter company name" ,title="Error input",font=(20,20))
        return False

    if not values['ID']:
        sg.popup("Enter plate number" ,title="Error input",font=(20,20))
        return False
    else:
        try:
            int(values['ID'])

        except Exception:
            sg.popup("Enter plate number integer " ,title="Error input",font=(20,20))
            return False

    if values['TYPE'] not in ["S", "L", "M"]:
        sg.popup("Enter types of S, L, M  " ,title="Error input",font=(20,20))
        return False
    
    if not values['GATE']:
        sg.popup("Choose gate " ,title="Error input",font=(20,20))
        return False
    


    return True

