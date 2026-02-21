# ChargeWise AI

Intelligent EV Charging Demand Prediction and Infrastructure Planning System.

## Project Status

This repository currently contains the initial project structure and development environment setup. Core functionality will be implemented in later stages.

---

## Setup Guide

Follow these steps to set up the project locally.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/neel3o115/chargewise-ai.git
cd chargewise-ai
```

---

### 2️⃣ Create a Virtual Environment

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

After activation, your terminal prompt should display:

```bash
(venv)
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Verify Setup

Run the welcome script to confirm that everything is working correctly:

```bash
python welcome.py
```

If successful, a console animation and welcome message will appear.

---

## Project Structure

```
chargewise-ai/
│
├── app/            # User interface (to be implemented)
├── src/            # Core modules (prediction, processing, etc.)
├── data/           # Datasets
├── models/         # Saved and trained models
├── notebooks/      # Research experiments and prototyping
├── docs/           # Documentation
│
├── requirements.txt
├── .gitignore
├── welcome.py      # Environment verification script
└── README.md
```

---

## Roadmap

* [x] Initial project structure
* [x] Development environment setup
* [ ] Data collection and preprocessing
* [ ] Demand prediction model
* [ ] Location optimization module
* [ ] Simulation engine
* [ ] Interactive dashboard
* [ ] Deployment
