from django.contrib import admin
from .models import Member

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date","favorite_game", "playing_hours", "game_gender")
  
admin.site.register(Member, MemberAdmin)