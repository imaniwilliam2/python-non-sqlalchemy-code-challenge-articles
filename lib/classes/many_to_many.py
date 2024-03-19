class Article:
     
    all = []


    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter 
    def title(self, title_parameter):
        if(not hasattr(self, 'title')) and (isinstance(title_parameter, str)) and (5 <= len(title_parameter) <= 50):
            self._title = title_parameter

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author_parameter):
        if(isinstance(author_parameter, Author)):
            self._author = author_parameter

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine_parameter):
        if(isinstance(magazine_parameter, Magazine)):
            self._magazine = magazine_parameter








class Author:
    def __init__(self, name):
        self.name = name


    @property 
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name_parameter):
        if(not hasattr(self, 'name')) and (isinstance(name_parameter, str)) and (len(name_parameter) > 0):
            self._name = name_parameter
    
    
    def articles(self):
        return [article for article in Article.all if article.author is self and (isinstance(article, Article))]

    def magazines(self):
        return list(set([article.magazine for article in self.articles() if isinstance(article.magazine, Magazine)]))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if any(self in magazine.contributors() for magazine in Magazine.all):
            return list(set([magazine.category for magazine in Magazine.all if self in magazine.contributors()]))
        else:
            None











class Magazine:

    all = []
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)
 

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name_parameter):
        if(isinstance(name_parameter, str)) and (2 <= len(name_parameter) <= 16):
            self._name = name_parameter

    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category_parameter):
        if(isinstance(category_parameter, str)) and (len(category_parameter) > 0):
            self._category = category_parameter
    

    def articles(self):
        return [article for article in Article.all if article.magazine is self and (isinstance(article, Article))]

    def contributors(self):
        return list(set([article.author for article in Article.all if article.magazine is self and (isinstance(article.author, Author))]))

    def article_titles(self):
        if any(article.magazine is self for article in Article.all):
            return [article.title for article in Article.all if article.magazine is self]
        else:
            return None

    def contributing_authors(self):
        list_more_than_two = [author for author in self.contributors() if len([article for article in self.articles() if article.author == author]) > 2]
        if(len(list_more_than_two) == 0):
            return None
        else:
            return list_more_than_two
        

    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        
        max_articles = None
        max_article_count = 0

        for magazine in cls.all:
            article_count = len(magazine.articles())
            if article_count > max_article_count:
                max_article_count = article_count
                max_articles = magazine
        return max_articles