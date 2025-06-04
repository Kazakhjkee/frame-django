
from django.db import models
from django.core.exceptions import ValidationError

# Валидатор: принимает только 0 или положительные числа
def validate_positive_or_zero(value):
    if value < 0:
        raise ValidationError("Только положительные числа, дружище!")

class Course(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(validators=[validate_positive_or_zero])
    duration_hours = models.PositiveIntegerField(validators=[validate_positive_or_zero])

    # Возвращает ID и название
    def full_info(self):
        return f"Курс #{self.id}: {self.name}"

    # Сумма цены и длительности
    def total_value(self):
        return self.price + self.duration_hours

    # Весёлый метод
    def hype(self):
        return f"🔥 {self.name.upper()} — твой путь к успеху за {self.duration_hours} часов и всего за {self.price} тенге! 🔥"

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(validators=[validate_positive_or_zero])
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    # Метод: имя и курс
    def short_intro(self):
        return f"{self.name} учится на {self.course.name}"

    # Метод для фана
    def motivation(self):
        return f"🚀 {self.name} — будущая легенда в {self.course.name}!"

    def __str__(self):
        return self.name
