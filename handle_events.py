import PySimpleGUI as sg
import gui_windows as wd
import parkingLot
import enums as es
import logger_parking_lot as lg
import reports


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
                lg.logger.debug("open capacity window")
                return True
            else:
                lg.logger.warning("You must specify a valid username and password")
                sg.popup(
                    "You must specify a valid username and password",
                    title="ERROR",
                    font=10,
                )
        else:
            lg.logger.warning("You must specify a valid username and password")
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

        switch_window_by_closing_it(window, windows_list,es.Windows.LOG_IN.value,wd.initialization_window)

def  is_change_to_main_window(window: sg.Window, windows_list: list[sg.Window], event: object) -> None:
    return window == windows_list[1] and event == "start"

def is_open_window_add_car( windows_list: list[sg.Window], event: object) -> bool:
    return event == "Add car" and not windows_list[3]

def is_open_window_remove_car( windows_list: list[sg.Window], event: object) -> bool:
    return event == "Remove car" and not windows_list[4]

def validate_input_car_details(values: sg) -> bool:
    if values['COLOR'] not in["red","green", "yellow","purple","cyan","pink","blue","orange"]:
        sg.popup("Enter valid color" ,title="Error input",font=(20,20))
        lg.logger.warning("Enter valid color")
        return False

    if not values['COMPANY']:
        sg.popup("Enter company name" ,title="Error input",font=(20,20))
        lg.logger.warning("Enter company name")
        return False

    if not values['ID']:
        sg.popup("Enter plate number" ,title="Error input",font=(20,20))
        lg.logger.warning("Enter plate number")
        return False
    else:
        try:
            int(values['ID'])

        except Exception:
            sg.popup("Enter plate number integer" ,title="Error input",font=(20,20))
            lg.logger.error("Enter plate number integer")
            return False

    if values['TYPE'] not in ["S", "L", "M"]:
        sg.popup("Enter types of S, L, M  " ,title="Error input",font=(20,20))
        lg.logger.warning("Enter types of S, L, M ")
        return False
    
    if not values['GATE']:
        sg.popup("Choose gate" ,title="Error input",font=(20,20))
        lg.logger.warning("Choose gate")
        return False
    
    return True

def added_new_car(window: sg.Window,instants_of_parking_lot:parkingLot.AutomatedParkingLot, values:object,windows_list) -> None:
    if current_slot := instants_of_parking_lot.park_vehicle(
        values['COMPANY'],
        int(values['ID']),
        values['COLOR'],
        values['TYPE'],
        values['GATE'],
    ):
        windows_list[es.Windows.MAIN.value][current_slot].update(background_color = values['COLOR'])
        window.close()
        windows_list[es.Windows.ADD_CAR.value] = None
        slot_id,type,plate_number,company,color,date=instants_of_parking_lot.tickets_list[-1].return_ticket()
        lg.logger.debug(f"Add new car the car type is: {type}\nname of company is: {company}\n color is: {color}\n id of car is {plate_number}\ndate of entrance is: {date}\n number of slot is: {slot_id}")
        sg.popup(f"Car type is: {type}\nname of company is: {company}\n color is: {color}\n id of car is {plate_number}\ndate of entrance is: {date}\n number of slot is: {slot_id}",font=(20,20))
        instants_entry =reports.ReportEntries()
        instants_entry.increment_entry(values['GATE'])
    else:
        lg.logger.warning("the parking lot is full")
        sg.popup("the parking lot is full")

def remove_car(window: sg.Window,instants_of_parking_lot:parkingLot.AutomatedParkingLot, values:object,windows_list) -> None:
    try:
        int(values['ID_REMOVE'])
    except Exception:
        sg.popup("Enter plate number integer " ,title="Error input",font=(20,20))
        lg.logger.error("Enter plate number integer")
        return
    
    price,slot_id = instants_of_parking_lot.remove_vehicle(int(values['ID_REMOVE']))
    if slot_id:
        windows_list[es.Windows.MAIN.value][slot_id].update(background_color = "white")
        lg.logger.debug("REMOVE_CAR window is closed")
        window.close()
        windows_list[es.Windows.REMOVE_CAR.value] = None
        lg.logger.info(f"you pay is{price} ")
        sg.popup(f"you pay is{price} ",font=(10,10),title="Error")
    else:
        sg.popup("the car wasn't found",font=(10,10),title="Error")

def handle_reports(values,instants_of_parking_lot):
    if values['list of reports']:
       
        report = values['list of reports']
        match report:
            case ['current capacity']:
                sg.popup( reports.track_of_capacity(instants_of_parking_lot))
            case ['vehicles by company']:
                pass
            case  ['vehicles of a certain color']:
                pass
            case ['vehicles of a certain type']:
                pass
            case ['slot of vehicle by plate no']:
                pass
            case ['vehicles parked during a period of time']:
                pass
            case ['income during a certain period of time']:
                pass
            case ['number of entries per each entry points']:
                report =reports.ReportEntries()
                sg.popup(f'{report.gateA}')
            case ['vehicles that parked more than 24 hours']:
                pass
            

                
