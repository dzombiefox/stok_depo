from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name="stok"),
    # url(r'^add',views.add,name="addBarang"),
    url(r'^save',views.save,name="saveStok"),
    url(r'^printstok',views.printstok,name="printstok"),
    url(r'^data',views.data,name="stokdata"),
    url(r'^tes',views.tes,name="tes"),
    url(r'^edit/(?P<id>.+)$',views.edit,name="editStok"),
    # url(r'^delete/(?P<data>.+)$',views.delete,name="deleteBarang"),

]