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

class DesktopFourView(View):
    def get(self, request):
        return render(request, 'calculator/desktop-4.html')

class DesktopFiveView(View):
    def get(self, request):
        return render(request, 'calculator/desktop-5.html')

class DesktopSixView(View):
    def get(self, request):
        return render(request, 'calculator/desktop-6.html')

class DesktopSevenView(View):
    def get(self, request):
        return render(request, 'calculator/desktop-7.html')

index_view = IndexView.as_view()
desktop_two_view = DesktopTwoView.as_view()
desktop_three_view = DesktopThreeView.as_view()
desktop_four_view = DesktopFourView.as_view()
desktop_five_view = DesktopFiveView.as_view()
desktop_six_view = DesktopSixView.as_view()
desktop_seven_view = DesktopSevenView.as_view()




