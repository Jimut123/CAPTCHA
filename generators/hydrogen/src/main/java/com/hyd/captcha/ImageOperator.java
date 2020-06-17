package com.hyd.captcha;

import java.awt.Graphics2D;
import java.awt.image.BufferedImage;

public interface ImageOperator {

    void paint(BufferedImage bufferedImage, Graphics2D graphics2D);
}
