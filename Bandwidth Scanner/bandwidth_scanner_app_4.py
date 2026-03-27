"""
    Name: bandwidth_scanner_app_4.py
    Author: Noel Onate
    Created: 3/26/26
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

        # Add padding to window
        self.root.configure(padx=10, pady=10)

        # Make the window unable to be resized
        self.root.resizable(False, False)

        # Get and select the current best server from SpeedTest
        self.test = speedtest.Speedtest()
        self.test.get_best_server()

        # Call method to create frames and widgets
        self.create_widgets()

        # Start program main loop
        self.root.mainloop()

    def test_internet(self):
        # Disable the buttons to prevent spamming
        self.start_test.config(state=DISABLED)
        self.clear_button.config(state=DISABLED)

        # Start thread to test internet
        threading.Thread(target=self.run_test, daemon=True).start()

    def run_test(self):
        try:
            # Start progress bar
            self.progress.start()

            # Empty text box
            self.root.after(0, lambda: self.test_results.delete(1.0, END))

            # Perform the download and upload speed tests on a thread
            # Convert results to Mbps and display status messages before testing
            self.root.after(0, lambda: self.test_results.insert(END, "Testing download speed...\n"))
            download = self.test.download() / 1000000
            self.root.after(0, lambda: self.test_results.insert(END, "Testing upload speed...\n"))
            upload = self.test.upload() / 1000000

            # Get the ping
            ping = self.test.results.ping

            # Update the GUI
            self.root.after(0, self.display_results, download, upload, ping)

            # Stop progress bar
            self.progress.stop()
        
        # If any errors occur, tell user
        except Exception as e:
            self.root.after(0, self.display_error, e)

    def display_results(self, download, upload, ping):
        # Empty text box
        self.test_results.delete(1.0, END)

        # Get the server name and ISP
        server = self.test.results.server['name']
        isp = self.test.results.client['isp']

        # Display results in text box
        self.test_results.insert(END, f"        Server: {server}\n")
        self.test_results.insert(END, f"           ISP: {isp}\n")
        self.test_results.insert(END, f"          Ping: {ping} ms\n")
        self.test_results.insert(END, f"  Upload Speed: {upload:,.1f} Mbps\n")
        self.test_results.insert(END, f"Download Speed: {download:,.1f} Mbps")

        # Re-enable the buttons
        self.start_test.config(state=NORMAL)
        self.clear_button.config(state=NORMAL)

    def display_error(self, error):
        self.test_results.insert(END, f"Error: {error}\n")

    def clear_results(self):
        self.test_results.delete(1.0, END)

    def create_widgets(self):
        # Create frame
        self.testing_frame = LabelFrame(self.root, text="Test Results", relief=GROOVE)

        # Create button to start test and set focus
        self.start_test = Button(self.testing_frame, text="Start Test", command=self.test_internet)
        self.start_test.focus_set()

        # Create button to clear results
        self.clear_button = Button(self.testing_frame, text="Clear", command=self.clear_results)

        # Create text widget
        self.test_results = Text(self.testing_frame, height=10, width=40, relief=GROOVE)

        # Create progress bar widget
        self.progress = Progressbar(self.testing_frame, mode='indeterminate')

        # Add widgets using grid method
        self.start_test.grid(row=0, column=0)
        self.clear_button.grid(row=0, column=1)
        self.test_results.grid(row=1, column=0, columnspan=2)
        self.testing_frame.grid(row=0, column=0)
        self.progress.grid(row=2, column=0, columnspan=2)

        # Set padding between frames and the window
        self.testing_frame.grid(padx=10, pady=(10, 0))

        # Set pad padding for all widgets inside each frame
        # set ipad padding inside the widgets
        for widget in self.testing_frame.winfo_children():
            widget.grid_configure(padx=6, pady=6, ipadx=2, ipady=2)

# Create program object to start program
bandwidth_scanner = BandwidthScanner()