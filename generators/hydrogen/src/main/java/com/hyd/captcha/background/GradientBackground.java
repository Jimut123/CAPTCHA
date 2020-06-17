package com.hyd.captcha.background;

import static com.hyd.captcha.CaptchaGenerator.random;
import static com.hyd.captcha.ImageUtil.randomColor;

import com.hyd.captcha.ImageOperator;
import java.awt.BasicStroke;
import java.awt.GradientPaint;
import java.awt.Graphics2D;
import java.awt.Paint;
import java.awt.image.BufferedImage;

public class GradientBackground implements ImageOperator {

    private boolean gradient;

    public GradientBackground(boolean gradient) {
        this.gradient = gradient;
    }

    @Override
    public void paint(BufferedImage bufferedImage, Graphics2D g) {
        int stroke = 10;
        int xmin = -stroke / 2;
        int xmax = bufferedImage.getWidth() + stroke / 2;
        int y1 = -stroke, y2 = bufferedImage.getHeight() + stroke;
        int x1 = random(xmin, xmax), x2 = random(xmin, xmax);

        g.setStroke(new BasicStroke(stroke));

        for (int i = 0; i < 200; i++) {
            g.setPaint(createPaint(y1, y2, x1, x2));
            g.drawLine(x1, y1, x2, y2);
            x1 = random(xmin, xmax);
            x2 = random(xmin, xmax);
        }

    }

    private Paint createPaint(int y1, int y2, int x1, int x2) {
        Paint paint;
        if (gradient) {
            paint = new GradientPaint(
                x1, y1, randomColor(),
                x2, y2, randomColor()
            );
        } else {
            paint = randomColor();
        }
        return paint;
    }
}
