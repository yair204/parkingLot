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

        if event == "Submit_Car":
            instants_of_parking_lot.park_vehicle(values['COMPANY'], values['ID'], values['COLOR'],values['TYPE'], values['GATE'])
            print(instants_of_parking_lot.vehicle_dict)
            window.close()
            
            windows_list[3] = None
            sg.popup(f"time of entrance\n slot number...\n color:{values['COLOR']}" )
        if event == "Submit_exit_car":
            window.close()
            windows_list[4] = None
            sg.popup("you pay is.. ")

        if event == "Reports" and not windows_list[5]:
            windows_list[5] = wd.reports_window()
        if event == "Submit report" :
            window.close()
            windows_list[5] = None
            sg.popup(values['list of reports'])

             

    window.close()
    
    
    
    
if __name__ == "__main__":
    main()