# Portfolio Optimizer

An interactive web application that helps users optimize their investment portfolios using Modern Portfolio Theory (MPT). The application visualizes the efficient frontier and allows users to select stocks from different sectors to create an optimized portfolio.

## Features

- Interactive stock selection by sector
- Real-time portfolio optimization
- Efficient frontier visualization
- Educational content about Modern Portfolio Theory
- User-friendly interface with search functionality

## Technologies Used

- Python (Flask)
- JavaScript
- Chart.js for visualization
- Select2 for enhanced dropdowns
- Modern Portfolio Theory for optimization

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

## Deployment

This application is deployed on Netlify. To deploy your own instance:

1. Fork this repository
2. Sign up for Netlify
3. Connect your GitHub repository to Netlify
4. Configure the build settings:
   - Build command: `pip install -r requirements.txt`
   - Publish directory: `templates`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 