# StockGPT
Predict Stock movements with GPT-4 or GPT-3.5

# DISCLAIMER
Please treat this like the high-tech gambling toy that it is and not like a good tool for stock analysis.
I.e. you probably shoudn't invest with it..or use it at all.

inspired by this paper: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4412788

# How to use it
1. If you haven't installed the dependencies already, run, ```pip install -r requirements.txt```
2. If you haven't already, put your OpenAI api token in the file called auth.txt
3. Put a list of companies you want to track in companies.txt
4. Run ```python sgpt.py -h``` to see your options, then run the command as you want.
The script will generate individual reports on every headline it fines for each company, as well as an overall report which includes the API costs.

# Examples
```python sgpt.py -t -c```

<img width="257" alt="Screen Shot 2023-04-22 at 4 07 07 AM" src="https://user-images.githubusercontent.com/29033313/233757108-6ddd34af-e3df-4bb4-a71c-34519166e785.png">

<img width="239" alt="Screen Shot 2023-04-22 at 4 11 01 AM" src="https://user-images.githubusercontent.com/29033313/233757155-63018c25-6a6f-4f19-ade4-cc0f0a43610c.png">

