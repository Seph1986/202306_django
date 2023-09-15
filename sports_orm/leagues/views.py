from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"baseball_all": League.objects.filter(sport__contains="baseball"),
		"womens_all": League.objects.filter(name__contains="womens"),
		"hockey_all": League.objects.filter(sport__contains="hockey"),
		"other_football_all": League.objects.exclude(sport__contains="football"),
		"conference_all": League.objects.filter(name__contains="conference"),
		"atlantic_all": League.objects.filter(name__contains="atlantic"),
		"dallas_teams": Team.objects.filter(location__contains="dallas"),
		"raptor_teams": Team.objects.filter(team_name__contains="raptors"),
		"city_location": Team.objects.filter(location__contains="city"),
		"t_names": Team.objects.filter(team_name__startswith="t"),
		"order_location": Team.objects.all().order_by("location"),
		"order_team_name": Team.objects.all().order_by("-team_name"),
		"player_cooper": Player.objects.filter(last_name__contains="cooper"),
		"player_joshua": Player.objects.filter(first_name__contains="joshua"),
		"joshua_without_cooper": Player.objects.filter(last_name__contains="cooper").exclude(first_name__contains="joshua"),
		"alexander_wyatt": Player.objects.filter(first_name__contains="alexander") | Player.objects.filter(first_name__contains="wyatt"),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")