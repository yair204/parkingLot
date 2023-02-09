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
    """
    switch to init window
    Args:
        window (sg.Window): gui window
        windows_list (list[sg.Window]): gui window
        event (object): event of sg.Window
        values (object): values of sg.Window

    Returns:
        bool: _description_
    """
    if window == windows_list[0] and is_valid_input(event, values):

        switch_window_by_closing_it(window, windows_list,es.Windows.LOG_IN.value,wd.initialization_window)

def  is_change_to_main_window(window: sg.Window, windows_list: list[sg.Window], event: object) -> None:
    """
    check if to open maun window

    Args:
        window (sg.Window): _description_
        windows_list (list[sg.Window]): _description_
        event (object): _description_

    Returns:
        bool: true/false
    """
    return window == windows_list[1] and event == "start"

def is_open_window_add_car( windows_list: list[sg.Window], event: object) -> bool:
    """
    check if to open window add car

    Args:
        windows_list (list[sg.Window]): gui window
        event (object): event of sg.Window

    Returns:
        bool: true/false
    """
    return event == "Add car" and not windows_list[3]

def is_open_window_remove_car( windows_list: list[sg.Window], event: object) -> bool:
    """
    check if to open window remove car

    Args:
        windows_list (list[sg.Window]): gui window
        event (object): event of sg.Window

    Returns:
        bool: true/false
    """
    return event == "Remove car" and not windows_list[4]

def validate_input_car_details(values: sg) -> bool:
    """
    validate input car details

    Args:
        values (sg): value

    Returns:
        bool:bool
    """
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
    """
    add new car if the parking lot is not full

    Args:
        window (sg.Window): window
        instants_of_parking_lot (parkingLot.AutomatedParkingLot): parking lot instant
        values (object): value
        windows_list (sg.window): windows
    """
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
    """
    remove car and validate that the id is correct
    Args:
        window (sg.Window): window
        instants_of_parking_lot (parkingLot.AutomatedParkingLot): instants_of_parking_lot
        values (object): _value
        windows_list (_type_): window
    """
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

def handle_reports(values:sg ,instants_of_parking_lot,event:object) -> None:
    """
    reports the the report event
    Args:
        values (sg: value
        instants_of_parking_lot (_type_):instants_of_parking_lot
        event (sg): event
    """
    if event == "Submit report" :
        report = values['list of reports']
        match report:
            case ['current capacity']:
                sg.popup( reports.track_of_capacity(instants_of_parking_lot))

            case ['number of entries per each entry points']:
                report =reports.ReportEntries()
                sg.popup(f'gate A:{report.gateA}\ngate B:{report.gateB}\ngate C:{report.gateC}',title=("Report"),font=(10,10))
            case ['vehicles that parked more than 24 hours']:
                sg.popup(reports.parked_more_24_hours(instants_of_parking_lot),title=("Report"),font=(10,10))

    def queries(event:sg,values:sg) -> None:
        """
        reports the the report queries
        Args:
            event (sg): event
            values (sg): value 
        """
        if event == "Submit queries" :
            
            if values['VEHICLE COLOR']:
                sg.popup(reports.specific_color(instants_of_parking_lot,values['VEHICLE COLOR']),title="Report",font=(10,10))
        
            elif  values['VEHICLE COMPANY']:
                sg.popup(reports.specific_company(instants_of_parking_lot ,values['VEHICLE COMPANY']),title="report",font=(10,10))    
            elif  values['VEHICLE TYPE']:
                sg.popup(reports.specific_type(instants_of_parking_lot,values['VEHICLE TYPE']),title="Report",font=(10,10))
            
            elif  values['VEHICLE NUM']:
                sg.popup(reports.specific_slot_ID(instants_of_parking_lot,values['VEHICLE NUM']),title="Report",font=(10,10))
            
            elif  values['VEHICLE TIME']:
                sg.popup("TODO",title="Error",font=(10,10))
                
            elif values['INCOME TIME']:
                sg.popup("TODO",title="Error",font=(10,10))
    queries(event,values)

def check_events_car_and_reports(window:sg.Window,values:sg, event:sg, instants_of_parking_lot:object,windows_list:list[sg.Window]) -> None:
    """
    run events of add cer remove car reports

    Args:
        window (sg.Window): window
        values (sg): value
        event (sg): events
        instants_of_parking_lot (object): instants_of_parking_lot
        windows_list (list[sg.Window]):  windows_list
    """
    if event == "Submit_Car" and validate_input_car_details(values):
            added_new_car(window,instants_of_parking_lot, values,windows_list) 

    if event == "Submit_exit_car":
        remove_car(window,instants_of_parking_lot, values,windows_list)

    if event == "Reports" and not windows_list[es.Windows.REPORTS.value]:
        wd.add_window(windows_list,es.Windows.REPORTS.value,wd.reports_window)

    if event in ["Submit report", "Submit queries"]:
        handle_reports(values,instants_of_parking_lot ,event)
        window.close()
        windows_list[es.Windows.REPORTS.value] = None

def open_windows(window:sg.Window, windows_list:list[sg.Window],event:sg,values:sg) -> bool:
    """
    handle events of windows open

    Args:
        window (sg.Window): window
        windows_list (list[sg.Window]):list[window]
        event (sg): events
        values (sg): value

    Returns:
        bool: true/false
    """
    change_to_initializ_window(window, windows_list, event, values)

    if event == "start":
        switch_window_by_closing_it(window, windows_list,es.Windows.CAPACITY.value,wd.main_window)

    if is_open_window_add_car( windows_list,event):
        wd.add_window(windows_list, es.Windows.ADD_CAR.value,wd.window_add_car)

    if is_open_window_remove_car( windows_list,event):
        wd.add_window(windows_list, es.Windows.REMOVE_CAR.value,wd.window_remove_car)
            

                
