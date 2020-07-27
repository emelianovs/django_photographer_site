from .models import Category


def category_url_processor(request):
    categories = Category.objects.all()
    return {"categories": categories}
