from ggplot import *
import matplotlib.pyplot as plt
import numpy as np
import pandas
import scipy
import scipy.stats


# ex2.6
def entries_histogram(turnstile_weather, csv=False):
    '''
    plots two histograms on the same axes to show hourly entries when raining
    vs. when not raining.
	
    '''
    if csv:
        df = pandas.read_csv(turnstile_weather)
    else:
        df = turnstile_weather

    bins = 150
    alpha = 0.5
    xmin = ymin = 0
    xmax = 6000
    ymax = 45000

    plt.figure()

    df['ENTRIESn_hourly'][df['rain'] == 0].hist(bins=bins, alpha=alpha)
    df['ENTRIESn_hourly'][df['rain'] == 1].hist(bins=bins, alpha=alpha)

    plt.axis([xmin, xmax, ymin, ymax])
    plt.suptitle('Histogram of ENTRIESn_hourly')
    plt.xlabel('ENTRIESn_hourly')
    plt.ylabel('Frequency')
    plt.legend(['No rain', 'Rain'])

    return plt

# ps2.8
#def means(turnstile_weather)
def mann_whitney_plus_means(turnstile_weather, csv=False):
    '''
    consumes the turnstile_weather dataframe (or csv file), and returns:
        1) the mean of entries with rain
        2) the mean of entries without rain
        3) the Mann-Whitney U-statistic and p-value comparing the number
           of entries with rain and the number of entries without rain
    '''
    if csv:
        df = pandas.read_csv(turnstile_weather)
    else:
        df = turnstile_weather

    df_wet = df['ENTRIESn_hourly'][df['rain'] == 1] #  44104
    df_dry = df['ENTRIESn_hourly'][df['rain'] == 0] # 87847

    with_rain_mean = df_wet.mean()
    without_rain_mean = df_dry.mean()

    U, p = scipy.stats.mannwhitneyu(df_wet, df_dry)

    return with_rain_mean, without_rain_mean, U, p
if __name__ == '__main__':
    filename = 'turnstile_data_master_with_weather.csv'
    df = pandas.DataFrame.from_csv(filename)

     print "Histogram of turnstile data:"
     entries_histogram(filename, True)
     plt.show()
    raw_input("Press enter to continue...")

    print "Mann-Whitney U test:"
    print mann_whitney_plus_means(filename, csv=True)
    raw_input("Press enter to continue...")




