# -*- coding: utf-8 -*-
import Queries as q

if __name__ == "__main__":
    source = "data/data.csv"
    #q.percent_income_share(source)
    #q.mean_normalized_percent_income_share(source)
    #q.capital_gains_lift(source)
    #q.average_incomes(source)
    #q.average_top_income_lift(source)
    #q.income_composition(source)
    q.generate_report_for_selected_countries(source)