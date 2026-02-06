"""
    Name: bandwidth_scanner_app.py
    Author: Noel Onate
    Created: 1/22/26
    Purpose: App to measure internet bandwidth
"""

# pip install speedtest-cli
import speedtest
from tkinter import *
from tkinter.ttk import *

# Create bandwidth test object
test = speedtest.Speedtest()

# Select the current best server from SpeedTest
test.get_best_server()

class BandwidthScanner:
    def __init__(self):
        self.root = Tk()
        self.root.title("SpeedTester")
        # Call methods to create frames and widgets
        self.create_frames()
        self.create_widgets()
        # Start program main loop
        mainloop()

    def test_internet(self):
        # Perform the download and upload speed tests
        # Convert results to Mbps
        self.test_results.insert(END, "Testing download speed...\n")
        self.download_speed = test.download() / 1000000
        self.test_results.insert(END, "Testing upload speed...\n")
        self.upload_speed = test.upload() / 1000000

        # Get the ping
        self.ping = test.results.ping

        # Show results
        self.test_results.insert(END, f"Ping: {self.ping} ms\n")
        self.test_results.insert(END, f"Download Speed: {self.download_speed:,.2f} Mbps\n")
        self.test_results.insert(END, f"Upload Speed: {self.upload_speed:,.2f} Mbps")
    
    def create_frames(self):
        self.testing_frame = LabelFrame(self.root, text="Test Results", relief=GROOVE)

        # Pack the frames to the edges of the window
        self.testing_frame.pack(fill=X)
        self.testing_frame.pack_propagate(False)

    def create_widgets(self):
        # Create button to start test and set focus
        self.start_test = Button(self.testing_frame, text="Start Test", command=self.test_internet)
        self.start_test.focus_set()

        # Create text widget
        self.test_results = Text(self.testing_frame, height=5, width=25, relief=GROOVE)

        # Add widgets using grid method
        self.start_test.grid(row=0, column=0)
        self.test_results.grid(row=1, column=0)

        # Set padding between frames and the window
        self.testing_frame.pack_configure(padx=10, pady=(10, 0))

        # Set pad padding for all widgets inside each frame
        # set ipad padding inside the widgets
        for widget in self.testing_frame.winfo_children():
            widget.grid_configure(padx=6, pady=6, ipadx=2, ipady=2)

# Create program object to start program
bandwidth_scanner = BandwidthScanner()