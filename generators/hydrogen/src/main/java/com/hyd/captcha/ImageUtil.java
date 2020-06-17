package com.hyd.captcha;

import java.awt.Color;
import java.awt.image.*;

public class ImageUtil {

    public static BufferedImage deepCopy(BufferedImage bi) {
        ColorModel cm = bi.getColorModel();
        boolean isAlphaPremultiplied = cm.isAlphaPremultiplied();
        WritableRaster raster = bi.copyData(bi.getRaster().createCompatibleWritableRaster());
        return new BufferedImage(cm, raster, isAlphaPremultiplied, null);
    }

    public static Color randomColor() {
        return randomColor(0, 255);
    }

    public static Color randomColor(int minGray, int maxGray) {
        int r = CaptchaGenerator.random(0, 255);
        int g = CaptchaGenerator.random(0, 255);
        int b = CaptchaGenerator.random(0, 255);

        int gray = (r * 30 + g * 59 + b * 11) / 100;

        while (gray < minGray) {
            int min = Math.min(r, Math.min(g, b));
            if (min == r) {
                r = Math.min(255, r + (minGray - gray) * 100 / 30);
            } else if (min == g) {
                g = Math.min(255, g + (minGray - gray) * 100 / 59);
            } else {
                b = Math.min(255, b + (minGray - gray) * 100 / 11);
            }
            gray = (r * 30 + g * 59 + b * 11) / 100;
        }

        while (gray > maxGray) {
            int max = Math.max(r, Math.max(g, b));
            if (max == r) {
                r = Math.max(0, r - (gray - maxGray) * 100 / 30);
            } else if (max == g) {
                g = Math.max(0, g - (gray - maxGray) * 100 / 59);
            } else {
                b = Math.max(0, b - (gray - maxGray) * 100 / 11);
            }
            gray = (r * 30 + g * 59 + b * 11) / 100;
        }

        return new Color(r, g, b);
    }
}
