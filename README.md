# 🎵 Universal Media Player: A Modern GUI-Based Multimedia Player

Welcome to the **Universal Media Player** project! This Python-based multimedia player brings together a sleek, modern interface and essential playback features, making it a versatile tool for playing your favorite media files. Whether you're listening to music or watching videos, this application provides a seamless experience.

## 🚀 Project Overview

The **Universal Media Player** is a desktop application built using Python, with a focus on providing a user-friendly GUI for loading and playing media files. The application supports a wide range of media formats and includes features like play, skip forward, skip backward, volume control, and more.

### Key Features:
- **Custom GUI**: Developed using Tkinter and CustomTkinter for a modern and visually appealing interface.
- **Media Playback**: Supports various media formats such as MP3, WAV, MP4, MKV, and AVI.
- **Album Cover Display**: Dynamically displays album cover art or a placeholder image during playback.
- **Progress Tracking**: Real-time progress bar for tracking media playback.
- **Volume Control**: Adjustable volume slider for precise audio control.
- **Skip Forward/Backward**: Easily navigate through your playlist with skip buttons.
- **Threading**: Ensures smooth playback and UI responsiveness by handling tasks concurrently.

## 🛠️ Skills and Technologies Used

- **Python**: The core programming language used to develop the application.
- **Tkinter**: Utilized for creating the graphical user interface (GUI).
- **CustomTkinter**: Enhances the GUI with advanced widgets and a modern aesthetic.
- **Pygame**: Used for managing media playback, including audio and video.
- **PIL (Pillow)**: Employed for handling and displaying album cover images.
- **Threading**: Ensures smooth user experience by performing tasks like progress tracking in the background.
- **File Dialog**: Allows users to load media files via a file explorer interface.
- **Cross-Platform Compatibility**: Works on multiple operating systems with minimal adjustments.

## 📂 Project Structure

```
Universal-Media-Player/
│
├── img/
│   └── default_cover.jpg  # Placeholder image for album covers
├── main.py                # Main application code
└── README.md              # Project documentation
```

## 📜 How to Run the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/twonum/Universal-Media-Player.git
   cd Universal-Media-Player
   ```

2. **Install Dependencies**:
   Ensure you have the required libraries installed:
   ```bash
   pip install customtkinter pygame pillow
   ```

3. **Run the Application**:
   ```bash
   python main.py
   ```

4. **Load Media**:
   Click the "Load Media" button to select and load your media files.

5. **Play, Skip, and Enjoy**:
   Use the Play button to start the media, and navigate through your playlist with the Skip buttons.


## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests. If you encounter any issues, please open an issue on GitHub.

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Enhance your media experience with the **Universal Media Player** – your all-in-one solution for playing music and videos with style!
