# hydrogen-captcha

This is a customizable captcha image generator.

## Usage

```java
CaptchaGenerator captchaGenerator = new CaptchaGenerator();
BufferedImage image = captchaGenerator.generate(200, 50, "ABCDEF");
```

Load fonts from a directory and `CaptchaGenerator` will use them:

```java
FontRepository.loadFonts("./sample-fonts/");
```

Setup a background: 

```java
captchaGenerator.setBackground(new CirclesBackground());
// or
captchaGenerator.setBackground(new GradientBackground(true));
```

And you can add effects on both background and char images:

```java
captchaGenerator.addBackgroundFilter(new CrossFilter(10, 1, true));
captchaGenerator.addCharImageFilter(new CrossFilter(10, 1, true));
```

And you can also create your own effects!

## Sample images

![screenshot](https://user-images.githubusercontent.com/900606/72231834-7f2c6980-35f8-11ea-8bb1-da819a3d8ca6.png)

![hDGRSI8Ov0](https://user-images.githubusercontent.com/900606/72612141-ddde4400-3966-11ea-9757-973aec7872f9.gif)


