package com.hyd.captcha;

import java.awt.Font;
import java.awt.image.BufferedImage;

public interface CharImageListener {

    void charImageGenerated(char ch, Font font, BufferedImage bufferedImage);
}
