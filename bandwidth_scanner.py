"""
    Name: bandwidth_scanner.py
    Author: Noel Onate
    Created: 1/22/26
    Purpose: Measure internet bandwidth
"""

# pip install speedtest-cli
import speedtest

# Display title
print("-----------------------------------")
print("|      Internet Speed Tester      |")
print("-----------------------------------")

# Create object
test = speedtest.Speedtest()

# Select the current best server from SpeedTest
test.get_best_server()

# Perform the download and upload speed tests
# Convert results to Mbps
print("Testing download speed...")
download_speed = test.download() / 1000000
print("Testing upload speed...")
upload_speed = test.upload() / 1000000

# Get the ping
ping = test.results.ping

# Print results
print(f"Ping: {ping} ms")
print(f"Download Speed: {download_speed:,.2f} Mbps")
print(f"Upload Speed: {upload_speed:,.2f} Mbps")