from django.contrib import admin
from .models import UserProfile, CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin



#User = get_user_model()
#admin.site.unregister(User)

class UserProfileInLine(admin.StackedInline):
	model = UserProfile
	can_delete = False


class CustomUserAdmin(admin.ModelAdmin):
	model = CustomUser
	inlines = [UserProfileInLine]


admin.site.register(CustomUser, CustomUserAdmin)
#admin.site.register(CustomUser)

