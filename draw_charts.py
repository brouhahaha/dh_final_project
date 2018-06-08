import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import json


##общий график профессий
def count_all(dic):
    occup = {}
    for k in dic:
        if dic[k]['occupationLabel']:
            for i in dic[k]['occupationLabel']:
                if i in occup:
                    occup[i] += 1
                else:
                    occup[i] = 1
    musor = ['автор', 'проза', 'драматургия', 'писатель', 'поэт', 'автор дневника', 'публицистика', 'мемуарист',
             'автобиограф', 'писатель-фантаст', 'детский писатель', 'романист', 'биограф', 'прозаик', 'эссеист',
             'новеллист', 'поэт-песенник']
    ys = [occup[n] for n in occup if occup[n] > 5 and n not in musor]
    xs = [n for n in occup if occup[n] > 5 and n not in musor]
    df = pd.DataFrame(dict(x=xs, y=ys))
    ax = sns.factorplot("x", "y", data=df, kind="bar", palette=sns.cubehelix_palette(100), size=6, aspect=2, legend_out=False)
    ax.set_axis_labels("occupation", "number")
    ax.set_xticklabels(rotation=90)
    plt.tight_layout()

    plt.savefig('occup_all.png', format='png')
    plt.show()


##общий график для языков
def draw_all_lang(dic):
    lang = {}
    for k in dic:
        if dic[k]['langLabel']:
            for i in dic[k]['langLabel']:
                if i in lang:
                    lang[i] += 1
                else:
                    lang[i] = 1

    ys = [lang[n] for n in lang if n != 'русский язык']
    xs = [n for n in lang if n != 'русский язык']
    df = pd.DataFrame(dict(x=xs, y=ys))
    ax = sns.factorplot("x", "y", data=df, kind="bar", palette=sns.cubehelix_palette(103), size=6, aspect=2,
                        legend_out=False)
    ax.set_axis_labels("language", "number")
    ax.set_xticklabels(rotation=90)
    plt.tight_layout()

    plt.savefig('lang_all.png', format='png')
    plt.show()


##рисуем график языка от пола
def draw_lang_gen(dic):
    print('hei')
    fem = {}
    masc = {}
    for k in dic:
        if dic[k]['langLabel'] and dic[k]['sexLabel']:
            if dic[k]['sexLabel'] == 'женский пол':
                for i in dic[k]['langLabel']:
                    if i in fem:
                        fem[i] += 1
                    else:
                        fem[i] = 1
            else:
                for i in dic[k]['langLabel']:
                    if i in masc:
                        masc[i] += 1
                    else:
                        masc[i] = 1
    f = {n: fem[n] for n in fem if n != 'русский язык'}
    m = {n: masc[n] for n in masc if n != 'русский язык'}
    occupation_m = {n: n for n in masc if n != 'русский язык'}
    occupation_f = {n: n for n in fem if n != 'русский язык'}
    oc_fin = {}
    for k in occupation_f:
        if k not in oc_fin:
            oc_fin[k] = k
    for k in occupation_m:
        if k not in oc_fin:
            oc_fin[k] = k

    final = {'occ': oc_fin, 'fem': f, 'masc': m}
    df = pd.DataFrame(final)
    df_fin = pd.melt(df, id_vars='occ', var_name='sex', value_name='occupations')

    ax = sns.factorplot(x="occ", y="occupations", hue='sex', data=df_fin, kind="bar", size=6, aspect=2, legend_out=False)
    ax.set_axis_labels("language", "number")
    ax.set_xticklabels(rotation=90)
    plt.tight_layout()

    plt.savefig('lang_sex.png', format='png')
    plt.show()


##рисуем график профессий от пола
def draw_gender(dic):
    print('hei')
    fem = {}
    masc = {}
    for k in dic:
        if dic[k]['occupationLabel'] and dic[k]['sexLabel']:
            if dic[k]['sexLabel'] == 'женский пол':
                for i in dic[k]['occupationLabel']:
                    if i in fem:
                        fem[i] += 1
                    else:
                        fem[i] = 1
            else:
                for i in dic[k]['occupationLabel']:
                    if i in masc:
                        masc[i] += 1
                    else:
                        masc[i] = 1
    musor = ['автор', 'проза', 'драматургия', 'писатель', 'поэт', 'автор дневника', 'публицистика', 'мемуарист',
             'автобиограф', 'писатель-фантаст', 'детский писатель', 'романист', 'биограф', 'прозаик', 'эссеист',
             'новеллист', 'поэт-песенник']
    f = {n: fem[n] for n in fem if fem[n] > 5 and n not in musor}
    m = {n: masc[n] for n in masc if masc[n] > 5 and n not in musor}
    occupation_m = {n: n for n in masc if masc[n] > 5 and n not in musor}
    occupation_f = {n: n for n in fem if fem[n] > 5 and n not in musor}
    oc_fin = {}
    for k in occupation_f:
        if k not in oc_fin:
            oc_fin[k] = k
    for k in occupation_m:
        if k not in oc_fin:
            oc_fin[k] = k

    final = {'occ': oc_fin, 'fem': f, 'masc': m}
    df = pd.DataFrame(final)
    df_fin = pd.melt(df, id_vars='occ', var_name='sex', value_name='occupations')

    ax = sns.factorplot(x="occ", y="occupations", hue='sex', data=df_fin, kind="bar", size=6, aspect=2, legend_out=False)
    ax.set_axis_labels("occupation", "number")
    ax.set_xticklabels(rotation=90)
    plt.tight_layout()

    plt.savefig('occup_sex.png', format='png')
    plt.show()



def draw_occ_time(dic):
    #time_per = {'1200':'1200', '1300':'1300', '1450':'1450', '1550':'1550', '1600':'1600', '1650':'1650', '1700':'1700', '1750':'1750', '1800':'1800',
    #                      '1850':'1850', '1900':'1900', '1950':'1950', '2000':'2000', '2050':'2050'}
    time_per = {'1750':'1700-1750', '1800':'1750-1800',
                          '1850':'1800-1850', '1900':'1850-1900', '1950':'1900-1950', '2000':'1950-2000', '2050':'2000-2050'}
    occupation = {}
    for k in dic:
        if dic[k]['death_year'] and dic[k]['occupationLabel']:
            death = int(dic[k]['death_year'])
            t = 0
            if death < 1200:
                t = 1200
            elif death < 1300:
                t = 1300
            elif death < 1450:
                t = 1450
            elif death < 1550:
                t = 1550
            elif death < 1600:
                t = 1600
            elif death < 1650:
                t = 1650
            elif death < 1700:
                t = 1700
            elif death < 1750:
                t = 1750
            elif death < 1800:
                t = 1800
            elif death < 1850:
                t = 1850
            elif death < 1900:
                t = 1900
            elif death < 1950:
                t = 1950
            elif death < 2000:
                t = 2000
            else:
                t = 2050
            for occ in dic[k]['occupationLabel']:
                if occ in occupation:
                    if str(t) in occupation[occ]:
                        occupation[occ][str(t)] += 1
                    else:
                        occupation[occ][str(t)] = 1
                else:
                    occupation[occ] = {}
                    occupation[occ][str(t)] = 1
    new_d = {'time_period':time_per}
    #print(occupation)
    musor = ['автор', 'проза', 'драматургия', 'писатель', 'поэт', 'автор дневника', 'публицистика', 'мемуарист',
             'автобиограф', 'писатель-фантаст', 'детский писатель', 'романист', 'биограф', 'прозаик', 'эссеист',
             'новеллист', 'поэт-песенник']
    for occ in occupation:
        if len(occupation[occ]) > 5 and occ not in musor:
            new_d[occ] = occupation[occ]
    df = pd.DataFrame(new_d)
    #print(df)
    df_f = pd.melt(df, id_vars='time_period', var_name='occupation', value_name='number')
    #print(df_f)

    ax = sns.factorplot(x="time_period", y="number", hue='occupation', data=df_f, kind="bar", size=6, aspect=2, legend_out=False)
    ax.set_axis_labels("occupation", "number")
    #ax.set_xticklabels(rotation=90)
    plt.tight_layout()

    plt.savefig('occup_time.png', format='png')
    plt.show()


def draw_lang_time(dic):
    #time_per = {'1200':'1200', '1300':'1300', '1450':'1450', '1550':'1550', '1600':'1600', '1650':'1650', '1700':'1700', '1750':'1750', '1800':'1800',
    #                      '1850':'1850', '1900':'1900', '1950':'1950', '2000':'2000', '2050':'2050'}
    time_per = {'1800':'1750-1800', '1850':'1800-1850', '1900':'1850-1900', '1950':'1900-1950', '2000':'1950-2000', '2050':'2000-2050'}
    occupation = {}
    for k in dic:
        if dic[k]['death_year'] and dic[k]['langLabel']:
            death = int(dic[k]['death_year'])
            t = 0
            if death < 1200:
                t = 1200
            elif death < 1300:
                t = 1300
            elif death < 1450:
                t = 1450
            elif death < 1550:
                t = 1550
            elif death < 1600:
                t = 1600
            elif death < 1650:
                t = 1650
            elif death < 1700:
                t = 1700
            elif death < 1750:
                t = 1750
            elif death < 1800:
                t = 1800
            elif death < 1850:
                t = 1850
            elif death < 1900:
                t = 1900
            elif death < 1950:
                t = 1950
            elif death < 2000:
                t = 2000
            else:
                t = 2050
            for occ in dic[k]['langLabel']:
                if occ in occupation:
                    if str(t) in occupation[occ]:
                        occupation[occ][str(t)] += 1
                    else:
                        occupation[occ][str(t)] = 1
                else:
                    occupation[occ] = {}
                    occupation[occ][str(t)] = 1
    new_d = {'time_period':time_per}
    #print(occupation)
    for occ in occupation:
        if len(occupation[occ]) > 3 and occ != 'русский язык':
            new_d[occ] = occupation[occ]
    df = pd.DataFrame(new_d)
    print(df)
    df_f = pd.melt(df, id_vars='time_period', var_name='occupation', value_name='number')
    #print(df_f)

    ax = sns.factorplot(x="time_period", y="number", hue='occupation', data=df_f, kind="bar", size=6, aspect=2, legend_out=False)
    ax.set_axis_labels("occupation", "number")
    #ax.set_xticklabels(rotation=90)
    plt.tight_layout()

    plt.savefig('lang_time.png', format='png')
    plt.show()


def draw_occ_men(dic):
    #time_per = {'1200':'1200', '1300':'1300', '1450':'1450', '1550':'1550', '1600':'1600', '1650':'1650', '1700':'1700', '1750':'1750', '1800':'1800',
    #                      '1850':'1850', '1900':'1900', '1950':'1950', '2000':'2000', '2050':'2050'}
    time_per = {'1750':'1700-1750', '1800':'1750-1800',
                          '1850':'1800-1850', '1900':'1850-1900', '1950':'1900-1950', '2000':'1950-2000', '2050':'2000-2050'}
    occupation = {}
    for k in dic:
        if dic[k]['death_year'] and dic[k]['occupationLabel'] and dic[k]['sexLabel'] == 'мужской пол':
            death = int(dic[k]['death_year'])
            t = 0
            if death < 1200:
                t = 1200
            elif death < 1300:
                t = 1300
            elif death < 1450:
                t = 1450
            elif death < 1550:
                t = 1550
            elif death < 1600:
                t = 1600
            elif death < 1650:
                t = 1650
            elif death < 1700:
                t = 1700
            elif death < 1750:
                t = 1750
            elif death < 1800:
                t = 1800
            elif death < 1850:
                t = 1850
            elif death < 1900:
                t = 1900
            elif death < 1950:
                t = 1950
            elif death < 2000:
                t = 2000
            else:
                t = 2050
            for occ in dic[k]['occupationLabel']:
                if occ in occupation:
                    if str(t) in occupation[occ]:
                        occupation[occ][str(t)] += 1
                    else:
                        occupation[occ][str(t)] = 1
                else:
                    occupation[occ] = {}
                    occupation[occ][str(t)] = 1
    new_d = {'time_period':time_per}
    #print(occupation)
    musor = ['автор', 'проза', 'драматургия', 'писатель', 'поэт', 'автор дневника', 'публицистика', 'мемуарист',
             'автобиограф', 'писатель-фантаст', 'детский писатель', 'романист', 'биограф', 'прозаик', 'эссеист',
             'новеллист', 'поэт-песенник']
    for occ in occupation:
        if len(occupation[occ]) > 5 and occ not in musor:
            new_d[occ] = occupation[occ]
    df = pd.DataFrame(new_d)
    #print(df)
    df_f = pd.melt(df, id_vars='time_period', var_name='occupation', value_name='number')
    #print(df_f)

    ax = sns.factorplot(x="time_period", y="number", hue='occupation', data=df_f, kind="bar", size=6, aspect=2, legend_out=False)
    ax.set_axis_labels("occupation", "number")
    #ax.set_xticklabels(rotation=90)
    plt.tight_layout()

    plt.savefig('occup_men_time.png', format='png')
    plt.show()

def draw_occ_women(dic):
    #time_per = {'1200':'1200', '1300':'1300', '1450':'1450', '1550':'1550', '1600':'1600', '1650':'1650', '1700':'1700', '1750':'1750', '1800':'1800',
    #                      '1850':'1850', '1900':'1900', '1950':'1950', '2000':'2000', '2050':'2050'}
    time_per = {'1850':'1800-1850', '1900':'1850-1900', '1950':'1900-1950', '2000':'1950-2000', '2050':'2000-2050'}
    occupation = {}
    for k in dic:
        if dic[k]['death_year'] and dic[k]['occupationLabel'] and dic[k]['sexLabel'] == 'женский пол':
            death = int(dic[k]['death_year'])
            t = 0
            if death < 1200:
                t = 1200
            elif death < 1300:
                t = 1300
            elif death < 1450:
                t = 1450
            elif death < 1550:
                t = 1550
            elif death < 1600:
                t = 1600
            elif death < 1650:
                t = 1650
            elif death < 1700:
                t = 1700
            elif death < 1750:
                t = 1750
            elif death < 1800:
                t = 1800
            elif death < 1850:
                t = 1850
            elif death < 1900:
                t = 1900
            elif death < 1950:
                t = 1950
            elif death < 2000:
                t = 2000
            else:
                t = 2050
            for occ in dic[k]['occupationLabel']:
                if occ in occupation:
                    if str(t) in occupation[occ]:
                        occupation[occ][str(t)] += 1
                    else:
                        occupation[occ][str(t)] = 1
                else:
                    occupation[occ] = {}
                    occupation[occ][str(t)] = 1
    new_d = {'time_period':time_per}
    #print(occupation)
    musor = ['автор', 'проза', 'драматургия', 'писатель', 'поэт', 'автор дневника', 'публицистика', 'мемуарист',
             'автобиограф', 'писатель-фантаст', 'детский писатель', 'романист', 'биограф', 'прозаик', 'эссеист',
             'новеллист', 'поэт-песенник']
    for occ in occupation:
        if len(occupation[occ]) > 2 and occ not in musor:
            new_d[occ] = occupation[occ]
    df = pd.DataFrame(new_d)
    #print(df)
    df_f = pd.melt(df, id_vars='time_period', var_name='occupation', value_name='number')
    #print(df_f)

    ax = sns.factorplot(x="time_period", y="number", hue='occupation', data=df_f, kind="bar", size=6, aspect=2, legend_out=False)
    ax.set_axis_labels("occupation", "number")
    #ax.set_xticklabels(rotation=90)
    plt.tight_layout()

    plt.savefig('occup_women_time.png', format='png')
    plt.show()


def main():
    with open('new_results.json', 'r', encoding='utf-8') as f:
        dict = json.loads(f.read())
    #count_all(dict)
    #draw_gender(dict)
    #draw_lang_gen(dict)
    #draw_all_lang(dict)
    #draw_occ_time(dict)
    #draw_lang_time(dict)
    #draw_occ_men(dict)
    draw_occ_women(dict)


if __name__ == '__main__':
    main()