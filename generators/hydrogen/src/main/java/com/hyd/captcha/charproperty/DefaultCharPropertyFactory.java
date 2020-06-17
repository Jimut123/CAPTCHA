package com.hyd.captcha.charproperty;

import static com.hyd.captcha.CaptchaGenerator.random;

import com.hyd.captcha.FontRepository;
import com.hyd.captcha.ImageUtil;

public class DefaultCharPropertyFactory implements CharPropertyFactory {

    @Override
    public CharProperty getCharProperty(char ch) {
        CharProperty charProperty = new CharProperty();
        charProperty.setStrikePaint(ImageUtil.randomColor(180, 255));
        charProperty.setFillPaint(ImageUtil.randomColor(0, 120));
        charProperty.setStrikeWidth(4);
        charProperty.setRotate(random(-Math.PI / 6, Math.PI / 6));
        charProperty.setShear(new double[]{random(-0.25, 0.25), random(-0.25, 0.25)});
        charProperty.setFont(FontRepository.pickRandomFont());
        return charProperty;
    }
}
