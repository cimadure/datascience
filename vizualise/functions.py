def split_job(df, column='job', title='title', company='company'):
    return df[column].str.split(' at ', expand=True, n=1).rename(columns={0: title, 1: company})


def count_column(df, column='company'):
    return df[column].value_counts(ascending=False, dropna=True)
