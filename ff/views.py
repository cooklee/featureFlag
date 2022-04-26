from django.shortcuts import render
import flags
# Create your views here.
from django.views import View


class FeatureFlagsViews(View):

    def get(self, request):
        return render(request, "base.html", {'flags':flags.all_flags},)
