🚦 Vibration Analysis of Two-Wheeler Chassis using FFT
This project simulates and analyzes vibration data from a two-wheeler chassis using Fast Fourier Transform (FFT) in Python. The goal is to identify critical vibration frequencies (like engine or frame-induced resonance) that can impact ride comfort and vehicle durability — just like in real-world NVH (Noise, Vibration, Harshness) testing at automotive companies like Bajaj.

🔧 Project Objectives
- Simulate time-domain vibration signal of a bike frame (1 second, 1000 Hz sampling).

- Apply FFT (Fast Fourier Transform) to convert the signal into the frequency domain.

- Identify and visualize dominant frequencies that could indicate possible resonance.

- Save plots for time and frequency domains for use in reports or presentations.

📁 Project Structure
vehicle_vibration_analysis/
├── bike_vibration_data.csv          # Simulated vibration signal (Amplitude only)
├── vibration_analysis.py            # Python script to run FFT and generate plots
├── vibration_time_plot.png          # Time-domain visualization
├── vibration_fft_plot.png           # Frequency-domain visualization
└── README.md  

📊 Sample Output
## Time Domain Plot
Shows how the vibration amplitude changes over time.


## Frequency Domain (FFT) Plot
Shows dominant frequencies — peaks represent potential resonance frequencies like 50 Hz (frame) or 150 Hz (engine).

📦 Tools & Libraries
- Python 3.x
- numpy
- pandas
- matplotlib
- scipy.fft

🧠 Engineering Context
- This simulation reflects what NVH engineers do in ride quality testing.
- Identifying dominant vibration frequencies helps in:

  - Frame tuning
  - Damping design
  - Reducing fatigue and improving comfort

✅ Future Improvements (if time allows)
- Integrate with actual sensor data from accelerometers
- Build a GUI using tkinter
- Real-time vibration monitoring using Raspberry Pi or Arduino

🤝 Connect
I'm always up for connecting with fellow data lovers, mentors, and potential collaborators! 

<p align="left">
  <a href="https://www.linkedin.com/in/ravina-patidar-474a9b255/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
  </a>
  
  <a href=" https://ravina172.github.io/" target="_blank">
    <img src="https://img.shields.io/badge/Portfolio-FF6F61?style=for-the-badge&logo=internet-explorer&logoColor=white" alt="Portfolio"/>
  </a>
  
  <a href="https://github.com/ravina172" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-6e6e6e?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
  </a>
  
  <a href="https://www.kaggle.com/ravinapatidar" target="_blank">
    <img src="https://img.shields.io/badge/Kaggle-89CFF0?style=for-the-badge&logo=kaggle&logoColor=white" alt="Kaggle"/>
  </a>

  <a href="mailto:ravinapatidar13634@gmail.com" target="_blank">
    <img src="https://img.shields.io/badge/Gmail-8BC34A?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail"/>
  </a>
</p>
