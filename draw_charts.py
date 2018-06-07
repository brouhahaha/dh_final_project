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
    musor = ['автор', 'проза', 'драматургия', 'писатель', 'поэт', 'автор дневника', 'публицистика', 'мемуарист', 'автобиограф', 'писатель-фантаст']
    ys = [occup[n] for n in occup if occup[n] > 5 and n != 'писатель' and n != 'поэт']
    xs = [n for n in occup if occup[n] > 5 and n != 'писатель' and n != 'поэт']
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
    f = {n: fem[n] for n in fem if fem[n] > 5 and n != 'писатель' and n != 'поэт'}
    m = {n: masc[n] for n in masc if masc[n] > 5 and n != 'писатель' and n != 'поэт'}
    occupation_m = {n: n for n in masc if masc[n] > 5 and n != 'писатель' and n != 'поэт'}
    occupation_f = {n: n for n in fem if fem[n] > 5 and n != 'писатель' and n != 'поэт'}
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


def main():
    with open('results.json', 'r', encoding='utf-8') as f:
        dict = json.loads(f.read())
    #count_all(dict)
    draw_gender(dict)
    draw_lang_gen(dict)
    #draw_all_lang(dict)

if __name__ == '__main__':
    main()