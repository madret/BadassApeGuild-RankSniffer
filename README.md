# BadassApeGuild-RankSniffer
Get an overview of Badass Apes that are listed on Binance, sorted on Rank within seconds. No more manual hassle.

<img src="https://user-images.githubusercontent.com/56820649/153955706-07672c73-06fa-4554-83d1-a52eb64064f7.gif" width="400" height="230">

## Prerequisites / what do you need to run the program:
- Windows OS
- Google chrome
- Chromedriver
- Python
- Internet connection 🙉

# Installation guide:

### 1. Download / check Chrome version
- Download google chrome (if not already):
https://www.google.com/intl/eng_eng/chrome/
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

- After clicking the correct link choose the zip file: `chromedriver_win32.zip`
- After downloading Chromedriver copy it to: `C:\Program Files (x86)`
- Press Continue

### 3. Install python & pip

- Download & install Python: https://www.python.org/downloads/
- Check the box add python to PATH:

<img src="https://user-images.githubusercontent.com/56820649/151678507-67dd067d-1aaa-4754-9445-2e836734d6d1.png" width="400" height="250">

- The installation has to include Pip, press Install now

### 4. FINAL STEP: Install zip file from this github repository
- Scroll to top: https://github.com/madret/BadassApeGuild-RankSniffer
- You can download the entire ranksniffer folder as zip like so:

<img src="https://user-images.githubusercontent.com/56820649/151702319-88194648-7c64-4831-b61e-4cdf41cc38af.png" width="350" height="250">

- Copy the folder to somewhere you prefer, for example: `C:\Users\username\Documents\ranksniffer`
- Now it's time to install requirements.txt
- Open up Powershell:
Press Windows+R and type "powershell" press Enter
- Type in the following commands to install the final requirements:
1. `cd /folder/where/ranksniffer/is/located` 
2. `pip install -r requirements.txt`
- You're now good to go.
- Run the program in powershell with the following command: `python bag_rank_sniffer.py`

## Example usage
- Call the program in your Command line OR by double clicking the python file: `python bag_rank_sniffer.py`   
- Hereafter the program goes to work, a chrome browser opens and does a gentle web crawl on Binance NFT to check the current listed Badass Apes.
- After a little more than a minute (depending on ISP connection) a textfile `ID+rank.txt` is created that contains all the ID numbers with corresponding Rank sorted on highest first:

<img src="https://user-images.githubusercontent.com/56820649/151707582-d1f18cab-f4ca-4f21-b028-5c9f731aad61.png" width="700" height="300">
     
- Et voila:

<img src="https://user-images.githubusercontent.com/56820649/151707626-92b76a1c-8072-43b6-b8b0-d53c27132b02.png" width="700" height="20">


Text file results example:

<img src="https://user-images.githubusercontent.com/56820649/151703878-d0be8944-17d5-4742-a9a0-cfdb9a4f03b1.png" width="120" height="220">

e.g.
`['1550', 1], ['1370', 84], ['1821', 178]` rankings can be fact checked on the official Badass Ape Guild site:

<img src="https://user-images.githubusercontent.com/56820649/151580603-441b9552-d9db-4933-9110-74504ba761e4.png" width="150" height="180"> , <img src="https://user-images.githubusercontent.com/56820649/151574311-cd763eb0-bf9f-4023-ba2f-80772fe9292f.png" width="150" height="180"> , <img src="https://user-images.githubusercontent.com/56820649/151580694-653d90bd-08e6-4acb-8fdc-917f1c0d24fe.png" width="150" height="180">

- The text file contains Apes that are listed on Binance NFT: https://bit.ly/3IL5tV7
- Spare yourself a lot of time and get automation in your life 🙊

# Credits

- There are only 3333 Apes in total and they are all sold out.
- The offical Badass Ape Guild website: https://badassapeguild.com/
- Binance NFT marketplace: https://bit.ly/3IL5tV7
- My modest twitter handle: https://twitter.com/b41ss
