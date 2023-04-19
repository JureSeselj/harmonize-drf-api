from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    A class for the post model
    """
    category_choices = [
        ('Quotes', 'Quotes'),
        ('Animals', 'Animals'),
        ('Lifestyle', 'Lifestyle'),
        ('Fun Fact', 'Fun Fact'),
        ('Creative', 'Creative'),
        ('Nature', 'Nature'),
        ('Arts & Entertainmen', 'Arts & Entertainmen'),
        ('Books', 'Books'),
        ('Design & Fashion', 'Design & Fashion'),
        ('Education', 'Education'),
        ('Food & Beverage', 'Food & Beverage'),
        ('Health/Beauty', 'Health/Beauty'),
        ('Sport', 'Sport'),
        ('Clothing (Brand)', 'Clothing (Brand)'),
        ('Automotive', 'Automotive'),
        ('Games/Toys', 'Games/Toys'),
        ('Musician/Band', 'Musician/Band'),
        ('Movie', 'Movie'),
        ('Other', 'Other')
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=category_choices)
    image = models.ImageField(
        upload_to='images/',
        default='../default_post_aiks6l',
        blank=True
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.id} {self.title}'
