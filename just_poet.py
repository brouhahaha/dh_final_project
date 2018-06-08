import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import json

def draw_just_writers(dic):
    print('hi')
    f_periods = {'1150':[], '1200':[], '1250':[], '1300':[], '1350':[], '1400':[], '1450':[], '1500':[], '1550':[], '1600':[], '1650':[], '1700':[], '1750':[], '1800':[], '1850':[], '1900':[], '1950':[], '2000':[]}
    m_periods = {'1150':[], '1200':[], '1250':[], '1300':[], '1350':[], '1400':[], '1450':[], '1500':[], '1550':[], '1600':[], '1650':[], '1700':[], '1750':[], '1800':[], '1850':[], '1900':[], '1950':[], '2000':[]}
    periods = {'1150':'1150', '1200':'1200', '1250':'1250', '1300':'1300', '1350':'1350', '1400':'1400', '1450':'1450', '1500':'1500', '1550':'1550', '1600':'1600', '1650':'1650', '1700':'1700', '1750':'1750', '1800':'1800', '1850':'1850', '1900':'1900', '1950':'1950', '2000':'2000'}
    fem = {}
    masc = {}
    for k in dic:
        if dic[k]['occupationLabel']=='писатель' or dic[k]['occupationLabel']=='автор' or dic[k]['occupationLabel']=='поэт' or dic[k]['occupationLabel']=='детский писатель' or dic[k]['occupationLabel']=='писатель-фантаст' and dic[k]['sexLabel'] and dic[k]['death_year']:
            print('ei')
            if dic[k]['sexLabel'] == 'женский пол':
                key_year = int(dic[k]['death_year'])-int(dic[k]['death_year'])%50
                f_periods[key_year] += 1
            if dic[k]['sexLabel'] == 'мужской пол':
                m_periods[key_year] += 1

    final = {'periods': periods, 'fem': f_periods, 'masc': m_periods}
    df = pd.DataFrame(final)
    print(df)
    df_fin = pd.melt(df, id_vars='periods', var_name='sex', value_name='poets')

    ax = sns.factorplot(x="periods", y="poets", hue='sex', data=df_fin, kind="bar", size=6, aspect=2, legend_out=False)
    ax.set_axis_labels("period", "number")
    ax.set_xticklabels(rotation=90)
    plt.tight_layout()

    plt.savefig('just_writers.png', format='png')
    plt.show()
            
def main():
    with open('new_results.json', 'r', encoding='utf-8') as f:
        dict = json.loads(f.read())
    draw_just_writers(dict)

if __name__ == '__main__':
    main()
