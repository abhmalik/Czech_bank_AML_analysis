import pandas as pd

def negative(tr_full, mode):

    neg_dict = {}
    neg_dict['latent_dim1'] = f"Looking at the amount and mode of transactions of this account in the last 4 month, deep learning model asses the combination of {tr_full.amount} CZK and mode of transaction '{mode}' to be normal."
    neg_dict['latent_dim2'] = f"Looking at the timing and amount of transactions of this account in the last 4 month, deep learning model asses the combination of {tr_full.amount} CZK and {tr_full.date.strftime('%d %b %y')} to be normal."
    neg_dict['latent_dim3'] = f"Looking at the amount and mode of transactions of this account in the last 4 month, deep learning model asses the combination of {tr_full.amount} CZK and mode of transaction '{mode}' to be normal."
    neg_dict['latent_dim4'] = f"Looking at the timing and amount of transactions of this account in the last 4 month, deep learning model asses the combination of {tr_full.amount} CZK and {tr_full.date.strftime('%d %b %y')} to be normal."

    neg_dict['common_amount_4m'] = f'{tr_full.amount} CZK is a common amount for this account.'
    neg_dict['reoccuring_trx_4m'] = f'A transaction of {tr_full.amount} CZK around this time of the month is common for this account.'
    neg_dict['ave_dist_same_amt_4m'] = f'The average amount of time spent between transactions of {tr_full.amount} CZK in last 4 months is {tr_full.ave_dist_same_amt_4m/(1-tr_full.ave_dist_same_amt_4m)}, not low for this account. Transactions of this amount are relatively frequent.'
    neg_dict['credit_txcount_last_month_vs_4months'] = f'Number of credit transactions processed in last month were usual for this account based on its perivous 4 month history.'
    neg_dict['debit_txcount_last_month_vs_4months'] = f'Number of debit transactions processed in last month were usual for this account based on its perivous 4 month history.'
    neg_dict['credit_vol_last_month_vs_4months'] = f'Total money credited within last month by similar transactions is normal for this account.'
    neg_dict['debit_vol_last_month_vs_4months'] = f'Total money debited within last month by similar transactions is normal for this account.'
    neg_dict['mean_credit_last_month_vs_4months'] = f'Average amount credited by similar transactions in the last month is normal for this account.'
    neg_dict['mean_debit_last_month_vs_4months'] = f'Average amount debited by similar transactions in the last month is normal for this account.'
    neg_dict['high_risk_trx_last_month_vs_4months'] = f'Number of high risk country transactions within last 1 month is normal for this account.'
    neg_dict['credit_from_high_risk_last_month_vs_avg_in_4months'] = f'Amount credited to high risk countries like {tr_full.counter_party}[0:2] in the last month is normal for this account.'
    neg_dict['debit_to_high_risk_last_month_vs_avg_in_4months'] = f'Amount credited to high risk countries like {tr_full.counter_party}[0:2] in last 4 months is normal for this account.'
    neg_dict['trcount_new_CP_vs_total_cp_4months'] = f'Number of transactions sent to new counter parties like {tr_full.counter_party} in last one month is usual for this account based on its history.'
    neg_dict['no_trx_high_risk_vs_total_trx1_months'] = f'{tr_full.no_trx_high_risk_vs_total_trx1_months/(1-tr_full.no_trx_high_risk_vs_total_trx1_months)}% of transactions were sent to high risk country in the last month. This is normal behaviour for this account.'
    neg_dict['no_trx_high_risk_vs_total_trx4_months'] = f'{tr_full.no_trx_high_risk_vs_total_trx4_months/(1-tr_full.no_trx_high_risk_vs_total_trx4_months)}% of transactions were sent to high risk country in last 4 months. This is normal behaviour for this account.'
    neg_dict['credit_from_high_risk_vs_avg_credit1_months'] = f'{tr_full.credit_from_high_risk_vs_avg_credit1_months/(1-tr_full.credit_from_high_risk_vs_avg_credit1_months)} of amount is credited to high risk country in the last month. This is normal behaviour for this account.'
    neg_dict['credit_from_high_risk_vs_avg_credit4_months'] = f'{tr_full.credit_from_high_risk_vs_avg_credit4_months/(1-tr_full.credit_from_high_risk_vs_avg_credit4_months)}% of amount is credited to high risk country in last 4 months. This is normal behaviour for this account.'
    neg_dict['debit_to_high_risk_vs_avg_debit1_months'] = f'{tr_full.debit_to_high_risk_vs_avg_debit1_months/(1-tr_full.debit_to_high_risk_vs_avg_debit1_months)}% of amount is debited to high risk country in last 1 month. This is normal behaviour for this account.'
    neg_dict['debit_to_high_risk_vs_avg_debit4_months'] = f'{tr_full.debit_to_high_risk_vs_avg_debit4_months/(1-tr_full.debit_to_high_risk_vs_avg_debit4_months)}% of amount is debited to high risk country in last 4 months. This is normal behaviour for this account.'
    neg_dict['no_trx_same_amt_vs_total_trx1_months'] = f'The ratio of number of transactions of {tr_full.amount} CZK vs total transactions in last month is {round(tr_full.no_trx_same_amt_vs_total_trx1_months/(1-tr_full.no_trx_same_amt_vs_total_trx1_months), 3)}, this is normal for this account.'
    neg_dict['no_trx_same_amt_vs_total_trx4_months'] = f'The ratio of number of transactions of {tr_full.amount} CZK vs total transactions in last 4 months is {round(tr_full.no_trx_same_amt_vs_total_trx1_months/(1-tr_full.no_trx_same_amt_vs_total_trx1_months), 3)}, this is normal for this account.'
    neg_dict['tx_amount_vs_avg_debit_CP_1_months'] = f'Transaction of {tr_full.amount} CZK sent to {tr_full.counter_party} is usual in last 1 month.'
    neg_dict['tx_amount_vs_avg_debit_CP_4_months'] = f'Transaction of {tr_full.amount} CZK sent to {tr_full.counter_party} is usual in last 4 months.'
    neg_dict['tx_amount_vs_avg_credit_CP_1_months'] = f'Transaction of {tr_full.amount} CZK received from {tr_full.counter_party} is usual in last 1 month.'
    neg_dict['tx_amount_vs_avg_credit_CP_4_months'] = f'Transaction of {tr_full.amount} CZK received from {tr_full.counter_party} is usual in last 4 months.'
    neg_dict['number_credit_CP_1_months'] = f'Number of credit transactions to {tr_full.counter_party} in last 1 month is usual.'
    neg_dict['number_credit_CP_4_months'] = f'Number of credit transactions to {tr_full.counter_party} in last 4 months is usual.'
    neg_dict['number_debit_CP_1_months'] = f'Number of debit transactions to {tr_full.counter_party} in last 1 month is usual.'
    neg_dict['number_debit_CP_4_months'] = f'Number of debit transactions to {tr_full.counter_party} in last 4 months is usual.'
    neg_dict['credit_vol_CP_1_months'] = f'Total money received from {tr_full.counter_party} in last 1 month is usual for this account.'
    neg_dict['credit_vol_CP_4_months'] = f'Total money received from {tr_full.counter_party} in last 4 months is usual for this account.'
    neg_dict['debit_vol_CP_1_months'] = f'Total money sent to {tr_full.counter_party} in last 1 month was usual for this account.'
    neg_dict['debit_vol_CP_4_months'] = f'Total money sent to {tr_full.counter_party} in last 4 months is usual for this account.'
    neg_dict['tr_amt_CP_vs_avg_credit_CP_1_months'] = f'Its normal  for this account to receive {tr_full.amount} CZK from {tr_full.counter_party} in the last month.'
    neg_dict['tr_amt_CP_vs_avg_credit_CP_4_months'] = f'Its normal  for this account to receive  {tr_full.amount} CZK from {tr_full.counter_party} based on its 4 months history.'
    neg_dict['tr_amt_CP_vs_avg_debit_CP_1_months'] = f'Its normal  for this account to send {tr_full.amount} CZK to {tr_full.counter_party} in the last month.'
    neg_dict['tr_amt_CP_vs_avg_debit_CP_4_months'] = f'Its normal  for this account to send {tr_full.amount} CZK to {tr_full.counter_party} based on its 4 months history.'
    neg_dict['tx_amount_vs_mean_credit_1_months'] = f'Credit transaction of {tr_full.amount} CZK is an usual for this account based on its last month history.'
    neg_dict['tx_amount_vs_mean_credit_4_months'] = f'Credit transaction of {tr_full.amount} CZK is an usual for this account based on its last 4 months history.'
    neg_dict['tx_amount_vs_mean_debit_1_months'] = f'Debit transaction of {tr_full.amount} CZK is an usual for this account based on its last month history.'
    neg_dict['tx_amount_vs_mean_debit_4_months'] = f'Debit transaction of {tr_full.amount} CZK is an usual for this account based on its last 4 months history.'
    neg_dict['trcount_round_amt_vs_total_trx1_months'] = f'{(tr_full.trcount_round_amt_vs_total_trx1_months/(1-tr_full.trcount_round_amt_vs_total_trx1_months))} transactions with rounded amounts like {tr_full.amount} CZK were processed in last 1 month, this is normal for this account.'
    neg_dict['trcount_round_amt_vs_total_trx4_months'] = f'{(tr_full.trcount_round_amt_vs_total_trx4_months/(1-tr_full.trcount_round_amt_vs_total_trx4_months))} transactions with rounded amounts like {tr_full.amount} CZK were processed in last 4 months, this is normal for this account.'
    neg_dict['txcount_new_CP_vs_total_CP_1_months'] = f'{tr_full.txcount_new_CP_vs_total_CP_1_months/(1-tr_full.txcount_new_CP_vs_total_CP_1_months)}% of counter parties encountered by this account in the last month are new. This is normal for this account based on its history.'
    neg_dict['txcount_new_CP_vs_total_CP_4_months'] = f'{tr_full.txcount_new_CP_vs_total_CP_1_months/(1-tr_full.txcount_new_CP_vs_total_CP_1_months)}% of counter parties encountered by this account in last 4 months are new. This is normal for this account based on its history.'
    neg_dict['avg_outgoing_vs_avg_income_1_months'] = f'The ratio of average debit/credit amount {tr_full.avg_outgoing_vs_avg_income_1_months/(1-tr_full.avg_outgoing_vs_avg_income_1_months)} in the last month is normal for this account.'
    neg_dict['avg_outgoing_vs_avg_income_4_months'] = f'The ratio of average debit/credit amount {tr_full.avg_outgoing_vs_avg_income_4_months/(1-tr_full.avg_outgoing_vs_avg_income_4_months)} in last 4 months is normal for this account.'
    neg_dict['tx_amount_vs_avg_incoming'] = f'{tr_full.amount} CZK is normal for this account as compared to sum of incoming amount per month based on last 4 months history.'
    neg_dict['first_week'] = f'Its normal to have this transaction in {(tr_full.date.day - 1)//7+1}th week of the month.'
    neg_dict['last_week'] = f'Its normal to have this transaction in {(tr_full.date.day - 1)//7+1}th week of the month.'
    neg_dict['days_to_accumulate_tr_amt'] = f'The {tr_full.amount} CZK that is being transferred was collected in less than {int(tr_full.days_to_accumulate_tr_amt/(1-tr_full.days_to_accumulate_tr_amt))+1} days, this is a normal time frame for this account.'
    neg_dict['fast_money_movement'] = f'The {tr_full.amount} CZK that is being transferred was collected within a normal time frame.'
    neg_dict['tr_amt_exceeds_allowed_limit'] = f'The {tr_full.amount} CZK that is being transferred is within the allowed limit for {tr_full.counter_party}[0:2].'
    neg_dict['country_risk'] = f'No party of this transaction belongs to a high risk country.'
    neg_dict['did_test_trx'] = f'Customer did not attempt a suspecious test transaction when the account was opened.'
    neg_dict['isCash'] = f"The transaction medium is {mode} and this is normal based on {tr_full.holding_party_name}'s history"
    neg_dict['day_of_week'] = f'Its normal to have this transaction in {tr_full.date.dayofweek}th day of the week.'
    neg_dict['day_of_month'] = f'Its normal to have this transaction in {tr_full.date.day}th day of the month.'
    neg_dict['day_of_year'] = f'Its normal to have this transaction in {tr_full.date.dayofyear}th day of the year.'
    neg_dict['month_of_year'] = f'Its normal to have this transaction in {tr_full.date.month}th month.'
    
    return neg_dict


def positive(tr_full, mode):

    pos_dict = {}
    pos_dict['latent_dim1'] = f"Looking at the amount and mode of transactions of this account in the last 4 month, deep learning model asses the combination of {tr_full.amount} CZK and mode of transaction '{mode}' to be unusual."
    pos_dict['latent_dim2'] = f"Looking at the timing and amount of transactions of this account in the last 4 month, deep learning model asses the combination of {tr_full.amount} CZK and timing {tr_full.date.strftime('%d %b %y')} to be unusual."
    pos_dict['latent_dim3'] = f"Looking at the amount and mode of transactions of this account in the last 4 month, deep learning model asses the combination of {tr_full.amount} CZK and mode of transaction '{mode}' to be unusual."
    pos_dict['latent_dim4'] = f"Looking at the timing and amount of transactions of this account in the last 4 month, deep learning model asses the combination of {tr_full.amount} CZK and {tr_full.date.strftime('%d %b %y')} to be unusual."

    pos_dict['common_amount_4m'] = f'{tr_full.amount} CZK is not a common amount for this account.'
    pos_dict['reoccuring_trx_4m'] = f'A transaction of {tr_full.amount} CZK around this time of the month is not common for this account.'
    pos_dict['ave_dist_same_amt_4m'] = f'The average amount of time spent between transactions of {tr_full.amount} CZK in last 4 months is {tr_full.ave_dist_same_amt_4m/(1-tr_full.ave_dist_same_amt_4m)}, low for this account. Transactions of this amount are not expected to happen frequently.'
    pos_dict['credit_txcount_last_month_vs_4months'] = f'Number of credit transactions processed in last month were unusual for this account based on its perivous 4 month history.'
    pos_dict['debit_txcount_last_month_vs_4months'] = f'Number of debit transactions processed in last month were unusual for this account based on its perivous 4 month history.'
    pos_dict['credit_vol_last_month_vs_4months'] = f'Total money credited within last month by similar transactions is unusual for this account.'
    pos_dict['debit_vol_last_month_vs_4months'] = f'Total money debited within last month by similar transactions is unusual for this account.'
    pos_dict['mean_credit_last_month_vs_4months'] = f'Average amount credited by similar transactions in the last month is unusual for this account.'
    pos_dict['mean_debit_last_month_vs_4months'] = f'Average amount debited by similar transactions in the last month is unusual for this account.'
    pos_dict['high_risk_trx_last_month_vs_4months'] = f'Too many transactions with high risk countries for this account in the last month.'
    pos_dict['credit_from_high_risk_last_month_vs_avg_in_4months'] = f'Too much amount credited to high risk countries like {tr_full.counter_party}[0:2] in last month'
    pos_dict['debit_to_high_risk_last_month_vs_avg_in_4months'] = f'Too much amount debited to high risk countries like {tr_full.counter_party}[0:2] in last month'
    pos_dict['trcount_new_CP_vs_total_cp_4months'] = f'Too many transactions sent to new counter parties like {tr_full.counter_party} in last one month based on its history.'
    pos_dict['no_trx_high_risk_vs_total_trx1_months'] = f'{tr_full.no_trx_high_risk_vs_total_trx1_months/(1-tr_full.no_trx_high_risk_vs_total_trx1_months)}% of transactions were sent to high risk country in the last month. This is unusual behaviour for this account.'
    pos_dict['no_trx_high_risk_vs_total_trx4_months'] = f'{tr_full.no_trx_high_risk_vs_total_trx4_months/(1-tr_full.no_trx_high_risk_vs_total_trx4_months)}% of transactions were sent to high risk country in last 4 months. This is unusual behaviour for this account.'
    pos_dict['credit_from_high_risk_vs_avg_credit1_months'] = f'{tr_full.credit_from_high_risk_vs_avg_credit1_months/(1-tr_full.credit_from_high_risk_vs_avg_credit1_months)} of amount is credited to high risk country in the last month. This is unusual behaviour for this account.'
    pos_dict['credit_from_high_risk_vs_avg_credit4_months'] = f'{tr_full.credit_from_high_risk_vs_avg_credit4_months/(1-tr_full.credit_from_high_risk_vs_avg_credit4_months)}% of amount is credited to high risk country in last 4 months. This is unusual behaviour for this account.'
    pos_dict['debit_to_high_risk_vs_avg_debit1_months'] = f'{tr_full.debit_to_high_risk_vs_avg_debit1_months/(1-tr_full.debit_to_high_risk_vs_avg_debit1_months)}% of amount is debited to high risk country in last 1 month. This is unusual behaviour for this account.'
    pos_dict['debit_to_high_risk_vs_avg_debit4_months'] = f'{tr_full.debit_to_high_risk_vs_avg_debit4_months/(1-tr_full.debit_to_high_risk_vs_avg_debit4_months)}% of amount is debited to high risk country in last 4 months. This is unusual behaviour for this account.'
    pos_dict['no_trx_same_amt_vs_total_trx1_months'] = f'{(tr_full.no_trx_same_amt_vs_total_trx1_months/(1-tr_full.no_trx_same_amt_vs_total_trx1_months))} transactions with the {tr_full.amount} CZK were processed in last 1 month, this is unusual for this account.'
    pos_dict['no_trx_same_amt_vs_total_trx4_months'] = f'{(tr_full.no_trx_same_amt_vs_total_trx4_months/(1-tr_full.no_trx_same_amt_vs_total_trx4_months))} transactions with the {tr_full.amount} CZK were processed in last 4 months, this is unusual for this account.'
    pos_dict['tx_amount_vs_avg_debit_CP_1_months'] = f'Transaction of {tr_full.amount} CZK sent to {tr_full.counter_party} is unusual in last 1 month.'
    pos_dict['tx_amount_vs_avg_debit_CP_4_months'] = f'Transaction of {tr_full.amount} CZK sent to {tr_full.counter_party} is unusual in last 4 months.'
    pos_dict['tx_amount_vs_avg_credit_CP_1_months'] = f'Transaction of {tr_full.amount} CZK received from {tr_full.counter_party} is unusual in last 1 month.'
    pos_dict['tx_amount_vs_avg_credit_CP_4_months'] = f'Transaction of {tr_full.amount} CZK received from {tr_full.counter_party} is unusual in last 4 months.'
    pos_dict['number_credit_CP_1_months'] = f'Number of credit transactions to {tr_full.counter_party} in last 1 month is unusual.'
    pos_dict['number_credit_CP_4_months'] = f'Number of credit transactions to {tr_full.counter_party} in last 4 months is unusual.'
    pos_dict['number_debit_CP_1_months'] = f'Number of debit transactions to {tr_full.counter_party} in last 1 month is unusual.'
    pos_dict['number_debit_CP_4_months'] = f'Number of debit transactions to {tr_full.counter_party} in last 4 months is unusual.'
    pos_dict['credit_vol_CP_1_months'] = f'Total money received from {tr_full.counter_party} in last 1 month is unusual for this account.'
    pos_dict['credit_vol_CP_4_months'] = f'Total money received from {tr_full.counter_party} in last 4 months is unusual for this account.'
    pos_dict['debit_vol_CP_1_months'] = f'Total money sent to {tr_full.counter_party} in last 1 month is unusual for this account.'
    pos_dict['debit_vol_CP_4_months'] = f'Total money sent to {tr_full.counter_party} in last 4 months is unusual for this account.'
    pos_dict['tr_amt_CP_vs_avg_credit_CP_1_months'] = f'Its unusual for this account to receive {tr_full.amount} CZK from {tr_full.counter_party} in the last month.'
    pos_dict['tr_amt_CP_vs_avg_credit_CP_4_months'] = f'Its unusual for this account to receive  {tr_full.amount} CZK from {tr_full.counter_party} based on its 4 months history.'
    pos_dict['tr_amt_CP_vs_avg_debit_CP_1_months'] = f'Its unusual for this account to send {tr_full.amount} CZK to {tr_full.counter_party} in the last month.'
    pos_dict['tr_amt_CP_vs_avg_debit_CP_4_months'] = f'Its unusual for this account to send {tr_full.amount} CZK to {tr_full.counter_party} based on its 4 months history.'
    pos_dict['tx_amount_vs_mean_credit_1_months'] = f'Credit transaction of {tr_full.amount} CZK is an unusual for this account based on its last month history.'
    pos_dict['tx_amount_vs_mean_credit_4_months'] = f'Credit transaction of {tr_full.amount} CZK is an unusual for this account based on its last 4 months history.'
    pos_dict['tx_amount_vs_mean_debit_1_months'] = f'Debit transaction of {tr_full.amount} CZK is an unusual for this account based on its last month history.'
    pos_dict['tx_amount_vs_mean_debit_4_months'] = f'Debit transaction of {tr_full.amount} CZK is an unusual for this account based on its last 4 months history.'
    pos_dict['trcount_round_amt_vs_total_trx1_months'] = f'{(tr_full.trcount_round_amt_vs_total_trx1_months/(1-tr_full.trcount_round_amt_vs_total_trx1_months))} transactions with rounded amounts like {tr_full.amount} CZK were processed in last 1 month, this is unusual for this account.'
    pos_dict['trcount_round_amt_vs_total_trx4_months'] = f'{(tr_full.trcount_round_amt_vs_total_trx4_months/(1-tr_full.trcount_round_amt_vs_total_trx4_months))} transactions with rounded amounts like {tr_full.amount} CZK were processed in last 4 months, this is unusual for this account.'
    pos_dict['txcount_new_CP_vs_total_CP_1_months'] = f'{tr_full.txcount_new_CP_vs_total_CP_1_months/(1-tr_full.txcount_new_CP_vs_total_CP_1_months)}% of counter parties encountered by this account in the last month are new. Its unusual behaviour based on its history.'
    pos_dict['txcount_new_CP_vs_total_CP_4_months'] = f'{tr_full.txcount_new_CP_vs_total_CP_1_months/(1-tr_full.txcount_new_CP_vs_total_CP_1_months)}% of counter parties encountered by this account in last 4 months are new. Its unusual behaviour based on its history.'
    pos_dict['avg_outgoing_vs_avg_income_1_months'] = f'The ratio of average debit/credit amount {tr_full.avg_outgoing_vs_avg_income_1_months/(1-tr_full.avg_outgoing_vs_avg_income_1_months)} in the last month is unusual for this account.'
    pos_dict['avg_outgoing_vs_avg_income_4_months'] = f'The ratio of average debit/credit amount {tr_full.avg_outgoing_vs_avg_income_4_months/(1-tr_full.avg_outgoing_vs_avg_income_4_months)} in last 4 months is unusual for this account.'
    pos_dict['tx_amount_vs_avg_incoming'] = f'{tr_full.amount} CZK is unusual for this account as compared to sum of incoming amount per month based on last 4 months history.'
    pos_dict['first_week'] = f'This transaction is not expected to happen in {(tr_full.date.day - 1)//7+1}th week of the month.'
    pos_dict['last_week'] = f'This transaction is not expected to happen in {(tr_full.date.day - 1)//7+1}th week of the month.'
    pos_dict['days_to_accumulate_tr_amt'] = f'The {tr_full.amount} CZK that is being transferred was collected in {int(tr_full.days_to_accumulate_tr_amt/(1-tr_full.days_to_accumulate_tr_amt))+1} days which is an abnormally short time frame for this account.'
    pos_dict['fast_money_movement'] = f'The {tr_full.amount} CZK that is being transferred was collected within a short period of time.'
    pos_dict['tr_amt_exceeds_allowed_limit'] = f'The {tr_full.amount} CZK that is being transferred is too high for {tr_full.counter_party}[0:2].'
    pos_dict['country_risk'] = f'This transaction is associated with {tr_full.counter_party} who belongs to a high risk country.'
    pos_dict['did_test_trx'] = f'Customer attempted a test transaction when the account was opened, this is common in fraud cases.' 
    pos_dict['isCash'] = f"The transaction medium is {mode} and this is abnormal based on {tr_full.holding_party_name}'s history"
    pos_dict['day_of_week'] = f'Its unusual to have this transaction in {tr_full.date.dayofweek}th day of the week.'
    pos_dict['day_of_month'] = f'Its unusual to have this transaction in {tr_full.date.day}th day of the month.'
    pos_dict['day_of_year'] = f'Its unusual to have this transaction in {tr_full.date.dayofyear}th day of the year.'
    pos_dict['month_of_year'] = f'Its unusual to have this transaction in {tr_full.date.month}th month.'
    
    return pos_dict



def trx_select(selected_fp, i):
    
    tr_feat = suspicious_cases_feat.iloc[i]    
    tr_full = selected_fp.iloc[i].apply(lambda x: round(x, 3) if isinstance(x, float) else x)
    
    shap_contrib = clf.predict(tr_feat, pred_contrib=True)

    featsxg = {} # a dict to hold feature_name
    for feature, shap_temp in zip(tr_feat.index, shap_contrib[0][:-1]):
        featsxg[feature] = shap_temp #add the name/value pair

    shaps_pd = pd.DataFrame.from_dict(featsxg, orient='index').rename(columns={0: 'LGBM Shap'})
    mode = 'cash' if tr_full.isCash == 1 else 'bank transfer'
    
    anomaly = 0
    if clf.predict(tr_feat) > 0.5: 
        top_shap = shaps_pd.sort_values(by='LGBM Shap', ascending=False)[0:5]
        exp_dict = positive(tr_full, mode)
        anomaly = 1
    else: 
        top_shap = shaps_pd.sort_values(by='LGBM Shap', ascending=True)[0:5]
        exp_dict = negative(tr_full, mode)
        
    return top_shap, exp_dict, anomaly, shaps_pd['LGBM Shap']

def show_trx_data(selected_fp, i):
    print(selected_fp.iloc[i, 1:])
    
#     print(dd[useful_feats]/(1-dd[useful_feats]))
    
def show_account_hist(selected_fp, i):
    account = selected_fp.iloc[i].account_id
    display(df.loc[df.account_id==account])
    
def plot_shap_values(dd, i):
    plt.figure(figsize=(15,10))
    dd = dd.sort_values(ascending=False)
    dd[:10].sort_values(ascending=True).plot(kind='barh')
    plt.title(f'Index: {i}', fontsize=16)
    show_inline_matplotlib_plots()
    
def plot_selected(i):
        clear_output()

        selected_fp = suspicious_cases
        top_shap, exp_dict, anomaly, shaps_pd = trx_select(selected_fp, i)

        if dropdown.value == 'Transaction data':
            printmd(f'### Transaction data for index: {i}')
            show_trx_data(selected_fp, i)         
#             printmd(f'### Important behavioural features data for index: {i}')
#             show_useful_feats(selected_fp, i)
        if dropdown.value == 'Account history':
            printmd(f'### Account history for this card: {i}')
            show_account_hist(selected_fp, i)
        if dropdown.value == 'Decision Explanations':
            if anomaly>0: 
                printmd(f'### The transaction (index {i}) is anomalous due to the factors shown below:')
            else:
                printmd(f'### The transaction (index {i}) is non-anomalous due to the factors shown below:')
            for x in top_shap.index:
                printmd('- '+exp_dict[x])
        if dropdown.value == 'Shap Analysis':
            printmd(f'### Shap Analysis for the index: {i}')
            plot_shap_values(shaps_pd, i)
            
def next_button_clicked(b):
    with out:
        global ix
        ix += 1

def prev_button_clicked(b):
    with out:
        global ix
        ix -= 1
        if ix<0: ix=0
        
def refresh_button_clicked(b):
    with out:
        global ix
        plot_selected(ix)