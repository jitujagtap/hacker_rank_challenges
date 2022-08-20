from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author
    @abstractmethod
    def display(): pass
#Write MyBook class
class Mybook(Book):
    def __init__(self,title,author,price):
        self.price = price

    def display(self):
        print("Title:", title)
        print("Author:", author)
        print("Price:",price)
title=input('The Alchemist')
author=input('Paulo Coelho')
price=int(input(248))
new_novel=MyBook(title,author,price)
new_novel.display()