package com.hyd.captcha.background;

import static com.hyd.captcha.CaptchaGenerator.random;
import static com.hyd.captcha.ImageUtil.randomColor;

import com.hyd.captcha.CaptchaGenerator;
import com.hyd.captcha.ImageOperator;
import java.awt.Graphics2D;
import java.awt.geom.Ellipse2D.Double;
import java.awt.image.BufferedImage;

public class CirclesBackground implements ImageOperator {

    private static final int OFFSET = 10;

    private static final int MAX_RADIUS = 50;

    @Override
    public void paint(BufferedImage image, Graphics2D g) {
        int minx = -OFFSET, maxx = image.getWidth() + OFFSET,
            miny = -OFFSET, maxy = image.getHeight() + OFFSET;

        for (int i = 0; i < 50; i++) {
            int radius = random(OFFSET, MAX_RADIUS);
            int centerx = random(minx, maxx), centery = random(miny, maxy);

            while (radius > 0) {
                int x = centerx - radius, y = centery - radius;
                g.setPaint(randomColor());
                g.fill(new Double(x, y, radius * 2, radius * 2));
                radius -= random(1, 10);
            }
        }
    }
}
