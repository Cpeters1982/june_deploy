from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count


from . import team_maker

def index(request):
	context = {
	# # All baseball leagues
	#    "leagues":
	#    League.objects.filter(sport="Baseball"),
	# # All womens' leagues
	#    "leagues":
	#    League.objects.filter(name__contains="Womens'"),
	# # Hockey leagues of any kind
	#    "leagues":
	#    League.objects.filter(name__contains="hockey"),
	# #  League that isn't football
	#    "leagues":
	#    League.objects.exclude(sport="football"),
	# # Leagues that call themselves confereces
	#    "leagues":
	#    League.objects.filter(name__contains="conference"),
	#    # Leagues in the atlantic region
	#    "leagues":
	#    League.objects.filter(name__contains="atlantic"),
	#    #Teams located in Dallas
	#    "teams":
	#    Team.objects.filter(location="Dallas"),
	#    # Teams called Raptors
	#    "teams":
	#    Team.objects.filter(team_name="Raptors"),
	#    # team contains "City"
	#    "teams"
	#    Team.objects.filter(name__contains="city"),
	#    # team whose name begins with T
	#    "teams":
	#    Team.objects.filter(team_name__startswith="T"),
	#    all teams ordered alphabetically by location
	#    "teams":
	#    Team.objects.order_by("location"),
	#    # order in reverse alphabetical
	#    "teams":
	#    Team.objects.order_by("-location"),
	#    # Every player with lastname "Cooper"
	#    "players":
	#    Player.objects.filter(last_name="Cooper"),
	#    # First name of "Joshua"
	#    "players":
	#    Player.objects.filter(first_name="Joshua"),
	#    #every player with the last name Cooper EXCEPT those named Joshua
	#    "players":
	#    Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),
	#    "players":
	#     # Players named Alexander and Wyatt
	# 	"players":
	# 	Player.objects.filter(first_name="Alexander")|Player.objects.filter(first_name="Wyatt")


	# All teams in the atlantic soccer conference
		# "teams":
		# Team.objects.filter(league__name="Atlantic Soccer Conference"),

	# all current players on the boston Penguins
		# "players":
		# Player.objects.filter(curr_team__team_name="Penguins")
	#all current players in the International Collegiate Baseball Conference
	    # "players":
		# Player.objects.filter(curr_team__league__name="International Collegiate Baseball Conference"),
	#All players in the American Conf of Am Football with last name Lopez
		# "players":
		# Player.objects.filter(curr_team__league__name="American Conference of Amateur Football", last_name="Lopez"),
	# all football players
	# "players":
	# Player.objects.filter(curr_team__league__sport="Football"),
	#all teams with a current player named Sophia
		# "teams":
		# Team.objects.filter(curr_players__first_name="Sophia"),
		# "leagues":
		# League.objects.filter(teams__curr_players__first_name="Sophia"),
		# everyone last named Flores who Doesnt play for the Washington Roughriders
		# "players":
		# Player.objects.filter(last_name="Flores").exclude(curr_team__team_name="Roughriders"),
		#All teams, Past and present, that Samuel Evans has played for
		# "teams":
		# Team.objects.filter(all_players__first_name="Samuel", all_players__last_name="Evans"),
		#all players of the Manitoba Tiger-Cats
		# "players":
		# Player.objects.filter(all_teams__location="Manitoba", all_teams__team_name="Tiger-Cats"),
		#All players formerly with the Wichita Vikings
		# "players":
		# Player.objects.filter(all_teams__location="Wichita", all_teams__team_name="Vikings").exclude(curr_team__location="Wichita", curr_team__team_name="Vikings"),
		#Jacob Gray played for all these teams before the Oregon Colts
		# "teams":
		# Team.objects.filter(all_players__first_name="Jacob", all_players__last_name="Gray").exclude(team_name="Colts", location="Oregon")
		#Everyone named Joshua who has ever played int he atlantic federaration of amateur baseball players
		# "players":
		# Player.objects.filter(first_name="Joshua", all_teams__league__name="Atlantic Federation of Amateur Baseball Players")
		#all teams that have had 12 or more players past and present
		# "teams":
		# Team.object.all().annotate(player_count=(Count)('all_players')).filter(player_count_gte=12),

		#all players sorted by the number of teams they've played for
		"players":
		Player.objects.all().annotate(team_count=(Count('all_teams')).order_by('-team_count'),
	}


# ...all teams in the Atlantic Soccer Conference
# ...all (current) players on the Boston Penguins
# ...all (current) players in the International Collegiate Baseball Conference
# ...all (current) players in the American Conference of Amateur Football with last name "Lopez"
# ...all football players
# ...all teams with a (current) player named "Sophia"
# ...all leagues with a (current) player named "Sophia"
# ...everyone with the last name "Flores" who DOESN'T (currently) play for the Washington Roughriders
# ...all teams, past and present, that Samuel Evans has played with
# ...all players, past and present, with the Manitoba Tiger-Cats
# ...all players who were formerly (but aren't currently) with the Wichita Vikings
# ...every team that Jacob Gray played for before he joined the Oregon Colts
# ...everyone named "Joshua" who has ever played in the Atlantic Federation of Amateur Baseball Players
# ...all teams that have had 12 or more players, past and present. (HINT: Look up the Django annotate function.)
# ...all players, sorted by the number of teams they've played for
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
