import gui_windows as wd
import PySimpleGUI as sg
import handle_events as events
import initialize_parking_lot as init_parking
import enums as es 
import logger_parking_lot as lg
def main():
    
    windows_list = wd.create_widows_list()
    while True:  # Event Loop
        window, event, values = sg.read_all_windows()
        
        if event in [sg.WIN_CLOSED, "Exit","Cancel"]:
            window.close()
    
            wd.mark_windows_as_None(window,windows_list)
            if wd.validate_status_of_windows(windows_list):
                lg.logger.debug("exit parking lot program")
                break

          
        events.change_to_initializ_window(window, windows_list, event, values)
    
        if event == "start":
            instants_of_parking_lot = wd.initialize_parking_lot(20,20,20)
            events.switch_window_by_closing_it(window, windows_list,es.Windows.CAPACITY.value,wd.main_window)

        if events.is_open_window_add_car( windows_list,event):
            wd.add_window(windows_list, es.Windows.ADD_CAR.value,wd.window_add_car)

        if  events.is_open_window_remove_car( windows_list,event):
            wd.add_window(windows_list, es.Windows.REMOVE_CAR.value,wd.window_remove_car)

        if event == "Submit_Car" and events.validate_input_car_details(values):
            events.added_new_car(window,instants_of_parking_lot, values,windows_list) 

        if event == "Submit_exit_car":
           events.remove_car(window,instants_of_parking_lot, values,windows_list)
            
        if event == "Reports" and not windows_list[es.Windows.REPORTS.value]:
            wd.add_window(windows_list,es.Windows.REPORTS.value,wd.reports_window)

        if event == "Submit report" :
            events.handle_reports(values,instants_of_parking_lot)
            window.close()
            windows_list[es.Windows.REPORTS.value] = None
          

    window.close()
     
if __name__ == "__main__":
    main()