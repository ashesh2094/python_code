import json

with open("covid_19.json") as c:
    data = json.load(c)

global dates, confirmed_cases_week, death_cases_week, recovered_cases_week

confirmed_cases_week=[]
death_cases_week=[]
recovered_cases_week=[]
cd=[]
dd=[]
rd=[]

def eachday_analysis(i):
    confirmed_cases = 0
    death_cases = 0
    recovered_cases = 0
    for key, value in data.items():
        for index in range(len(value)):
            if index == i:
                confirmed_cases += value[index]["confirmed"]
                death_cases += value[index]["deaths"]
                recovered_cases += value[index]["recovered"]

    confirmed_cases_week.append(confirmed_cases)
    death_cases_week.append(death_cases)
    recovered_cases_week.append(recovered_cases)
    return confirmed_cases, death_cases, recovered_cases

def week_analysis():
    total_weekly_cases = 0

    for i in range(0, len(confirmed_cases_week), 7):
        cc = (confirmed_cases_week[i:i + 7])
        dc = (death_cases_week[i:i + 7])
        rc= (recovered_cases_week[i:i + 7])
        cd.append(cc)
        dd.append(dc)
        rd.append(rc)
    for n in range(len(cd)):
        print("Week ", n + 1, ": \n=============== \n Confirmed cases are: ", sum(cd[n]),"\n Death Cases Are: ",sum(dd[n]),"\n recovered cases are: ",sum(rd[n]),"\n==============")

    return total_weekly_cases

def weekly_max(j):
    highest = 0
    for key, value in data.items():
        for index in range(len(value)):
            if index == i:
                if (highest < value[index]["confirmed"]):
                    highest = value[index]["confirmed"]
                    print("highest :", confirmed_cases_week,"-",key ,"-", highest)
    return highest

for i in range(len(data["Thailand"])):
    d=eachday_analysis(i)
    h=weekly_max(j)
wc=week_analysis()


