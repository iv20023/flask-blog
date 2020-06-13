from database import Database
from models.blog import Blog


class Menu(object):
    def __init__(self):
        # ask for author name
        self.user=input("Enter your author name: ")
        self.user_blog = None

        # check if user has an account
        if self._user_has_account():
            print("Welcome back {}".format(self.user))
        else:
            self._prompt_user_for_account() # if not, prompt to create account

    def _user_has_account(self):
        blog =  Database.find_one(collection='blogs', query={"author": self.user})
        if blog is not None:
            self.user_blog=Blog.from_mongo(blog['id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        print("Since you are the new user, please fill in some data!\n")
        title=input("Enter the blog title: ")
        description=input("Enter blog description: ")

        blog=Blog(author=self.user,title=title,description=description)
        blog.save_to_mongo()
        self.user_blog=blog

    def run_menu(self):

        # read blog or write blog
        read_or_write = input("Do you want to read (R) or write (W) the blogs?")
        # if read:
        if read_or_write=='R':
            self._list_blogs()
            self._view_blog()
        elif read_or_write=='W':
            self.user_blog.new_post()

        else:
            print("Thank you for blogging!")
        #   list blogs in database
        #   allow user to pick one
        #   display posts
        # if write:
        #   prompt to write a post

    def _list_blogs(self): # find all blogs in database
        blogs = Database.find(collection='blogs', query={})
        for blog in blogs:
            print("ID: {}, Title: {}, Author: {}, Description: {}".format(blog['id'], blog['title'], blog['author'], blog['description']))

    def _view_blog(self):
        blog_to_see=input("Enter the blog ID that you would like to see: ")
        blog=Blog.from_mongo(blog_to_see)
        #list the posts from that blog
        posts=blog.get_posts()
        for post in posts:
            print("Date: {}, Title: {}\n\n {}".format(post['created_date'],post['title'], post['content']))