# 📚 P.L.M. CLI: The Personal Library Manager

> A robust Command Line Interface (CLI) application for managing personal book collections, built with Python, SQLAlchemy, and Rich.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy-red)
![Rich](https://img.shields.io/badge/CLI-Rich-purple)

---

## 📖 Overview

P.L.M.CLI is a Python-based tool that allows users to organize their reading library efficiently. It features an interactive menu system, beautiful terminal tables, and fuzzy search capabilities to help you track Authors and their associated Books.

---

## ✨ Features

| Feature                  | Description                                                          |
| ------------------------ | -------------------------------------------------------------------- |
| 📋 **Interactive Menus** | Navigate through organized menus to manage your library              |
| 👤 **Author Management** | Create, view, search, and delete authors                             |
| 📖 **Book Management**   | Add books with titles, publication years, and author links           |
| 🔗 **Relationships**     | One-to-many linking between Authors and Books                        |
| 🔍 **Fuzzy Search**      | Find records using partial keywords (e.g., "Harry" → "Harry Potter") |
| ✅ **Smart Validation**  | Prevents invalid data like future publication years or empty names   |
| 🎨 **Rich UI**           | Colorful, formatted tables in the terminal                           |

---

## 📂 Project Structure

```text
personal_library/
├── main.py                  # Entry point (Click CLI commands)
├── Pipfile                  # Dependency definitions
├── library.db               # SQLite database (created on first run)
├── lib/
│   ├── db/
│   │   └── connection.py    # Database engine, session & Base
│   ├── models/
│   │   ├── author.py        # Author model with validation
│   │   └── book.py          # Book model with Foreign Key
│   └── cli/
│       └── main_menu.py     # Interactive menu logic & Rich tables
└── README.md
```

---

## 🚀 Installation

### Prerequisites

- Python 3.10 or higher
- [Pipenv](https://pipenv.pypa.io/) for dependency management

### Setup Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/njoroofficial/personal_library_manager.git
   cd personal_library_manager
   ```

2. **Install dependencies**

   ```bash
   pipenv install
   ```

3. **Initialize the database**

   ```bash
   pipenv run python main.py initdb
   ```

   This creates the `library.db` SQLite database file.

4. **Run the application**
   ```bash
   pipenv run python main.py run
   ```

---

## 🎮 Usage Guide

### CLI Commands

| Command                            | Description                       |
| ---------------------------------- | --------------------------------- |
| `pipenv run python main.py initdb` | Initialize/reset the database     |
| `pipenv run python main.py run`    | Start the interactive application |

### Main Menu

When you run the application, you'll see:

```
📚 Welcome to P.L.M.CLI: The Personal Library Manager 📚

--- MAIN MENU ---
1. Manage Authors
2. Manage Books
3. Exit
```

---

### 👤 Author Management

Select option `1` from the main menu to access:

```
--- ✍️ AUTHOR MANAGEMENT ---
1. Create New Author
2. View All Authors
3. Search Authors (Fuzzy)
4. Delete Author
5. View Author's Books
6. Back to Main Menu
```

| Option                     | What it does                                                    |
| -------------------------- | --------------------------------------------------------------- |
| **1. Create New Author**   | Enter an author name to add to the database                     |
| **2. View All Authors**    | Display a table of all authors with their IDs                   |
| **3. Search Authors**      | Find authors by partial name (e.g., "Row" finds "J.K. Rowling") |
| **4. Delete Author**       | Remove an author by ID (also deletes all their books)           |
| **5. View Author's Books** | See all books written by a specific author                      |
| **6. Back**                | Return to main menu                                             |

#### Example: Adding an Author

```
Enter Author Name: J.K. Rowling
Author 'J.K. Rowling' created successfully!
```

---

### 📖 Book Management

Select option `2` from the main menu to access:

```
--- 📖 BOOK MANAGEMENT ---
1. Add New Book
2. View All Books
3. Search Books (Fuzzy)
4. Delete Book
5. Back to Main Menu
```

| Option                | What it does                                                      |
| --------------------- | ----------------------------------------------------------------- |
| **1. Add New Book**   | Enter title, publication year, and author ID                      |
| **2. View All Books** | Display a table of all books with author names                    |
| **3. Search Books**   | Find books by partial title (e.g., "Potter" finds "Harry Potter") |
| **4. Delete Book**    | Remove a book by ID                                               |
| **5. Back**           | Return to main menu                                               |

#### Example: Adding a Book

```
Enter Book Title: Harry Potter and the Sorcerer's Stone
Enter Publication Year: 1997
Enter Author ID: 1
Book added successfully!
```

> ⚠️ **Note**: You must create an author first before adding their books. Use the author's ID when adding a book.

---

### 📊 Sample Output

When viewing all books, you'll see a formatted table:

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃              Library Collection                  ┃
┣━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━┳━━━━━━┫
┃ ID ┃ Title                         ┃ Year ┃Author┃
┡━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━╇━━━━━━┩
│ 1  │ Harry Potter and the Sorcerer │ 1997 │ J.K. │
│    │ 's Stone                      │      │Rowli │
│ 2  │ 1984                          │ 1949 │George│
│    │                               │      │Orwell│
└────┴───────────────────────────────┴──────┴──────┘
```

---

## 🔧 Dependencies

| Package                                     | Purpose                       |
| ------------------------------------------- | ----------------------------- |
| [Click](https://click.palletsprojects.com/) | CLI command framework         |
| [SQLAlchemy](https://www.sqlalchemy.org/)   | ORM for database operations   |
| [Rich](https://rich.readthedocs.io/)        | Beautiful terminal formatting |

---

## 📝 Data Validation Rules

The application enforces these validation rules:

- **Author name**: Cannot be empty or whitespace-only
- **Book title**: Cannot be empty or whitespace-only
- **Publication year**: Must be a valid number and cannot be in the future

---

## 🗑️ Cascade Delete

When you delete an author, **all their books are automatically deleted** as well. This maintains database integrity.

---

## 💡 Tips

1. **Always create authors first** before adding books
2. **Use fuzzy search** to quickly find records without typing exact names
3. **Note the IDs** displayed in tables - you'll need them for delete operations
4. **Database persists** between sessions in `library.db`
