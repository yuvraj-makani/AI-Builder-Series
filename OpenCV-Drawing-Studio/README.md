# 🎨 OpenCV Drawing Studio

A simple drawing application built using **Python** and **OpenCV** to explore mouse events, GUI windows, and basic computer vision drawing functions.

---

## 🚀 Features

- Cursor Coordinates Detection
- Freehand Drawing
- Rectangle Drawing
- Save Drawing (`S`)
- Exit Application (`ESC`)

---

## 🛠️ Tech Stack

- Python 3.x
- OpenCV
- NumPy

---

## 📂 Project Structure

```
OpenCV-Drawing-Studio/
│
├── OpenCV_Drawing_Studio.py
├── README.md
├── requirements.txt
├── outputs/
└── screenshots/
    ├── home.png
    ├── freehand.png
    └── rectangle.png
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/OpenCV-Drawing-Studio.git
```

### 2. Navigate to the project

```bash
cd OpenCV-Drawing-Studio
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the project

```bash
python OpenCV_Drawing_Studio.py
```

---

## 🎮 Controls

| Action | Control |
|---------|---------|
| Display Cursor Coordinates | Move Mouse |
| Freehand Drawing | Left Mouse Button |
| Rectangle Drawing | Right Mouse Button *(if implemented)* |
| Save Drawing | **S** |
| Exit Application | **ESC** |

---

## 📚 Concepts Learned

- OpenCV GUI (`namedWindow`, `imshow`, `waitKey`)
- Mouse Callbacks
- Mouse Events
- Cursor Coordinates Detection
- Freehand Drawing using `cv2.line()`
- Rectangle Drawing using `cv2.rectangle()`
- Saving Images using `cv2.imwrite()`

---

## 📄 License

This project is created for learning and educational purposes.