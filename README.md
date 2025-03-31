# Directory Brute Forcer

A simple Python script that performs a brute force attack to discover hidden directories on a target website by checking for common paths using a wordlist.

## Features

- Tests for valid directories using status code `200 OK`
- Saves all positive results into `Positive_Responses.txt`
- Lightweight and easy to use
- Customizable wordlist support

## Requirements

- Python 3.x
- `requests` library

You can install the required library using:

```bash
pip install requests
```

## Usage

1. **Clone the script** or copy the code to your local machine.
2. **Prepare your wordlist**:
   - The script uses `wordlist_test.txt` by default.
   - For a full scan, **replace** `wordlist_test.txt` with `wordlist.txt` at line 14.

3. **Run the script**:

```bash
python brute_forcer.py
```

4. **Input the target URL** when prompted (e.g., `https://example.com`).

## Output

- Found directories (HTTP 200 OK) are saved in:
  ```
  Positive_Responses.txt
  ```

## Customization

- To scan using a different wordlist, change the file name at this line:

```python
with open("wordlist_test.txt", "r") as file:
```

- Replace with your preferred wordlist, for example:

```python
with open("wordlist.txt", "r") as file:
```

## Legal Notice

This tool is intended **for educational purposes only**. Do not use it against any website without **explicit permission**. Unauthorized scanning may be illegal and unethical.
