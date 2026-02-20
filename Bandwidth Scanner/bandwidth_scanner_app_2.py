"""
    Name: bandwidth_scanner_app_2.py
    Author: Noel Onate
    Created: 2/19/26
    Purpose: App to measure internet bandwidth
"""

# pip install speedtest-cli
import speedtest
from tkinter import *
from tkinter.ttk import *
import threading

class BandwidthScanner:
    def __init__(self):
        self.root = Tk()
        self.root.title("SpeedTester")

        # Get and select the current best server from SpeedTest
        self.test = speedtest.Speedtest()
        self.test.get_best_server()

        # Call method to create frames and widgets
        self.create_widgets()

        # Start program main loop
        self.root.mainloop()

    def test_internet(self):
        # Start thread to test internet
        threading.Thread(target=self.run_test, daemon=True).start()

    def run_test(self):
        try:
            # Empty text box
            self.test_results.delete(1.0, END)

            # Perform the download and upload speed tests on a thread
            # Convert results to Mbps
            self.test_results.insert(END, "Testing download speed...\n")
            self.download_speed = self.test.download() / 1000000

            self.test_results.insert(END, "Testing upload speed...\n")
            self.upload_speed = self.test.upload() / 1000000

            # Get the ping
            self.ping = self.test.results.ping

            # Show results
            self.test_results.insert(END, f"Ping: {self.ping} ms\n")
            self.test_results.insert(END, f"Download Speed: {self.download_speed:,.2f} Mbps\n")
            self.test_results.insert(END, f"Upload Speed: {self.upload_speed:,.2f} Mbps")
        
        # If any errors occur, tell user
        except Exception as e:
            self.test_results.insert(END, f"Error: {e}\n")

    def create_widgets(self):
        # Create frame
        self.testing_frame = LabelFrame(self.root, text="Test Results", relief=GROOVE)

        # Create button to start test and set focus
        self.start_test = Button(self.testing_frame, text="Start Test", command=self.test_internet)
        self.start_test.focus_set()

        # Create text widget
        self.test_results = Text(self.testing_frame, height=5, width=30, relief=GROOVE)

        # Add widgets using grid method
        self.start_test.grid(row=0, column=0)
        self.test_results.grid(row=1, column=0)
        self.testing_frame.grid(row=0, column=0)

        # Set padding between frames and the window
        self.testing_frame.pack_configure(padx=10, pady=(10, 0))

        # Set pad padding for all widgets inside each frame
        # set ipad padding inside the widgets
        for widget in self.testing_frame.winfo_children():
            widget.grid_configure(padx=6, pady=6, ipadx=2, ipady=2)

# Create program object to start program
bandwidth_scanner = BandwidthScanner()