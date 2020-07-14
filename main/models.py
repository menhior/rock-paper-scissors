from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Player(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    device = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        '''if self.name:
            name = self.name
        else:
            name = self.device
        return str(name)'''

        device = self.device
        return str(device)

    @property
    def get_player_total(self):

        player_rock = 0
        player_paper = 0
        player_scissors = 0

        try:
            all_stats = self.stat_set.all()
            
            for i in all_stats:
                player_rock += i.rock
                player_paper += i.paper
                player_scissors += i.scissors
               

            all_picks = player_rock + player_paper + player_scissors

            player_rock = round(player_rock/all_picks*100, 2)
            player_paper = round(player_paper/all_picks*100, 2)
            player_scissors = round(player_scissors/all_picks*100, 2)
        except:
            pass

        player_stats = {'Your rock picks %': player_rock, 'Your paper picks %': player_paper, 'Your scissors picks %': player_scissors, }
        return player_stats

    @property
    def get_player_winrates(self):
        all_stats = self.stat_set.all()
        player_tie = 0
        player_win = 0
        player_loss = 0
        number_of_runs = 0

        
        try:
            for i in all_stats:
                player_tie += i.tie
                player_win += i.pScore
                player_loss += i.cScore
                number_of_runs += 1
        except:
            pass

        player_winrates = {'player_win': player_win, 'player_loss': player_loss, 'player_tie': player_tie, }

        return player_winrates
    

class Stat(models.Model):
    player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)
    rock = models.IntegerField(default=0, null=True, blank=True)
    paper = models.IntegerField(default=0, null=True, blank=True)
    scissors = models.IntegerField(default=0, null=True, blank=True)
    pScore = models.IntegerField(default=0, null=True, blank=True)
    cScore = models.IntegerField(default=0, null=True, blank=True)
    tie = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.player
