# Homwwork_5_2
import pickle
import plotly.graph_objects as go
 


   
class Book:
    def __init__(self,title,author,publish_year,total_pages,Language,price,read_pages=None,left_pages=None,status=None,progress=None):
        self.title=title
        self.author=author
        self.publish_year=publish_year
        self.total_pages=total_pages
        self.Language=Language
        self.price=price
        self.read_pages=read_pages
        self.left_pages=left_pages
        self.status=status
        self.progress=progress


    def read(self):
        
        if self.read_pages is None:
            print(f'you have not red any pages from the "{self.title}" up to now\n')
        else:
            print(f'You have red {self.read_pages} from "{self.title}"')
            
        read_pages=int(input(f'if you want to change the number of read_pages please enter how many pages have you red from " {self.title}"? '))
        self.read_pages = read_pages
        if self.read_pages < self.total_pages:
            self.left_pages = self.total_pages - self.read_pages
            print(f'\n you have red {self.read_pages} pages from "{self.title}" and {self.left_pages} is left')
        else:
            self.left_pages=0
            print(f'\n it seems you have finished reading {self.title}, well done!')
        
        self.progress=round((self.read_pages*100)/self.total_pages)
        print(f'\n Your progress is {self.progress}%')
            
    def get_status(self):
        if self.read_pages==0:
            self.status='Unread'
            print(f' \n The status is {self.status}')
        elif self.left_pages==0:
            self.status='Finished'
            print(f'\n The status is {self.status}')
        else:
            self.status='Reading'
            print(f'\n The status is {self.status}')
            
            
    def __str__(self):
       return f'\n The "{self.title}" was written by "{self.author}" and published at {self.publish_year}'+\
               f' in {self.Language} , with {self.total_pages} pages and the price of {self.price}\n'
 
               
class Magazine(Book):

    def __init__(self,title,author,publish_year,total_pages,Language,price,issue,read_pages=None,left_pages=None,status=None,progress=None):
        super().__init__(title,author,publish_year,total_pages,Language,price,read_pages=None,left_pages=None,status=None,progress=None)
        self.issue=issue
       
        
    def __str__(self):
        return super().__str__() + f'and this is the issus of {self.issue}\n'
    


class Podcast:
    def __init__(self,title,speaker,publish_year,total_time,audio_language,price,listened_time=None,left_time=None,status=None,progress=None):
        self.title=title
        self.speaker=speaker
        self.publish_year=publish_year
        self.total_time=total_time
        self.audio_language=audio_language
        self.price=price
        self.listened_time=listened_time
        self.left_time=left_time
        self.status=status
        self.progress=progress
        
    
    def listen(self):
        if self.listened_time is None:
            print(f'\n you have not listened to the "{self.title}" up to now\n')
        else:
            print(f'\n You have listened {self.listened_time} minutes from "{self.title}"')
            
        listened_time=int(input(f'\n if you want to make chnges in listend_time please enter how many minutes have you listened to the "{self.title}" ? '))
        self.listened_time = listened_time
        if self.listened_time < self.total_time:
            self.left_time = self.total_time - self.listened_time
            print(f'\n you have listend {self.listened_time} minutes of "{self.title}" and {self.left_time} minutes are left')
        else:
            self.left_time=0
            print(f'\n it seems you have finished the "{self.title}", well done!')
            
        self.progress=round((self.listened_time*100)/self.total_time)
        print(f'\n Your progress is {self.progress}%')    

        
    def get_status(self):
        if self.listened_time==0:
            self.status='Unlistende'
            print(f'\n The status is {self.status}')
        elif self.left_time==0:
            self.status='Finished'
            print(f'\nThe status is {self.status}')
        else:
            self.status='Listening'
            print(f'\nThe status is {self.status}')
            
            
    def __str__(self):
       return f'\n The "{self.title}" is produced by "{self.speaker}" and published at {self.publish_year}'+\
               f' in {self.audio_language} , its duration is {self.total_time} minutes with the price of {self.price}\n'
        
        
class Audio_Book(Podcast,Book):
    
    def __init__(self, title, speaker, author,publish_year, total_time, audio_language, price,total_pages,Language,listened_time=None,left_time=None,progress=None):
        Podcast.__init__(self,title,speaker,publish_year,total_time,audio_language,price,listened_time=None,left_time=None,status=None,progress=None)
        Book.__init__(self,title,author,publish_year,total_pages,Language,price,read_pages=None,left_pages=None,status=None,progress=None)
  
      
    def __str__(self):
        return Podcast.__str__(self) + f' The original book language is {self.Language} and is written by {self.author}'
    
#########################################################################################################################

def get_data(string):
    string=string.lower()
    
    if string=='book':
        title=input('please enter the title of the book: ')
        author=input('please enter the author of the book: ')
        publish_year=input('please enter the publish_year of the book: ')
        total_pages=int(input('please enter the number of total_pages of the book: '))
        Language=input('please enter the Language of the book: ')
        price=float(input('please enter the Price of the book: '))
        item=Book(title,author,publish_year,total_pages,Language,price)
        print(item)
        item.read()
        item.get_status()
        
        
    elif string=='magazine':
        title=input('please enter the title of the magazine: ')
        author=input('please enter the Author of the magazine: ')
        publish_year=input('please enter the publish_year of the magazine: ')
        total_pages=int(input('please enter the number of total_pages of the magazine: '))
        Language=input('please enter the Language of the magazine: ')
        price=float(input('please enter the Price of the magazine: '))
        issue=int(input('please enter the issue of the magazine: '))
        item=Magazine(title,author,publish_year,total_pages,Language,price,issue)
        print(item)
        item.read()
        item.get_status()
        
        
    elif string=='podcast':
         title=input('Please enter the title of Podcast: ')
         speaker=input('Please enter the name of Speaker: ')
         publish_year=int(input('Please enter the published_year: '))
         total_time=int(input('Please enter the the total lenght of podcast: '))
         audio_language=input('Please enter the audio_language: ')
         price=int(input('please input the price of podcast: '))
         item=Podcast(title,speaker,publish_year,total_time,audio_language,price)
         print(item)
         item.listen()
         item.get_status()
         
                
    elif string=='audiobook':
        
        title=input('Please enter the title of AudioBook: ')
        speaker=input('Please enter the name of Speaker: ')
        publish_year=int(input('Please enter the published_year: '))
        total_time=int(input('Please enter the the total lenght of AudioBook: '))
        audio_language=input('Please enter the audio_language: ')
        price=int(input('please input the price of AudioBook: '))
        total_pages=input('please input the total_pages of written Book: ')
        Language=input('please input the original langauge of the written Book: ')
        author=input('Please enter the name of author: ')
        item=Audio_Book(title, speaker, author,publish_year, total_time, audio_language, price,total_pages,Language)
        print(item)
        item.listen()
        item.get_status()
        
    return item


            
        
#########################################################################################################################        
print('\n ______________________________ Hello Mina__________________________________\n');
print('________________________________Welcome Back__________________________________\n');
print('__________________________Please let me help you______________________________\n');
print('______________________ What do you wish to do today___________________________\n');


new_lib=[]
with open('library', "rb") as fp:# Unpickling
       library = pickle.load(fp) 
       input_item=100
       while input_item!=5:
           print('\n please select one of the item: \n');
           print('1. Add a Book/Magazine/Podcast/Audiobook to your library\n');
           print('2. Show my library\n');
           print('3. Change read_pages or listened_time\n');
           print('4. Sort my library\n');
           print('5. Exit\n');
           input_item=int(input('Enter Number, Please: '))
                             
           if input_item==1:
        
                get_class=input('Please enter which one do you want to enter: Book, Magazine, Podcast, audiobook: ') 
                item=get_data(get_class) 
                #pickle.dump(item, fp, pickle.HIGHEST_PROTOCOL)
                library.append(item) 
                new_lib.append(item)
       
           elif input_item==2:
               # making variable for creating table
               type_values=[item.__class__.__name__ for item in library]
               title_value=[item.title for item in library]
               progress_value=[item.progress for item in library]
               statu_value=[item.status for item in library]
               author_speaker_value=[item.author if 'read' in dir(item) else item.speaker for item in library]
        
               fig = go.Figure(data=[go.Table(header=dict(values=['Type', 'Title','Progress','Status','Speaker/Author']),
                     cells=dict(values=[type_values, title_value,progress_value,statu_value,author_speaker_value]))])
               fig.show()
                
                
       
           elif input_item==3:
                string=input('please enter thy title of the item you wish to change: ')
                for item in library:
                    if string.lower()==item.title.lower():
                        if item.__class__.__name__=='Book' or item.__class__.__name__=='Magazine':
                            item.read()
                        else:
                            item.listen()
        
        
           elif input_item==4:
               sorted_library=sorted(library,key=lambda x:x.__getattribute__('progress'))
            
        
   
with open('library', "wb") as fp:   #Pickling
  
      pickle.dump(library, fp)
       
        
        
        
        




        