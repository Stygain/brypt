# Our Code
Our code is located in three repositories:<br />
Brypt-Node: https://github.com/Stygain/brypt-node<br />
Brypt-Desktop: https://github.com/vpiscitello/brypt-desktop<br />
Brypt-Server: https://github.com/Stygain/brypt-server

# **Team 76 (Brypt) Setup Guide**


# Part One: Desktop Application

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
    + **Follow Brypt Setup Guide Part Two before continuing.**
    + Open a terminal and run the development version of the Brypt Desktop.

            cd ~/brypt-desktop
            npm run dev

        - Note: The application cache may think there’s two nodes connected. This is from the prior test run. The clear the nodes store, simply close the application and run again. 
    + Register for a new account or use the credentials: username: “piscitev” password “secured”.
    + **Follow Brypt Setup Guide Part Five to continue.**
* Manual Installation
    + Difficulty: **Hard**
    + Setup Time: 2-3 hours
    + Install required libraries and resources.
        - Requires: Ubuntu 18.04 LTS and an external Ubuntu/Debian/Linux WiFi adapter.
        - If running in a Virtual Machine follow steps _f_ through _h_ from Option 1 first.
        - **NOTE: FontAwesome Pro files must be requested from Vincenzo Piscitello ([piscitev@oregonstate.edu](mailto:piscitev@oregonstate.edu)) and moved into the requisite folder. The desktop application WILL NOT work without these files. **
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
        - OpenSSL 1.1.0fg
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
    + **Follow Brypt Setup Guide Part Two before continuing.**
    + Run the development version of the Electron application.
        ```bash 
        npm run dev
        ``` 
    + Start your Brypt network and login to the desktop application.
    + Register for a new account or use the credentials: username: “piscitev” password “secured”
    + **Follow Brypt Setup Guide Part Five to continue.**


# Part Two: Brypt Network - General Purpose Nodes

**You have two options: flash the Raspberry Pi and run our installation script (more difficult), or write our pre-made image to a micro-SD card and run a setup script (easier).**

**Write our Pre-made Image to a Micro-SD Card (Recommended):**

* Write our Raspberry Pi image to an 8GB+ micro-SD card:
    + (On Windows) - Install [Win32DiskImager](https://sourceforge.net/projects/win32diskimager/).
    + Download and unzip our [Raspberry Pi Image](https://oregonstate.box.com/s/99a9t0l4clebenrzdjp4pu4kkhe2i5rh) from Box.
    + Connect your micro-SD card to your computer.
    + Select your disk in Win32DiskImager.
    + Open the file-selector in Win32DiskImager and choose the downloaded Raspberry Pi image.
    + Select ‘Write’ in Win32DiskImager and wait for it to complete.
    + Starting up the Raspberry Pi:
        - Plug in the micro-SD card into the Raspberry Pi and boot it up.
        - Open a terminal and type:
            ```bash 
            ./startap.sh
            ```
        + Open a new terminal and type:
            ```bash 
            ./start_node.sh
            ```

**Flash the Raspberry Pi Yourself:**

* Flash the “Raspbian Stretch with Desktop” image onto a Raspberry Pi: [https://www.raspberrypi.org/downloads/raspbian/](https://www.raspberrypi.org/downloads/raspbian/)
    + To do this, download the zip file: 2018-10-09-raspbian-stretch.zip
    + Flash the image onto the Raspberry Pi’s SD card using Etcher: [https://etcher.io](https://etcher.io)  
    + Boot up the Raspberry Pi and walk through the setup steps. Be sure to connect to wifi.
        - Skip the software update
        - After finishing the setup steps, open up Chromium and try to search for something
        - You may need to enter in your credentials to connect to your LAN
    + Clone the Brypt Node Git repository from Github.com. Do this on both your client computer and designated Raspberry PI coordinator.
        ```bash
        cd ~
        git clone https://github.com/Stygain/brypt-node.git
        ```
    + General purpose computer install (Provided VM).
        - Ensure ZeroMQ and OpenSSL are installed on your system from _Part One._
        - Open a Command Line Interface (CLI) window to your local copy of brypt-node.
        - Move to the dev folder and run the make command.
            ```bash
            cd dev
            make
            ```
    + Raspberry PI install
        - Open a Command Line Interface (CLI) to your local copy of brypt-node.
        cd brypt-node
        - Move to the dev folder, run the setup script, and build the binary.
            ```bash
            cd dev
            chmod +x install.sh
            sudo ./install.sh
            ```
            1. Type ‘y’ as prompted. Hit ‘q’ or ‘Ok’ to continue through any other prompts.
            2. After reboot, open a new CLI:
                ```bash
                cd brypt-node/dev
                make
                ```
    + Starting a root coordinator on the Raspberry PI
        -  Once the device has rebooted open a new CLI window and ensure the Access Point is running.
            ```bash
            sudo service hostapd status
             ```
            * **If hostapd is not running**:
                ```bash
                sudo hostapd /etc/hostapd/hostapd.conf
                sudo service dnsmasq status
                ```
            * **If dnsmasq is not running**: In the dev folder of brypt-node run the Access Point startup script and reboot the device. 
                ```bash
                cd ./brypt-node/dev/config/AP
                sudo ./startup_ap.sh
                ```
                - If startup_ap.sh fails to run, make sure:
                    ```bash
                    perl -pe 's/\r$//' < startup_ap.sh > startup_ap.sh2
                    rm -f ./startup_ap.sh
                    mv ./startup_ap.sh2 ./startup_ap.sh
                    chmod +x startup_ap.sh
                    sudo ./startup_ap.sh
                    ```
                - The device should reboot automatically, but if not:
                    ```bash
                    sudo reboot
                    ```
        - Open a new CLI window to dev folder of brypt-node and start the coordinator.
            ```bash
            cd brypt-node/dev
            git checkout multi-punch
            make
            make root
            ```
        -  Troubleshooting: If you get a memory corruption error, run:
            ```bash
            make clean
            make
            ```
    + (Optional) To connect a leaf node to the Brypt root coordinator, use a general purpose computer running MacOS:
        - Since the node must be in the coordinator’s access point you must connect into the network after the desktop connection has been logged in. Otherwise the application will not be able to query the hosted central server at [https://www.brypt.com](https://www.brypt.com).
        - To add a leaf node, repeat steps 3-5 but **do not choose to start up the Access Point on reboot** when prompted.
        - Open the brypt-node/dev folder and start the leaf.
            ```bash
            make
            make leaf_two
            ```

# (Optional) Part Three: Brypt Network - Resource Constrained Nodes

1. Install required libraries and resources.
    * IDE
        + [https://www.arduino.cc/en/main/software](https://www.arduino.cc/en/main/software)
    * Arduino IDE library for your Adafruit Feather
        + [https://www.adafruit.com/category/943](https://www.adafruit.com/category/943)
    * Install Crypto library by Rhys Weatherley (Sketch -> Include library -> Manage libraries)
    * Follow Installation instructions for arduino-LoRa library: [https://github.com/sandeepmistry/arduino-LoRa](https://github.com/sandeepmistry/arduino-LoRa)
2. Ensure you have the brypt-node repository cloned from _Part Two._
3. Create a new folder called ‘Message’ in your Arduino IDE installation library folder. (For Windows: Program Files (x86)/Arduino/libraries)
4. Copy brypt-node/arduino/message/message.hpp and brypt-node/arduino/message/utility.hpp in the newly created ‘Message’ folder.
5. Open the Arduino.ino file in the Arduino IDE for your desired device (.ino files are found under brypt-node/arduino/SPECIFIC_DEVICE/).
6. Ensure the coordinator is running as this is a proof concept and the leaf node must be able make initial contact once it is flashed.
7. Flash the .ino file onto the Adafruit Feather using the Arduino IDE (Click right facing arrow ‘Upload’).


# (Optional) Part Four: Brypt Server



1. Install the Go programming language to your system.
    * [https://golang.org/doc/install](https://golang.org/doc/install)
2. Clone the Brypt Server Git repository from Github.com into your Go _src_ path.
    ```bash
    git clone https://github.com/Stygain/brypt-server.git
    ```
3. Open a Command Line Interface (CLI) to your local copy of brypt-server (i.e. _$GOPATH/src/brypt-server)_.
4. Get and install the Brypt Server Go dependencies.
    ```bash
    make deps
    make add-deps
    ```
5. Build the Brypt Server binary.
    ```bash
    make build
    ```
6. Run the Brypt Server binary.
    ```bash
    ./bin/bserv
    ```
7. If desired, the brypt-server _production_ branch may be used on Heroku to create a hosted server.


# Part Five: Demo Walkthrough and Network Lifecycle



1. Ensure that each application and network component is fully installed.
2. Startup the Brypt network root coordinator. This will be the Raspberry PI 3 running the local Access Point. 
    1. To easily verify the AP is running view your local Wifi connections and a _brypt-net-000000_ ssid should be visible.
    2. To verify that an IPv4 address is assigned to connected devices, connect to the AP and run _ifconfig_. From _ifconfig_ your Wifi interface should have some address starting with 192.168.30.x.
3. If testing with an additional Raspberry Pi 3 or additional Adafruit Feather nodes, you can connect them now.
4. With the Brypt network running start the desktop application on the client computer. 
    3. If you are still connected to the Brypt AP, disconnect and connect to a Wifi AP with direct internet access. 
5. Login to the Brypt network through the application interface
    4. This process will authenticate your user account and provide the program with any requisite network information (i.e. the Brypt AP ssid).
    5. You will be provided a success message and the login window will be closed to open the network dashboard. 
6. The dashboard interface will display a processing animation while it searches for the Brypt AP.
    6. If a notification is presented that it has found the network, click the button to connect.
    7. If a notification is presented that a network has not been found:
        1. Click the button to re-scan the local networks
        2. If the issue persists, ensure the Brypt root coordinator is hosting an Access Point and assigning devices a proper IPv4 address.
7. Once connected into the Brypt network, the dashboard interface will provide information on the connected nodes, arbitrary “sensor” readings, and additional network data processing modules. 
8. A cycle reading request is sent every thirty seconds and the aggregated data will be placed into the streaming chart. 


# Part Six: Brypt Ubuntu Virtual Machine in Action



1. Starting up Brypt Desktop

![alt_text](Documents/images/Untitled-document0.png "image_tooltip")


2. Logging in to the Brypt Application

![alt_text](Documents/images/Untitled-document1.png "image_tooltip")

![alt_text](Documents/images/Untitled-document2.png "image_tooltip")


3. Finding the Brypt Network

![alt_text](Documents/images/Untitled-document3.png "image_tooltip")


4. Initial Brypt Dashboard with one root coordinator and one leaf node

![alt_text](Documents/images/Untitled-document4.png "image_tooltip")


5. Brypt Dashboard and readings collected after 15 minutes of running

![alt_text](Documents/images/Untitled-document5.png "image_tooltip")

![alt_text](Documents/images/Untitled-document6.png "image_tooltip")
