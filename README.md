
# 🛒 Supermarket Sales Dashboard

An interactive and visually engaging Streamlit web application that provides deep insights into supermarket sales data. This dashboard allows users to explore sales performance across various dimensions including product lines, branches, cities, customer demographics, and payment methods. Designed for managers, analysts, and marketers who seek to extract actionable intelligence from transactional sales data.

---


This well detailed Sales Performance Analytics Dashboard which I built for a supermarket can be accessed live on streamlit [Here](https://salesperformance.streamlit.app/)

---


## 📬 Author

**Gbenga Kajola**
🎓 Certified Data Analyst | 👨‍💻 Certified Data Scientist | 🧠 AI/ML Engineer | 📱 Mobile App Developer 

[LinkedIn](https://www.linkedin.com/in/kajolagbenga)

[Portfolio](https://kajolagbenga.netlify.app)

[Certified_Data_Scientist](https://www.datacamp.com/certificate/DSA0012312825030)

[Certified_Data_Analyst](https://www.datacamp.com/certificate/DAA0018583322187)

[Certified_SQL_Database_Programmer](https://www.datacamp.com/certificate/SQA0019722049554)


---

## 📂 Project Structure

```
supermarket-sales-dashboard/
│
├── app.py                  # Streamlit application source code
├── requirements.txt        # Python dependencies for the app
├── supermarket_sales.csv   # Input dataset (original sales data)
└── README.md               # Project documentation
```

---

## 📊 Dataset Description

The dataset used is a real-world sample of 1,000 supermarket transactions with the following fields:

- **Invoice ID**: Unique ID for each transaction.
- **Branch**: Branch label (A, B, or C).
- **City**: City where the branch is located.
- **Customer type**: Type of customer ("Member" or "Normal").
- **Gender**: Gender of the customer.
- **Product line**: Category of the purchased product.
- **Unit price**: Unit price of the item.
- **Quantity**: Number of items bought.
- **Tax 5%**: Tax amount.
- **Total**: Total amount paid including tax.
- **Date**: Date of purchase.
- **Time**: Time of purchase.
- **Payment**: Payment method used.
- **cogs**: Cost of goods sold.
- **gross margin percentage**: Margin percentage.
- **gross income**: Profit made from the transaction.
- **Rating**: Customer rating (out of 10).

---

## 🚀 Features

- ✅ **Sidebar Filters**: Filter data by branch, city, gender, and customer type.
- ✅ **KPI Cards**: Real-time metrics such as revenue, quantity sold, rating, and profit.
- ✅ **Monthly Trend Analysis**: Line charts displaying total revenue and quantity trends.
- ✅ **Product Line Insights**: Bar charts showing product-wise sales performance.
- ✅ **Branch & City Comparison**: Visual breakdown by region and branch performance.
- ✅ **Customer Demographics**: Insights based on gender and customer type.
- ✅ **Payment Methods**: Pie chart showing preferred payment options.
- ✅ **Actionable Business Insights**: Recommendations based on data patterns.
- ✅ **CSV Export**: Download filtered dataset as CSV for further analysis.

---

## 🛠️ Installation Guide

### 📦 Prerequisites

- Python 3.8 or later
- pip

### 🔧 Setup

1. Clone the repository or download the source files.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run app.py
```

---

## 📈 Visualizations

This app uses `plotly` for interactive charts and `Streamlit` for the web interface. Each tab in the app presents a unique visualization:
- Line charts (Revenue & Quantity by Month)
- Bar plots (Revenue by Product Line, Branch, City)
- Pie charts (Gender, Customer Type, Payment Methods)

---

## 📌 Insights Delivered

- **Top Performing Product Lines**: Helps inventory and marketing planning.
- **Low-performing Regions**: Guide operational improvements.
- **Customer Segments**: Tailor promotions to gender and loyalty segments.
- **Payment Preferences**: Optimize for the most used payment methods.
- **Monthly Patterns**: Align supply chain and staffing with demand peaks.

---

## 📤 Deployment

To deploy this app online:
1. Push to GitHub.
2. Deploy on [Streamlit Cloud](https://streamlit.io/cloud) by linking the GitHub repo.
3. Ensure `requirements.txt` is present in the root folder.

---

## 🤝 Contribution

Feel free to fork the repo, create a new branch, and submit a pull request. Contributions and suggestions are welcome!

---

## 📃 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


---

## 🧠 Final Note

This project is ideal for:
- Data storytelling with real sales data
- Training junior data analysts
- Business decision support systems
- Dashboard development tutorials
