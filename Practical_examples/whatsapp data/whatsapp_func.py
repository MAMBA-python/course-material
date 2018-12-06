# Cleaning WhatsApp log
import os
import re
import pandas as pd
import numpy as np
import zipfile


def read_whatsapp(whatsapp_file, pattern=None, ):
    """
    read a whatsapp data file into a pandas dataframe

    Parameters
    ----------
    whatsapp_file: str
        path of the exported data from Whatsapp, can be a .zip or .txt file

    pattern: _sre.SRE_Pattern
        a compiled regular expression used to find the date format

    Returns
    -------
    time_user_df: pandas.DataFrame
        DataFrame with all the data from you whatsapp conversation
    """

    if whatsapp_file.endswith('.zip'):
        whatsapp_txt = unzip_whatsapp_file(whatsapp_file)
    else:
        whatsapp_txt = whatsapp_file

    # define regulare expressions
    pattern_en = re.compile('(\[\d\d\/\d\d\/\d\d\d\d, \d\d:\d\d:\d\d\])\s+(.+)')
    pattern_nl = re.compile('(\[\d\d\-\d\d\-\d\d \d\d:\d\d:\d\d\])\s+(.+)')
    group_pattern_en = 'Messages to this group are now secured with end-to-end encryption'
    group_pattern_nl = 'Berichten en oproepen in deze chat zijn nu beveiligd met end-to-end encryptie'

    # find usernames
    user_names = []
    datetime_list = []
    user_list = []
    text_list = []
    with open(whatsapp_txt, 'r', encoding="utf8") as fo:
        line = fo.readline()
        if group_pattern_en in line:
            pattern = re.compile('(\[\d\d\/\d\d\/\d\d\d\d, \d\d:\d\d:\d\d\])\s+(.+)')
            print('recognised English file format')
            for i in range(2):
                fo.readline()

        elif group_pattern_nl in line:
            pattern = re.compile('(\[\d\d\-\d\d\-\d\d \d\d:\d\d:\d\d\])\s+(.+)')
            print('recognised Dutch file format')
            for i in range(2):
                fo.readline()

        for line in fo:
            pattern_match = pattern.search(line)
            if pattern_match and ':' in pattern_match.group(2):
                user_name = pattern_match.group(2).split(':')[0]
                if user_name not in user_names:
                    user_names.append(user_name)
                user_list.append(user_name)
                datetime_list.append(pattern_match.group(1)[1:-1])
                text_list.append(":".join(pattern_match.group(2).split(':')[1:]))
            else:
                text_list[-1] = text_list[-1] + line

    time_user_df = pd.DataFrame(data={'user': user_list,
                                      'text': text_list,
                                      'message': [1] * len(user_list)},
                                index=pd.to_datetime(datetime_list, dayfirst=True))

    return time_user_df


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
    zip_ref.extractall(os.path.split(whatsapp_file)[0])
    zip_ref.close()

    zip_dir = os.path.split(whatsapp_file)[0]

    return os.path.join(zip_dir, '_chat.txt')
