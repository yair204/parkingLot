import gui_windows as wd
import PySimpleGUI as sg
import handle_events as events
import initialize_parking_lot as init
import enums as es 
import logger_parking_lot as lg
def main():
    instants_of_parking_lot = init.initialize_parking_lot(20,20,20)
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
           events.switch_window_by_closing_it(window, windows_list,es.Windows.CAPACITY.value,wd.main_window)

        if events.is_open_window_add_car( windows_list,event):
            wd.add_window(windows_list, es.Windows.ADD_CAR.value,wd.window_add_car)

        if  events.is_open_window_remove_car( windows_list,event):
            wd.add_window(windows_list, es.Windows.REMOVE_CAR.value,wd.window_remove_car)

        events.check_events(window,values, event, instants_of_parking_lot,windows_list)
       
    window.close()
     
if __name__ == "__main__":
    main()