# LeetCode AI Coach 🚀

A Python CLI tool that analyzes your LeetCode progress, identifies weak areas, and visualizes your coding interview preparation.

This project fetches your LeetCode statistics using the LeetCode GraphQL API and generates insights about your solved problems.

---

## 📌 Features

* Fetch solved problems from LeetCode
* Analyze difficulty distribution
* Visualize progress using graphs
* Identify weak areas in problem solving
* Lightweight CLI-based tool

---

## 🛠 Tech Stack

* Python
* Requests (API calls)
* Matplotlib (Data visualization)
* GraphQL (LeetCode API)

---

## 📂 Project Structure

```
leetcode-tracker/
│
├── main.py
├── fetch_data.py
├── analyzer.py
├── recommender.py
├── visualizer.py
│
├── data/
│   └── problems.json
│
├── graphs/
│   └── progress.png
│
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/yourusername/leetcode-tracker.git
cd leetcode-tracker
```

Install dependencies:

```
pip install requests matplotlib
```

---

## ▶️ Usage

Run the program:

```
python main.py
```

Example Output:

```
Solved Problems

Easy   : 102
Medium : 57
Hard   : 0
```

The program will also generate a visualization chart inside the **graphs** folder.

---

## 📊 Example Graph

The tool generates a difficulty distribution chart showing your LeetCode progress.

---

## 🎯 Purpose

This project was built to:

* Strengthen Python skills
* Practice API integration
* Analyze coding interview progress
* Build a useful developer tool

---

## 🚀 Future Improvements

* Topic-wise analysis (DP, Graph, Array, etc.)
* Automatic problem recommendations
* Web dashboard
* Weekly progress tracking
* GitHub action for automatic updates

---

## 👨‍💻 Author

Built with Python to improve problem-solving and coding interview preparation.
