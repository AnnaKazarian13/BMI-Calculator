# BMI Calculator / Калькулятор ИМТ

**Language:** [English](#english) | [Русский](#русский)

Desktop GUI application for Body Mass Index (BMI) calculation with WHO-based categories and risk screening text.

**Stack:** Python 3.10+, CustomTkinter

---

## English

### Features

* Light / dark theme support
* Full bilingual UI (**RU / EN**) with one-click language switch
* WHO BMI categories and associated risk notes
* Input validation: accepts `,` and `.`, converts height from cm to m when needed

### Install and run

```bash
git clone https://github.com/AnnaKazarian13/BMI-Calculator.git
cd BMI-Calculator
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

macOS / Linux:

```bash
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

### Repository structure

```
BMI-Calculator/
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## Русский

### Возможности

* Светлая / тёмная тема
* Полный двуязычный интерфейс (**RU / EN**) без перезапуска
* Категории ИМТ по критериям ВОЗ и связанные риски
* Защита ввода: точка и запятая, автоматический перевод роста из см в метры

### Установка и запуск

```bash
git clone https://github.com/AnnaKazarian13/BMI-Calculator.git
cd BMI-Calculator
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

macOS / Linux:

```bash
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

### Структура репозитория

```
BMI-Calculator/
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## Author / Автор

[AnnaKazarian13](https://github.com/AnnaKazarian13)
