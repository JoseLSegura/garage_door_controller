# Garage Door Controller

[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/) [![GitHub Actions status | JoseLSegura/garage_door_controller](https://github.com/JoseLSegura/garage_door_controller/workflows/CI%20unit%20tests%20and%20style/badge.svg)](https://github.com/JoseLSegura/garage_door_controller/actions?query=workflow%3A%22CI+unit+tests+and+style%22)

> A Python package with utilities to control my garage door. **This is a work in progress. Use it at your own risk**

## A bit of history...

At the end of the year 2019, I was messing around with my garage door controller board, trying to discover if it was
possible to control it as any other IoT device. While I was trying to figure out how to send some commands thought
an Ethernet port in the board, a power supply disruption occurred, breaking the old board.

As I had an old and forgotten Raspberry Pi stored, I took it and started to messing around with its GPIO port, learning
some libraries and commands to control it...

And here is the result.

## Which does this package intend?

The main objective of this package is provide a set of classes needed to control the different devices of my door
mechanism (mainly an electric lock and the motor), both individually and as a composited device.

I will be using [`gpiozero`](gpiozero.readthedocs.io/) as a base, extending and using it to create my own device
classes

## Secondary objectives

As every personal project, there are a few secondary objectives that will be covered with this project:

* Learning to work with some electric and electronic stuff
* Giving my Raspberry Pi a second life
* Learning about GPIO and how to use it
* Use and practice a bit with [GitHub Actions](https://github.com/JoseLSegura/garage_door_controller/actions)
