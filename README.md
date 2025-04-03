# 📈 Portfolio Optimizer

An interactive web application that helps users optimize their investment portfolios using Modern Portfolio Theory (MPT). The application visualizes the efficient frontier and allows users to select stocks from different sectors to create an optimized portfolio.

## 💻 Tech Stack

**Frontend:** HTML, CSS, JavaScript
<br>
**Backend:** Python (Flask)
<br>
Chart.js for visualization,
Select2 for enhanced dropdowns,
Modern Portfolio Theory for optimization

## 📸 Live Demo 
<img width="1501" alt="Image" src="https://github.com/user-attachments/assets/b1b38f39-7b4b-4e96-b562-e4289beac53e" />

## 🎯 Features

- Interactive stock selection by sector
- Real-time portfolio optimization
- Efficient frontier visualization
- Educational content about Modern Portfolio Theory
- User-friendly interface with search functionality

## Local Development Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd portfolio-optimizer
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to `http://localhost:5000`

## 📚 Future Improvements
- login feature and database to store users' portfolios
- discover page to find other users' portfolios
- connect to plaid/robinhood external API's

## Deployment

This application is deployed on Netlify.
