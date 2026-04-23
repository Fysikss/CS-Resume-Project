"""
Name: bandwidth_scanner_app_final.py
Author: Noel Onate
Created: 4/22/26
Purpose: App to measure internet bandwidth
"""

# pip install speedtest-cli
import speedtest
import tkinter as tk
from tkinter import ttk
import threading
from datetime import datetime

class BandwidthScanner:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SpeedTester")

        # Add padding to window
        self.root.configure(padx=10, pady=10)

        # Make the window unable to be resized
        self.root.resizable(False, False)

        # Create UI
        self.create_widgets()

        # Start program main loop
        self.root.mainloop()

    def test_internet(self):
        # Disable buttons to prevent spam
        self.start_test.config(state=tk.DISABLED)
        self.clear_button.config(state=tk.DISABLED)
        self.save_button.config(state=tk.DISABLED)

        # Start thread
        threading.Thread(target=self.run_test, daemon=True).start()

    def run_test(self):
        try:
            # Start progress bar
            self.root.after(0, self.progress.start)

            # Clear text box
            self.root.after(0, lambda: self.test_results.delete(1.0, tk.END))

            # Create speedtest object INSIDE thread (prevents freezing)
            self.test = speedtest.Speedtest()
            self.test.get_best_server()

            # Status updates
            self.root.after(0, lambda: self.test_results.insert(tk.END, "Testing download speed...\n"))

            try:
                download = self.test.download() / 1_000_000
            except:
                download = 0

            self.root.after(0, lambda: self.test_results.insert(tk.END, "Testing upload speed...\n"))

            try:
                upload = self.test.upload() / 1_000_000
            except:
                upload = 0

            # Get ping
            ping = self.test.results.ping

            # Update UI
            self.root.after(0, self.display_results, download, upload, ping)

        except Exception as e:
            self.root.after(0, self.display_error, e)

    def display_results(self, download, upload, ping):
        # Stop progress bar
        self.progress.stop()

        # Clear text box
        self.test_results.delete(1.0, tk.END)

        # Get info
        server = self.test.results.server['name']
        isp = self.test.results.client['isp']
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Display nicely formatted output
        self.test_results.insert(tk.END, f"{'Time:':>15} {time_now}\n")
        self.test_results.insert(tk.END, f"{'Server:':>15} {server}\n")
        self.test_results.insert(tk.END, f"{'ISP:':>15} {isp}\n")
        self.test_results.insert(tk.END, f"{'Ping:':>15} {ping:.2f} ms\n")
        self.test_results.insert(tk.END, f"{'Upload:':>15} {upload:,.2f} Mbps\n")
        self.test_results.insert(tk.END, f"{'Download:':>15} {download:,.2f} Mbps\n")

        # Auto-scroll
        self.test_results.see(tk.END)

        # Re-enable buttons
        self.start_test.config(state=tk.NORMAL)
        self.clear_button.config(state=tk.NORMAL)
        self.save_button.config(state=tk.NORMAL)

    def display_error(self, error):
        # Stop progress bar (FIX)
        self.progress.stop()

        self.test_results.insert(tk.END, f"Error: {error}\n")

        # Re-enable buttons
        self.start_test.config(state=tk.NORMAL)
        self.clear_button.config(state=tk.NORMAL)
        self.save_button.config(state=tk.NORMAL)

    def clear_results(self):
        self.test_results.delete(1.0, tk.END)

    def save_results(self):
        data = self.test_results.get(1.0, tk.END).strip()

        # Prevent empty saves
        if data:
            with open("speedtest_results.txt", "a") as f:
                f.write(data + "\n\n")

    def create_widgets(self):
        # Title label (UI improvement)
        title = ttk.Label(self.root, text="Internet Speed Tester", font=("Arial", 14, "bold"))
        title.grid(row=0, column=0, pady=(0, 10))

        # Frame
        self.testing_frame = ttk.LabelFrame(self.root, text="Test Results", relief=tk.GROOVE)
        self.testing_frame.grid(row=1, column=0, padx=10, pady=(0, 10))

        # Buttons
        self.start_test = ttk.Button(self.testing_frame, text="Start Test", command=self.test_internet)
        self.start_test.focus_set()

        self.clear_button = ttk.Button(self.testing_frame, text="Clear", command=self.clear_results)

        self.save_button = ttk.Button(self.testing_frame, text="Save", command=self.save_results)
        self.save_button.config(state=tk.DISABLED)  # Disabled initially

        # Text box
        self.test_results = tk.Text(self.testing_frame, height=10, width=45, relief=tk.GROOVE)

        # Progress bar
        self.progress = ttk.Progressbar(self.testing_frame, mode='indeterminate')

        # Layout
        self.start_test.grid(row=0, column=0)
        self.clear_button.grid(row=0, column=1)
        self.save_button.grid(row=0, column=2)

        self.test_results.grid(row=1, column=0, columnspan=3)
        self.progress.grid(row=2, column=0, columnspan=3)

        # Padding for all widgets
        for widget in self.testing_frame.winfo_children():
            widget.grid_configure(padx=6, pady=6, ipadx=2, ipady=2)


# Run app
if __name__ == "__main__":
    bandwidth_scanner = BandwidthScanner()