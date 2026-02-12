from django.contrib import admin
from .models import *
from simple_history.admin import SimpleHistoryAdmin
from .forms import *

# Register your models here.
admin.site.register(Role, SimpleHistoryAdmin)
admin.site.register(User, SimpleHistoryAdmin)
admin.site.register(UserCredenetials, SimpleHistoryAdmin)
admin.site.register(UserFavorites, SimpleHistoryAdmin)

