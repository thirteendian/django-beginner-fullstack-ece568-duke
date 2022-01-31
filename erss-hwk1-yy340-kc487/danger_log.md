# Ride share Service

Yuxuan Yang (yy340)
Keyu Chen (kc487)


## 17th Jan 2022 Database user password authentication failed

Migrate FATAL: jango.db.utils.OperationalError: could not initiate GSSAPI security context: Unspecified GSS failure.  Minor code may provide more information: Server not found in Kerberos database
FATAL:  password authentication failed for user "myuser"
FATAL:  password authentication failed for user "myuser"

## [update] 17th Jan 2022 Database user password authentication failed

Follow up the solutions provided:
Creating user
$ sudo -u postgres createuser <username>
Creating Database
$ sudo -u postgres createdb <dbname>
Giving the user a password
$ sudo -u postgres psql
psql=# alter user <username> with encrypted password '<password>';
Granting privileges on database
psql=# grant all privileges on database <dbname> to <username> ;


## 18th Jan 2022 Database permission failed on peer

## [update] 18th Jan 2022 Database permission failed on peer
Change ~/etc/postgresql/12/main/pg_hba.conf
 
All 'peer' / 'md5' changed to 'trust'
 
Sudo service postgresql restart

## 20th After new models were created, migrate failed

## [update] 20th After new models were created, migrate failed

Drop all tables in database:

python3 manage.py makemigrations --empty managerbook
python3 manage.py makemigrations
python3 manage.py migrate

## 22th Unsynchronous driver confirm problem:

## [update] 22th Unsynchronous driver confirm problem:

Because all view_open_ride should show all available rides that driver can choose depends on his maximun number of passengers of the car, the ride should also confirm the selected ride as above requirements, when driver clicks confirm button, we need to add extra statement to make sure we do not have new sharers joining in this  “going-to-confirm ” ride that make the total number of passengers outside of the car capcity.

Same as problem mentioned above, will be caused by cancelling the rides, or any ride changes as well.

## 25th Username of each account may become the same after new user register or edit user information

## [update] 25th Username of each account may become the same after new user register or edit user information

When user created an account, we user id to distinguish different users rather than username, this will make sure even 2 users have same username, their id is different.(also under url links)


## 25th Manytomany field reverse get objects

## [update] 25th Manytomany field reverse get objects

One difference is in the attribute naming: The model that defines the ManyToManyField uses the attribute name of that field itself, whereas the “reverse” model uses the lowercased model name of the original model, plus '_set' (just like reverse one-to-many relationships).



## 29th Jan 2022 Arrival Time can be any regardless of the ride creation Time

When user start a ride, after entering the form page and put their arrival time, the form does not check if or not the arrival time is earlier or later than the current time. This will cause one possible situation that the creation time is later than the entering arrival that the user is going to create. 
## 29th Jan 2022 Arrival Time can be any regardless of the ride creation Time [update]:
A condition can be updated in the later version to judge the current system time and the arrival time that the owner entered.
