from django.utils.translation import gettext_lazy as _

import django_filters

from froide.helper.search.filters import BaseSearchFilterSet
from froide.helper.widgets import BootstrapSelect

from .models import Author, Category


class ArticleFilterset(BaseSearchFilterSet):
    query_fields = ["title^5", "description^3", "content", "author"]

    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        empty_label=_("all categories"),
        widget=BootstrapSelect(attrs={"label": _("category")}),
        method="filter_category",
    )

    author = django_filters.ModelChoiceFilter(
        queryset=Author.objects.all(),
        empty_label=_("all authors"),
        widget=BootstrapSelect(attrs={"label": _("author")}),
        method="filter_author",
    )

    def filter_category(self, qs, name, value):
        return qs.filter(category=value.id)

    def filter_author(self, qs, name, value):
        return qs.filter(author=value.id)
