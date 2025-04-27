import tkinter as tk
from tkinter import messagebox
import subprocess
import threading

class ARPScanner(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("ARP Scanner Tool")
        self.geometry("400x300")
        
        # Label and input for IP range
        self.label = tk.Label(self, text="Enter the IP Range (e.g., 192.168.1.1/24):")
        self.label.pack(pady=10)

        self.ip_range_entry = tk.Entry(self, width=30)
        self.ip_range_entry.pack(pady=10)

        # Start scan button
        self.scan_button = tk.Button(self, text="Start Scan", command=self.start_scan)
        self.scan_button.pack(pady=10)

        # Text box to display results
        self.results_box = tk.Text(self, height=10, width=40, wrap=tk.WORD)
        self.results_box.pack(pady=10)
        self.results_box.config(state=tk.DISABLED)

    def start_scan(self):
        # Get IP range input
        ip_range = self.ip_range_entry.get()
        if not ip_range:
            messagebox.showerror("Input Error", "Please enter a valid IP range!")
            return

        # Start the scanning in a separate thread
        self.scan_button.config(state=tk.DISABLED)
        threading.Thread(target=self.scan_network, args=(ip_range,)).start()

    def scan_network(self, ip_range):
        self.results_box.config(state=tk.NORMAL)
        self.results_box.delete(1.0, tk.END)  # Clear previous results

        try:
            # Windows/Unix-based ARP scan command (replace with arp-scan if available)
            # For Windows, use 'arp -a', or for Unix/Linux, 'arp-scan' is a good tool.
            if subprocess.os.name == "nt":  # Windows
                command = ["arp", "-a"]
            else:  # Unix/Linux
                command = ["sudo", "arp-scan", ip_range]
            
            # Run the command and capture the output
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
            self.display_results(output)

        except subprocess.CalledProcessError as e:
            self.results_box.insert(tk.END, f"Error: {e.output}\n")
        except Exception as e:
            self.results_box.insert(tk.END, f"Unexpected error: {str(e)}\n")

        self.scan_button.config(state=tk.NORMAL)
        self.results_box.config(state=tk.DISABLED)

    def display_results(self, output):
        # Display the output from the scan in the text box
        self.results_box.insert(tk.END, output)

if __name__ == "__main__":
    app = ARPScanner()
    app.mainloop()
