from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # --- 1. Main Pages (Connected to your Logic) ---
    
    # Homepage (Index)
    path('', views.home, name='home'),
    path('index/', views.home, name='pages_index'),

    # List Page (With Search, Filter & Pagination Logic)
    path('list-page/', views.biodata_list, name='biodata_list'),

    # Create Form (With Save & File Upload Logic)
    path('form/', views.biodata_create, name='biodata_create'),

    # Detail Page (With Single Profile Fetching Logic)
    # IMPORTANT: Added <int:pk> so we know which profile to show
    path('detail-page/<int:pk>/', views.biodata_detail, name='biodata_detail'),
    
    
    path('matching/<int:pk>/', views.biodata_matching, name='biodata_matching'),


    # --- 2. Static Pages (No Logic Yet) ---
    # These render the HTML templates directly. 
    
    path('search/', TemplateView.as_view(template_name='SearchResult.html'), name='pages_search'),
    path('account/settings/', TemplateView.as_view(template_name='accountSetting.html'), name='pages_account_settings'),
    path('card/', TemplateView.as_view(template_name='biodata_card.html'), name='pages_biodata_card'),
    path('chats/', TemplateView.as_view(template_name='chats.html'), name='pages_chats'),
    path('member/detail/', TemplateView.as_view(template_name='memberProfileDetail.html'), name='pages_member_profile_detail'),
    path('premium/', TemplateView.as_view(template_name='premiumPlan.html'), name='pages_premium'),
    path('register/', TemplateView.as_view(template_name='registration.html'), name='pages_register'),
    path('dashboard/', TemplateView.as_view(template_name='userDashboard.html'), name='pages_dashboard'),
]




# from django.urls import path
# from django.views.generic import TemplateView
# from . import views

# urlpatterns = [

#     # Main biodata views
#     path('', views.biodata_list, name='biodata_list'),
#     path('create/', views.biodata_create, name='biodata_create'),
#     path('profile/<int:pk>/', views.biodata_detail, name='biodata_detail'),

#     # Static template pages
#     path('index/', TemplateView.as_view(template_name='index.html'), name='pages_index'),
#     path('search/', TemplateView.as_view(template_name='SearchResult.html'), name='pages_search'),
#     path('account/settings/', TemplateView.as_view(template_name='accountSetting.html'), name='pages_account_settings'),
#     path('card/', TemplateView.as_view(template_name='biodata_card.html'), name='pages_biodata_card'),
#     path('list-page/', TemplateView.as_view(template_name='biodata_list.html'), name='pages_biodata_list'),
#     path('form/', TemplateView.as_view(template_name='biodata_form.html'), name='pages_biodata_form'),
#     path('detail-page/', TemplateView.as_view(template_name='biodata_detail.html'), name='pages_biodata_detail'),
#     path('chats/', TemplateView.as_view(template_name='chats.html'), name='pages_chats'),
#     path('member/detail/', TemplateView.as_view(template_name='memberProfileDetail.html'), name='pages_member_profile_detail'),
#     path('premium/', TemplateView.as_view(template_name='premiumPlan.html'), name='pages_premium'),
#     path('register/', TemplateView.as_view(template_name='registration.html'), name='pages_register'),
#     path('dashboard/', TemplateView.as_view(template_name='userDashboard.html'), name='pages_dashboard'),
# ]


 
