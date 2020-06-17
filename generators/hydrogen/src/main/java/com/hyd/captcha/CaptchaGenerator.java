package com.hyd.captcha;

import com.hyd.captcha.charproperty.CharProperty;
import com.hyd.captcha.charproperty.CharPropertyFactory;
import com.hyd.captcha.charproperty.DefaultCharPropertyFactory;
import java.awt.*;
import java.awt.font.FontRenderContext;
import java.awt.font.TextLayout;
import java.awt.geom.AffineTransform;
import java.awt.image.BufferedImage;
import java.security.SecureRandom;
import java.util.*;
import java.util.List;

public class CaptchaGenerator {

    private static final ThreadLocal<java.util.List<BufferedImage>> CHAR_IMAGE_LIST = new ThreadLocal<>();

    public static final Random RANDOM = new SecureRandom();

    public static int random(int min, int max) {
        return RANDOM.nextInt(Math.abs(max - min) + 1) + min;
    }

    public static double random(double min, double max) {
        return RANDOM.nextDouble() * (max - min) + min;
    }

    public static java.util.List<BufferedImage> getCharImages() {
        return CHAR_IMAGE_LIST.get();
    }

    //////////////////////////////////////////////////////////////

    private CharPropertyFactory charPropertyFactory = new DefaultCharPropertyFactory();

    private ImageOperator background;

    private List<ImageOperator> backgroundFilters = new ArrayList<>(
    );

    private List<ImageOperator> charImageFilters = new ArrayList<>(
    );

    private CharImageListener charImageListener;

    public void setCharImageListener(CharImageListener charImageListener) {
        this.charImageListener = charImageListener;
    }

    public void setBackground(ImageOperator background) {
        this.background = background;
    }

    public void addBackgroundFilter(ImageOperator imageOperator) {
        this.backgroundFilters.add(imageOperator);
    }

    public void addCharImageFilter(ImageOperator imageOperator) {
        this.charImageFilters.add(imageOperator);
    }

    public void setCharPropertyFactory(CharPropertyFactory charPropertyFactory) {
        this.charPropertyFactory = charPropertyFactory;
    }

    //////////////////////////////////////////////////////////////

    public BufferedImage generate(int width, int height, String content) {

        BufferedImage bufferedImage = new BufferedImage(width, height, BufferedImage.TYPE_INT_ARGB);
        Graphics2D g = (Graphics2D) bufferedImage.getGraphics();
        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
        g.setColor(Color.WHITE);
        g.fillRect(0, 0, bufferedImage.getWidth(), bufferedImage.getHeight());

        drawBackground(bufferedImage, g);

        java.util.List<BufferedImage> charImages = new ArrayList<>();
        drawChars(width, height, content, bufferedImage, charImages);
        CHAR_IMAGE_LIST.set(charImages);

        return bufferedImage;
    }

    private void drawBackground(BufferedImage bufferedImage, Graphics2D g) {
        if (this.background != null) {
            this.background.paint(bufferedImage, g);
            this.backgroundFilters.forEach(p -> p.paint(bufferedImage, g));
        }
    }

    private void drawChars(
        int width, int height, String content, BufferedImage bufferedImage, List<BufferedImage> charImages
    ) {
        char[] chars = content.toCharArray();

        int cellWidth = width / (chars.length + 1);
        int charWidth = (int) (cellWidth * 1.3);

        FontRenderContext frc = new FontRenderContext(null, false, false);
        Graphics2D g = (Graphics2D) bufferedImage.getGraphics();
        g.setComposite(AlphaComposite.getInstance(AlphaComposite.SRC_OVER));

        for (int i = 0; i < chars.length; i++) {
            char aChar = chars[i];
            BufferedImage charImage = generateCharImage(aChar, charWidth, frc);

            int[] pos = adjustCharPosition(height, cellWidth, i, charImage);

            g.drawImage(charImage, pos[0], pos[1], charImage.getWidth(), charImage.getHeight(), null);
            charImages.add(charImage);
        }
    }

    private int[] adjustCharPosition(int height, int cellWidth, int i, BufferedImage charImage) {
        int left = cellWidth * (i + 1);
        left = random(left - cellWidth / 8, left + cellWidth / 8) - charImage.getWidth() / 2;
        int top = random(height / 8, height * 7 / 8 - charImage.getHeight());
        return new int[]{left, top};
    }

    private static AffineTransform translate(double x, double y) {
        AffineTransform transform = new AffineTransform();
        transform.translate(x, y);
        return transform;
    }

    private Shape resetPosition(Shape shape) {
        AffineTransform transform = translate(-shape.getBounds().x, -shape.getBounds().y);
        return transform.createTransformedShape(shape);
    }

    private Shape apply(Shape shape, AffineTransform transform) {
        return resetPosition(transform.createTransformedShape(shape));
    }

    private BufferedImage generateCharImage(char aChar, int fontSize, FontRenderContext frc) {
        char[] aCharArr = {aChar};

        CharProperty charProperty = charPropertyFactory.getCharProperty(aChar);
        Font font = charProperty.getFont().deriveFont((float) fontSize);

        Shape charShape = new TextLayout(new String(aCharArr), font, frc).getOutline(null);
        charShape = resetPosition(charShape);

        //////////////////////////////////////////////////////////////

        if (charProperty.getRotate() != 0) {
            AffineTransform transform = new AffineTransform();
            Rectangle bounds = charShape.getBounds();
            if (charProperty.getRotate() > 0) {
                transform.translate(bounds.getHeight() * Math.abs(Math.sin(charProperty.getRotate())), 0);
            } else {
                transform.translate(0, bounds.getWidth() * Math.abs(Math.sin(charProperty.getRotate())));
            }
            transform.rotate(charProperty.getRotate());
            charShape = apply(charShape, transform);
        }

        if (charProperty.getShear() != null) {
            AffineTransform transform = new AffineTransform();
            transform.shear(charProperty.getShear()[0], charProperty.getShear()[1]);
            charShape = apply(charShape, transform);
        }

        //////////////////////////////////////////////////////////////

        BufferedImage image = new BufferedImage(
            charShape.getBounds().width + (fontSize / 4), charShape.getBounds().height + (fontSize / 4),
            BufferedImage.TYPE_INT_ARGB
        );

        Graphics2D g = (Graphics2D) image.getGraphics();
        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
        g.setComposite(AlphaComposite.Clear);
        g.fillRect(0, 0, image.getWidth(), image.getHeight());
        g.setComposite(AlphaComposite.Src);

        if (charProperty.getStrikeWidth() > 0 &&  charProperty.getStrikePaint() != null) {
            g.translate(charProperty.getStrikeWidth() / 2, charProperty.getStrikeWidth() / 2);
            g.setPaint(charProperty.getStrikePaint());
            g.setStroke(new BasicStroke(charProperty.getStrikeWidth()));
            g.draw(charShape);
        }

        if (charProperty.getFillPaint() != null) {
            g.setPaint(charProperty.getFillPaint());
            g.fill(charShape);
        }

        for (ImageOperator operator : charImageFilters) {
            operator.paint(image, g);
        }

        if (charImageListener != null) {
            charImageListener.charImageGenerated(aChar, font, image);
        }

        return image;
    }
}
