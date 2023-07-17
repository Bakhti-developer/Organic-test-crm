from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [ 
    path("", views.control_index, name="control_index"),

    # Akademy And About #############################################################
    path("academy/", views.control_academy, name="control_academy"),

    path("about/edit/", views.control_about_edit, name="control_about_edit"),
    # Address
    path("address/add/", views.control_address_add, name="control_address_add"),
    path("address/remove/<int:id>/", views.control_address_remove, name="control_address_remove"),
    # Email
    path("email/add/", views.control_email_add, name="control_email_add"),
    path("email/remove/<int:id>/", views.control_email_remove, name="control_email_remove"),
    # Phone
    path("phone/add/", views.control_phone_add, name="control_phone_add"),
    path("phone/remove/<int:id>/", views.control_phone_remove, name="control_phone_remove"),


    # Gallery ########################################################################
    path("gallery/", views.control_gallery, name="control_gallery"),
        path("gallery/add/", views.control_gallery_add, name="control_gallery_add"),
        path("gallery/remove/<int:id>/", views.control_gallery_remove, name="control_gallery_remove"),


    # Discount ########################################################################
    path("discount/", views.control_discount, name="control_discount"),
        path("discount/add/", views.control_discount_add, name="control_discount_add"),
        path("discount/edit/", views.control_discount_edit, name="control_discount_edit"),
        path("discount/remove/<int:id>", views.control_discount_remove, name="control_discount_remove"),



    # Category #######################################################################
    path("category/all/", views.control_category_all, name="control_category_all"),
        path("category/add/", views.control_category_add, name="control_category_add"),
        path("category/create/", views.control_category_create, name="control_category_create"),
    path("category/detail/<str:slug>/", views.control_category_detail, name="control_category_detail"),
        path("category/edit/", views.control_category_edit, name="control_category_edit"),
        path("category/remove/", views.control_category_remove, name="control_category_remove"),
    
    # Course ##########################################################################
    path("course/all/", views.control_course_all, name="control_course_all"),
        path("course/add/", views.control_course_add, name="control_course_add"),
        path("course/create/", views.control_course_create, name="control_course_create"),
    # Course lesson ####################################################################    
        path("course/lesson/create/", views.control_course_lesson_create, name="control_course_lesson_create"),
        path("course/lesson/edit/", views.control_course_lesson_edit, name="control_course_lesson_edit"),
        path("course/lesson/remove/<str:course_slug>_<str:course_lesson_id>", views.control_course_lesson_remove, name="control_course_lesson_remove"),
    
    # Course Guest #####################################################################   
        path("course/guest/create/", views.control_course_guest_create, name="control_course_guest_create"),
        path("course/guest/edit/", views.control_course_guest_edit, name="control_course_guest_edit"),
        path("course/guest/remove/<str:course_slug>_<str:course_guest_id>", views.control_course_guest_remove, name="control_course_guest_remove"),


    path("course/detail/<str:slug>/", views.control_course_detail, name="control_course_detail"),
        path("course/edit/", views.control_course_edit, name="control_course_edit"),
        path("course/remove/", views.control_course_remove, name="control_course_remove"),

    # Slider #############################################################################   
    path("slider/all/", views.control_slider_all, name="control_slider_all"),
    path("slider/add/", views.control_slider_add, name="control_slider_add"),
        path("slider/create/", views.control_slider_create, name="control_slider_create"),
    path("slider/detail/<int:id>", views.control_slider_detail, name="control_slider_detail"),
        path("slider/edit/", views.control_slider_edit, name="control_slider_edit"),
    path("slider/remove/", views.control_slider_remove, name="control_slider_remove"),

    # Teacher ############################################################################
    path("teacher/all/", views.control_teacher_all, name="control_teacher_all"),
    path("teacher/add/", views.control_teacher_add, name="control_teacher_add"),
        path("teacher/create/", views.control_teacher_create, name="control_teacher_create"),
    path("teacher/detail/<int:id>", views.control_teacher_detail, name="control_teacher_detail"),
        path("teacher/edit/", views.control_teacher_edit, name="control_teacher_edit"),
        path("teacher/remove/", views.control_teacher_remove, name="control_teacher_remove"),

    # News ###############################################################################
    path("news/all/", views.control_news_all, name="control_news_all"),
    path("news/add/", views.control_news_add, name="control_news_add"),
        path("news/create/", views.control_news_create, name="control_news_create"),
    path("news/detail/<str:slug>/", views.control_news_detail, name="control_news_detail"),
        path("news/edit/", views.control_news_edit, name="control_news_edit"),
        path("news/remove/", views.control_news_remove, name="control_news_remove"),

    # CRM ################################################################################
    path("crm/", include("crm.urls")),

    # User ###############################################################################
    path("user/all/", views.control_user_all, name="control_user_all"),
    path("user/add/", views.control_user_add, name="control_user_add"),
    path("user/detail/<int:id>/", views.control_user_detail, name="control_user_detail"),
        path("user/create/", views.control_user_create, name="control_user_create"),
        path("user/edit/", views.control_user_edit, name="control_user_edit"),
        path("user/password/edit/", views.control_user_password_change, name="control_user_password_edit"),
        path("user/remove/", views.control_user_delete, name="control_user_remove"),

]