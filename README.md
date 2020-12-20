# Albert QR Code Plugin

## Description

The QR Albert plugin lets you create a QR code directly from the Albert prompt.

## Usage

You can generate a QR code by typing `qr <text to convert>` in the albert prompt. The space after `qr` is not counted, but all other whitespace is.

## Requirements

You can install the required python dependencies with `pip`:

`pip install qrcode[pil]`

Additionally, you'll need the `display` command, which is provided by the [ImageMagick](https://imagemagick.org) package. Most distros will ship with this, but distro-specific installations can be found [here.](https://imagemagick.org/script/download.php#unix)
