from typing import List
import random

from .shuffle_v4 import statistical_shuffle


def big_data_api_shuffle(deck_size, test_num, error):
    _, _, _, optimal_series = statistical_shuffle(deck_size, test_num, error)
    return optimal_series
    

def api_suffle(series: List[any]) -> List[any]:
    optimal_series = big_data_api_shuffle(len(series), 7, 0.5)
    return [series[opt-1] for opt in optimal_series]


def insert_item(series: List[any], item: any) -> None:
    # toss (0/1) 0 = left, 1 = right
    toss = random.choice([0, 1])
    
    # shuffle current series
    shuffled_series= api_suffle(series)
    
    # pick the first value
    first = shuffled_series[0]
    
    #find the position to insert
    pos = series.index(first) + toss
    
    #insert the data
    series.insert(pos, item)
    
    

def final_shuffle(series: List[any], n, r) -> List[any]:    
    # Shuffle series using the right shuffle function
    shuffled_series = api_suffle(series)
    
    # select the first n values as your set
    items = shuffled_series[:n]
    
    # shuffle the set
    shuffled_items = api_suffle(items)
    
    # Insert the first data item to the result
    res = [shuffled_items[0]]
    
    # Iterate through each data one by one and insert using the rule described above
    # Skip the first value since it is trivialy inserted in the result above
    for idx in range(1, r):
        # Get the item at that index
        item = shuffled_items[idx]
        
        # call the insert function for each data point that implements the above logic
        insert_item(res, item)
    
    return items, res