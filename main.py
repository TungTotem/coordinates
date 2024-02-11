import tkinter as tk
from pynput.mouse import Listener, Controller
from threading import Thread


class MouseTracker(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Mouse Tracker")
        self.label = tk.Label(self, text="Bewege die Maus auf den gewünschten Bereich und drücke 'K'...")
        self.label.pack(pady=10)
        self.coordinates_text = tk.Text(self, height=2, width=65)
        self.coordinates_text.pack(pady=5)
        self.bind("<Key>", self.on_key_press)
        self.listener_thread = Thread(target=self.start_mouse_listener)
        self.listener_thread.daemon = True
        self.listener_thread.start()

    def on_key_press(self, event):
        if event.char.lower() == 'k':
            mouse_controller = Controller()
            current_position = mouse_controller.position
            cleaned_coordinates = self.clean_coordinates(current_position)
            self.coordinates_text.delete(1.0, tk.END)
            self.coordinates_text.insert(tk.END, cleaned_coordinates)

    def start_mouse_listener(self):
        with Listener(on_move=self.on_move) as listener:
            listener.join()

    def on_move(self, x, y):
        pass  # We don't need to do anything with mouse movements

    def clean_coordinates(self, position):
        cleaned_x = str(int(position[0]))
        cleaned_y = str(int(position[1]))
        return f"{cleaned_x}, {cleaned_y}"


if __name__ == "__main__":
    app = MouseTracker()
    app.mainloop()
