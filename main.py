import pandas as pd
from data_utils.duplication import DfCounter


if __name__ == '__main__':
    test_df = pd.DataFrame(data=[
        ['A', 'a', 'x', 1],
        ['A', 'b', 'x', 1],
        ['A', 'c', 'x', 1],
        ['B', 'a', 'x', 1],
        ['B', 'b', 'x', 1],
        ['B', 'c', 'x', 1],
        ['A', 'a', 'y', 1],
    ],
        columns=['col1', 'col2', 'col3', 'col4']
    )
    test_cols = ['col1']
    counter = DfCounter(test_df, test_cols)

    print(counter.duplicates_stats())

