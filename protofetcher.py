import requests
from bs4 import BeautifulSoup

def fetch_problem_details(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('div', class_='title').text.strip()
    contest_id = url.split('/')[-3]
    problem_code = url.split('/')[-1]
    statement = soup.find('div', class_='problem-statement').find('div', class_='').text.strip()
    inputs = soup.find_all('div', class_='input')
    outputs = soup.find_all('div', class_='output')

    print(f"Problem Title: {title}")
    print(f"Problem Code: {contest_id}/{problem_code}")
    print(f"\nProblem Statement:\n{statement}\n")

    if not inputs or not outputs:
        print("Failed to find test cases. The page structure may have changed.")
        return

    for i, input_case in enumerate(inputs):
        input_text = input_case.find('pre').text.strip()
        output_text = outputs[i].find('pre').text.strip()

        print(f"Test Case {i + 1}:")
        print("Input:")
        print(input_text)
        print("Output:")
        print(output_text)
        print("\n" + "-" * 50 + "\n")


fetch_problem_details("https://codeforces.com/problemset/problem/2010/B")

