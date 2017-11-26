# -*- coding: utf-8 -*-
import json
import PlotData as pld
import GetDataSet as gds
import ModifyData as md
import GenerateReport as gr
def percent_income_share(source):
    """Create Income Share chart"""
    columns = (
            "Top 10% income share",
            "Top 5% income share",
            "Top 1% income share",
            "Top 0.5% income share",
            "Top 0.1% income share",
            )
    source = list(gds.getDataSetUsingCSV(source))
    return pld.linechart([gds.timeseries(source, col) for col in columns], labels=columns, title="U.S. Percentage Income Share", ylabel="Percentage")

def mean_normalized_percent_income_share(source):
    dataset = gds.getDataSetUsingCSV(source)
    columns = (
            "Top 10% income share",
            "Top 5% income share",
            "Top 1% income share",
            "Top 0.5% income share",
            "Top 0.1% income share",
            )
    source = list(dataset)
    return pld.linechart([md.normalize(gds.timeseries(source, col)) for col in columns],labels=columns,title="Mean Normalized U.S. Percentage Income Share",
                      ylabel="Percentage")

def capital_gains_lift(source):
    """
    Computes capital gains lift in top income percentages over time chart
    """
    dataset = gds.getDataSetUsingCSV(source)
    columns = (
            ("Top 10% income share-including capital gains", "Top 10% income share"),
            ("Top 5% income share-including capital gains", "Top 5% income share"),
            ("Top 1% income share-including capital gains", "Top 1% income share"),
            ("Top 0.5% income share-including capital gains", "Top 0.5% income share"),
            ("Top 0.1% income share-including capital gains", "Top 0.1% income share"),
            ("Top 0.05% income share-including capital gains","Top 0.05% income share"),)
    source = list(dataset)
    series = [md.delta(gds.timeseries(source, a), gds.timeseries(source,b)) for a, b in columns]
    return pld.linechart(series,labels=list(col[1] for col in columns), title="U.S. Capital Gains Income Lift", ylabel="Percentage Difference")

def average_incomes(source):
    """
    Compares percentage average incomes
    """
    dataset = gds.getDataSetUsingCSV(source)
    columns = (
            "Top 10% average income",
            "Top 5% average income",
            "Top 1% average income",
            "Top 0.5% average income",
            "Top 0.1% average income",
            "Top 0.05% average income",
            )
    source = list(dataset)
    return pld.linechart([gds.timeseries(source, col) for col in columns], labels=columns, title="U.S. Average Income", ylabel="2008 US Dollars")

def average_top_income_lift(source):
    """
    Compares top percentage avg income over total avg
    """
    dataset = gds.getDataSetUsingCSV(source)
    columns = (
            ("Top 10% average income", "Top 0.1% average income"),
            ("Top 5% average income", "Top 0.1% average income"),
            ("Top 1% average income", "Top 0.1% average income"),
            ("Top 0.5% average income", "Top 0.1% average income"),
            ("Top 0.1% average income", "Top 0.1% average income"),)
    source = list(dataset)
    series = [md.delta(gds.timeseries(source, a), gds.timeseries(source,b)) for a, b in columns]
    return pld.linechart(series,labels=list(col[0] for col in columns),title="U.S. Income Disparity",ylabel="2008 US Dollars")

def income_composition(source):
    """
    Compares income composition
    """
    dataset = gds.getDataSetUsingCSV(source)
    columns = (
            "Top 10% income composition-Wages, salaries and pensions",
            "Top 10% income composition-Dividends",
            "Top 10% income composition-Interest Income",
            "Top 10% income composition-Rents",
            "Top 10% income composition-Entrepreneurial income",
            )
    source = list(dataset)
    labels = ("Salary", "Dividends", "Interest", "Rent","Business")
    return pld.stackedarea([gds.timeseries(source, col) for col in columns], labels=labels, title="U.S. Top 10% Income Composition", ylabel="Percentage")

def generate_report_for_selected_countries(source):
    # Select countries to include
    include = ("United States", "France", "Italy","Germany", "South Africa", "New Zealand")
    # Get dataset from CSV
    data = list(gds.getDataSetUsingDictReader(source, include))
    years = set(gds.extract_years(data))
    # Generate context
    context = {'title': "Average Income per Family, %i - %i" % (min(years), max(years)),
               'years': json.dumps(list(years)),
               'countries': [v[0] for v in data],
               'series': json.dumps(list(gds.extract_series(data, years))),}
    # Write HTML with template
    gr.write(context)