class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        type(self).all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and 5 <= len(title) <= 50 and not hasattr(self, "_title"):
            self._title = title
        else:
            raise ValueError('Title must be a string with characters in between 5 and 50 and CANNOT change after instantiation')
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise TypeError('Author is not instance of Author class')
        
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise TypeError('Magazine is not instance of Magazine class')
        
class Author:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0 and not hasattr(self, "_name"):
            self._name = name
        else:
            raise ValueError('Name must be a string and with at least 1 char and CANNOT change after instantiation')

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return (list(
            {
                article.magazine.category
                for article in self.articles()
                if article.author == self
            }
        ) if self.magazines() else None)

class Magazine:
    all = []
    def __init__(self, name, category):
        self.name = name
        self.category = category
        type(self).all.append(self)
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise ValueError('Name must be a string and with at least 1 char.')
    
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError('Category must be a string and with at least 1 char.')

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        return ([article.title for article in self.articles()] if self.articles() else None)

    def contributing_authors(self):
        ## Method 1
        # list_of_authors = [article.author for article in self.articles()]
        # if authors := list({author for author in list_of_authors if list_of_authors.count(author) > 2}):
        #     return authors
        # else:
        #     None

        ## Method 2
        authors_count = {}
        
        for article in self.articles():
            if article.author in authors_count:
                authors_count[article.author] += 1
            else:
                authors_count[article.author] = 1

        if contributing_authors := [
            author for author, count in authors_count.items() if count > 2
        ]:
            return contributing_authors
        else:
            None

    @classmethod
    def top_publisher(cls):
        return max(cls.all, key=lambda magazine: len(magazine.articles())) if Article.all else None
