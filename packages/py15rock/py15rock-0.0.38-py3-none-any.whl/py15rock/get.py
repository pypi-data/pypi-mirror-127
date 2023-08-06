import requests    
import pandas as pd
import json
import httpx

timeout = httpx.Timeout(timeout=120)

class config:
    api_key = None
    api_endpoint = 'https://api.15rock.com'

#actual api calls
def requestCompanyReturning(ticker, endpoint, singleRow=False):
    with httpx.Client() as client:
        r = client.get(f'{config.api_endpoint}/company/{ticker}/{endpoint}', headers={'Authorization': f'{config.api_key}'}, timeout=timeout)
    if singleRow==True:
        df = pd.DataFrame([pd.read_json(r.content,  typ='series')])

        # df = pd.Series(r.content)
    else:
        df = pd.read_json(r.content)
    return df

#api calls for endpoints that require years 
def requestCompanyReturningYears(ticker, years, endpoint, singleRow=False):
    with httpx.Client() as client:
        r = client.get(f'{config.api_endpoint}/company/{ticker}/{endpoint}/{years}', headers={'Authorization': f'{config.api_key}'}, timeout=timeout)
    if singleRow==True:
        df = pd.DataFrame([pd.read_json(r.content,  typ='series')])

        # df = pd.Series(r.content)
    else:
        df = pd.read_json(r.content)
    return df

#api call for fund level analytics
def requestFundAnalytics(fund_ticker, endpoint):
    with httpx.Client() as client:
        r = client.get(f'{config.api_endpoint}/fund/{fund_ticker}/{endpoint}', headers={'Authorization': f'{config.api_key}'}, timeout=timeout)
    df = pd.read_json(r.content)
    return df

#api call for portflio level analytics
def requestPortflioAnalytics(data, endpoint):
    with httpx.Client() as client:
        r = client.post(f'{config.api_endpoint}/portfolio/analytics/{endpoint}', headers={'Authorization': f'{config.api_key}'}, data=data, timeout=timeout)
    df = pd.read_json(r.content)
    return df

#api call for country level analytics
def requestCountryAnalytics(countryName, endpoint):
    with httpx.Client() as client:
        r = client.get(f'{config.api_endpoint}/country/{countryName}/{endpoint}', headers={'Authorization': f'{config.api_key}'}, timeout=timeout)
    df = pd.read_json(r.content)
    return df



#company endpoints

def companyCarbon(ticker):
    df = requestCompanyReturning(ticker, "carbon-footprint")
    return df

def companyRelated(ticker):
    df = requestCompanyReturning(ticker, "related-companies")
    return df

def companyC02Breakdown(ticker):
    df = requestCompanyReturning(ticker, "co2_breakdown")
    return df

def companyNews(ticker):
    df = requestCompanyReturning(ticker, "news")
    return df

def companyIndustryAverage(ticker):
    df = requestCompanyReturning(ticker, "industry-average")
    return df

def companyNetincomeCarbon(ticker):
    df = requestCompanyReturning(ticker, "netincome-carbon")
    return df

def company15rockScore(ticker):
    df = requestCompanyReturning(ticker, "15rock-globalscore")
    return df

def companyInfo(ticker):
    df = requestCompanyReturning(ticker, "info")
    return df

def companyCalculator(ticker):
    df = requestCompanyReturning(ticker, "equivalencies_calculator")
    return df

def companyValuation(ticker):
    df = requestCompanyReturning(ticker, "valuation")
    return df

def companyIndustrySum(ticker):
    df = requestCompanyReturning(ticker, "industry-sum")
    return df

def companyEmissionsEfficiency(ticker):
    df = requestCompanyReturning(ticker, "EmissionsEfficiency")
    return df

def companyHistoricalPrices(ticker):
    df = requestCompanyReturning(ticker, "historicalPrices")
    return df

def companyCOGS(ticker):
    df = requestCompanyReturning(ticker, "cogs")
    return df

def companySumHistoricCarbon(ticker, years):
    df = requestCompanyReturningYears(ticker, years, "sumhistoriccarbon")
    return df

def companyIndustryTempImpact(ticker, years):
    df = requestCompanyReturningYears(ticker, years, "industry-temp-impact")
    return df

def companyTempConversation(ticker, years):
    df = requestCompanyReturningYears(ticker, years, "temperatureconversion")
    return df

def companyCarbonAlpha(ticker, years):
    df = requestCompanyReturningYears(ticker, years, "carbonAlpha")
    return df

def companyCarbonTransitionRisk(ticker, years):
    df = requestCompanyReturningYears(ticker, years, "CarbonTransitonRisk",  singleRow=True)
    return df

def companyCarbonBudget(ticker):
    df = requestCompanyReturning(ticker, "carbonbudget")
    return df

def companyFinancials(ticker):
    df = requestCompanyReturning(ticker, "financials")
    return df

def companyCarbonTax(ticker):
    df = requestCompanyReturning(ticker, "carbontax")
    return df

def companyCarbonGrowthRate(ticker):
    df = requestCompanyReturning(ticker, "carbongrowthrate", singleRow=True)
    return df

def companyCarbonProductionEfficency(ticker):
    df = requestCompanyReturning(ticker, "productionefficency")
    return df

def companyCarbonCapture(ticker):
    df = requestCompanyReturning(ticker, "carboncapture")
    return df




def getCompany(ticker, endpoint):
    r = requests.get(f'{config.api_endpoint}/company/{ticker}/{endpoint}', headers={'Authorization': f'{config.api_key}'})
    df = pd.read_json(r.content)
    return df


#fund data
def getFundHoldings(fund_ticker):
    df = requestFundAnalytics(fund_ticker, "holdings")
    return df


#portfolio analytics
def getPortfolioCOGS(holdings_list, agg="sum"):
    data = {'tickers' : holdings_list, "func":agg}
    data = json.dumps(data)
    df = requestPortflioAnalytics(data=data, endpoint="cogs")
    return df

def getPortfolioCarbon(holdings_list, agg="sum"):
    data = {'tickers' : holdings_list, "func":agg}
    data = json.dumps(data)
    print(data)
    df = requestPortflioAnalytics(data=data, endpoint="carbon-footprint")
    return df

def getPortfolioHistoricalPrices(holdings_list):
    data = {'tickers' : holdings_list}
    data = json.dumps(data)
    print(data)
    df = requestPortflioAnalytics(data=data, endpoint="historicalprices")
    return df


#country data
def getCountryCarbon(countryName):
    df = requestCountryAnalytics(countryName, "carbon")
    return df


def getCountryTax(countryName):
    df = requestCountryAnalytics(countryName, "tax")
    return df


#industry