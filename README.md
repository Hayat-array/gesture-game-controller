# Gesture-Controlled Game with Mediapipe and Python

**Author:** Hayat Ali  

Control games using your hand gestures! This project allows **real-time hand gesture detection** via webcam and converts gestures into keyboard inputs for gaming.

---

## 🎯 Features

- **Real-time hand tracking** using Mediapipe.
- Gesture-based controls:
  - **Right hand movement → Accelerate (Right arrow key)**
  - **Left hand movement → Brake/Reverse (Left arrow key)**
- Visual feedback:
  - Draws hand landmarks and connections.
  - Displays current action on screen.
  - Shows FPS (Frames Per Second) for performance monitoring.
- Prevents repeated key presses to avoid multiple inputs.
- Works with Windows games that accept keyboard input.

---

## 🖼️ Demo

### Hand Detection in Action

![Hand Detection GIF](demo_hand_tracking.gif)  
*Shows hand landmarks and gesture detection in real-time.*

### Gesture Control for Game

![Gesture Control GIF](demo_game_control.gif)  
*Index finger movement mapped to accelerate or brake in a game.*



---

## ⚙️ Requirements

- Python 3.8+
- Libraries:
  - [OpenCV](https://pypi.org/project/opencv-python/)
  - [Mediapipe](https://pypi.org/project/mediapipe/)
  - [PyDirectInput](https://pypi.org/project/PyDirectInput/)


Control games using your hand gestures! This project allows **real-time hand gesture detection** via webcam and converts gestures into keyboard inputs for gaming using Mediapipe and PyDirectInput.

---

## 🧩 Step 1: Clone the Repository

1. Open your terminal or command prompt.
2. Navigate to the directory where you want to store your project:

```bash
cd path/to/your/projects
🐍 Step 2: Set Up a Virtual Environment (Recommended)

Create a virtual environment:

python -m venv venv


Activate the virtual environment:

Windows (PowerShell):

.\venv\Scripts\Activate.ps1


Windows (CMD):

.\venv\Scripts\activate.bat


Linux/Mac:

source venv/bin/activate


Upgrade pip:

pip install --upgrade pip

📦 Step 3: Install Dependencies

Install all required libraries:

pip install -r requirements.txt


This will install:

OpenCV

Mediapipe

PyDirectInput

🎮 Step 4: Run the Script

Ensure your webcam is connected and your game window is active.

Run the main script:

python gesture_control.py
```

Install dependencies:

```bash
pip install opencv-python mediapipe pydirectinput
🚀 Installation
Clone the repository or download the gesture_control.py script.

Open a terminal in the project directory.

Ensure your webcam is connected.

▶️ Usage
Run the script:

bash
Copy code
python gesture_control.py
Allow access to your webcam.

Move your hand in front of the camera:

Right side → Accelerate

Left side → Brake/Reverse

Press ESC to exit the program.

🧠 How It Works
Captures video from the webcam using OpenCV.

Uses Mediapipe Hands to detect hand landmarks in real-time.

Determines the x-position of the index finger tip.

Maps finger position to game controls:

Right side → Right arrow key

Left side → Left arrow key

Simulates key presses using PyDirectInput.

Draws landmarks and connections for visual feedback.

⚙️ Customization
Screen resolution: Adjust webcam capture resolution:

python
Copy code
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height
Gesture threshold: Adjust sensitivity for left/right detection:

python
Copy code
if index_x > w // 2 + 50:  # Right gesture
if index_x < w // 2 - 50:  # Left gesture
Detection confidence: Modify Mediapipe detection/tracking confidence:

python
Copy code
min_detection_confidence=0.5
min_tracking_confidence=0.5
🛠️ Troubleshooting
Hand not detected:

Ensure webcam is working.

Increase lighting in the room.

Increase min_detection_confidence.

Keys not working in the game:

Run the script as Administrator.

Ensure the game window is active.

Low FPS:

Close other heavy applications.

Reduce webcam resolution.

💡 Tips
Use a plain background for better detection.

Move hands smoothly for accurate tracking.

Can be extended for more gestures like jump, drift, or custom actions.

📜 License
This project is open-source. Feel free to modify and use it for personal projects. No warranty provided.

🙏 Acknowledgements
Mediapipe – Hand tracking library by Google

PyDirectInput – Simulate keyboard input

OpenCV – Webcam capture and drawing utilities

📝 Author
Hayat Ali – Python Developer & AI Enthusiast