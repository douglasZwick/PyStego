# PyStego
###### A Python steganography tool

<!-- some kind of friendly image or screenshot or whatever -->

PyStego is a fun little Python tool I wrote as a student of [Boot.dev](https://boot.dev/)'s "First Personal Project" portfolio project course. It takes some given data and hides it in a given image, such that with the same settings, it can extract the original data from the output image. It's not really intended for serious use, and in fact there may already be existing tools that do what it does and better, but that's not the point anyway. The main goal here is to create a little bit of software that I can call my own in an environment where I haven't really done much already (namely, Python).

**PyStego was created for educational purposes only. You should not use it to conceal sensitive information that you don't want others to learn. The creator of PyStego assumes no responsibility for any damages or distress caused by the use of this tool.**

### What Is Steganography?

According to Wiktionary.org, **steganography** is

> The art and science of concealing a secret message, data, or file within another innocuous message, image, audio file, or physical object in a way that hides the very existence of the hidden information from casual observation.

In other words, it's a way to hide data in plain sight. Naturally, it draws comparisons to cryptography, which makes a secret message unreadable to an outside observer. The key difference is, with steganography, the observer doesn't even know that the message exists in the first place.

### The Method

Any data someone might want to send via computer is fundamentally represented as a series of bits, whether it's a single integer, a string of text, a sound file, an executable program, etc. As long as the recipient's computer knows the relevant bits and the order they should go in, it can read the data. PyStego takes some data called the **payload** and hides it in an image by *overwriting the least significant bits* of some of the image's pixel data.

An image consists of pixels, each of some color or another. The color of each pixel can be encoded as a trio of bytes, one for each color channel in the image. So if an image uses RGB color (as a typical image generally does), then it encodes its pixel data as one byte for the red channel, one byte for the green channel, and one byte for the blue channel. (Many images also use an "alpha" channel, which is generally used for transparency, but we'll ignore that for now.) Each of these bytes stores the intensity of its respective channel as a value from 0 to 255. These values taken together determine the color of one pixel.

These RGB numbers can, of course, be represented as a series of bits.

Now, I won't go too far into the details of how binary numbers work, but let's just say that if you alter the *rightmost* one or two digits of a binary number, flipping them from 0 to 1 or vice versa, the overall effect on the magnitude of the number is much smaller than if you flip the *leftmost digits*. This is because the digits are the right are **less significant** to the value of the number than the digits on the left. So if we overwrite the least significant one or two bits of the RGB color values of an image, the effect is minimal &mdash; often completely imperceptible.

PyStego takes advantage of this fact to hide payload data in an image. It converts the data into a series of bit clusters, goes through the pixels of an image and overwrites the least significant bits of some of the color values with the bits from the payload, and then saves the final image file to disk. The result is an image that is *visually indistinguishible* from the original (though a computer would easily be able to tell them apart).

### Usage

I'll get into that later, the dang tool is still in the works anyway!

### Feature Roadmap

Here are the basic features PyStego will include at version 1.0.0:

- Encoding and decoding of basic data (i.e. numbers and strings)
- Encoding and decoding of full files

And, in no particular order, here is a perpetually incomplete list of the stretch goal features I intend to implement:

- Some way of mixing up which pixels are altered, e.g. distributing them uniformly throughout the image or using some sort of prime number-based scattering magic
- A way to do multiple passes over the same pixels (useful in cases of very long input bit strings or very small images)

### Image Attribution

What this project does with the images it uses constitutes fair use. If you are the copyright holder of an image in this project, please feel free to contact me (dougzwick at dougzwick dot com), and I will happily add an attribution.
