from django.db import models

from django.db import models

class SlangWord(models.Model):
    word = models.CharField(max_length=50)
    definition = models.TextField()
    image_url = models.URLField(help_text="Enter the URL of an image that represents this slang word")
    category = models.CharField(max_length=50, default='uncategorized')
    tags = models.CharField(max_length=255, blank=True, help_text="Comma-separated tags")  # NEW TAGS FIELD 🚀
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word

    class Meta:
        ordering = ['-created_at']
