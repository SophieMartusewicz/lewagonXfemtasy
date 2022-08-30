# Dataset Documentation
- 'fantasies'(Categorical): One of 44 thematical tags associated with the audio
- 'longterm' (Boolean): denotes if the listener is a long-term user
- 'user'(ID): User ID of the listener
- 'story id'(ID): ID of the audio file
- 'voice id'(ID): ID of the speaker of the audio
- 'voice type'(Categorical): Type (gender) of the speaker voice
    - male           6451
    - female         2036
    - anonym         1572
    - male_female     836
    - female_male     697 
- 'genre'(Categorical):
    - Erotic Stories         4944
    - Sex Sounds             2994
    - Phone Sex              1014
    - 360° Audios             823
    - Sounds of Lovers        738
    - Moaning Sounds          690
    - Guided Masturbation     257
    - Love Letters             95
    - Affirmations             31
    - Meditations               6
- 'language intensity'(Ordinal): intensity of the language used in the audio in three categories:
    - soft(1)
    - intense(2)
    - rough(3)
- 'timestamp'(datetime): datetime of when the play session was started
- 'session breakups': date and (categorical) time of day of when the play session started:
    - Feature Engineering:
        - session_breakup_date(date): session start date
        - session_breakups_breakup: time of day when the audio was played:
            - 'First Peak', 'Early', 'Late Peak', 'OFF'
- 'story release date'(datetime): datetime of when the audio was released
- 'kinky score'(Integer): score calculated out of number of associated tags and intensity of the audio
    - Feature Engineering:
        - audio_intensity: Intensity level of the audio
        - audio_kinks: Number of kinks associated with the audio
- 'content type'(Enumerated Categorical): One of four content groups that the audio falss into:
    - 1 = Soul
    - 2 = Sounds
    - 3 = Stories
    - 4 = Series
- 'story duration'(Integer): Length of audio file in seconds
- 'play duration'(Integer): Played portion of the audio in seconds
    - Feature engineering:
        - play_percentage(Percentage): played portion of the audio as percentage of overall duration

# Data analysis
- Document here the project: lewagon_x_femtasy
- Description: Project Description
- Data Source:
- Type of analysis:

Please document the project the better you can.

# Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

Check for lewagon_x_femtasy in gitlab.com/{group}.
If your project is not set please add it:

- Create a new project on `gitlab.com/{group}/lewagon_x_femtasy`
- Then populate it:

```bash
##   e.g. if group is "{group}" and project_name is "lewagon_x_femtasy"
git remote add origin git@github.com:{group}/lewagon_x_femtasy.git
git push -u origin master
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
lewagon_x_femtasy-run
```

# Install

Go to `https://github.com/{group}/lewagon_x_femtasy` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:{group}/lewagon_x_femtasy.git
cd lewagon_x_femtasy
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
lewagon_x_femtasy-run
```
