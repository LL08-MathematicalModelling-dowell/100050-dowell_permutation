from django.shortcuts import render

# Create your views here.
from django.views import View


class IndexView(View):

    def get(self, request):
        return render(request, 'calculator/index.html')


class DesktopTwoView(View):

    def get(self, request):
        return render(request, 'calculator/desktop-2.html')

class DesktopThreeView(View):

    def get(self, request):
        return render(request, 'calculator/desktop-3.html')


index_view = IndexView.as_view()
desktop_two_view = DesktopTwoView.as_view()
desktop_three_view = DesktopThreeView.as_view()
