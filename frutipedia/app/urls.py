from django.urls import path, include

from frutipedia.app.views import index, dashboard, fruit_create, fruit_details, fruit_edit, fruit_delete, \
    profile_create, profile_delete, profile_details, profile_edit

urlpatterns = (
    path('', index, name='home page'),
    path('dashboard/', dashboard, name='dashboard page'),
    path('create/', fruit_create, name='fruit create page'),
    path('<int:fruitId>/', include([
        path('details/', fruit_details, name='fruit details page'),
        path('edit/', fruit_edit, name='fruit edit page'),
        path('delete/', fruit_delete, name='fruit delete page'),
    ])),

    path('profile/', include([
        path('create/', profile_create, name='profile create page'),
        path('delete/', profile_delete, name='profile delete page'),
        path('details/', profile_details, name='profile details page'),
        path('edit/', profile_edit, name='profile edit page'),
    ])),

)
