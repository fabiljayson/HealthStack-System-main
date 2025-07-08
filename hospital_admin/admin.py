from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.sites import NotRegistered
from .models import Admin_Information, Clinical_Laboratory_Technician, hospital_department, specialization, service, Test_Information
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import AdminPasswordChangeForm

User = get_user_model()

class UserAdmin(BaseUserAdmin):
    change_password_form = AdminPasswordChangeForm

# Unregister default User admin safely
try:
    admin.site.unregister(User)
except NotRegistered:
    pass

# Re-register the User model
admin.site.register(User, UserAdmin)

# Your existing registrations
admin.site.register(Admin_Information)
admin.site.register(Clinical_Laboratory_Technician)
admin.site.register(hospital_department)
admin.site.register(specialization)
admin.site.register(service)
admin.site.register(Test_Information)
