import gui_windows as wd
import PySimpleGUI as sg
import handle_events as events
import initialize_parking_lot as init
import logger_parking_lot as lg


def main():
    instants_of_parking_lot = init.initialize_parking_lot(20, 20, 20)
    windows_list = wd.create_widows_list()
    while True:  # Event Loop
        window, event, values = sg.read_all_windows()

        if event in [sg.WIN_CLOSED, "Exit", "Cancel"]:
            window.close()

            wd.mark_windows_as_None(window, windows_list)
            if wd.validate_status_of_windows(windows_list):
                lg.logger.debug("exit parking lot program")
                break
        events.open_windows(window, windows_list, event, values)
        events.check_events_car_and_reports(
            window, values, event, instants_of_parking_lot, windows_list
        )

    window.close()


if __name__ == "__main__":
    main()
