from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from parts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', views.upload_car_part, name='upload_car_part'),
    path('', views.car_part_list, name='car_part_list'),
]

# إضافة دعم عرض الصور والوسائط في وضع التطوير فقط
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
