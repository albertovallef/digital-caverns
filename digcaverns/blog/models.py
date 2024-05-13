from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
import markdown


class User(models.Model):
    """
    Model use to describe `members` or `authors`
    Notes: 
        - Currently there will be only one user (the author)
    """
    email = models.EmailField(unique=False, blank=False, 
                              null=False)
    first_name = models.CharField(max_length=30, blank=False, 
                                  null=False)
    last_name = models.CharField(max_length=30, blank=False, 
                                 null=False)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class ArticleManger(models.Manager):
    def published(self):
        ...


class Article(models.Model):
    """
    Model to create articles
    """
    title = models.CharField(max_length=100, blank=False,
                             null=False)
    content = models.TextField(default="", blank=True, 
                               null=False)  # Store markdown text
    about = models.TextField(max_length=280, default="", 
                             blank=True, null=False)  # Forces about to be concise! 
    image = models.ImageField(upload_to='articles_imgs/', 
                              null=True, blank=True)
    author = models.ForeignKey(to=User,
                               on_delete=models.SET_DEFAULT, 
                               related_name='article',
                               default="Anonymous")
    publish_date = models.DateField()
    update_date = models.DateField(auto_now=True,  # Auto change date on save
                                   editable=False)

    class Status(models.TextChoices):
        DRAFT = "DFT", _("Draft"),
        READY = "RDY", _("Ready"),
        PUBLISH = "PUB", _("Published"),
        UNPUBLISH = "UPUB", _("Unpublished")

    status = models.CharField(max_length=5, 
                              choices=Status.choices, 
                              default=Status.DRAFT)
    views = models.PositiveIntegerField()

    objects = ArticleManger()


    def __str__(self) -> str:
        return self.title

    def increment_views(self):
        """Increments view count of the given article"""
        self.views += 1
        self.save(update_fields=['views'])

    def get_markdown(self):
        """Converts markdown text to HTML"""
        return mark_safe(markdown.markdown(self.content, 
                                           extensions=['codehilite', 'fenced_code']))
        

