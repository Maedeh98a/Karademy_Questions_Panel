from django import template
from ..models import Category

register = template.Library()


@register.inclusion_tag("questions/partials/cat_nav.html")
def cat_nav():
    return {"category": Category.objects.all()}
