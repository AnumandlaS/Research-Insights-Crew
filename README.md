# 📰 Research Insights Crew

This project automates the **research, writing, and fact-checking** of tech-related news articles using **CrewAI** and **Gemini (Google Generative AI)**.  
It brings together specialized AI agents **Researcher**, **Writer**, and **Fact Checker** to collaboratively generate high-quality, fact-verified blog posts on any given topic.

---

## 🚀 Features

- 🤖 **Automated Research** – Gathers insights and trends from multiple sources.  
- ✍️ **Intelligent Writing** – Produces engaging, markdown-formatted articles.  
- ✅ **Fact Verification** – Ensures accuracy of information before publishing.  
- 🔄 **Sequential Workflow** – Agents work collaboratively in order (Research → Write → Fact Check).  
- ⚙️ **Customizable Topics** – Easily specify any topic through input.

---

## 🧠 Project Structure

```
project/
│
├── agents.py        # Defines Researcher, Writer, Fact Checker
├── tasks.py         # Defines tasks for each agent
├── crew.py          # Forms the Crew and runs the workflow
├── tools.py         # Added the serper tool
├── .env             # Stores your keys
├── .gitignore       # Ignores venv/ and .env
└── requirements.txt # dependencies
```

---

## 🧩 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ai-news-crew.git
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the root directory and add your Gemini API key and Serper API key:
```
GOOGLE_API_KEY=your_google_api_key_here
SERPER_API_KEY=your_serper_api_key_here
```

### 5. Run the Project
```bash
python crew.py
```

This will trigger a sequence of:
1. **Research Report** generation  
2. **Article Writing** in markdown  
3. **Fact Checking** of the output  

The final markdown article will be saved as `new-blog-post.md` and the fact checking will output a `fact-check-report.md`.

---

## 🧾 Example Output

When you run:
```python crew.py```

You'll get two Markdown files, one containing the generated article and another containing the fact-checking report, both discussing the latest trends and insights on synthetic data generation (basically, the topic).

---


## 💡 Future Improvements
- Add more specialized agents which can help researchers (Maybe another kind of agent which helps researchers format their papers, find references relevant, etc).  
- Support parallel agent collaboration using CrewAI’s distributed mode.

--- 
Exploring multi-agent AI workflows using CrewAI and Gemini.  
