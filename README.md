# 🎥 Live Camera Gaussian Blur

A real-time camera application built with **Python** and **OpenCV**.

This project captures live video from a webcam, applies a Gaussian Blur filter to every frame, and displays both the original and blurred video simultaneously.

## ✨ Features

- Live webcam capture
- Real-time Gaussian Blur effect
- Side-by-side original and blurred camera windows
- Save the blurred image as a JPG file
- Simple keyboard controls

## 🛠️ Requirements

- Python 3
- OpenCV
- A webcam

## 📦 Installation

Install OpenCV:

```bash
pip install opencv-python
```

## 🚀 Usage

Run the program:

```bash
python3 main.py
```

Make sure your webcam is connected and accessible.

## ⌨️ Controls

| Key | Action |
|---|---|
| Q | Save the blurred frame and exit |

## 🧠 How It Works

1. OpenCV accesses the webcam using `cv2.VideoCapture(0)`.
2. Each video frame is captured.
3. `cv2.GaussianBlur()` applies a Gaussian smoothing filter.
4. Two windows display the original and blurred frames.
5. Pressing `Q` saves the blurred frame as `gaussian_image.jpg`.

## 📁 Output

The program generates:

`gaussian_image.jpg`

## 👨‍💻 Author

Created by **Amirreza**.

---

*Built with Python 🐍 and OpenCV 👁️*
