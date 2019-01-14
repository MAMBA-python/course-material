import os
import re
import pandas as pd
import numpy as np
import zipfile



def strftime_to_re_pattern(strftime_format):
    re_pattern = strftime_format.replace('%d', '\\d\\d')
    re_pattern = re_pattern.replace('%m', '\\d\\d')
    re_pattern = re_pattern.replace('%Y', '\\d\\d\\d\\d')
    re_pattern = re_pattern.replace('%H', '\\d\\d')
    re_pattern = re_pattern.replace('%M', '\\d\\d')
    re_pattern = re_pattern.replace('%S', '\\d\\d')
    re_pattern = re_pattern.replace('/', '\\/')
    re_pattern = re_pattern.replace('[', '\\[')
    re_pattern = re_pattern.replace(']', '\\]')
    re_pattern = '(' + re_pattern + ')'

    return re_pattern

def read_whatsapp(whatsapp_file, datetime_pattern = '(\[\d\d\/\d\d\/\d\d\d\d, \d\d:\d\d:\d\d\])',
                  user_sep=':', strftime_format = '[%d/%m/%Y, %H:%M:%S]',
                  encoding="utf8"):
    """
    read a whatsapp data file into a pandas dataframe

    Parameters
    ----------
    whatsapp_file: str
        path of the exported data from Whatsapp, can be a .zip or .txt file

    Returns
    -------
    time_user_df: pandas.DataFrame
        DataFrame with all the data from you whatsapp conversation
    """

    #check file type
    if whatsapp_file.endswith('txt'):
        whatsapp_txt = whatsapp_file
    elif whatsapp_file.endswith('.zip'):
        whatsapp_txt = unzip_whatsapp_file(whatsapp_file)
    else:
        raise FileNotFoundError('could not open file: %s'%whatsapp_file)

    re_datetime = re.compile(datetime_pattern)
    datetimeuser_pattern = datetime_pattern + '(.*?)' + user_sep
    re_datetimeuser = re.compile(datetimeuser_pattern)

    with open(whatsapp_txt, 'r', encoding=encoding) as fo:
        line = fo.readline()
        check_date_pattern(line, re_datetime)
        check_date_user_pattern(line, re_datetimeuser)

        re_datetimeuser.split(line)

        empty, date, user, message = re_datetimeuser.split(line)
        datetime_list = [date]
        user_list = [user]
        message_list = [message]

        for line in fo:
            pattern_match = re_datetimeuser.search(line)
            if pattern_match:
                empty, date, user, message = re_datetimeuser.split(line)
                datetime_list.append(date)
                user_list.append(user)
                message_list.append(message)
            else:
                message_list[-1] = message_list[-1] + line

    time_user_df = pd.DataFrame(data={'datetime': datetime_list,
                                      'user': user_list,
                                      'text': message_list,
                                      'message': [1] * len(user_list)}, )

    time_user_df.index = pd.to_datetime(time_user_df.datetime,
                                        format=strftime_format, dayfirst=True)

    return time_user_df


def check_date_pattern(line, re_datetime):
    if re_datetime.search(line):
        print('date pattern recognized')
    else:
        raise ValueError('pattern not recgonized')


def check_date_user_pattern(line, re_datetimeuser):
    if re_datetimeuser.search(line):
        print('user separator recognized')
    else:
        raise ValueError('pattern not recgonized')


def check_anonymized_dataset(time_user_df):
    """
    check if a pandas dataframe is an anonymized dataset. If so a KeyError is raised.

    Parameters
    ----------
    time_user_df

    Returns
    -------


    """
    if 'text' not in time_user_df.columns:
        print('making a wordcload only works with a dataset in which the text is included.')
        print('Therefore it does not work on anonymized datasets')
        raise KeyError('working with anonymised dataset')


def unzip_whatsapp_file(whatsapp_file):
    """
    unzips a whatsapp .zip file and returns the path of the _chat.txt file that was extracted from the zip

    Parameters
    ----------
    whatsapp_file: str
        path to a .zip file with the exported data from Whatsapp.

    Returns
    -------
    str
    path to the _chat.txt file that was extracted from the .zip

    """

    zip_ref = zipfile.ZipFile(whatsapp_file, 'r')
    txt_file = zip_ref.namelist()[0]
    zip_ref.extractall(os.path.split(whatsapp_file)[0])
    zip_ref.close()

    zip_dir = os.path.split(whatsapp_file)[0]

    return os.path.join(zip_dir, txt_file)
