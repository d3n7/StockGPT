import csv, re, os, argparse
import openai
from duckduckgo_search import ddg_news

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--turbo', action='store_true', help='use gpt-3.5-turbo instead of gpt-4')
parser.add_argument('-c', '--combined', action='store_true', help='send and receive all the headlines in bulk (cheaper but probabaly less good)')
parser.add_argument('-T', '--temp', default=0.3, help='temperature (variability) of the model. a value between 0.0 and 1.0 (default: 0.3)')
args = parser.parse_args()

sysPrompt = 'You are a financial advisor. When the user gives you a headline, ' \
            'respond with a number between -1.0 and 1.0, signifying whether the ' \
            'headline is extremely negative (-1.0), neutral (0.0), or extremely ' \
            'positive (1.0) for the stock value of {}.'
if args.combined:
    sysPrompt = 'You are a financial advisor. When the user gives you a list of headlines, ' \
                'respond with a number between -1.0 and 1.0 for each headline, signifying whether the ' \
                'headline is extremely negative (-1.0), neutral (0.0), or extremely ' \
                'positive (1.0) for the stock value of {}.'
modelV = 'gpt-3.5-turbo' if args.turbo else 'gpt-4'
tScores = []
apiCost = 0
openai.api_key = open('auth.txt', 'r').readlines()[0].strip()
if not os.path.isdir('Individual_Reports'):
    os.mkdir('Individual_Reports')

def askGPT(prompt):
    global apiCost
    resp = openai.ChatCompletion.create(model=modelV, temperature=args.temp, messages=[{'role': 'system', 'content': sysPrompt},{'role': 'user', 'content': prompt}])
    costFactor = [0.03, 0.06] if modelV == 'gpt-4' else [0.002, 0.002]
    apiCost += resp['usage']['prompt_tokens']/1000*costFactor[0]+resp['usage']['completion_tokens']/1000*costFactor[1]
    return resp['choices'][0]['message']['content']

#for every company in companies.txt
for company in open('companies.txt', 'r').readlines():
    company = company.strip()
    scores = []
    sysPrompt = sysPrompt.format(company)
    sum = 0 # these two vars for calculating the mean score
    num = 0

    #collect scores for every headine from the last day one by one
    r = ddg_news(company, safesearch='Off', time='1')
    if not args.combined:
        for i in r:
            headline = i['title']
            try:
                score = float(re.findall(r'-?\d+\.\d+', askGPT(headline))[0])
                scores.append([headline, score])
                sum += score
                num += 1
            except:
                scores.append([headline, ''])

    #or as a batch
    else:
        headlines = []
        headlineStr = ''
        for i in r:
            headlines.append(i['title'])
        for x, i in enumerate(headlines):
            headlineStr += str(x+1)+'. '+i+'\n'*(x!=len(headlines)-1)
        for x, score in enumerate(re.findall(r'-?\d+\.\d+', askGPT(headlineStr))):
            score = float(score)
            try:
                scores.append([headlines[x], score])
            except:
                scores.append(['???', score])
            sum += score
            num += 1


    #calculate mean score, log it
    mean = sum/num
    scores.append(['Mean Score', mean])
    tScores.append([company, mean])

    #make individual report
    with open('Individual_Reports/'+company+'.csv', 'w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(['Headline', 'Score'])
        csvwriter.writerows(scores)
    print('[*] Saved Individual_Reports/'+company+'.csv')

#make final report
tScores.append(['Total Cost', apiCost])
with open('report.csv', 'w') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(['Company', 'Mean Score'])
    csvwriter.writerows(tScores)
