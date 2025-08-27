# Cucumber QA Demo

This repository demonstrates a **BDD (Behavior-Driven Development)** style automation project using **Behave (Cucumber for Python)** and **Selenium WebDriver**.  
It is part of my QA portfolio, showcasing how I design and run end-to-end automated tests with clear, human-readable scenarios.

---

## Features Covered
- **Login functionality**  
  - Successful login with valid credentials  
  - Error message on invalid credentials  
  - Error message on empty credentials  

- **Shopping cart functionality**  
  - Add single item to cart  
  - Add multiple items to cart  
  - Remove items from cart  

All tests are written in **Gherkin** syntax for readability and collaboration between QA, developers, and stakeholders.

---

## Project Structure
cucumber-qa-demo/
├─ features/
│ ├─ login.feature
│ └─ add_to_cart.feature
├─ step_definitions/
│ ├─ login_steps.py
│ └─ cart_steps.py
├─ support/
│ └─ environment.py
├─ requirements.txt
├─ README.md
└─ .github/workflows/cucumber-tests.yml (optional CI workflow)
