from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import PBKDF2PasswordHasher


###########################################################################################
# Index Page
###########################################################################################
def control_index(request):
    context = {
    }
    return render(request, 'control/index.html')


###########################################################################################
# Akademy
###########################################################################################
def control_academy(request):
    about = AboutUs.objects.last()
    gallery = Gallery.objects.all()
    address = AcademyAdress.objects.all()
    email = AcademyEmail.objects.all()
    phone = AcademyPhone.objects.all()
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    context = {
        "code": code,
        "about": about,
        "gallery": gallery,
        "email": email,
        "phone": phone,
        "address": address,
    }
    return render(request, 'control/academy/about.html', context)

def control_about_edit(request):
    if request.method == "POST":
        about = AboutUs.objects.last()
        about.title_uz = request.POST['title_uz']
        about.description_uz = request.POST['description_uz']
        about.instagram = request.POST['instagram']
        about.facebook = request.POST['facebook']
        about.tiktok = request.POST['tiktok']
        about.youtube = request.POST['youtube']
        about.save()
        return redirect("/control/academy/?edit")

# Academy Address ########################################################################
def control_address_add(request):
    if request.method == "POST":
        AcademyAdress.objects.create (
            address = request.POST["address"]
        )
        return redirect("/control/academy/?added_address")

def control_address_remove(request, id):
    a = AcademyAdress.objects.get(id = id)
    a.delete()
    return redirect("/control/academy/?removed_address")


# Academy Email ########################################################################
def control_email_add(request):
    if request.method == "POST":
        AcademyEmail.objects.create (
            email = request.POST["email"]
        )
        return redirect("/control/academy/?added_email")

def control_email_remove(request, id):
    a = AcademyEmail.objects.get(id = id)
    a.delete()
    return redirect("/control/academy/?removed_email")


# Academy Email ########################################################################
def control_phone_add(request):
    if request.method == "POST":
        AcademyPhone.objects.create (
            phone = request.POST["phone"]
        )
        return redirect("/control/academy/?added_phone")

def control_phone_remove(request, id):
    a = AcademyPhone.objects.get(id = id)
    a.delete()
    return redirect("/control/academy/?removed_phone")



###########################################################################################
# Gallery
###########################################################################################

def control_gallery(request):
    gallery = Gallery.objects.all()
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    context = {
        "code": code,
        "gallery": gallery,
    }
    return render(request, 'control/academy/gallery.html', context)


def control_gallery_add(request):
    if request.method == "POST" and request.FILES["file"]:
        Gallery.objects.create (
            img_min = request.FILES["file"],
            img_max = request.FILES["file"]
        )
        return redirect("/control/gallery/?added_photo")

def control_gallery_remove(request, id):
    g = Gallery.objects.get(id = id)
    g.delete()
    return redirect("/control/gallery/?removed_photo")

###########################################################################################
# Discount
###########################################################################################
def control_discount(request):
    discount = Discount.objects.all()
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    context = {
        "code": code,
        "discount": discount,
    }
    return render(request, 'control/academy/discount.html', context)

def control_discount_add(request):
    if request.method == "POST":
        Discount.objects.create (
            title = request.POST["title"],
            unit = request.POST["unit"],
        )
        return redirect("/control/discount/?added_discount")

def control_discount_edit(request):
    if request.method == "POST":
        discount = Discount.objects.get(id=request.POST["id"])
        discount.title = request.POST["title"]
        discount.unit = request.POST["unit"]
        discount.save()
        return redirect("/control/discount/?edited_discount")

def control_discount_remove(request, id):
    d = Discount.objects.get(id = id)
    d.delete()
    return redirect("/control/discount/?removed_discount")



###########################################################################################
# Category Add, Remove and Edit 
###########################################################################################
def control_category_all(request):
    categories = Category.objects.all()
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    context = {
        "categories": categories,
        "code": code
    }
    return render(request, 'control/category/all.html', context)
    
def control_category_add(request):
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    context = {
        "code": code
    }
    return render(request, 'control/category/add.html', context)

def control_category_create(request):
    if request.method == "POST":
        arr = list(map(lambda x: x.title_uz.lower(), Category.objects.all()))
        if request.POST["title_uz"].lower() not in arr:
            Category.objects.create(
                title_uz = request.POST["title_uz"],
                priority = request.POST["priority"]
            )
            return redirect("/control/category/all/?create")
        else:
            return redirect("/control/category/add/?title")

def control_category_detail(request, slug):
    category = Category.objects.get(slug = slug)
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    context = {
        "category": category,
        "code": code
    }
    return render(request, 'control/category/detail.html', context)

def control_category_edit(request):
    if request.method == "POST":
        category = Category.objects.get(slug=request.POST["category_slug"])
        arr = list(map(lambda x: x.title_uz.lower(), Category.objects.all()))
        print(arr)
        if request.POST["title_uz"].lower() == category.title_uz.lower():
            pass
        elif request.POST["title_uz"].lower() in arr:
            return redirect("/control/category/detail/{}/?title".format(category.slug))
        else:
            category.title_uz = request.POST['title_uz']
        category.priority = request.POST['priority']
        category.save()

        return redirect("/control/category/all/?edit")

def control_category_remove(request):
    if request.method == "POST":
        category = Category.objects.get(slug = request.POST["category_slug"])
        category.delete()
        return redirect(f"/control/category/all/?remove")

###########################################################################################
# Course Add, Remove and Edit
###########################################################################################

def control_course_all(request):
    courses = Course.objects.all()
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    context = {
        "courses": courses,
        "code": code
    }
    return render(request, 'control/course/all.html', context)

def control_course_add(request):
    categories = Category.objects.all() 
    discount = Discount.objects.all() 
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    context = {
        "categories": categories,
        "discount": discount,
        "code": code
    }
    return render(request, 'control/course/add.html', context)

def control_course_create(request):
    if request.method == "POST" and request.FILES["file"]:
        arr = list(map(lambda x: x.title_uz.lower(), Course.objects.all()))
        category = Category.objects.get(id=request.POST["category_id"])
        discount = Discount.objects.get(id=request.POST["discount_id"].title())
        if request.POST["title_uz"].lower() not in arr:
            Course.objects.create(
                img = request.FILES["file"],
                category = category,
                discount = discount,
                title_uz = request.POST["title_uz"],
                priority = request.POST["priority"],
                price = request.POST["price"],
                description_uz = request.POST["description_uz"],
            )
            return redirect("/control/course/all/?create")
        else:
            return redirect("/control/course/add/?title")

def control_course_detail(request, slug):
    course = Course.objects.get(slug = slug)
    categories = Category.objects.all()
    discount = Discount.objects.all()
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    context = {
        "course": course,
        "discount": discount,
        "categories": categories,
        "code": code
    }
    return render(request, 'control/course/detail.html', context)

def control_course_edit(request):
    if request.method == "POST" or request.FILES["file"]:
        course = Course.objects.get(slug=request.POST["course_slug"])
        arr = list(map(lambda x: x.title_uz.lower(), Course.objects.all()))
        category = Category.objects.get(id=request.POST["category_id"])
        if request.POST["title_uz"].lower() == course.title_uz.lower():
            pass
        elif request.POST["title_uz"].lower() in arr:
            return redirect("/control/course/detail/{}/?title".format(course.slug))
        else:
            course.title_uz = request.POST['title_uz']
        course.category = category
        course.priority = request.POST['priority']
        course.price = request.POST['price']
        course.desciption_uz = request.POST['description_uz']
        try:
            course.img = request.FILES["file"]
        except:
            pass
        course.save()

        return redirect("/control/course/all/?edit")

def control_course_remove(request):
    if request.method == "POST":
        course = Course.objects.get(slug = request.POST["course_slug"])
        course.delete()
        return redirect(f"/control/course/all/?remove")

def control_course_lesson_create(request):
    if request.method == "POST":
        arr = list(map(lambda x: x.title_uz.lower(), CourseLesson.objects.all()))
        course = Course.objects.get(slug=request.POST["course_slug"])
        if request.POST["title_uz"].lower() not in arr:
            CourseLesson.objects.create(
                course = course, 
                title_uz = request.POST["title_uz"], 
                minute = request.POST["minute"],
                content_uz = request.POST["content_uz"],
            )
            return redirect(f"/control/course/detail/{course.slug}/?add_type")
        else:
            return redirect("/control/course/detail/?title")

def control_course_lesson_edit(request):
    if request.method == "POST":
        course = Course.objects.get(slug=request.POST["course_slug"])
        course_lesson = CourseLesson.objects.get(id=request.POST["course_lesson_id"])
        course_lesson.title_uz = request.POST["title_uz"]
        course_lesson.minute = int(request.POST["minute"])
        course_lesson.content_uz = request.POST["content_uz"]
        course_lesson.save()
        return redirect(f"/control/course/detail/{course.slug}/?add_type")

def control_course_lesson_remove(request, course_slug, course_lesson_id):
        course = Course.objects.get(slug=course_slug)
        course_lesson = CourseLesson.objects.get(course=course, id=course_lesson_id)
        course_lesson.delete()
        return redirect(f"/control/course/detail/{course.slug}/?delete")

def control_course_guest_create(request):
    if request.method == "POST" and request.FILES["file"]:
        course = Course.objects.get(slug=request.POST["course_slug"])
        CourseGuest.objects.create(
            course = course, 
            img = request.FILES["file"],
            fio = request.POST["fio"], 
            content = request.POST["content"],
        )
        return redirect(f"/control/course/detail/{course.slug}/?add_guest")

def control_course_guest_edit(request):
    if request.method == "POST" or request.FILES["file"] :
        course = Course.objects.get(slug=request.POST["course_slug"])
        course_guest = CourseGuest.objects.get(id=request.POST["course_guest_id"])
        course_guest.fio = request.POST["fio"]
        course_guest.content = request.POST["content"]
        try:
            course_guest.img = request.FILES["file"]
        except:
            pass
        course_guest.save()
        return redirect(f"/control/course/detail/{course.slug}/?edit_guest")

def control_course_guest_remove(request, course_slug, course_guest_id):
        course = Course.objects.get(slug=course_slug)
        course_guest = CourseGuest.objects.get(course=course, id=course_guest_id)
        course_guest.delete()
        return redirect(f"/control/course/detail/{course.slug}/?delete_guest")


###########################################################################################
# Slider
###########################################################################################

def control_slider_all(request):
    slider = Slider.objects.all()
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    context = {
        "slider": slider,
        "code": code
    }
    return render(request, 'control/slider/all.html', context)
  
def control_slider_add(request):
    slider = Slider.objects.all() 
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    context = {
        "slider": slider,
        "code": code
    }
    return render(request, 'control/slider/add.html', context)

def control_slider_create(request):
    if request.method == "POST" and request.FILES["file"]:
        Slider.objects.create(
            img = request.FILES["file"],
            title_uz = request.POST["title_uz"],
        )
        return redirect("/control/slider/all/?create")

def control_slider_detail(request, id):
    slider = Slider.objects.get(id = id)
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    context = {
        "slider": slider,
        "code": code
    }
    return render(request, 'control/slider/detail.html', context)

def control_slider_edit(request):
    if request.method == "POST" or request.FILES["file"]:
        slider = Slider.objects.get(id=request.POST["slider_id"])
        slider.title_uz = request.POST['title_uz']
        try:
            slider.img = request.FILES["file"]
        except:
            pass
        slider.save()
        return redirect("/control/slider/all/?edit")

def control_slider_remove(request):
    if request.method == "POST":
        slider = Slider.objects.get(id = request.POST["slider_id"])
        slider.delete()
        return redirect(f"/control/slider/all/?remove")


###########################################################################################
# Teacher
###########################################################################################

def control_teacher_all(request):
    teachers = Teacher.objects.all()
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    context = {
        "teachers": teachers,
        "code": code
    }
    return render(request, "control/teacher/all.html", context)

def control_teacher_add(request):
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    context = {
        "code": code
    }
    return render(request, 'control/teacher/add.html', context)

def control_teacher_create(request):
    if request.method == "POST" and request.FILES["file"]:
        Teacher.objects.create(
            img = request.FILES["file"],
            fio = request.POST["fio"],
            profession = request.POST["profession"],
            description_uz  = request.POST["description_uz "],
            instagram = request.POST["instagram"],
            email = request.POST["email"],
            facebook = request.POST["facebook"],
            youtube = request.POST["youtube"],
        )
        return redirect("/control/teacher/all/?create")

def control_teacher_detail(request, id):
    teacher = Teacher.objects.get(id = id) 
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    context = {
        "teacher": teacher,
        "code": code
    }
    return render(request, 'control/teacher/detail.html', context)

def control_teacher_edit(request):
    if request.method == "POST" or request.FILES["file"]:
        teacher = Teacher.objects.get(id=request.POST["teacher_id"])
        teacher.fio = request.POST['fio']
        teacher.profession = request.POST['profession']
        teacher.instagram = request.POST['instagram']
        teacher.facebook = request.POST['facebook']
        teacher.email = request.POST['email']
        teacher.youtube = request.POST['youtube']
        try:
            teacher.img = request.FILES["file"]
        except:
            pass
        teacher.save()
        return redirect("/control/teacher/all/?edit")

def control_teacher_remove(request):
    if request.method == "POST":
        teacher = Teacher.objects.get(id = request.POST["teacher_id"])
        teacher.delete()
        return redirect(f"/control/teacher/all/?remove")

###########################################################################################
# News
###########################################################################################

def control_news_all(request):
    news = News.objects.all()
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    context = {
        "news": news,
        "code": code
    }
    return render(request, "control/news/all.html", context)

def control_news_add(request):
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    context = {
        "code": code
    }
    return render(request, 'control/news/add.html', context)

def control_news_create(request):
    if request.method == "POST" and request.FILES["file"]:
        arr = list(map(lambda x: x.title_uz.lower(), News.objects.all()))
        if request.POST["title_uz"].lower() not in arr:
            News.objects.create(
                img_min = request.FILES["file"],
                img_max = request.FILES["file"],
                title_uz = request.POST["title_uz"],
                description_uz = request.POST["description_uz"],
            )
            return redirect("/control/news/all/?create")
        else:
            return redirect("/control/news/add/?title")


def control_news_detail(request, slug):
    new = News.objects.get(slug = slug) 
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    context = {
        "new": new,
        "code": code
    }
    return render(request, 'control/news/detail.html', context)

def control_news_edit(request):
    if request.method == "POST" or request.FILES["file"]:
        new = News.objects.get(slug=request.POST["new_slug"])
        arr = list(map(lambda x: x.title_uz.lower(), News.objects.all()))
        if request.POST["title_uz"].lower() == new.title_uz.lower():
            pass
        elif request.POST["title_uz"].lower() in arr:
            return redirect("/control/news/detail/{}/?title".format(new.slug))
        else:
            new.title_uz = request.POST['title_uz']
        new.desciption_uz = request.POST['description_uz']
        try:
            new.img_min = request.FILES["file"]
            new.img_max = request.FILES["file"]
        except:
            pass
        new.save()

        return redirect("/control/news/all/?edit")

def control_news_remove(request):
    if request.method == "POST":
        new = News.objects.get(slug = request.POST["new_slug"])
        new.delete()
        return redirect("/control/news/all/?remove")



###########################################################################################
# User
###########################################################################################

def control_user_all(request):
    users = User.objects.all()
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    context = {
        "users": users,
        "code": code
    }
    return render(request, "control/user/all.html", context)

def control_user_add(request):
    all_roles = Role.objects.all()
    roles = []
    for i in all_roles:
        if i.code == 1 or i.code == 2 or i.code == 3:
            roles.append(i)
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    context = {
        "code": code,
        "roles": roles
    }
    return render(request, 'control/user/add.html', context)

def control_user_detail(request, id):
    user = User.objects.get(id = id) 
    all_roles = Role.objects.all()
    roles = []
    for i in all_roles:
        if i.code == 1 or i.code == 2 or i.code == 3:
            roles.append(i)
    try:
        code = request.build_absolute_uri().split("?")[1]
    except:
        code = None
    context = {
        "user": user,
        "code": code,
        "roles": roles
    }
    return render(request, 'control/user/detail.html', context)

def control_user_create(request):
    if request.method == 'POST':
        users = User.objects.all()

        for i in users:
            if request.POST['username'].lower() == i.username:
                return redirect('/control/user/add/?username')

        for i in users:
            if request.POST['email'].lower() == i.email:
                return redirect('/control/user/add/?email')

        u = User.objects.create_user(
            username = request.POST['username'].lower(),
            password = request.POST['password'],
            email = request.POST['email'].lower(),
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
        )
        u.account.phone = request.POST['phone']
        u.account.role_id = request.POST['role']
        u.account.save()
        return redirect('/control/user/all/?create')

def control_user_edit(request):
    if request.method == 'POST':
        c = User.objects.get(id=request.POST['id'])

        usernames = list(map(lambda x: x.username.lower(), User.objects.all()))
        emails = list(map(lambda x: x.email.lower(), User.objects.all()))  

        if request.POST["username"].lower() == c.username.lower():
            pass
        elif request.POST["username"].lower() not in usernames:
            c.username = request.POST["username"]
        else:
            return redirect("/control/user/detail/{}/?username".format(c.id))

        if request.POST["email"].lower() == c.email.lower():
            pass
        elif request.POST["email"].lower() not in emails:
            c.email = request.POST["email"]
        else:
            return redirect("/control/user/detail/{}/?email".format(c.id))

        c.first_name = request.POST['first_name']
        c.last_name = request.POST['last_name']

        c.account.phone = request.POST['phone']
        c.account.role_id = request.POST["role"]
        c.account.save()

        c.save()
        return redirect("/control/user/all/?edit")
        
#! change password
def control_user_password_change(request):
    u = User.objects.get(id=request.POST["id"])
    hash = PBKDF2PasswordHasher()
    password = request.POST['password']
    password = hash.encode(password=password, salt="salt", iterations=50000)
    u.password = password
    u.save()
    return redirect('/control/user/all/?edit') 

def control_user_delete(request):
    if request.method == "POST":
        c = User.objects.get(id=request.POST['id'])
        c.delete()
    return redirect("/control/user/all/?delete")

























