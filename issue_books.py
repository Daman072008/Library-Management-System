from utils import books, issue_books
from datetime import datetime

def issue_book():
    if len(books) == 0:
        print("No book available")
    else:
        book_name = input("Enter book to be issued: ").strip().upper()
        
        if book_name in books:
            student = input("Enter student name: ").strip().title()
            days = int(input("Enter number of days for issue: "))
            
            issue_books[book_name] = {
                "student": student,
                "date": datetime.now(),
                "days": days
            }
            
            del books[book_name]
            
            print(f"Book - {book_name} issued successfully to {student}.")
            print("Note: Fine will be charged after due date.")
        else:
            print("No such book available")