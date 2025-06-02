from django.db import models

class CarPart(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField()  # بدون upload_to
    image_url = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # احفظ أولاً عشان نحصل على رابط الصورة من Cloudinary
        super().save(*args, **kwargs)

        # نخزن الرابط النهائي (مثلاً https://res.cloudinary.com/...)
        if self.image and not self.image_url:
            self.image_url = self.image.url
            super().save(update_fields=["image_url"])

    def __str__(self):
        return self.name
