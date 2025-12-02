# 🎯 Internship Domain Recommender (StaxTech AI Project)

An interactive and user-friendly **web-based recommendation system** that suggests the best internship domains based on a student’s skills.  
Built using **HTML, CSS, and Vanilla JavaScript**, the system uses **content-based filtering** with **Jaccard similarity** to rank domains by skill overlap.

🌐 **Live Demo:**  
👉 https://shubham-goud.github.io/stax_ai_recommender/

---

## 🚀 Features

### 🔍 **Skill-Based Domain Matching**
- Users enter their skills (comma separated).
- The system compares skills with domain requirements.
- Domains are ranked using **Jaccard similarity**.

### 🎨 **Modern & Clean UI**
- Simple, easy-to-use layout.
- Green chips → Skills you already have.
- Red chips → Skills recommended to learn next.
- Fully responsive design.

### ⚡ **Preset Skill Buttons**
Quick test profiles:
- Data / ML
- Web Development
- UI/UX Design

### 📊 **Covers 15+ Internship Domains**
Including:
- AI & Machine Learning  
- Data Science  
- NLP  
- Deep Learning & Computer Vision  
- Web Development  
- Mobile App Development  
- Cloud & DevOps  
- Product Management  
- QA Automation  
- Cybersecurity  
- IoT  
…and more!

---

## 🛠️ Tech Stack

| Component | Technology |
|----------|------------|
| Frontend | HTML, CSS, Vanilla JavaScript |
| Algorithm | Content-Based Filtering (Jaccard Similarity) |
| Deployment | GitHub Pages |

---

## 🧠 How It Works

1. User enters technical skills (example: `python, html, css, sql`).
2. These skills are normalized and converted into a set.
3. Each domain has a predefined set of required skills.
4. The similarity between user skills and domain skills is calculated using:

### **📐 Jaccard Similarity**
\[
J(A, B) = \frac{|A \cap B|}{|A \cup B|}
\]

5. All domains are ranked from highest to lowest match score.
6. The result is displayed with highlighted skill chips.

---

## 📂 Project Structure

stax_ai_recommender/
│
├── docs/
│ └── index.html # Main UI (GitHub Pages loads from here)
│
├── data/ # (Optional) Supporting files
│
└── requirements.txt # Not used, kept for project completeness


---

## 🖥️ Running Locally

You can run this instantly without any setup:

1. Download the repository.
2. Open `docs/index.html` in any browser (Chrome, Edge, Firefox).
3. That's it — no installation or server needed.

---

## 🌐 Deployment

Deployed using **GitHub Pages** at:

👉 **https://shubham-goud.github.io/stax_ai_recommender/**

---

## 📜 License

This project is open-source under the MIT License.

---

## 👨‍💻 Author

**Shubham Goud**  
B.Tech Artificial Intelligence & Data Science  
StaxTech Internship – AI Track  

---

## ⭐ If you like this project  
Give it a **star** ⭐ on GitHub — it motivates me to build more awesome tools!

