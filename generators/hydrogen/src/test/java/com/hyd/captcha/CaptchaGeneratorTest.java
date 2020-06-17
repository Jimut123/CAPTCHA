package com.hyd.captcha;

import com.hyd.captcha.background.CirclesBackground;
import com.hyd.captcha.charproperty.DefaultCharPropertyFactory;
import com.hyd.captcha.filter.CrossFilter;
import com.hyd.captcha.background.GradientBackground;
import java.awt.*;
import java.awt.event.*;
import java.awt.image.BufferedImage;
import java.security.SecureRandom;
import java.util.List;
import java.util.Random;
import java.util.function.Supplier;
import javax.swing.*;

public class CaptchaGeneratorTest extends JFrame {

    public static void main(String[] args) throws Exception {

        // FontRepository.loadFont("./sample-fonts/RobotoSlab.ttf");  // load single font
        FontRepository.loadFonts("./sample-fonts/");            // load multiple fonts

        CaptchaGenerator captchaGenerator = new CaptchaGenerator();
        // captchaGenerator.setBackground(new GradientBackground(true));
        captchaGenerator.setBackground(new CirclesBackground());

        // captchaGenerator.addBackgroundFilter(new CrossFilter(10, 1, true));
        // captchaGenerator.addBackgroundFilter(new CrossFilter(10, 1, false));

        captchaGenerator.setCharPropertyFactory(
            new DefaultCharPropertyFactory()
        );

        // captchaGenerator.addCharImageFilter(new CrossFilter(10, 1, true));
        captchaGenerator.setCharImageListener(
            (ch, font, bufferedImage) -> System.out.println(ch + ", " + font.getFontName())
        );

        int captchaWidth = 250;
        int captchaHeight = 70;
        int captchaLength = 8;
        String captchaChars = "ADEFGHJKLMNPRTUVWXY23456789";

        // How to create captcha image
        Supplier<BufferedImage> generateCaptcha = () -> {
            String str = generateRandomString(captchaChars, captchaLength);
            return captchaGenerator.generate(captchaWidth, captchaHeight, str);
        };

        //////////////////////////////////////////////////////////////

        JLabel imageLabel = new JLabel();
        JPanel charImagePanel = new JPanel();

        Runnable displayImage = () -> {
            BufferedImage bufferedImage = generateCaptcha.get();
            imageLabel.setIcon(new ImageIcon(bufferedImage));

            List<BufferedImage> charImages = CaptchaGenerator.getCharImages();
            charImagePanel.removeAll();
            charImages.forEach(charImage -> charImagePanel.add(imageLabel(charImage)));
            charImagePanel.revalidate();
            charImagePanel.repaint();

            System.out.println();
        };

        CaptchaGeneratorTest frame = new CaptchaGeneratorTest();
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        frame.setSize(400, 300);
        frame.setTitle("Captcha Image Samples");

        frame.getContentPane().setLayout(new BorderLayout());
        frame.getContentPane().add(imageLabel, BorderLayout.CENTER);

        charImagePanel.setLayout(new FlowLayout(FlowLayout.LEFT, 5, 5));
        frame.getContentPane().add(charImagePanel, BorderLayout.NORTH);

        JButton button = new JButton("Refresh");
        button.addActionListener(e -> displayImage.run());
        JPanel buttonsPanel = new JPanel();
        buttonsPanel.setLayout(new FlowLayout(FlowLayout.CENTER, 5, 5));
        buttonsPanel.add(button);
        frame.getContentPane().add(buttonsPanel, BorderLayout.SOUTH);

        frame.setLocation(500, 300);
        frame.addWindowListener(new WindowAdapter() {
            @Override
            public void windowOpened(WindowEvent e) {
                displayImage.run();
            }
        });
        frame.setVisible(true);
    }

    private static String generateRandomString(String captchaChars, Integer size) {
        Random random = new SecureRandom();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < size; i++) {
            sb.append(captchaChars.charAt(random.nextInt(captchaChars.length())));
        }
        return sb.toString();
    }

    private static JLabel imageLabel(BufferedImage bufferedImage) {
        return new JLabel(new ImageIcon(bufferedImage));
    }
}