from django.urls import path
from .views import test_management_token, list_users, list_roles, assign_role, create_user_view, search_user, update_metadata, block_user_view, change_user_role, delete_user_view, bulk_create_users, import_users_from_csv, debug_user_roles


urlpatterns = [
    path('token/', test_management_token, name='test_management_token'),
    path('users/', list_users, name='list_users'),
    path('roles/', list_roles, name='list_roles'),
    path('assign-role/', assign_role, name='assign_role'),
    path('create-user/', create_user_view, name='create_user'),
    path('search-user/', search_user, name='search_user'),
    path('update-metadata/', update_metadata, name='update_metadata'),
    path('block-user/', block_user_view, name='block_user'),
    path('change-role/', change_user_role, name='change_user_role'),
    path('delete-user/', delete_user_view, name='delete_user'),
    path('bulk-create-users/', bulk_create_users, name='bulk_create_users'),
    path('import-users-csv/', import_users_from_csv, name='import_users_csv'),
    path("debug-roles/", debug_user_roles),
]