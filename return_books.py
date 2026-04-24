from utils import books, issue_books
from datetime import datetime

def return_book():
    if len(issue_books) == 0:
        print("No issued books")
    else:
        book_name = input("Enter book to return: ").strip().upper()
        
        if book_name in issue_books:
            data = issue_books[book_name]
            issue_date = data["date"]
            allowed_days = data["days"]
            
            return_date = datetime.now()
            used_days = (return_date - issue_date).days
            
            fine = 0
            if used_days > allowed_days:
                extra_days = used_days - allowed_days
                
                for i in range(1, extra_days + 1):
                    fine += 10 * i
            
            del issue_books[book_name]
            books[book_name] = True
            
            print(f"Book - {book_name} returned successfully.")
            print(f"Used Days: {used_days}")
            
            if fine > 0:
                print(f"Late return! Fine = Rs.{fine}")
            else:
                print("Returned on time. No fine.")
        else:
            print("No such issued book found")
            