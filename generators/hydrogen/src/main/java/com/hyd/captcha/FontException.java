package com.hyd.captcha;

public class FontException extends RuntimeException {

    public FontException() {
    }

    public FontException(String message) {
        super(message);
    }

    public FontException(String message, Throwable cause) {
        super(message, cause);
    }

    public FontException(Throwable cause) {
        super(cause);
    }
}
