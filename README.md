# StockGPT
Predict Stock movements with GPT-4 or GPT-3.5
inspired by this paper: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4412788

# DISCLAIMER
Please only use this to see how it correlates to stock movements rather than use it to invest.
it's probably not very good at it anyways.

# How it works
For every company you put in the file company.txt, it will search the internet for news articles in the last day about your company.
It will evaluate each headline as a number between -1 and 1 signigying if it will impact the stock price negatively or postively.
It generates the reports for you on each company's healdines, in the form of a .csv file. And a final report which includes ths api costs.

# How to use it
1. If you haven't installed the dependencies already, run, ```pip install -r requirements.txt```
2. If you haven't already, put your OpenAI api token in the file called auth.txt
3. Put a list of companies you want to track in companies.txt
4. Run ```python sgpt.py -h``` to see your options, then run the command as you want.

# Examples
```python sgpt.py -t -c```

<img width="257" alt="Screen Shot 2023-04-22 at 4 07 07 AM" src="https://user-images.githubusercontent.com/29033313/233757108-6ddd34af-e3df-4bb4-a71c-34519166e785.png">

<img width="239" alt="Screen Shot 2023-04-22 at 4 11 01 AM" src="https://user-images.githubusercontent.com/29033313/233757155-63018c25-6a6f-4f19-ade4-cc0f0a43610c.png">

# Full options
```optional arguments:
  -h, --help            show this help message and exit
  -t, --turbo           use gpt-3.5-turbo instead of gpt-4
  -c, --combined        send and receive all the headlines in bulk (cheaper but probabaly less good)
  -T TEMP, --temp TEMP  temperature (variability) of the model. a value between 0.0 and 1.0 (default: 0.3)```
