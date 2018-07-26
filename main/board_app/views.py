from django.shortcuts import render,get_object_or_404
from .models import *
# Create your views here.
def index(request):
    board_list = Board.objects.all()
    # board_list = [board.name for board in boards]

    context = {'board_list':board_list}
    return render(request,'index.html',context)

def board_topics_all(request,pk=None):
    board = get_object_or_404(Board,pk=pk)
    return render(request,'topics.html',{'board':board})

def board_topics_new(request,pk=None):
    board = get_object_or_404(Board,pk=pk)

    return render(request,'new_topic.html',{'board':board})