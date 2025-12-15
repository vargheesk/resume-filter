# 📄 Intelligent Resume Filter
### Powered by OCR & Tesseract

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Tesseract](https://img.shields.io/badge/Tesseract_OCR-blue?style=for-the-badge)

---

## 🌟 Overview

The **Intelligent Resume Filter** is a smart tool designed to streamline the recruitment process. By leveraging the power of **Optical Character Recognition (OCR)**, it automatically extracts text from resume images and analyzes them against a set of required skills. 

This project demonstrates the practical application of Deep Learning and Computer Vision in HR Tech, providing instant feedback on candidate suitability.

---

## 🚀 Key Features

*   **🖼️ Image-based Parsing**: Upload resume images (JPG, PNG) directly.
*   **👁️ Optical Character Recognition**: Uses Tesseract to accurately extract text from documents.
*   **🎯 Skill Matching Algorithm**: Automatically compares extracted text with your specific job requirements.
*   **📊 Instant Scoring**: Generates a percentage match score instantly.
*   **✅ Visual Feedback**: Highlights found vs. missing skills for quick analysis.
*   **✨ Minimalist UI**: Clean, professional interface built with Streamlit.

---

## 🛠️ Tech Stack

*   **Frontend**: Streamlit
*   **Image Processing**: OpenCV, PIL (Python Imaging Library)
*   **OCR Engine**: Tesseract-OCR
*   **Language**: Python

---

## 📦 Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/vargheesk/resume-filter.git
    cd resume-filter
    ```

2.  **Install dependencies**
    ```bash
    pip install opencv-python pytesseract streamlit pillow
    ```

3.  **Install Tesseract OCR**
    *   Download and install Tesseract from [here](https://github.com/UB-Mannheim/tesseract/wiki).
    *   *Note: Ensure the path `D:\Luminar\Study\Deep learning\DL Project\OCR\Tesseract-OCR\tesseract.exe` matches your installation or update it in the code.*

---

## 🎮 Usage

1.  **Run the Streamlit App**
    ```bash
    streamlit run app2.py
    ```

2.  **Steps to Filter**:
    *   **Upload**: Drag and drop a resume image into the upload area.
    *   **Define Skills**: Enter the required skills separated by commas (e.g., *python, java, sql*).
    *   **Analyze**: Click the "Analyze Resume" button.
    *   **View Results**: See the match score and detailed breakdown of skills found.

---

## 📂 Project Structure

```
├── app2.py              # Main Streamlit application
├── fiter.ipynb          # Jupyter Notebook with step-by-step logic
├── resume.jpeg          # Sample resume for testing
└── README.md            # Project documentation
```

---

<div align="center">

**[Made with ❤️ by Vargheeskutty]**

</div>
