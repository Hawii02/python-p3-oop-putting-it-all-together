#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
        self.current_page = 0
    
    @property
    def page_count(self):
        return self.set_page_count
    
    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
            return
        self.set_page_count = value

    def turn_page(self):
        if self.current_page < self.page_count:
            self.current_page += 1
            print("Flipping the page...wow, you read fast!")
        else:
            print("You've reached the end of the book.")
    

    # def set_title(self, title):
    #     if isinstance(title, str) and len(title)== 272:
    #         self._title = title()
    # def set_page_count(self, page_count):
    #     if 
 
    
       