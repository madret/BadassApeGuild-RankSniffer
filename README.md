# BadassApeGuild-RankSniffer
Get an overview of Badass Apes that are listed on Binance, sorted on Rank within seconds. No more manual hassle.

## Example usage
- Call the program in your Command line: `python bag_rank_sniffer.py`   
- Hereafter the program goes to work, a chrome browser opens and does a gentle web crawl on Binance NFT to check the current listed Badass Apes.
- After a little more than a minute (depending on ISP connection) a textfile `ID+rank.txt` is created that contains all the ID numbers with corresponding Rank sorted on highest first:

<img src="https://user-images.githubusercontent.com/56820649/151678040-c0caed30-e27e-4d5d-985b-dc4a36509ba5.png" width="700" height="300">

Text file example:

<img src="https://user-images.githubusercontent.com/56820649/151678366-3a5a78e8-bbda-46de-ab0b-5f4a54a7b728.png" width="100" height="200">

e.g.
`['1550', 1], ['1370', 84], ['1821', 178]` rankings can be fact checked on the official Badass Ape Guild site:

<img src="https://user-images.githubusercontent.com/56820649/151580603-441b9552-d9db-4933-9110-74504ba761e4.png" width="150" height="180"> , <img src="https://user-images.githubusercontent.com/56820649/151574311-cd763eb0-bf9f-4023-ba2f-80772fe9292f.png" width="150" height="180"> , <img src="https://user-images.githubusercontent.com/56820649/151580694-653d90bd-08e6-4acb-8fdc-917f1c0d24fe.png" width="150" height="180">

- https://badassapeguild.com/rarity.html
- If the Apes are listed / for sale they can be found on Binance NFT: https://bit.ly/3IL5tV7
- Spare yourself a lot of time and get automation in your life 🙊

## Prerequisites / what do you need to run the program:
- Windows OS
- Google chrome
- Chromedriver
- Python
- Internet connection 🙉

# Installation guide:
### 1. Download / check Chrome version
- Download google chrome (if not already):
https://www.google.com/intl/nl_nl/chrome/
- Open Google Chrome
- Click the three dots icon on the top right corner
- Go to Help & About Google Chrome
- Check your version
<img src="https://user-images.githubusercontent.com/56820649/151449904-9751edde-5549-4131-bcc0-ae9d379c236c.png" width="300" height="250">

### 2. Install Chromedriver

- Download Chromedriver via Official Chromium project:
https://chromedriver.chromium.org/downloads
- Choose the corresponding version.
- Like the example above i would now choose ChromeDriver 97.*

<img src="https://user-images.githubusercontent.com/56820649/151450613-af0476b7-6151-47d4-83b1-7fa2e09f6323.png" width="600" height="200">

- After downloading Chromedriver put it in: `C:\Program Files (x86)`

### 3. Last but not least

- Download & install Python: https://www.python.org/downloads/
- Check the box add python to PATH:

<img src="https://user-images.githubusercontent.com/56820649/151678507-67dd067d-1aaa-4754-9445-2e836734d6d1.png" width="450" height="250">

- As an additional feature Pip needs to be checked:

<img src="https://user-images.githubusercontent.com/56820649/151678525-17d08ea2-7e39-495f-8329-d3b2bcecaf34.png" width="300" height="250">

- After installing python now it's time to install requirements.txt: 
`cd /folder/where/RankSniffer/is/located` & `pip install -r requirements.txt`
- You're now good to go, go get some 😎

# Credits

- There are only 3333 Apes in total and they are all sold out.
- The offical Badass Ape Guild website: https://badassapeguild.com/
- Binance NFT marketplace: https://bit.ly/3IL5tV7
- My modest twitter handle: https://twitter.com/b41s_
