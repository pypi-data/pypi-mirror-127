# Astblick
## A simple gitolite repo viewer

Astblick will connect to your gitolite repo(s), clone a local copy, and let
you browse them.

### Requirements

* Python 3
* cherrypy
* GitPython
* sqlalchemy
* openssl (binaries and python module, pyOpenSSL)
* markdown
* requests

### Installation

1. Install the dependencies. Most of these are available in most Linux
distributions, but pip or a virtualenv is fine if necessary.

2. To run under your own user, just unpack the tarball. You can also set up
as a system daemon using the enclosed systemd unit file.

3. Run astblick-makecert to generate the self-signed SSL key and cert for
astblick, or note the location of a pair you already have and would like to
use.

4. Run the daemon once to create the database and config file. The database
will be at ~/.astblick.db, and the config is ~/.astblick.conf.

    [Options]
    database = /home/<username>/.astblick.db
    ip = 127.0.0.1
    port = 8080
    refresh = 300
    key = /home/<astblick>/.astblick_key.pem
    cert = /home/<astblick>/.astblick_cert.pem
    tempdir = 0

5. Modify the config file as needed.

6. Create a passwordless RSA ssh key. The recommended path and filename is
**~/.ssh/astblick**

7. Add the public RSA key to the keydir of your gitolite-admin, and grant R
access to that key for the repos you'd like to use astblick with.

8. Access the gitolite host via ssh as the user you'll be running astblick as, so
that the host key is added to ~/.ssh/known_hosts.

9. Run astblick-repo. Enter a repo name, gitolite URL, and key name for each
repo.  For my installation, to view my astblick repo, I have:

    Astblick | gitolite@<hostname>:astblick | ~/.ssh/astblick

10. Start the daemon, either manually or via systemd.

11. Browse to https://<hostname>[:port]/

12. After the number of seconds in the refresh parameter in the config file,
astblick will create local clones of the configured repos.

13. Once created, you can click through your repos, display text files, open
other files externally, and view images by clicking and holding on the
image's filename.  Clicking a commit's SHA button will open a new tab
containing a diff for that commit.

### tempdir note
If tempdir = 0, the default, astblick will clone repos to a folder in the
current user's homedir, and read from those clones.  If you set tempdir = 1,
it will still clone to that location, but it will also then create a secure
tempdir, clone the repos to that additional location, and read from _those_
clones.  This can result in a slight performance increase, especially if
your tempdir is on tmpfs.  Use what works better for your situation.
