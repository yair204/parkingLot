import gui_windows as wd
import PySimpleGUI as sg
import handle_events as events
import initialize_parking_lot as init_parking


def main():
    
    windows_list = wd.create_widows_list()
    while True:  # Event Loop
        window, event, values = sg.read_all_windows()
        
        if event in [sg.WIN_CLOSED, "Exit","Cancel"]:
            window.close()
    
            wd.mark_windows_as_None(window,windows_list)
            if wd.validate_status_of_windows(windows_list):
                break

          
        if events.is_change_to_main_window(window, windows_list, event):
            instants_of_parking_lot = init_parking.initialize_parking_slot( int(values["BIKE"]), int(values["CAR"]), int(values["BUS"]))
            events.switch_window_by_closing_it(window, windows_list,1,wd.main_window)

        events.change_to_initializ_window(window, windows_list, event, values)
        
        if events.is_open_window_add_car( windows_list,event):
            
            wd.add_window(windows_list, 3,wd.window_add_car)

        if  events.is_open_window_remove_car( windows_list,event):
            wd.add_window(windows_list, 4,wd.window_remove_car)

        if event == "Submit_Car" and events.validate_input_car_details(values):

            current_slot =  instants_of_parking_lot.park_vehicle(values['COMPANY'], int(values['ID']), values['COLOR'],values['TYPE'], values['GATE'])
            
            windows_list[2][current_slot].update(background_color = values['COLOR'])
            window.close() 
            windows_list[3] = None
            slot_id,type,plate_number,company,color,date=instants_of_parking_lot.tickets_list[-1].return_ticket()
            sg.popup(f"Car type is: {type}\nname of company is: {company}\n color is: {color}\n id of car is {plate_number}\ndate of entrance is: {date}\n number of slot is: {slot_id}",font=(20,20))

        if event == "Submit_exit_car":
            price,slot_id = instants_of_parking_lot.remove_vehicle(int(values['ID_REMOVE']))
            windows_list[2][slot_id].update(background_color = "white")
            window.close()
            windows_list[4] = None
            sg.popup(f"you pay is{price} ")
            
        if event == "Reports" and not windows_list[5]:
            windows_list[5] = wd.reports_window()

        if event == "Submit report" :
            window.close()
            windows_list[5] = None
            sg.popup(values['list of reports'])

             

    window.close()
    
    
    
    
if __name__ == "__main__":
    main()