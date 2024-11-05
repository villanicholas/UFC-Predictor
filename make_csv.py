import pandas as pd


def main():
    # open data
    # @@ if updating data with the web crawler, change the filenames...
    fight_info = pd.read_csv("ufc-stats-crawler/data/fight_info/2019-12-11T15-15-57.csv")

    fighter_stats = pd.read_csv("ufc-stats-crawler/data/fighter_stats/2019-12-11T23-32-40.csv")

    print(fighter_stats.info())
    # first milestone: 
    # make a csv where each row is a fight 
    print(fight_info.info())

    merged_df = fight_info.merge(fighter_stats, left_on='fighter_1_id', right_on='fighter_id', how='left')

    merged_df = merged_df.rename(columns={'fighter_data': 'fighter_1_data'}).drop(columns=['fighter_id'])

    merged_df = merged_df.merge(fighter_stats, left_on='fighter_2_id', right_on='fighter_id', how='left')
    merged_df = merged_df.rename(columns={'fighter_data': 'fighter_2_data'}).drop(columns=['fighter_id'])

    merged_df.to_csv('out.csv', index=False)  # index=False omits row indices from the CSV
    print(merged_df.info)




"""
Current feature list
['date', 'B_fighter', 'R_fighter', 'Winner', 'B_current_lose_streak',
       'B_current_win_streak', 'B_longest_win_streak', 'B_losses',
       'B_total_rounds_fought', 'B_total_title_bouts',
       'B_win_by_Decision_Majority', 'B_win_by_Decision_Split',
       'B_win_by_Decision_Unanimous', 'B_win_by_KO_TKO', 'B_win_by_Submission',
       'B_win_by_TKO_Doctor_Stoppage', 'B_wins', 'B_Height_cms', 'B_Reach_cms',
       'B_Weight_lbs', 'B_age', 'B_Stance_Open_Stance', 'B_Stance_Orthodox',
       'B_Stance_Southpaw', 'B_Stance_Switch', 'R_current_lose_streak',
       'R_current_win_streak', 'R_longest_win_streak', 'R_losses',
       'R_total_rounds_fought', 'R_total_title_bouts',
       'R_win_by_Decision_Majority', 'R_win_by_Decision_Split',
       'R_win_by_Decision_Unanimous', 'R_win_by_KO_TKO', 'R_win_by_Submission',
       'R_win_by_TKO_Doctor_Stoppage', 'R_wins', 'R_Height_cms', 'R_Reach_cms',
       'R_Weight_lbs', 'R_age', 'R_Stance_Open_Stance', 'R_Stance_Orthodox',
       'R_Stance_Southpaw', 'R_Stance_Switch']
"""


if __name__ == '__main__':
    main()
