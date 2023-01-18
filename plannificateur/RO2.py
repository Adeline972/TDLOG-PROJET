import data
import database
import tools

def planning(nb_packages, activity_field):
    planning = tools.dict_creation()
    nb_post = tools.nb_post()
    nb_interim = []

    for post in range (0, nb_post):
        time_needed = tools.time_needed_post(nb_packages, activity_field, post)
        nb_operators_needed_post = 0
        while time_needed > 0 :
            time_needed = time_needed - 7
            nb_operators_needed_post += 1

        nb_operators_post = 0
        for p in tools.persons_available_post():
            nb_operators_post += 1

        if nb_operators_needed_post > nb_operators_post * 5 :
            nb_interim_post = nb_operators_needed_post - nb_operators_post * 5
            nb_interim.append(nb_interim_post)
        else :
            nb_interim.append(0)

        if nb_operators_needed_post > 2*6*data.nb_max_team:
            nb_operators_night = nb_operators_needed - 2*6 * data.nb_max_team
            nb_operators_needed = 2*6* data.nb_max_team

        for j in range(0, 6):
            day = data.week[j]
            for k in range(0,2):
                team = data.team[k]
                planning["{}".format(day)]["{}".format(team)]["{}".format(post)] = nb_operators_needed//12
        for j in range(nb_operators_needed%12):
            day = data.week[j]
            for k in range(0, 2):
                team = data.team[k]
                planning["{}".format(day)]["{}".format(team)]["{}".format(post)] += 1

        for j in range(0, 6):
            day = data.week[j]
            team = data.team[2]
            planning["{}".format(day)]["{}".format(team)]["{}".format(post)] = nb_operators_night // 6

        for j in range(nb_operators_night%6):
            day = data.week[j]
            team = data.team[2]
            planning["{}".format(day)]["{}".format(team)]["{}".format(post)] += 1

    nb_operators = tools.total_operators()
    print(planning)
    return (planning, nb_interim, nb_operators)


