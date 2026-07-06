<p align="center">
  <a href="https://www.saucedemo.com" target="_blank">
    <img src="swaglabs.png" alt="Swag Labs Logo" width="400">
  </a>
</p>

<h1 align="center">
SauceDemo Playwright Test Automation Framework
</h1>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Playwright](https://img.shields.io/badge/Playwright-Latest-45ba4b)
![Pytest](https://img.shields.io/badge/Pytest-Testing-0A9EDC)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI-black)
![Docker](https://img.shields.io/badge/Docker-2496ED)

</p>

---

## Overview

This project is a UI test automation framework for the SauceDemo application built with **Python**, **Playwright**, and **Pytest**.

The framework follows the **Page Object Model (POM)** design pattern and provides automated end-to-end test scenarios covering the complete purchase flow.

---

## Features

- Page Object Model (POM) architecture
- End-to-end UI test automation
- Cross-browser testing
- Reusable BasePage
- Modular Page Objects
- Docker support
- GitHub Actions integration
- Simple test execution
- Scalable project architecture

---

## Tech Stack

- Python
- Playwright
- Pytest
- Docker
- GitHub Actions

---

## Project Structure

```text
.
├── .github/
│   └── workflows/          # GitHub Actions workflows
├── config/                 # Configuration files
├── docs/                   # Project documentation and diagrams
├── framework/
│   └── base_test.py        # Base test configuration
├── pages/
│   ├── components/         # Reusable page components
│   ├── BasePage.py
│   ├── LoginPage.py
│   ├── InventoryPage.py
│   ├── CartPage.py
│   ├── CheckoutPage.py
│   ├── OverviewPage.py
│   └── OrderCompletePage.py
├── tests/                  # Automated test suites
├── conftest.py             # Pytest fixtures
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

### Directory Overview

- **config/** – project configuration files.
- **docs/** – documentation, diagrams, and project assets.
- **framework/** – base test classes and shared test functionality.
- **pages/** – Page Objects and reusable UI components.
- **tests/** – automated UI test scenarios.
- **conftest.py** – shared Pytest fixtures and configuration.

---

## Application E2E Test Flow

The automated test suite covers the following end-to-end user journey:

1. Login
2. Inventory
3. Cart
4. Checkout
5. Checkout Overview
6. Order Complete

![SauceDemo E2E Test Flow](SauceDemo_E2E_TestFlow_Diagram.png)

---

## Framework Architecture

The framework follows the **Page Object Model (POM)** design pattern.

```text
Tests
   │
   ▼
Page Objects
   │
   ▼
BasePage
   │
   ▼
Playwright
   │
   ▼
Browser
   │
   ▼
SauceDemo
```

### Responsibilities

- **Tests** contain business logic and assertions.
- **Page Objects** contain page actions and locators.
- **BasePage** contains reusable Playwright methods shared across all pages.

---

## Test Coverage

### Login

- Valid login
- Invalid login
- Locked user validation

### Cart

- Add product to cart
- Remove product from cart
- Add multiple products
- Remove one product from cart
- Cart badge validation

### Checkout

- Empty first name validation
- Empty last name validation
- Empty postal code validation
- Cancel checkout flow

### Checkout Overview

- Product validation
- Product description validation
- Quantity validation
- Payment information validation
- Shipping information validation
- Total price validation
- Price calculation validation
- Cancel order flow
- Finish order flow

### Order Complete

- Success title validation
- Success message validation
- Back Home button validation
- Return to Inventory page validation

---

## Setup

### Clone Repository

```bash
git clone https://github.com/aagaathaa/saucedemo-playwright-tests.git

cd saucedemo-playwright-tests
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### macOS / Linux

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Playwright Browsers

```bash
playwright install
```

---

## Running Tests

### Run All Tests

```bash
pytest
```

### Run Specific Test Suites

```bash
pytest tests/login
pytest tests/cart
pytest tests/checkout
pytest tests/overview
pytest tests/order_complete
```

### Run Tests in Headed Mode

```bash
pytest --headed
```

### Run Tests in Headed Mode with Slow Motion

```bash
pytest --headed --slowmo 1000
```

---

## Docker

### Build Image

```bash
docker build -t saucedemo-tests .
```

### Run Tests

```bash
docker run saucedemo-tests
```

---

## CI/CD

The GitHub Actions workflow automatically:

- Sets up the Python environment
- Installs project dependencies
- Installs Playwright browsers
- Executes automated UI tests

---

## Design Pattern

This framework follows the **Page Object Model (POM)** design pattern.

- BasePage contains reusable Playwright methods.
- Each application page has its own Page Object.
- Tests contain only business logic and assertions.
- Fixtures prepare the application state before test execution.

---

## Author

**Agatha Abakumova**

QA Engineer

Python • Playwright • Pytest