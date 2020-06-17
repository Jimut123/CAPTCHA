package com.hyd.captcha;

import java.awt.*;
import java.util.stream.Stream;

public class ShowAllFonts {

    public static void main(String[] args) {
        GraphicsEnvironment ge = GraphicsEnvironment.getLocalGraphicsEnvironment();

        System.out.println("All fonts: ");
        Stream.of(ge.getAllFonts()).forEach(font -> {
            System.out.println(font.getFontName() + " : " + font.getFamily() + " : " + font.getName());
        });

        System.out.println("All available font family names: ");
        Stream.of(ge.getAvailableFontFamilyNames()).forEach(System.out::println);
    }
}
