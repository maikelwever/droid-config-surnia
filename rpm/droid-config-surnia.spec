# These and other macros are documented in ../droid-configs-device/droid-configs.inc
%define device surnia
%define vendor motorola

%define vendor_pretty Motorola
%define device_pretty Moto E 2015 (LTE)

%define dcd_path ./

# Adjust this for your device
%define pixel_ratio 1.0

# We assume most devices will
%define have_modem 1

%include droid-configs-device/droid-configs.inc
