package com.hyd.captcha.filter;

import com.hyd.captcha.ImageUtil;
import com.hyd.captcha.ImageOperator;
import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.util.ArrayList;
import java.util.List;

public class CrossFilter implements ImageOperator {

    private int crossWidth;

    private int crossOffset;

    private boolean vertical;

    public CrossFilter(int crossWidth, int crossOffset, boolean vertical) {
        this.crossWidth = crossWidth;
        this.crossOffset = crossOffset;
        this.vertical = vertical;
    }

    @Override
    public void paint(BufferedImage bufferedImage, Graphics2D g) {

        if (crossOffset <= 0 || crossWidth <= 0) {
            return;
        }

        if (vertical) {
            crossVertical(bufferedImage, g);
        } else {
            crossHorizontal(bufferedImage, g);
        }
    }

    private void crossVertical(BufferedImage bufferedImage, Graphics2D g) {
        List<BufferedImage> subImages = new ArrayList<>();
        int height = bufferedImage.getHeight();
        int x = 0, direction = -1;
        while (x < bufferedImage.getWidth()) {
            int cropX = x;
            int cropY = direction < 0 ? crossOffset : 0;
            int cropWidth = Math.min(bufferedImage.getWidth() - cropX, crossWidth);
            int cropHeight = height - crossOffset;

            subImages.add(ImageUtil.deepCopy(
                bufferedImage.getSubimage(cropX, cropY, cropWidth, cropHeight)
            ));

            x += crossWidth;
            direction = -direction;
        }

        x = 0;
        direction = -1;
        for (BufferedImage subImage : subImages) {
            int drawX = x;
            int drawY = direction < 0 ? 0 : crossOffset;
            g.drawImage(subImage, drawX, drawY, null);

            x += crossWidth;
            direction = -direction;
        }
    }

    private void crossHorizontal(BufferedImage bufferedImage, Graphics2D g) {
        int width = bufferedImage.getWidth(), height = bufferedImage.getHeight();
        List<BufferedImage> subImages = new ArrayList<>();
        int y = 0, direction = -1;
        while (y < bufferedImage.getHeight()) {
            int cropX = direction < 0 ? crossOffset : 0;
            int cropY = y;
            int cropWidth = width - crossOffset;
            int cropHeight = Math.min(height - cropY, crossWidth);

            subImages.add(ImageUtil.deepCopy(
                bufferedImage.getSubimage(cropX, cropY, cropWidth, cropHeight)
            ));

            y += crossWidth;
            direction = -direction;
        }

        y = 0;
        direction = -1;
        for (BufferedImage subImage : subImages) {
            int drawX = direction < 0? 0: crossOffset;
            int drawY = y;
            g.drawImage(subImage, drawX, drawY, null);

            y += crossWidth;
            direction = -direction;
        }
    }
}
