# **Brypt Desktop Setup Guide**

**Pick one of the following two testing methods:**

* Brypt Ubuntu Virtual Machine (Recommended)
    + Difficulty: **Easy**
    + Setup Time: Download Time + VM Install Time
    + Requires: VMWare Workstation 15 or VMWare fusion and an external Ubuntu/Debian/Linux WiFi adapter (Confirmed working: TP-Link WN725n).
    + Download the Brypt Ubuntu VM.
        - [https://drive.google.com/open?id=1qHn1LcWTNlIxZfp3BWeQqCVIhMY78lTz](https://drive.google.com/open?id=1qHn1LcWTNlIxZfp3BWeQqCVIhMY78lTz)
        - [https://oregonstate.box.com/s/vkcfl9doalik1khi3iwz2oixvxndgdr3](https://oregonstate.box.com/s/vkcfl9doalik1khi3iwz2oixvxndgdr3)
    + Make a new Virtual Machine with the Brypt Ubuntu OVA using VMWare Workstation 15 or VMWare Fusion.
        - The Brypt Ubuntu VM login credentials are username: “brypt-client” and password: “secured”.
    + Ensure you can connect your external WiFi adapter directly to the VM.
    + Disable the default shared/bridged internet connection to the VM.
    + Connect to an Internet accessible WiFi Access Point.
    + **Stetup the Brypt Network before Continuing**
    + Open a terminal and run the development version of the Brypt Desktop.

            cd ~/brypt-desktop
            npm run dev

        - Note: The application cache may think there’s two nodes connected. This is from the prior test run. The clear the nodes store, simply close the application and run again. 
    + Register for a new account or use the credentials: username: “piscitev” password “secured”.
    + **Follow the Brypt lifecycle to continue.**
* Manual Installation
    + Difficulty: **Hard**
    + Setup Time: 2-3 hours
    + Install required libraries and resources.
        - Requires: Ubuntu 18.04 LTS and an external Ubuntu/Debian/Linux WiFi adapter.
        - If running in a Virtual Machine follow steps _f_ through _h_ from Option 1 first.
        - **NOTE: A FontAwesome Pro license must be obtained to run the desktop application. Move the fontawesome.all.css.min into the src/renderer/assets/css folder and the webfonts folder into src/renderer/assets folder **
    + Install the required libraries and resources:
        - Basic Setup
            ```bash 
            cd ~
            sudo apt update
            sudo apt upgrade
            sudo apt-get install libtool pkg-config build-essential autoconf automake git openssl libssl-dev libgonf-2-4 build-essential
            ```
        - Node.js/NPM 
            1. [https://nodejs.org/en/](https://nodejs.org/en/)
            ```bash 
            cd ~
            curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
            sudo apt-get install -y nodejs
            ```
        - ZeroMQ 4.x
            1. [http://zeromq.org/intro:get-the-software](http://zeromq.org/intro:get-the-software)
            2. Install the ZeroMQ C++ language bindings
                * [https://github.com/zeromq/cppzmq](https://github.com/zeromq/cppzmq)
            ```bash 
            cd ~
            wget http://download.zeromq.org/zeromq-4.1.4.tar.gz
            tar -zxvf zeromq-4.1.4.tar.gz
            cd zeromq-4.1.4/
            ./configure --without-libsodium
            make
            sudo make install
            sudo ldconfig
            cd ~
            git clone https://github.com/zeromq/cppzmq.git
            sudo cp cppzmq/zmq.hpp /usr/local/include/
            ```
        - OpenSSL 1.1.0g
            1. Note: Electron and Node.js use competing branches of OpenSSL; a static library must be installed onto your system. 
                * [https://wiki.openssl.org/index.php/Compilation_and_Installation](https://wiki.openssl.org/index.php/Compilation_and_Installation#OS_X)
            ```bash 
            cd ~
            cd /tmp/
            wget http://www.openssl.org/source/openssl-1.1.0g.tar.gz
            tar -zxvf openssl-1.1.0g.tar.gz
            cd openssl-1.1.0g/
            make clean
            ./config --static -static -fPIC shared
            sudo make INSTALL_PREFIX=/tmp/package-root install
            ```
            2. You should now see “libcrypto.a” in the list of files using the command _ls /usr/local/lib/_
        - Node-gyp
            ```bash 
            cd ~
            npm install node-gyp -g
            ```
    + Clone and build the Brypt Desktop Git repository from Github.com.
        ```bash 
        cd ~
        git clone https://github.com/vpiscitello/brypt-desktop.git
        cd ~/brypt-desktop
        git checkout ubuntu-64
        npm install
        node-gyp configure && node-gyp build
        ./node_modules/.bin/electron-rebuild
        ```
    + **Stetup the Brypt Network before Continuing**
    + Run the development version of the Electron application.
        ```bash 
        npm run dev
        ``` 
    + Start your Brypt network and login to the desktop application.
    + Register for a new account or use the credentials: username: “piscitev” password “secured”
    + **Follow the Brypt lifecycle to continue.**


# Demo Walkthrough and Network Lifecycle

1. Ensure that each application and network component is fully installed.
2. Startup the Brypt network root coordinator. This will be the Raspberry PI 3 running the local Access Point. 
    * To easily verify the AP is running view your local Wifi connections and a _brypt-net-000000_ ssid should be visible.
    * To verify that an IPv4 address is assigned to connected devices, connect to the AP and run _ifconfig_.
        + From _ifconfig_ your Wifi interface should have some address starting with 192.168.30.x.
3. If testing with an additional Raspberry Pi 3 or additional Adafruit Feather nodes, you can connect them now.
4. With the Brypt network running start the desktop application on the client computer. 
    * If you are still connected to the Brypt AP, disconnect and connect to a Wifi AP with direct internet access. 
5. Login to the Brypt network through the application interface
    * This process will authenticate your user account and provide the program with any requisite network information (i.e. the Brypt AP ssid).
    * You will be provided a success message and the login window will be closed to open the network dashboard. 
6. The dashboard interface will display a processing animation while it searches for the Brypt AP.
    * If a notification is presented that it has found the network, click the button to connect.
    * If a notification is presented that a network has not been found:
        + Click the button to re-scan the local networks
        + If the issue persists, ensure the Brypt root coordinator is hosting an Access Point and assigning devices a proper IPv4 address.
7. Once connected into the Brypt network, the dashboard interface will provide information on the connected nodes, arbitrary “sensor” readings, and additional network data processing modules. 
8. A cycle reading request is sent every thirty seconds and the aggregated data will be placed into the streaming chart. 


# Brypt Ubuntu Virtual Machine in Action

1. Starting up Brypt Desktop

![alt_text](https://raw.githubusercontent.com/Stygain/brypt/master/Documents/Setup%20Guide/images/electron-setup.png "image_tooltip")


2. Logging in to the Brypt Application

![alt_text](https://raw.githubusercontent.com/Stygain/brypt/master/Documents/Setup%20Guide/images/login-form.png "image_tooltip")

![alt_text](https://raw.githubusercontent.com/Stygain/brypt/master/Documents/Setup%20Guide/images/login-success.png "image_tooltip")


3. Finding the Brypt Network

![alt_text](https://raw.githubusercontent.com/Stygain/brypt/master/Documents/Setup%20Guide/images/network-found.png "image_tooltip")


4. Initial Brypt Dashboard with one root coordinator and one leaf node

![alt_text](https://raw.githubusercontent.com/Stygain/brypt/master/Documents/Setup%20Guide/images/initial-dashboard.png "image_tooltip")


5. Brypt Dashboard and readings collected after 15 minutes of running

![alt_text](https://raw.githubusercontent.com/Stygain/brypt/master/Documents/Setup%20Guide/images/15-minute-dashboard.png "image_tooltip")

![alt_text](https://raw.githubusercontent.com/Stygain/brypt/master/Documents/Setup%20Guide/images/15-minute-readings.png "image_tooltip")
