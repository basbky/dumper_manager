from typing import Dict

from django.db.models import QuerySet
from django.shortcuts import render
from django.views import View

from .models import Dumper, Model


class DumpersListView(View):
    """
    View to handle the request for dumper list and filter them by model
    """

    def get(self, request, *args, **kwargs) -> Dict[str, QuerySet]:
        """
        Handle the GET request and return filtered dumpers and models

        Args:
        request (HttpRequest): The GET request

        Returns:
        Dict[str, QuerySet]: context containing list of dumpers and models
        """
        dumpers: QuerySet[Dumper] = Dumper.objects.select_related(
            'model'
        ).all()
        current_model = request.GET.get('model') or 'all'
        models: QuerySet[Model] = Model.objects.values()
        if current_model != 'all':
            dumpers = dumpers.filter(model__name=current_model)
        context = {
            'dumpers': dumpers,
            'models': models,
            'current_model': current_model,
        }
        return render(request, 'dumpers_list.html', context)
