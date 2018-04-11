import pandas as pd

csv_data = pd.read_csv('emails.csv', index_col=False, header=0)

general_words_list = ['info', 'support', 'team', 'contact', 'careers', 'finance']

general_emails = []
personal_emails = []


def classify_emails():
    for row in csv_data.itertuples():

        get_email = row.Email
        get_email_lower = get_email.lower()

        for i in general_words_list:

            try:
                if len(row) == 0:
                    continue
                else:
                    if -1 != get_email_lower.find(i):
                        general_emails.append(get_email_lower)

            except ValueError:
                print('No result')
                continue
        if get_email_lower not in general_emails:
            personal_emails.append(get_email_lower)
    classified_csv()


def classified_csv():

    df1 = pd.DataFrame(general_emails, columns=['General'])
    df2 = pd.DataFrame(personal_emails, columns=['Personal'])
    df1.reset_index(drop=False)
    df2.reset_index(drop=False)
    df = pd.concat([df1, df2], axis=1)
    # df.dropna()
    df.drop_duplicates(inplace=True)
    df.index = df.index + 1
    df.to_csv('classified_emails.csv')
    return df


classify_emails()