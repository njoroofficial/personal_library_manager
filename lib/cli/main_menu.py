from lib.models.author import Author
from lib.models.book import Book
from rich.console import Console
from rich.table import Table

console = Console()

def start():
    console.print("\n[bold cyan]📚 Welcome to p.l.m.CLI: The Personal Library Manager 📚[/bold cyan]")
    
    while True:
        console.print("\n[bold yellow]--- MAIN MENU ---[/bold yellow]")
        print("1. Manage Authors ")
        print("2. Manage Books ")
        print("3. Exit ")
        
        choice = input("\nSelect an option: ").strip()
        
        if choice == '1':
            manage_authors()
        elif choice == '2':
            manage_books()
        elif choice == '3':
            console.print("[bold green]Goodbye! Happy Reading.[/bold green]")
            break
        else:
            console.print("[bold red]Invalid option. Please try again.[/bold red]")

# Functions To Display Tables

def display_table(objects, title, type="author"):
    """Renders a list of objects as a pretty table."""
    if not objects:
        console.print(f"[italic red]No {title.lower()} found.[/italic red]")
        return

    table = Table(title=f" {title}")

    if type == "author":
        table.add_column("ID", style="cyan", no_wrap=True)
        table.add_column("Name", style="magenta")
        
        for author in objects:
            table.add_row(str(author.id), author.name)
            
    elif type == "book":
        table.add_column("ID", style="cyan", no_wrap=True)
        table.add_column("Title", style="green")
        table.add_column("Year", style="yellow")
        table.add_column("Author", style="magenta")
        
        for book in objects:
            author_name = book.author.name if book.author else "Unknown"
            table.add_row(str(book.id), book.title, str(book.year), author_name)

    console.print(table)


# Author Menu

def manage_authors():
    while True:
        console.print("\n[bold magenta]--- ✍️ AUTHOR MANAGEMENT ---[/bold magenta]")
        print("1. Create New Author")
        print("2. View All Authors")
        print("3. Search Authors (Fuzzy) ") 
        print("4. Delete Author")
        print("5. View Author's Books")
        print("6. Back to Main Menu")

        choice = input("\nSelect an option: ").strip()

        if choice == '1':
            name = input("Enter Author Name: ")
            if Author.create(name):
                console.print(f"[green]Author '{name}' created successfully![/green]")
        
        elif choice == '2':
            authors = Author.get_all()
            display_table(authors, "All Authors", type="author")
        
        elif choice == '3':
            # SEARCH LOGIC 
            term = input("Enter search term (e.g., 'Rowling'): ")
            results = Author.find_by_name_partial(term)
            display_table(results, f"Search Results for '{term}'", type="author")

        elif choice == '4':
            id_input = input("Enter Author ID to delete: ")
            author = Author.find_by_id(id_input)
            if author:
                author.delete()
                console.print(f"[red]Author '{author.name}' deleted.[/red]")
            else:
                console.print("[red]Author not found.[/red]")

        elif choice == '5':
            id_input = input("Enter Author ID: ")
            author = Author.find_by_id(id_input)
            if author:
                # Reuse the book table logic for this specific author's books
                display_table(author.books, f"Books by {author.name}", type="book")
            else:
                console.print("[red]Author not found.[/red]")

        elif choice == '6':
            break
        else:
            console.print("[red]Invalid option.[/red]")

# Books Menu 

def manage_books():
    while True:
        console.print("\n[bold green]--- 📖 BOOK MANAGEMENT ---[/bold green]")
        print("1. Add New Book")
        print("2. View All Books")
        print("3. Search Books (Fuzzy) ") 
        print("4. Delete Book")
        print("5. Back to Main Menu")

        choice = input("\nSelect an option: ").strip()

        if choice == '1':
            title = input("Enter Book Title: ")
            year = input("Enter Publication Year: ")
            author_id = input("Enter Author ID: ")
            
            if Book.create(title, year, author_id):
                console.print("[green]Book added successfully![/green]")
            
        elif choice == '2':
            books = Book.get_all()
            display_table(books, "Library Collection", type="book") 

        elif choice == '3':
            # Search Logic
            term = input("Enter search term (e.g., 'Harry'): ")
            results = Book.find_by_title_partial(term)
            display_table(results, f"Search Results for '{term}'", type="book")

        elif choice == '4':
            id_input = input("Enter Book ID to delete: ")
            book = Book.find_by_id(id_input)
            if book:
                book.delete()
                console.print("[red]Book deleted.[/red]")
            else:
                console.print("[red]Book not found.[/red]")

        elif choice == '5':
            break
        else:
            console.print("[red]Invalid option.[/red]")