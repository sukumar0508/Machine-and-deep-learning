# 🎨 Pixel to Panel: Anime-Style Image Conversion using CNN Autoencoder

Transform your real-life images into anime-style art using deep learning!  
This project implements a **CNN-based Autoencoder model** trained to convert real human face images into stylized anime images.

---

## 📑 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Workflow](#project-workflow)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Model Architecture](#model-architecture)
- [Results](#results)
- [Technologies Used](#technologies-used)
- [Contributors](#contributors)
- [License](#license)

---

## 🚀 Project Overview

**Pixel to Panel** is a deep learning project focused on real-to-anime image conversion using a **Convolutional Autoencoder**. Inspired by the growing popularity of AI-generated anime art, the model learns pixel-level transformations to generate anime-style features from regular human images.

---

## ✨ Features

- Drag & Drop + Upload Image Interface
- Converts image to anime-style using trained CNN Autoencoder
- Web-based front-end using HTML + CSS + JavaScript
- Real-time prediction and display
- Fully responsive and aesthetic UI
- Optimized loading animation ✨

---

## 🔁 Project Workflow

```mermaid
graph TD
A[Input Real Image] --> B[Preprocessing]
B --> C[Feature Extraction using CNN]
C --> D[Latent Encoding (Autoencoder Bottleneck)]
D --> E[Reconstruction into Anime Image]
E --> F[Display Anime Output on Web]
