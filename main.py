
class Library:
    def __init__(self, listofBooks):
        self.books = listofBooks

    def displayAvailableBooks(self):
        print(f"\n{len(self.books)} Available Books Are Given Below : ")
        for book in self.books:

            print(" * " + book)
        print("\n")

    def borrowBook(self, name, bookname):
        if bookname not in self.books:
            print(
                f"{bookname} Book Is Not Available Either Taken By Someone Else, Wait Until He Returned.\n")
        else:
            track.append({name: bookname})
            print("Book Issued : Thank You! Keep It With Care And Return On Time.\n")
            self.books.remove(bookname)

    def returnBook(self, bookname):
        print("Book Returned : Thank You! \n")
        self.books.append(bookname)

    def donateBook(self, bookname):
        print("Book Donated : Thank You So Much, Have A Good Day!.\n")
        self.books.append(bookname)


class Student():
    def requestBook(self):
        print("So, you want to borrow book!")
        self.book = input("Enter name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        print("So, you want to return book!")
        name = input("Enter your name: ")
        self.book = input("Enter name of the book you want to return: ")
        if {name: self.book} in track:
            track.remove({name: self.book})
        return self.book

    def donateBook(self):
        print("Okay! you want to donate book!")
        self.book = input("Enter name of the book you want to donate: ")
        return self.book


if __name__ == "__main__":

    library = Library(
        ["Tech yourself C", "Hand Book of Java", "Python for kids", "Linux Sell", "Hands on Machine Learning", "Deep Learning Book"])
    student = Student()
    track = []

    print("\t\t\t\t\t**** Book's Paradise Online Library ****\n")
    print("""Please select What you want to do? \n
        1. Show all available books
        2. Borrow books
        3. Return books
        4. Donate books
        5. Track books
        6. Exit\n""")

    while (True):

        try:
            usr_response = int(input("Enter your choice: "))

            if usr_response == 1:  # listing
                library.displayAvailableBooks()
            elif usr_response == 2:
                library.borrowBook(
                    input("Enter your name: "), student.requestBook())
            elif usr_response == 3:  # return
                library.returnBook(student.returnBook())
            elif usr_response == 4:  # donate
                library.donateBook(student.donateBook())
            elif usr_response == 5:  # track
                for i in track:
                    for key, value in i.items():
                        holder = key
                        book = value
                        print(f"{book} book is taken/issued by {holder}.")
                print("\n")
                if len(track) == 0:
                    print("No books are issued yet! \n")

            elif usr_response == 6:
                print("Thanks a lot for taking our service. \n")
                exit()
            else:
                print("Invalid input here! \n")
        except Exception as e:
            print(f"{e}---> Invalid input here! \n")