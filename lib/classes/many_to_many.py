class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
    
    @property
    def title (self):
        return self._title
    
    @title.setter
    def title (self, title):
        # if isinstance(title, str):
        #     # raise ValueError(f"{title} is not a string")
        # elif not 5 < len(title) < 50:
        #     raise ValueError(f"{title} is not between 5 and 50 characters")
        # elif hasattr(self, '_title'):
        #     raise ValueError (f"{title} can't be changed")
        # else:
        #     self._title = title
        if isinstance(title, str) and 5 < len(title) < 50 and not hasattr(self, '_title'):
            self._title = title
    
    @property
    def author (self):
        return self._author
    
    @author.setter
    def author (self, author):
        if not isinstance(author, Author):
            raise ValueError(f"{author} is not an instance in Author class")
        else:
            self._author = author

    @property
    def magazine (self):
        return self._magazine
    
    @magazine.setter
    def magazine (self, magazine): 
        if not isinstance(magazine, Magazine):
            raise ValueError(f"{magazine} is not an instance of Magazine class")
        else:
            self._magazine = magazine
        
class Author:

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0 and not hasattr(self, '_name'):
            self._name = name

    def articles(self):
        articles_list = [article for article in Article.all if article.author == self]
        return articles_list
        

    def magazines(self):
        magazines_list = {article.magazine for article in Article.all if article.author == self and isinstance(article.magazine, Magazine)}
        return list(magazines_list)
    
    def add_article(self, magazine, title):
        if isinstance(magazine, Magazine):
        
            new_article = Article(self, magazine, title)

            return new_article

    def topic_areas(self):
        magazines_list = self.magazines()
        category_list = [magazine.category for magazine in magazines_list if isinstance(magazine, Magazine)]
        
        if len(category_list) == 0:
            return None
        
        return category_list

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name (self, name):
        if isinstance(name, str) and (2 <= len(name) <= 16):
            self._name = name
        
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category (self, category):
        if isinstance(category, str) and len(category) > 0 :
            self._category = category

    def articles(self):
        articles_list = [article for article in Article.all if article.magazine == self]
        return articles_list

    def contributors(self):
        contributors_list = {article.author for article in Article.all if article.magazine == self}
        return list(contributors_list)

    def article_titles(self):
        article_list = self.articles()
        title_list = [article.title for article in article_list]
        
        if len(title_list) == 0:
            return None
        
        return title_list

    def contributing_authors(self):
        contributor_count = {}
        
        for article in Article.all:
            if article.magazine == self:
                if article.author in contributor_count:
                    contributor_count[article.author] += 1
                else:
                    contributor_count[article.author] = 1

        contributing_authors = [author for author, count in contributor_count.items() if count > 2]
        
        if not contributing_authors:
            return None
        return contributing_authors
    
    @classmethod
    def top_publisher(cls):
        article_magazine_list = [article.magazine for article in Article.all if isinstance(article.magazine, cls)]

        if not article_magazine_list:
            return None
        
        magazine_count = {}

        for magazine in article_magazine_list:
            if magazine in magazine_count:
                magazine_count[magazine] += 1
            else:
                magazine_count[magazine] = 1
        
        max_magazine_count = max(magazine_count.items(), key=lambda item: item[1])

        return max_magazine_count[0]
        


