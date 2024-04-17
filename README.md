# email_sender [licence-expiry-notification]

## Context
Sends an email to a email recipient from a pre-configured tenplate using [postmarkapp]() and the python [postmarker lib](https://pypi.org/project/postmarker/)
> This particular script is designed to be run as a cron job.
> <br>
> It sends an email notification about a potential software license renewal reminder.
> <br>
> However, it can also serve as a template for other scenarios that require sending emails.

<br>

## Install dependencies

```zsh
python3 -m pip install -r requirements.txt
```

<br>

## Create a .env file with Postmark's API token

1. Go to [Postmark app](https://postmarkapp.com) and login.  
2. Locate your server and go to __API Tokens__. Note it.
3. Then come into this project directory and set the POSTMARK_API_KEY environment variable to the noted API Token, in a `.env` file.

```zsh
touch .env
echo POSTMARK_API_KEY=<YOUR_API_TOKEN>
```

## Execute
```zsh
python3 app.py --help  # for help
python3 app.py --to <RECIPIENT EMAIL>
```
