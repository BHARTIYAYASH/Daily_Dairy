# DailyDairy

## 📌 Project Description
DailyDairy is a web-based **Daily Dairy Consumption Tracker** that allows users to log, edit, and track their dairy consumption. Users can record items such as milk, cheese, and butter along with their quantity and date of consumption. The app supports real-time date selection and allows modifications to entries.

**This is a small-scale personal project that I initially built on my own, and the full code is available here on GitHub. Later, I experimented with  Lovable (no-code just prompts) to create it, and it turned out to be quite decent.**

🚀 **Live Demo**: Check out here: https://daily-dairy.lovable.app

## 🚀 Features
- 📅 **Real-time Date Selection** – Default date is set to the current day, but users can choose a different date.
- ✏️ **Edit Entries** – Modify item name, quantity, and date after adding them.
- 📊 **Track Consumption** – View and manage past records of dairy usage.
- 🎨 **User-Friendly UI/UX** – Simple and clean interface for seamless tracking.

## 🛠️ Technologies Used
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (Can be switched to PostgreSQL for deployment)
- **Hosting:** Render.com (for free long-term hosting)

## ⚙️ Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/dailydairy.git
cd dailydairy
```
### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Run Migrations
```bash
python manage.py migrate
```
### 5️⃣ Start the Development Server
```bash
python manage.py runserver
```


## 🌍 Deployment on Render
1. Push code to **GitHub**
2. Create a **new Web Service on Render.com**
3. Connect GitHub repository
4. Use the following commands for build & start:
   ```bash
   pip install -r requirements.txt && python manage.py migrate
   gunicorn dailydairy.wsgi:application
   ```
5. Get your **live URL** and start tracking!



---

Let me know if you want any modifications! 🚀

