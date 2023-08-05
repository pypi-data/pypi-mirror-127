bloggy
======

bloggy is A Django blog app with features of a standard blogging platform, Comment system and tagging functionality, System to share your site's content by email and a custom sitemap and feed for blog posts.

Detailed documentation is in the docs directory.

Quick start
===========

1.  Add bloggy to your INSTALLED\_APPS setting like this:

        INSTALLED_APPS = [
            ...
            'blog',
        ]

2.  Include the blog URLconf in your project urls.py like this:

        path('blog/', include('blog.urls')),
        

3.  Run python manage.py migrate to create the polls models.

4.  Start the development server and visit <http://127.0.0.1:8000/admin/> to create a blog (you'll need the Admin app enabled).

5.  Visit <http://127.0.0.1:8000/blog/> to participate in the poll.

