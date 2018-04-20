# Take Back Day Admin Pages

This component serves as the admin pages for the Take Back Day map and texting.

# Installation

### 0. Setup Environment Variables

|`Variable`|Description|
| - |-- |
| `FIREBASE_URL` | URL for the Firebase DB. ex. https://tdb.firebase.io |
| `FIREBASE_API_KEY` | API Key used for the Firebase DB calls.|
| `FIREBASE_SECRET` | Database secret for your firebase account. [More info where to get the secret here](https://stackoverflow.com/a/39054425)|
| `FIREBASE_ID` | Your user ID for the firebase account.|
| `FIREBASE_EMAIL` | Your email for the firebase account.|
| `UPCOMING_TBD` | Date formatted value for the next TBD text blast. Ex. `2018-04-23 09:00:00` |
| `TWILIO_API_KEY` | API Key for Twilio API Calls|
| `TWILIO_SECRET_KEY` | Secret Key for Twilio Calls |
| `TWILIO_SOURCE_NUMBER` | Source number provided by twilio that will send / receive messages |
| `SENDGRID_API_KEY` | SendGrid API for sending emails |

### 1. Install modules

  $ pipenv install

### 2. Setup Database

For PostGreSQL

  $ createdb takebackday

### 3. Run migration and load data

    $ python manage.py migrate
    $ python manage.py collecstatic
    $ python manage.py loaddata locations
    $ python manage.py loaddata message


**Note:** `locations` and `message` are the initial data for all the locations and messages.


### 4. Setup Scheduled tasks

In your Heroku project root:

```
heroku addons:create redistogo
heroku scale worker=1
heroku scale clock=1
```

# TBD Django Commands

These commands can be incorporated to your cron / scheduled tasks.

To Pull data from firebase:

    $ python manage.py pull_data

To send confirmation texts/emails:

    $ python manage.py send_confirmation

To send TakeBackDay day-of reminders:

    $ python manage.py send_reminder (!!! Under Construction)


------

# Heroku Setup:

Make sure you have Python [installed properly](http://install.python-guide.org). Also, install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone git@github.com:heroku/python-getting-started.git
$ cd python-getting-started

$ pipenv install

$ createdb twilio_mgr

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```
