from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
import json
import ast

from .models import *
from .forms import *

# Create your views here.
def indexView(request):
    players = Player.objects.all()

    try:
        stats = request.COOKIES['stats']
        stats = ast.literal_eval(stats)
    except:
        stats = {"playerStats":{"rock":0,"paper":0,"scissors":0},"pScore":0,"cScore":0, 'tie':0,}

    try:
        device = request.COOKIES['device']
        player, created = Player.objects.get_or_create(device=device)
    except:
        player = 'Nobody'


    if stats != {"playerStats":{"rock":0,"paper":0,"scissors":0},"pScore":0,"cScore":0, 'tie':0,}:
        player_run_stats, created = Stat.objects.get_or_create(player=player,rock = stats['playerStats']['rock'],
         paper = stats['playerStats']['paper'],scissors = stats['playerStats']['scissors'], 
         pScore = stats['pScore'],  cScore = stats['cScore'], tie = stats['tie'])

    
    """
    player_stats, created = PlayerStat.objects.get_or_create(player=player,)
    player_stats.rock = stats['playerStats']['rock']
    player_stats.paper = stats['playerStats']['paper']
    player_stats.scissors = stats['playerStats']['scissors']
    player_stats.pScore = stats['pScore']
    player_stats.cScore = stats['cScore']
    player_stats.save()"""

    context = {'player': player}

    return render(request, 'main/index.html', context)

def statsView(request, pk):
    try:
        stats = request.COOKIES['stats']
        stats = ast.literal_eval(stats)
    except:
        stats = {"playerStats":{"rock":0,"paper":0,"scissors":0},"pScore":0,"cScore":0, 'tie':0,}

    try:
        device = request.COOKIES['device']
        player, created = Player.objects.get_or_create(device=device)
    except:
        player = 'Nobody'


    if stats != {"playerStats":{"rock":0,"paper":0,"scissors":0},"pScore":0,"cScore":0, 'tie':0,}:
        player_run_stats, created = Stat.objects.get_or_create(player=player,rock = stats['playerStats']['rock'],
         paper = stats['playerStats']['paper'],scissors = stats['playerStats']['scissors'], 
         pScore = stats['pScore'],  cScore = stats['cScore'], tie = stats['tie'])


    try:
        player = get_object_or_404(Player, pk=pk)
        if request.method == 'GET':
            form = ContactForm()
        else:
            form = ContactForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['Your_name']
                from_email = form.cleaned_data['Your_email']
                subject = form.cleaned_data['subject']
                message = 'name: ' +  + 'email: ' + from_email + '\n' + '\n' +"Message: " + form.cleaned_data['message']
                try:
                    send_mail(subject, message, from_email, ['menhior1@gmail.com'])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return redirect('success')
        context = {'player': player,'form': form,}
        return render(request, 'main/stats.html', context)
    except:
        return render(request, 'main/error_404.html', {})

def statsData(request, pk):


    player = get_object_or_404(Player, pk=pk)


    players = Player.objects.all()

    total_rock = 0
    total_paper = 0
    total_scissors = 0
    total_wins = 0
    total_losses = 0
    total_ties = 0
    

    try:
        for i in players:
            total_rock += i.get_player_total['Your rock picks %']
            total_paper += i.get_player_total['Your paper picks %']
            total_scissors += i.get_player_total['Your scissors picks %']
            total_wins += i.get_player_winrates['player_win']
            total_losses += i.get_player_winrates['player_loss']
            total_ties += i.get_player_winrates['player_tie']

        total_picks = total_rock + total_paper + total_scissors




        total_rock = round(total_rock/total_picks*100, 2)
        total_paper = round(total_paper/total_picks*100, 2)
        total_scissors = round(total_scissors/total_picks*100, 2)
    except:
        pass


    total_pick_stats = {'Average player rock picks %': total_rock, 'Average player paper picks %': total_paper, 'Average player scissors picks %': total_scissors, }
    total_winrate_stats = {'total_wins': total_wins, 'total_losses': total_losses, 'total_ties': total_ties}

    full_stats_data = []
    full_stats_data.append(player.get_player_total)
    full_stats_data.append(total_pick_stats)
    full_stats_data.append(player.get_player_winrates)
    full_stats_data.append(total_winrate_stats)

    return JsonResponse(full_stats_data, safe=False)
    """return HttpResponse('Hi there')"""

def saveData(request):
    """data = json.loads(request.body)
    pScore = data['pScore']
    cScore = data['cScore']
    print('pScore:',pScore)
    print('cScore:',cScore)"""
    return JsonResponse('Hello there!', safe=False)