import tkinter as tk
import time

class CountdownTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Countdown Timer")
        self.master.configure(background='black')
        
        self.time_left = tk.IntVar(value=60)  # Default to 60 seconds
        self.running = False
        
        self.time_label = tk.Label(master, font=("ds-digital", 80), background="black", foreground="cyan")
        self.time_label.pack(anchor='center', pady=50)
        
        entry_frame = tk.Frame(master, background='black')
        entry_frame.pack()
        
        tk.Label(entry_frame, text="Set time (seconds):", font=("ds-digital", 18), background='black', foreground='cyan').pack(side=tk.LEFT, padx=10)
        self.entry = tk.Entry(entry_frame, textvariable=self.time_left, font=("ds-digital", 18), background="cyan", foreground="black", justify='center')
        self.entry.pack(side=tk.LEFT)
        
        button_frame = tk.Frame(master, background='black')
        button_frame.pack()
        
        self.start_button = tk.Button(button_frame, text="Start", font=("ds-digital", 18), background="black", foreground="cyan", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=10)
        
        self.stop_button = tk.Button(button_frame, text="Stop", font=("ds-digital", 18), background="black", foreground="cyan", command=self.stop)
        self.stop_button.pack(side=tk.LEFT, padx=10)
        
        self.reset_button = tk.Button(button_frame, text="Reset", font=("ds-digital", 18), background="black", foreground="cyan", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=10)
        
        tk.Button(master, text="Quit", font=("ds-digital", 18), background="black", foreground="cyan", command=self.master.destroy).pack(pady=20)
        
        self.update_clock()
    
    def update_clock(self):
        if self.running and self.time_left.get() > 0:
            self.time_left.set(self.time_left.get() - 1)
        if self.time_left.get() <= 0 and self.running:
            self.running = False
            self.time_up()
        self.time_label.config(text=self.format_time(self.time_left.get()))
        self.time_label.after(1000, self.update_clock)
    
    def format_time(self, seconds):
        mins, secs = divmod(seconds, 60)
        hours, mins = divmod(mins, 60)
        return f"{int(hours):02}:{int(mins):02}:{int(secs):02}"
    
    def start(self):
        if not self.running:
            self.running = True
    
    def stop(self):
        if self.running:
            self.running = False
    
    def reset(self):
        self.running = False
        self.time_left.set(60)  # Reset to 60 seconds or any default value
        self.time_label.config(text="00:01:00")
    
    def time_up(self):
        tk.messagebox.showinfo("Time's up!", "The countdown has finished.")

def main():
    root = tk.Tk()
    root.geometry("600x400")
    countdown_timer = CountdownTimer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
