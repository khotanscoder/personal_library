
class Library():

    def __init__(self):
        self.books = []
        self.magazines = []
        self.podcatEpisodes = []
        self.audioBooks = []
        
    def add_book(self, book_object):
        self.books.append(book_object)

        with open("books.txt", "a") as file:
            file.write(f'{book_object.title:10} {book_object.title:10} {book_object.publish_year:10} {book_object.pages:10}\n')

    def add_magazine(self, magazine_object):
        self.magazines.append(magazine_object)

        with open("magazines.txt", "a") as file:
            file.write(f'{magazine_object.title:10} {magazine_object.title:10} {magazine_object.publish_year:10} {magazine_object.pages:10}\n')


    def add_podcast(self, podcast_object):
        self.podcatEpisodes.append(podcast_object)

        with open("podcasts.txt", "a") as file:
            file.write(f'{podcast_object.title:10} {podcast_object.title:10} {podcast_object.publish_year:10} {podcast_object.pages:10}\n')


    def add_audioBook(self, audioBook_object):
        self.audioBooks.append(audioBook_object)

        with open("audioBooks.txt", "a") as file:
            file.write(f'{audioBook_object.title:10} {audioBook_object.title:10} {audioBook_object.publish_year:10} {audioBook_object.pages:10}\n')


    def printBooks(self):
        with open('books.txt', 'r') as books:
            books = books.readlines()
            print(f'Title  Author  Pages')
            for index, b in enumerate(books):
                print(f'{index: <5}: {b}')

    def printMagazins(self):
        i = 0
        for Magazine in self.magazines:
            i += 1
            print('{i} : ',  self.magazines[i-1] )

    def check_capacity(self):
        return f'The number of books in this repo is {len(self.books)} and The number of magazines in this repo is {len(self.magazines)} and The number of podcastEpisodes in this repo is {len(self.podcatEpisodes)} and The number of audioBooks in this repo is {len(self.audioBooks)}'
    
    def __str__(self):
        return f'This library has {len(self.books)} books, {len(self.magazines)} magazines, {len(self.podcatEpisodes)} episodes and {len(self.audioBooks)} audioBooks. '



class Book():
    def __init__(self, title=None, author=None, publish_year=None, price=None, pages=None, language=None):
        self.title = title
        self.author = author
        self.publish_year = publish_year
        self.pages = pages
        self.language = language
        self.price = price
        self.read_pages = 0

    def get_data(self, bookshelf):
        # while True:
        self.title = input('Enter title of book : ')
        self.author = input('Enter author of book : ')
        self.publish_year = input('Enter publish_year of book : ')
        self.pages = int(input('Enter number of pages of book : '))
        self.price = input("Enter book's price in $ : ")
        bookshelf.add_book(book)

    def read_book(self, page):
        if page > self.read_pages:
            self.read_pages = page
            last_page = page + self.read_pages
            # return f'There are {last_page} pages left'
            print(last_page, 'pages left!')
            if last_page == self.pages:
                print('you can not read more than pages!')

    def get_status(self, page):
        if self.read_pages == 0:
            print("unread")
        elif self.read_pages - self.pages > 0:
            print("reading")
        elif self.read_pages == self.pages:
            print("finished")
            
    def __str__(self):
        return f"title : {self.title}, author:{self.author}, This book with {self.pages}pages published in {self.publish_year} in {self.language} language and it's price is {self.price}$ !"



class Magazine(Book):
    def __init__(self, title=None, author=None, publish_year=None, price=None, pages=None, language=None, issue=None):
        super.__init__(self, title, author, publish_year, pages, language, price)
        self.issue = issue

    def get_data(self, bookshelf):
        while True:
            self.title = input('Enter title of magazine : ')
            self.author = input('Enter author of magazine : ')
            self.publish_year = input('Enter publish_year of magazine : ')
            self.pages = int(input('Enter number of pages of magazine : '))
            self.price = input("Enter magazine's price in $ : ")
            self.issue = input('Enter the issue of magazine : ')

            bookshelf.add_magazine(magazine)

    def read_magazine(self, page):
        if page > self.read_pages:
            self.read_pages = page
            last_page = page + self.read_pages
            # return f'There are {last_page} pages left'
            print(last_page, 'pages left!')
            if last_page == self.pages:
                print('you can not read more than pages!')

    def get_status(self, page):
        if self.read_pages == 0:
            print("unread")
        elif self.read_pages - self.pages > 0:
            print("reading")
        elif self.read_pages == self.pages:
            print("finished")
            
    def __str__(self):
        return f"title : {self.title}, author:{self.author}, This book with {self.pages}pages published in {self.publish_year} in {self.language} language and it's price is {self.price}$ !"

    
    
class PodcastEpisode(Book):
    def __init__(self, title=None, publish_year=None, language=None, price=None, speaker=None, time=None):
        super.__init__(self, title, publish_year, language, price)
        self.speaker = speaker
        self.time = time
        self.listening_time = 0

    def get_data(self, bookshelf):
        while True:
            self.title = input('Enter title of podcast : ')
            self.publish_year = input('Enter publish_year of podcast : ')
            self.pages = input('Enter number of pages of podcast : ')
            self.price = input("Enter podcast's price in $ : ")
            self.time = input('Enter the time of podcast in minute : ')

            bookshelf.add_podcast(bookshelf)

    def listened(self, time):
        if time > self.listening_time:
            self.listening_time = time
            last_time = time + self.listening_time
            print(last_time, 'minutes left!')
            if last_time == self.time:
                print("you can not listen more than podcast's time!")

    def get_status(self, time):
        if self.listening_time == 0:
            print("unlistened")
        elif self.listening_time - self.time > 0:
            print("listening")
        elif self.listening_time == self.time:
            print("finished")

    def __str__(self):
        return f"title: {self.title}, author:{self.author}, This podcast episode with {self.time} minutes published in {self.publish_year} in {self.language} language and it's price is {self.price}$"

        

class AudioBook(Magazine,PodcastEpisode):
    def __init__(self, title=None, speaker=None, author=None, publish_year=None, pages=None, book_language=None, audio_language=None, price=None, time=None):
        super.__init__(self, title, author, publish_year, pages, price)
        super.__init__(self, speaker, time)
        self.book_language = book_language
        self.audio_language = audio_language

    
    def get_data(self, bookshelf):
        while True:
            self.title = input('Enter title of audioBook : ')
            self.speaker = input("Enter speaker's name of audioBook : ")
            self.author = input('Enter author of audioBook : ')
            self.publish_year = input('Enter publish_year of audioBook : ')
            self.pages = input('Enter number of pages of audioBook : ')
            self.pages = input('Enter number of pages of audioBook : ')
            self.book_language = input('Enter book_language of audioBook : ')
            self.audio_language = input('Enter audio_language of audioBook : ')
            self.price = input("Enter audioBook's price in $ : ")
            self.time = input('Enter the time of audioBook in minute : ')

            bookshelf.add_audioBook(bookshelf)

    def listened(self, time):
        if time > self.listening_time:
            self.listening_time = time
            last_time = time + self.listening_time
            print(last_time, 'minutes left!')
            if last_time == self.time:
                print("you can not listen more than podcast's time!")

    def get_status(self, time):
        if self.listening_time == 0:
            print("unlistened")
        elif self.listening_time - self.time > 0:
            print("listening")
        elif self.listening_time == self.time:
            print("finished")


    def __str__(self):
        return f"title: {self.title}, author:{self.author}, This audio book  with {self.time} minutes published in {self.publish_year} with {self.book_language} book language and {self.audio_language} audio language and it's price is {self.price}$"




print('---------------------------------hello guys!--------------------------------')
print('what do you do?')
print('1_ Add a Book/Magazine/PodcastEpisod/Audiobook')
print('2_ Show my bookshelf')
print('3_ Add read page or time listen')
print('4_ Sort my bookshelf')

choosen = int(input('Please select an item above : '))
bookshelf = Library()

while True:

    if choosen == 1:
        choice = input('choose Book/Magazine/Podcast or Audiobook : ')
        if choice == 'Book':
            book = Book()
            book.get_data(bookshelf)

            exit_or_not = input('Enter x to exit or enter to continue: ')
            if exit_or_not == 'x': break            

        elif choice == 'Magazine':
            magazine = Magazine()
            magazine.get_data(bookshelf)
        
        elif choice == 'PadcastEpisode':
            podcast = PodcastEpisode()
            podcast.get_data(bookshelf)

        elif choice == 'Audiobook':
            audioBok = AudioBook()
            audioBok.get_data(bookshelf)

    elif choosen == 2:
        bookshelf.printBooks()
        break

    elif choosen == 3:
        choice = input('choose Book/Magazine/Podcast or Audiobook : ')
        if choice == 'Book':
            book = book()
            book.read_book()

        elif choice == 'Magazine':
            magazine = Magazine()
            magazine.read_magazine(int(input('Enter number of pages you read !')))

        elif choice == 'Podcast':
            podcast = PodcastEpisode()
            podcast.listened(int(input('Enter the time of podcastEpisod you listen !')))

        if choice == 'Audiobook':
            audiobook = AudioBook()
            audiobook.listened(int(input('Enter time of audio-book you read !')))


    
# book1 = Book('No Friend But the Mountains', 'Behrouz Boochani', 2018, 10, 374, 'english')
# print(book1)

# print(book_shelf.check_capacity())
        