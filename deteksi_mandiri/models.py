<<<<<<< HEAD
from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):
    name = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="Duration of the Quiz in minutes")
    required_score_to_pass = models.IntegerField(
        help_text="Required score to pass the test")

    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_questions(self):
        return self.questions.all()[:self.number_of_questions]


class Question(models.Model):
    text = models.CharField(max_length=100)
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name="questions")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answers.all()


class Answer(models.Model):
    text = models.CharField(max_length=100)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Question : {self.question.text}, Answer : {self.text}, Correct : {self.correct}"


class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skor = models.FloatField()

    def __str__(self):
        return str(self.pk)
=======
from django.db import models
from django.contrib.auth.models import User


# Quiz model
class Quiz(models.Model):

    # Attribute
    name = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="durations of the quiz in minutes")
    required_score_to_pass = models.IntegerField(help_text="required score to diagnosed negative in percent")

    # Str function
    def __str__(self):
        return f"{self.name}-{self.topic}"

    # Get all question fro this quiz
    def get_questions(self):
        return self.questions.all()[:self.number_of_questions]


# Question model
class Question(models.Model):

    # Attribute
    text = models.CharField(max_length=100)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    created = models.DateTimeField(auto_now_add=True)

    # Str function
    def __str__(self):
        return str(self.text)

    # Get all answer for this question
    def get_answers(self):
        return self.answers.all()


# Answer model
class Answer(models.Model):

    # Attribute
    text = models.CharField(max_length=100)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    created = models.DateTimeField(auto_now_add=True)
    poin = models.IntegerField()

    # Str function
    def __str__(self):
        return f"question : {self.question.text} | answer : {self.text} ({self.poin}) |correct : {self.correct}"


# Result model
class Result(models.Model):

    # Attribute
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    result_score = models.FloatField()

    # Str function
    def __str__(self):
        return str(self.pk)

>>>>>>> 99d81d9a1038e3c401a758a44d449b85248bed7d
