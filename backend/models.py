from django.db import models

# Feedback models .

class FeedbackCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    category = models.ForeignKey(FeedbackCategory, on_delete=models.CASCADE)
    message = models.TextField()
    attachment = models.FileField(upload_to='feedback_attchments/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f"Anonymous Feedback - {self.timestamp}"