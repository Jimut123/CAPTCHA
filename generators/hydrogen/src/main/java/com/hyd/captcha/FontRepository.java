package com.hyd.captcha;

import java.awt.*;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Random;

public class FontRepository {

    private static final java.util.List<Font> FONTS = new ArrayList<>();

    private static final Random RANDOM = new Random();

    public static void loadFont(String filePath) throws IOException, FontFormatException {
        FONTS.add(Font.createFont(Font.TRUETYPE_FONT, new File(filePath)));
    }

    public static void loadFonts(String dirPath) throws IOException {
        Files.list(Paths.get(dirPath)).forEach(path -> {
            try {
                String fileName = path.getFileName().toString().toLowerCase();
                if (fileName.endsWith(".ttf") || fileName.endsWith(".otf")) {
                    loadFont(path.toAbsolutePath().toString());
                }
            } catch (IOException | FontFormatException e) {
                throw new FontException(e);
            }
        });
    }

    public static Font pickRandomFont() {
        if (FONTS.isEmpty()) {
            FONTS.add(Font.getFont("Dialog"));
        }

        if (FONTS.size() == 1) {
            return FONTS.get(0);
        }

        return FONTS.get(RANDOM.nextInt(FONTS.size()));
    }
}
