<B> SO KIDS! </B>


! you clone this repo

! next you cd into this project folder

! run commands:

<B> virtualenv venv </b>

<b> . venv/bin/activate </b>

<B> git init </B>

<B> git add . </B>

<B> git commit -m "first commit"</B>

<B> heroku create YOUR_APP_NAME_INSTEAD_OF_BLOCK_CAPITALS</B>

<B> git push heroku master </B>


! then you run the following

<B> heroku addons:add heroku-postgresql:hobby-dev </B>

! This sets up a heroku hobby developer postgres db on you heroku account

! look: once it has provisioned a database you should get the following code:

<B> heroku addons:add heroku-postgresql:hobby-dev </B>

Creating heroku-postgresql:hobby-dev on ⬢ flaskpos... free
Database has been created and is available
 ! This database is empty. If upgrading, you can transfer
 ! data from another database with pg:copy
Created postgresql-fluffy-53405 as HEROKU_POSTGRESQL_ORANGE_URL

! THIS IS WHAT YOU ARE AFTER: HEROKU_POSTGRESQL_ORANGE_URL (name of your db in heroku)

! next run  run the following command with the DB color tag Heroku gave you:

 <b> heroku pg:promote HEROKU_POSTGRESQL_ORANGE_URL </B>

! This links the db URL of the hobby dev created to your app that you deployed

! next are these commands:

<b> heroku run python </B>

<b> from app import db </B>

<b> db.create_all() </B>

<b> exit() </B>

and BOOM!
you got a landing page.


! to query the db run:

<b> heroku pg:psql </B>

and then when pg opens you can do as we learned in class:

<b> SELECT * FROM users; </B>

etc........

GOOD LUCK!




