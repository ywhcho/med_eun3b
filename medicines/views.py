from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Medicine

# Create your views here.

def index(request):
    """의약정보 메인 페이지 - 성분별, 회사별, 효능별 검색 링크"""
    # Get unique values for each category
    ingredients = Medicine.objects.values_list('성분명', flat=True).distinct().order_by('성분명')
    companies = Medicine.objects.values_list('회사명', flat=True).distinct().order_by('회사명')
    # For effects, we'll show top 20 most common keywords
    all_effects = Medicine.objects.values_list('효능', flat=True)
    effect_keywords = set()
    for effect in all_effects:
        # Extract keywords from effects (simple split by common delimiters)
        words = effect.replace(',', ' ').replace('.', ' ').replace('/', ' ').split()
        for word in words:
            if len(word) > 2:  # Only include words with more than 2 characters
                effect_keywords.add(word)
    effect_keywords = sorted(list(effect_keywords))[:30]
    
    context = {
        'ingredients': ingredients,
        'companies': companies,
        'effect_keywords': effect_keywords,
    }
    return render(request, 'medicines/index.html', context)


def by_ingredient(request):
    """성분별 검색"""
    ingredient = request.GET.get('ingredient', '')
    medicines = Medicine.objects.filter(성분명__icontains=ingredient) if ingredient else Medicine.objects.all()
    context = {
        'medicines': medicines,
        'search_type': '성분',
        'search_value': ingredient,
    }
    return render(request, 'medicines/search_results.html', context)


def by_company(request):
    """회사별 검색"""
    company = request.GET.get('company', '')
    medicines = Medicine.objects.filter(회사명__icontains=company) if company else Medicine.objects.all()
    context = {
        'medicines': medicines,
        'search_type': '회사',
        'search_value': company,
    }
    return render(request, 'medicines/search_results.html', context)


def by_effect(request):
    """효능별 검색"""
    effect = request.GET.get('effect', '')
    medicines = Medicine.objects.filter(효능__icontains=effect) if effect else Medicine.objects.all()
    context = {
        'medicines': medicines,
        'search_type': '효능',
        'search_value': effect,
    }
    return render(request, 'medicines/search_results.html', context)


def detail(request, pk):
    """약품 상세 정보"""
    medicine = get_object_or_404(Medicine, pk=pk)
    # Find related medicines (same ingredient or same company)
    related_medicines = Medicine.objects.filter(
        Q(성분명=medicine.성분명) | Q(회사명=medicine.회사명)
    ).exclude(pk=pk)[:5]
    
    context = {
        'medicine': medicine,
        'related_medicines': related_medicines,
    }
    return render(request, 'medicines/detail.html', context)

