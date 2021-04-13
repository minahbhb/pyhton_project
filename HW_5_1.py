# Homwwork_5_1
class Book:
    def __init__(self,title,author,publish_year,total_pages,Language,price,read_pages=None,left_pages=None):
        self.title=title
        self.author=author
        self.publish_year=publish_year
        self.total_pages=total_pages
        self.Language=Language
        self.price=price
        self.read_pages=read_pages
        self.left_pages=left_pages

    def read(self):
        read_pages=int(input('please enter how many pages have you red? '))
        self.read_pages=read_pages
        if self.read_pages< self.total_pages:
            self.left_pages=self.total_pages-self.read_pages
            print(f'you have red {self.read_pages} pages and {self.left_pages} is left')
        else:
            self.left_pages=0
            print(f'it seems you have finished the "{self.title}", well done!')
            
    def get_status(self):
        if self.read_pages==0:
            print(' The book status is unread')
        elif self.left_pages==0:
            print('The book status is finished')
        else:
            print('The book status is reading')
            
            
    def __str__(self):
       return f'The "{self.title}" book was written by "{self.author}" and published at {self.publish_year}'+\
               f' in {self.Language} , with {self.total_pages} pages and the price of {self.price}\n'
               

def get_data():
    title=input('please enter the Title of the book: ')
    author=input('please enter the Author of the book: ')
    publish_year=input('please enter the publish_year of the book: ')
    total_pages=int(input('please enter the number of total_pages of the book: '))
    Language=input('please enter the Language of the book: ')
    price=float(input('please enter the Price of the book: '))
    return [title,author,publish_year,total_pages,Language,price]
    

##################################################
number_of_books=int(input('Please enter how many numbers of books do you want to register for the library: \n'))
Book_list = []
for i in range(1,(number_of_books+1)):
        book_dict={}
        print(f'\n Lets input the information of the {i} book:\n')
        book_info=get_data()
        book_dict['book_'+str(i)]=Book(book_info[0],book_info[1],book_info[2],book_info[3],book_info[4],book_info[5])
        book_dict['book_'+str(i)].read()
        book_dict['book_'+str(i)].get_status()
        print(book_dict['book_'+str(i)])
        Book_list.append(book_dict)



        
