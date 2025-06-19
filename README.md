# GreenEdge-Zero-Carbon-Edge-Datacenter-Powered-by-Solar-Energy
A zero-carbon edge datacenter powered entirely by solar energy. GreenEdge integrates sustainable energy solutions with high-performance computing at the network edge, minimizing carbon footprint while maintaining reliable, low-latency services.

---

## Features

- Real-time solar energy monitoring (voltage, current, power)
- Battery management with state of charge (SoC) tracking
- Intelligent workload scheduling based on energy availability
- Modular architecture for easy extension and integration
- Console dashboard for live status updates

---

## Project Structure

```

GreenEdge/
├── solar\_monitor.py      # Simulates solar panel sensor readings
├── battery\_manager.py    # Manages battery charge and discharge
├── load\_balancer.py      # Schedules tasks based on battery status
├── dashboard.py          # Displays energy and system status
├── main.py               # Main program integrating all modules
└── README.md             # This documentation file

````

---

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/GreenEdge.git
   cd GreenEdge
````

2. (Optional) Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. This project uses only Python’s standard library; no additional packages are required.

---

## Usage

Run the main controller to start the simulation:

```bash
python main.py
```

The program will:

* Simulate solar panel energy generation periodically
* Update battery state of charge based on input energy and loads
* Schedule workloads depending on available energy
* Display current system status in the console

---

## Module Details

### solar\_monitor.py

* Simulates solar panel output readings (voltage, current, power)
* Provides data to battery and load management modules

### battery\_manager.py

* Tracks battery state of charge (SoC)
* Manages charging from solar and discharging for workloads
* Prevents battery overcharge and deep discharge

### load\_balancer.py

* Schedules computing tasks based on available battery energy
* Prioritizes critical workloads when energy is limited

### dashboard.py

* Displays live updates on solar output, battery charge, and system status
* Designed for console output, easily extendable for GUI/web

### main.py

* Integrates all modules into a continuous simulation loop
* Coordinates energy flow, workload scheduling, and status updates

---

## Future Work

* Integrate with real solar panel and battery hardware
* Develop a web-based dashboard with interactive charts
* Implement predictive workload scheduling with machine learning
* Expand energy sources with grid fallback and wind integration
* Add persistent logging and alerting for system events

---

## Contributing

Contributions and improvements are welcome! Please open issues or pull requests for bug fixes, features, or documentation enhancements.

---

## License

This project is licensed under the MIT License.
