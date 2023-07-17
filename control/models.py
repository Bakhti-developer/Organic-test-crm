from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django_resized import ResizedImageField
from slugify import slugify
from django.contrib.auth.models import User



# Role #####################################################################
class Role(models.Model):
    title = models.CharField(max_length=200)
    code = models.IntegerField(default=4)

    def __str__(self):
        return self.title


# Account ##################################################################
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    telegram_id = models.IntegerField(null=True, blank=True)
    telegram_lang = models.CharField(max_length=255, default="uz")
    telegram_code = models.CharField(max_length=255, null=True, blank=True)
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Аккаунт: {self.user.username}"

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"


# DISCOUNT ##################################################################
class Discount(models.Model):
    title = models.CharField(max_length=225)
    unit = models.IntegerField(default=1,
        validators=[
            MaxValueValidator(100),
            MaxValueValidator(0)
        ]
    )

    def __str__(self):
        return f"Скидка: {self.title}-{self.unit}%"

    class Meta:
        verbose_name = "Скидка"
        verbose_name_plural = "Скидки"

    @property
    def total_courses(self):
        count = Course.objects.filter(discount=self).count()
        return count


# SLIDER ##################################################################
class Slider(models.Model):
    img = ResizedImageField(size=[1200, 600], quality=100, upload_to="slider/img/1200x600")
    title_uz = models.CharField(max_length=300)
    def __str__(self):
        return f"Слайдер: {self.title_ru}"

    class Meta:
        verbose_name = "Slayder"
        verbose_name_plural = "Slayderlar"


# CATEGORY #################################################################
class Category(models.Model):
    title_uz = models.CharField(max_length=225)
    priority = models.IntegerField()
    slug = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return f"Категория: {self.title_uz}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title_uz).lower()
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    @property
    def total_courses(self):
        count = Course.objects.filter(category=self).count()
        return count


# COURSE COURSE_LESSON, COURSE_TYPE, COURSE_GUEST ##########################
class CourseType(models.Model):
    title_uz = models.CharField(max_length=225, null=True, blank=True)
    title_ru = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return f"Тип курса: {self.title_uz}"

    class Meta:
        verbose_name = "Тип курса"
        verbose_name_plural = "Типы курсы"


class Course(models.Model):
    type = models.ManyToManyField(CourseType)
    img = ResizedImageField(size=[400, 400], quality=100, upload_to="courses/")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    title_uz = models.CharField(max_length=500)
    description_uz = models.TextField(null=True, blank=True)
    duration = models.CharField(max_length=225, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True)
    priority = models.IntegerField()
    slug = models.CharField(max_length=500, null=True, blank=True)

    langs = [
        ("uz", "O'zbekcha"),
        ("ru", "Русский"),
    ]
    lang = models.CharField(max_length=2, choices=langs, default="uz")

    def __str__(self):
        return f"Курс: {self.title_uz}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title_uz).lower()
        super(Course, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    @property
    def total_lesson(self):
        count = CourseLesson.objects.filter(category=self).count()
        return count

class CourseLesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title_uz = models.CharField(max_length=225, null=True, blank=True)
    content_uz = models.TextField()
    minute = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Этап урока: {self.course.title_uz}-{self.title_uz}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

class CourseGuest(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    fio = models.CharField(max_length=225, null=True, blank=True)
    img = ResizedImageField(size=[400, 600], quality=100, upload_to="course/guest/", null=True, blank=True)
    content = models.CharField(max_length=225)

    def __str__(self):
        return f"Гост курса: {self.course.title_uz}({self.fio})"

    class Meta:
        verbose_name = "Гост"
        verbose_name_plural = "Госты"




# TEACHER ###################################################################
class Teacher(models.Model): 
    fio = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    description_uz = models.TextField()
    img = ResizedImageField(size=[600, 600], quality=100, upload_to="teachers/", null=True, blank=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    youtube = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Ustoz: {self.fio}"

    class Meta:
        verbose_name = "Ustoz"
        verbose_name_plural = "Ustozlar"


# NEWS ######################################################################
class News(models.Model):
    title_uz = models.CharField(max_length=500)
    description_uz = models.TextField()
    img_min = ResizedImageField(size=[600, 400], quality=100, upload_to="news/img_min/600x300")
    img_max = ResizedImageField(size=[1000, 600], quality=100, upload_to="news/img_max/1000x600")
    slug = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.title_ru

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title_uz).lower()
        super(News, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"


# GALLERY ###################################################################
class Gallery(models.Model): 
    img_min = ResizedImageField(size=[400, 350], quality=100, upload_to="img/gallery/400x350/")
    img_max = ResizedImageField(size=[800, 500], quality=100, upload_to="img/gallery/800x500/")
        
    def __str__(self):
        return f"Галерея: {self}"

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галерея"


# CONTACT ###################################################################
class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.IntegerField()
    email = models.CharField(max_length=255)
    message = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("date_create",)


# ABOUT #####################################################################
class AboutUs(models.Model):
    title_uz = models.CharField(max_length=350)
    description_uz = models.TextField()
    lat = models.CharField(max_length=225)
    long = models.CharField(max_length=225)
    google_map = models.TextField()
    instagram = models.CharField(max_length=300, null=True, blank=True)
    facebook = models.CharField(max_length=300, null=True, blank=True)
    youtube = models.CharField(max_length=300, null=True, blank=True)
    tiktok = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f"Название Академия: {self.title_uz}"

    class Meta: 
        verbose_name = "Академия"
        verbose_name = "Академия"


class AcademyAdress(models.Model):
    address = models.CharField(max_length=255)

class AcademyEmail(models.Model):
    email = models.CharField(max_length=255)

class AcademyPhone(models.Model):
    phone = models.CharField(max_length=255)



class Order(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
    process = models.IntegerField(default=1)
    date_process_1 = models.DateTimeField(auto_now_add=True)
    date_process_2 = models.DateTimeField(null=True, blank=True)
    date_process_3 = models.DateTimeField(null=True, blank=True)
    date_process_4 = models.DateTimeField(null=True, blank=True)
    date_process_5 = models.DateTimeField(null=True, blank=True)
    date_process_6 = models.DateTimeField(null=True, blank=True)
    date_process_7 = models.DateTimeField(null=True, blank=True)
    date_process_8 = models.DateTimeField(null=True, blank=True)
    date_process_9 = models.DateTimeField(null=True, blank=True)
    social = models.CharField(max_length=255)
    fio = models.CharField(max_length=255)
    phone = models.IntegerField()
    reminder = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.fio


class OrderComment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    comment = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order.course.title_uz

    class Meta:
        ordering = ("-date_create",)