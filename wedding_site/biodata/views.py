from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic import TemplateView # Kept if you still want to use it, but functions are below
from .models import CommunityBiodata
from .forms import CommunityBiodataForm
import urllib.parse

 

from django.http import JsonResponse
from django.shortcuts import render
import urllib



# --- Functional Views (Logic) ---

def home(request):
    return render(request, 'index.html')

def biodata_list(request):
    profiles = CommunityBiodata.objects.all().order_by('-id') # Added ordering for better pagination
    
    search_query = request.GET.get('search', '')
    gotra_filter = request.GET.get('gotra', '')

    if search_query:
        profiles = profiles.filter(
            Q(full_name__icontains=search_query) | 
            Q(serial_number__icontains=search_query)
        )
    
    if gotra_filter:
        profiles = profiles.filter(gotra__icontains=gotra_filter)

    paginator = Paginator(profiles, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'profiles': page_obj,
        'search_query': search_query,
        'gotra_filter': gotra_filter
    }
    return render(request, 'biodata_list.html', context)

def biodata_detail(request, pk):
    profile = get_object_or_404(CommunityBiodata, pk=pk)
    
    share_text = f"""*गोंडवाना वैवाहिक ग्रुप (नि:शुल्क बायोडाटा)*
*सरल क्रमांक {profile.serial_number}*
▶️ नाम :- {profile.full_name}
▶️ जाति :- {profile.caste}
▶️ गोत्र :- {profile.gotra}
▶️ देव संख्या :- {profile.deity_number}
▶️ पिता का नाम :- {profile.father_name}
▶️ माता का नाम :- {profile.mother_name}
▶️ रंग :- {profile.complexion}
▶️ कद :- {profile.height}
▶️ जन्मतिथि :- {profile.date_of_birth}
▶️ मामा का गोत्र :- {profile.maternal_uncle_gotra}
▶️ शिक्षा :- {profile.education}
▶️ व्यवसाय :- {profile.occupation}
▶️ पारिवारिक स्थिति :- {profile.family_status}
▶️ पता :- {profile.address}
*(संपर्क के लिए एडमिन से बात करें)*"""
    
    whatsapp_url = f"https://wa.me/?text={urllib.parse.quote(share_text)}"

    return render(request, 'biodata_detail.html', {
        'profile': profile,
        'whatsapp_url': whatsapp_url
    })

def biodata_create(request):
    if request.method == 'POST':
        form = CommunityBiodataForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('biodata_list') 
    else:
        form = CommunityBiodataForm()
    
    return render(request, 'biodata_form.html', {'form': form})

 
def biodata_matching(request, pk):
    # Get the base profile to find matches for
    profile = get_object_or_404(CommunityBiodata, pk=pk)
    
    # Simple Matching Logic:
    # 1. Exclude the same Gotra (usually prohibited in the community)
    # 2. You can add logic for Deity Number compatibility here
    # 3. Exclude the profile itself
    
    suggestions = CommunityBiodata.objects.exclude(
        Q(gotra=profile.gotra) | Q(pk=profile.pk)
    ).order_by('?')[:6]  # Randomly pick 6 compatible profiles

    return render(request, 'biodata_matching.html', {
        'base_profile': profile,
        'suggestions': suggestions
    })
    
     

# --- Simple Page Views (Static Renders) ---

def search_page(request):
    return render(request, 'SearchResult.html')

def account_settings(request):
    return render(request, 'accountSetting.html')

def biodata_card(request):
    return render(request, 'biodata_card.html')

def chats(request):
    return render(request, 'chats.html')

def member_profile_detail(request):
    return render(request, 'memberProfileDetail.html')

def premium_plan(request):
    return render(request, 'premiumPlan.html')

def register(request):
    return render(request, 'registration.html')

def dashboard(request):
    return render(request, 'userDashboard.html')



# from django.shortcuts import render, get_object_or_404, redirect
# from django.db.models import Q
# from django.core.paginator import Paginator
# from .models import CommunityBiodata
# from .forms import CommunityBiodataForm
# import urllib.parse
# def home(request):
#     return render(request, 'index.html')

# def biodata_list(request):
#     profiles = CommunityBiodata.objects.all()
    
#     search_query = request.GET.get('search', '')
#     gotra_filter = request.GET.get('gotra', '')

#     if search_query:
#         profiles = profiles.filter(
#             Q(full_name__icontains=search_query) | 
#             Q(serial_number__icontains=search_query)
#         )
    
#     if gotra_filter:
#         profiles = profiles.filter(gotra__icontains=gotra_filter)

#     paginator = Paginator(profiles, 12)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     context = {
#         'profiles': page_obj,
#         'search_query': search_query,
#         'gotra_filter': gotra_filter
#     }
#     return render(request, 'biodata_list.html', context)

# # 2. Detail View
# def biodata_detail(request, pk):
#     profile = get_object_or_404(CommunityBiodata, pk=pk)
    
#     share_text = f"""*गोंडवाना वैवाहिक ग्रुप (नि:शुल्क बायोडाटा)*
# *सरल क्रमांक {profile.serial_number}*
# ▶️ नाम :- {profile.full_name}
# ▶️ जाति :- {profile.caste}
# ▶️ गोत्र :- {profile.gotra}
# ▶️ देव संख्या :- {profile.deity_number}
# ▶️ पिता का नाम :- {profile.father_name}
# ▶️ माता का नाम :- {profile.mother_name}
# ▶️ रंग :- {profile.complexion}
# ▶️ कद :- {profile.height}
# ▶️ जन्मतिथि :- {profile.date_of_birth}
# ▶️ मामा का गोत्र :- {profile.maternal_uncle_gotra}
# ▶️ शिक्षा :- {profile.education}
# ▶️ व्यवसाय :- {profile.occupation}
# ▶️ पारिवारिक स्थिति :- {profile.family_status}
# ▶️ पता :- {profile.address}
# *(संपर्क के लिए एडमिन से बात करें)*"""
    
#     whatsapp_url = f"https://wa.me/?text={urllib.parse.quote(share_text)}"

#     return render(request, 'biodata_detail.html', {
#         'profile': profile,
#         'whatsapp_url': whatsapp_url
#     })

# # 3. Create View (UPDATED)
# def biodata_create(request):
#     if request.method == 'POST':
#         # MUST INCLUDE request.FILES here
#         form = CommunityBiodataForm(request.POST, request.FILES) 
#         if form.is_valid():
#             form.save()
#             return redirect('biodata_list')
#     else:
#         form = CommunityBiodataForm()
    
#     return render(request, 'biodata_form.html', {'form': form})


 
