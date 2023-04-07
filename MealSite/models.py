from django.db import models
from .consts import MAX_RATE


RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE + 1)]


class Tag(models.Model):
    name = models.CharField('Tag', max_length=50)

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField("Meal", max_length=120)
    imageUrl = models.CharField("URL", max_length=200)
    countryOfOrigin = models.CharField("Country", max_length=120)
    tag = models.ManyToManyField(Tag, verbose_name='Tag')
    description = models.TextField("Description")
    dateAdded = models.DateTimeField("create", auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def getAvgRating(self):
        mealName = self.name
        votes = MealRating.objects.filter(meal__name=mealName)

        sumRating = 0
        for vote in votes:
            sumRating += vote.rating

        if self.NumberOfVotes():
            avgRating = sumRating / self.NumberOfVotes()
        else:
            avgRating = 0
        return avgRating

    def NumberOfVotes(self):
        mealName = self.name
        count = MealRating.objects.filter(meal__name=mealName).count()
        return count

    class Meta:
        verbose_name = "Meal"
        verbose_name_plural = "Meals"


class MealRating(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATE_CHOICES)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    dateOfRating = models.DateTimeField("Create", auto_now_add=True)

    class Meta:
        verbose_name = 'MealRating'
        verbose_name_plural = 'MealRatings'

