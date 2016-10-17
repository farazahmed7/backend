from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from accounts import views
from accounts.models import Post



class RssFeed(Feed):
    title=""
    link="/feed/"
    description="nothing"

    def items(self):
        return Post.objects.all()[:5]
    def item_title(self, item):
        return self.title
    def item_description(self, item):
        return self.description
    def item_link(self, item):
        return reverse(views.Post,)