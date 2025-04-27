# 🌐 ARP Scanner Tool

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

---

**ARP Scanner Tool** is a simple, yet effective tool designed to help you scan your local network for connected devices using ARP (Address Resolution Protocol).  
With a graphical interface built using `tkinter`, this tool allows users to scan a given IP range and display the results in real-time.

---

## 🚀 Features

- 🔍 **Scan IP Range**  
  • Allows users to input an IP range (e.g., 192.168.1.1/24) and performs a network scan to find devices in the specified range.

- ⚡ **ARP Scan for Connected Devices**  
  • Utilizes ARP scanning to detect devices in the local network and displays results such as IP and MAC addresses.

- 🖥️ **Cross-platform Support**  
  • Works on both Windows and Unix/Linux systems for scanning local networks.

---

## 📥 Installation

**Requirements**  
- Python 3.x or higher
- `tkinter` (included with Python for most distributions)
- `arp-scan` (for Unix/Linux users, can be installed with `sudo apt-get install arp-scan`)

**Quick Setup**

```bash
# Clone the repository
git clone https://github.com/yourusername/arp-scanner.git
cd arp-scanner

# Install required dependencies (for Linux/Unix)
sudo apt-get install arp-scan

# Run the tool
python arp_scanner.py
```

---

## 🔨 Usage

After launching the ARP Scanner tool, you'll be greeted with a graphical interface.

```bash
Enter the IP Range (e.g., 192.168.1.1/24):
```
Simply enter the desired IP range and click on Start Scan. The tool will start scanning the network and display the results, showing the connected devices along with their IP and MAC addresses.

---

## ✨ Roadmap

- ✅ Add functionality for exporting results to a file.
- 🔜 Improve error handling and scanning capabilities.
- 🔒 Implement additional network protocols for scanning.
- 📚 Expand features for deeper network analysis.

---

## 🤝 Contributing

Contributions are highly welcome! 🚀
If you'd like to propose improvements, report bugs, or add new features:
**1.** Fork the repository.
**2.** Create a new branch (git checkout -b feature/AmazingFeature).
**3.** Commit your changes (git commit -m 'Add some AmazingFeature').
**4.** Push to the branch (git push origin feature/AmazingFeature).
**5.** Open a pull request.
Let's make ARP Scanner Tool even better!

## ⚠️ Legal Disclaimer

> WASTT is provided for **educational and authorized security testing** only.
> - Use only on systems you own **or** have **explicit written permission** to test.
> - Unauthorized use of this tool against systems without consent is **illegal** and **unethical**.
> - The developers take **no responsibility** for misuse, damages, or legal consequences.

Use responsibly. Stay ethical. 🛡️

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

# ✨ Happy Testing!
