# Chaotic Double Pendulum Simulation

A real-time physical simulation of a **Double Pendulum system** built using Python and Pygame. The project simulates multiple double pendulums simultaneously, starting with microscopic variations in their initial angles to visually demonstrate **chaos theory** and the *butterfly effect*.

## 🚀 Features
* **Chaotic Motion Visualization:** Simulates 6 unique double pendulums simultaneously.
* **Sensitivity to Initial Conditions:** Watch how starting angles differing by just 0.05 degrees completely diverge into wildly different paths over time.
* **Motion Trails:** Vibrant, color-coded particle paths showing the chaotic trajectory of the secondary masses.
* **Lagrangian Physics Engine:** Uses explicit equations of motion solved iteratively per frame with an adjustable time-scaling factor.

## 🛠️ Tech Stack & Dependencies
* **Language:** Python 3.x
* **Graphics/UI:** `pygame`
* **Mathematics:** `numpy`, `scipy` (Ready for extension)

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd YOUR_REPO_NAME
   ```

2. **Install the required packages:**
   ```bash
   pip install pygame numpy scipy matplotlib
   ```

3. **Run the simulation:**
   ```bash
   python main.py
   ```

## 📐 How It Works
The system calculates the angular accelerations ($\alpha_1$ and $\alpha_2$) at each frame using the differential equations derived from the Lagrangian mechanics of a double pendulum. Earth's exact gravitational acceleration ($g$) is calculated using the actual values for the Earth's mass ($M_\oplus$) and radius ($r$).

$$g = \frac{G \cdot M_\oplus}{r^2}$$
