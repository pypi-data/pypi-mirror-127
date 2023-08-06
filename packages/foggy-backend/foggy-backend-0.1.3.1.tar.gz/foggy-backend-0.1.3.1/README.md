# Foggy

Foggy keeps photos and videos shot with a smartphone in sync between devices. 
It does so without requiring a separate app to delete, update or add files. 
On an iPhone you will install the app and keep on using the built-in Photos
app to edit and sort your photos and videos. When space gets low on the device
you move the photos to an archive on the backend and clear the phone memory 
knowing that you have copies on the server.

The name foggy is a silly reference to fog as compared to cloud. Fog is
something that you can see and almost touch. A cloud is high up in the sky and
you have no idea what happens up there.

## Test it

At the moment Foggy is much a work in progress and requires more testing and 
development before it can be trusted as your only handler of photos and videos.
But you can try it out with your own server (mostly tested in Arch and Debian).

    sudo python3 -m pip install foggy-backend
    sudo sh -c "cat <<EOF > /etc/systemd/system/foggy@.service
    [Unit]
    Description=foggy syncronization backend service

    [Service]
    User=%i
    Type=simple
    ExecStart=/usr/local/bin/foggy
    Restart=on-failure
    RestartSec=5s

    [Install]
    WantedBy=multi-user.target
    EOF"

If you do not have the possibility to run pip you can symlink the launch-script
like so:

    ln -s scripts/run_server /usr/local/bin/
    chmod +x scripts/run_server

Finally reload the systemd daemon and start the service:

    sudo systemctl daemon-reload
    sudo systemctl enable foggy@$USER
    sudo systemctl start foggy@$USER
    
After this you can build the Xcode-project from the `ios` folder and deploy it to
a simulator or physical device. The app should then connect to the server and you
should be able to sync the device with the server.

The backend will create a folder in `$HOME/pictures/` for each device that is 
synced. If you want this folder elsewhere it is recommended to symlink it to
another directory or set the environment variable `FOGGY_ROOT`.


### Raspbian instruction

With a clean Raspbian installation here is what you do to get going. Login through
ssh or directly on the pi and add your user. E.g.:

    sudo useradd -m -G sudo mrfog
    sudo passwd mrfog

Logout and login with your new user. Run these commands to update and initiate the
system:

    sudo userdel pi
    sudo apt update ; sudo apt upgrade
    sudo apt install git
    
After that you can follow above instructions.


## Docker

In case you want to deploy your app with docker, here is an example 
`docker-compose.yaml` file:

    version: "3"
    services:
        backend:
            image: python:3.8
            container_name: foggy
            environment:
                PYTHONPATH: /foggy_backend
            command: python -m foggy
            ports:
                - 21210:21210
            logging:
                driver: journald
                options:
                    tag: "foggy"
            volumes:
                - ./backend:/backend

## Current limitations

Here are some limitations that needs to be taken into consideration:

- Use only one active backend server on the local network. There is no way to control
which backend is connected so you will not know which server gets connected.


# Developers documentation


## 1. Server and app connection

The connection between the server and the app is initiated with a 

## 2. Vendoring

There are two dependencies that have been vendored as compared to creating a
virtual environment or using system packages, see `backend/foggy/vendor`. The
reason for choosing this approach is a much simpler configuration. There is
really no need for docker or virtualenvs, just run it with `python -m...`.

## 3. Style and formatting

The code is formatted with *black* and linted with *pylint*.

Format all code with black:

    black  --target-version py38 --exclude 'vendor/*.?' rednas tests


## 4a. Tests

There are two test suites to be run, one for the `foggy-backend` Python package
and one for the `foggy-ios` iOS app. Here is how to run them:


### `foggy-backend`

### `foggy-ios`

    1. Initialize the backend virtualenv:

        pipenv sync --dev

    2. Start the `python-backend` server:

        pipenv run foggy --disable-mdns

    3. Build and run the tests in XCode (CMD-U)

## 4b. Test packaging

    pipenv run python setup.py sdist bdist_wheel
    pipenv run twine upload --repository testpypi dist/*


## 5. Make a release

    1. Set the version
    2. Build the package:

        pipenv run python setup.py sdist bdist_wheel

    3. Test the release:
        
        pipenv run twine upload dist/* --verbose -r testpypi

    4. Make the release
       
        pipenv run twine upload dist/* --verbose
    
    3. Tag the commit with the release

        git tag 0.1.0
        git push --tags

## 6. Build and test Synology DSM package

    1. Clone ...

    2. Build the package (run docker command from folder above the spskrc repo directory):

        docker run -it -v (pwd):/spksrc -e TAR_CMD="fakeroot tar" ghcr.io/synocommunity/spksrc /bin/bash
        cd spksrc/spk/foggy-backend/
        make clean && make TCVERSION=7.0

    3. Copy the .spk file to the Synology DSM system, e.g.:

        scp packages/foggy-backend_noarch-dsm7_0.1.2-1.spk quagmire.local:.

    4. Install manually:

        sudo synopkg install foggy-backend_noarch-dsm7_0.1.2-1.spk

    5. Grant sc-foggy-backend permissions rwx for homes/$USER/pictures

        TODO: fix so that the installer does this.