# Network Router Configuration Store

## Project Description
This project simulates how a network router stores fixed (non-volatile) configuration settings.  
We used tuples to store permanent IP address + port combinations and mapped them to device names using dictionaries.  
Because tuples are immutable, the configuration cannot be changed accidentally once it is set — just like real router settings that stay in non-volatile memory.

## Team Members
1.⁠ ⁠[Md Sikandar] - [BWU/BTA/25/563] - (Lead / Coding / Documentation)
2.⁠ ⁠[Shivam Kumar] - [BWU/BTA/25/554] - (Coding / Testing)
3.⁠ ⁠[Sunrise Sk] - [BWU/BTA/25/555] - (Documentation / Presentation)
4.⁠ ⁠[Samima Nasrin] - [BWU/BTA/25/572] - (Testing / Research)

## Features
•⁠  ⁠Store device name → (IP address, port) using dictionary + tuple
•⁠  ⁠Prevent accidental modification of configuration (tuples are immutable)
•⁠  ⁠View all stored configurations
•⁠  ⁠Search configuration by device name
•⁠  ⁠Simple menu-driven interface

## How to Run
1.⁠ ⁠Make sure Python 3 is installed.
2.⁠ ⁠Open terminal / command prompt in the project folder.
3.⁠ ⁠Run: