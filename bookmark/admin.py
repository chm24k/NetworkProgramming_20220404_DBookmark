from django.contrib import admin

from bookmark.models import Bookmark

# Register your models here.
#북마크 테이블 보이게하기
admin.site.register(Bookmark) #어드민 사이트에 북마크 올리겠다