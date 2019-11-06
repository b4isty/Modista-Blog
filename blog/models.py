from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Post(models.Model):
    """Post model"""
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, db_index=True, blank=False, null=False)
    content = models.TextField(db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Pagination is intended to work for ordered queryset
        so here ordering it by default to avoid using order_by method everywhere
        """
        ordering = ('-created_at',)

    def __str__(self):
        return self.title



