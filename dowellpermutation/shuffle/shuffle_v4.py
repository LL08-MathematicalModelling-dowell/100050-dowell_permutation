import random
import numpy as np



# Function to split the deck into N/30 and N/2 different parts
def cut_specs(deck):
    if len(deck) < 2:
        return [deck]
    
    if len(deck) > 60:
        cut_num = int(len(deck) / 30)
    else:
        cut_num = int(len(deck) / 2)

    cut_len = int(np.floor(len(deck) / cut_num))
    splits = []
    
    for start in range(0, len(deck), cut_len):
        splits.append(deck[start:start + cut_len])

    return splits


# Function to perform the ruffle
def ruffle(sample):
    mid = len(sample) // 2
    
    left = sample[:mid]
    right = sample[mid:]
    
    random.shuffle(left)
    random.shuffle(right)
    
    return left + right


# Function to rearrange the cuts into the deck using a random sequence
def results(samples):
    sequence = list(range(len(samples)))
    random.shuffle(sequence)
    
    result = []
    
    for i in sequence:
        result += samples[i]
    
    return result


# Function to compile the complete process of shuffle based on the procedure
# First, the deck is ruffled, then it is divided into multiple stacks, and the stacks are rearranged randomly
def compile(deck, test_num):
    curr_deck = deck
    for i in range(test_num):
        ruffeled_deck = ruffle(curr_deck)
        splited_deck = cut_specs(ruffeled_deck)
        result = results(splited_deck)
        curr_deck = result

    return curr_deck

# Function to calculate the rolling mean of an array
def rolling_mean(arr, window=10):
    return np.convolve(arr, np.ones(window), 'valid') / window

# Function to determine if a sample mean is an outlier
def is_outlier(mean, mean_, standard_deviation, error):
    return mean > mean_ + error * standard_deviation or mean < mean_ - error * standard_deviation


# Function to count outliers
def count_outliers(rolling_means, mean_, standard_deviation, error):
    outliers = 0
    for mean in rolling_means:
        if is_outlier(mean, mean_, standard_deviation, error):
            outliers += 1
    return outliers


# Function to calculate series_df
def calculate_series_df(deck_size, test_num, number_of_tries = 15):
    curr_deck = list(range(1, deck_size + 1))
    
    for i in range(number_of_tries):
        result = compile(curr_deck, test_num)
        if i == 0:
            series_df = np.array(result)
        else:
            series_df = np.vstack((series_df, result))
            
    return series_df
            
            
# Function to calculate the rolling mean of the series_df in numpy
def calculate_rolling_mean(series_df, window=10):
    return np.apply_along_axis(rolling_mean, 1, series_df, window)

# Function to find and return the optimal series in numpy (ie. the series with the least outliers)
def calculate_num_outliers(rolling_means, mean, standard_deviation, error):
    return np.apply_along_axis(count_outliers, 1, rolling_means, mean, standard_deviation, error)


def find_optimal_series(series_df, mean_df, outliers):
    idx = np.argmin(outliers)
    return series_df[idx], mean_df[idx]


def statistical_shuffle(deck_size, test_num, error, number_of_tries = 15):
    # set the window size for the rolling mean
    window = 50 if deck_size > 50 else max(1, deck_size // 2)
    
    # Calculate the series_df
    series_df = calculate_series_df(deck_size, test_num, number_of_tries)
    
    # Calculate the mean and standard deviation of the series_df
    mean_ = (deck_size + 1) / 2
    standard_deviation = np.std(list(range(1, deck_size + 1))) / np.sqrt(window)
    
    # Calculate the rolling mean of the series_df
    rolling_means = calculate_rolling_mean(series_df, window)
    
    # Caluclate number of outliers for each series
    outliers = calculate_num_outliers(rolling_means, mean_, standard_deviation, error)
    
    # Find the optimal series
    optimal_series, optimal_means = find_optimal_series(series_df, rolling_means, outliers)
    
    # Plot the optimal serie
    
    # return the final results
    return series_df.tolist(), rolling_means.tolist(), outliers.tolist(), optimal_series.tolist()

    
def process_request(
    deck_size,
    test_num,
    error,
    optimal_only=False
):
    # Perform your logic using the parameters
    series_df, rolling_means, outliers, optimal_series, plot_html = statistical_shuffle(deck_size, test_num, error)

    if optimal_only:
        # Return only the optimal series and the plot
        return {
            'optimal_series': optimal_series,
        }
    
    return {
        'series_df': series_df,
        'mean_df': rolling_means,
        'outliers': outliers,
        'optimal_series': optimal_series,
        'plot_html': plot_html
    }