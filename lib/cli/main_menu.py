from lib.models.author import Author
from lib.models.book import Book

def start():
    print("\n Welcome to BiblioCLI: The Personal Library Manager ")
    
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Manage Authors ")
        print("2. Manage Books ")
        print("3. Exit ")
        
        choice = input("\nSelect an option: ").strip()
        
        if choice == '1':
            manage_authors()
        elif choice == '2':
            manage_books()
        elif choice == '3':
            print("Goodbye! Happy Reading.")
            break
        else:
            print("Invalid option. Please try again.")

# AUTHOR MENU 

def manage_authors():
    while True:
        print("\n--- ✍️ AUTHOR MANAGEMENT ---")
        print("1. Create New Author")
        print("2. View All Authors")
        print("3. Find Author by ID")
        print("4. Delete Author")
        print("5. View Author's Books (Relationship)")
        print("6. Back to Main Menu")

        choice = input("\nSelect an option: ").strip()

        if choice == '1':
            name = input("Enter Author Name: ")
            Author.create(name)
            print("Author created successfully!")
        
        elif choice == '2':
            authors = Author.get_all()
            print("\nList of Authors:")
            for author in authors:
                print(f"{author.id}: {author.name}")
        
        elif choice == '3':
            id_input = input("Enter Author ID: ")
            author = Author.find_by_id(id_input)
            print(author if author else "Author not found.")

        elif choice == '4':
            id_input = input("Enter Author ID to delete: ")
            author = Author.find_by_id(id_input)
            if author:
                author.delete()
                print("Author deleted.")
            else:
                print("Author not found.")

        elif choice == '5':
            # One-to-Many Relationship
            id_input = input("Enter Author ID: ")
            author = Author.find_by_id(id_input)
            if author:
                print(f"\nBooks by {author.name}:")
                if author.books:
                    for book in author.books:
                        print(f" - {book.title} ({book.year})")
                else:
                    print("No books found for this author.")
            else:
                print("Author not found.")

        elif choice == '6':
            break
        else:
            print("Invalid option.")

# BOOK MENU

def manage_books():
    while True:
        print("\n--- 📖 BOOK MANAGEMENT ---")
        print("1. Add New Book")
        print("2. View All Books")
        print("3. Delete Book")
        print("4. Back to Main Menu")

        choice = input("\nSelect an option: ").strip()

        if choice == '1':
            # We need an author to create a book
            title = input("Enter Book Title: ")
            year = input("Enter Publication Year: ")
            author_id = input("Enter Author ID: ")
            
            # Validation 
            Book.create(title, year, author_id)
            
            
        elif choice == '2':
            books = Book.get_all()
            print("\nLibrary Collection:")
            for book in books:
                # We can access book.author.name through the relationship
                author_name = book.author.name if book.author else "Unknown"
                print(f"{book.id}: {book.title} ({book.year}) by {author_name}")

        elif choice == '3':
            id_input = input("Enter Book ID to delete: ")
            book = Book.find_by_id(id_input)
            if book:
                book.delete()
                print("Book deleted.")
            else:
                print("Book not found.")

        elif choice == '4':
            break
        else:
            print("Invalid option.")