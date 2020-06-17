module RCaptcha

  class Generator

    # Generates the CAPTCHA image with +captcha_text+
    # @param [String] captcha_text the text to include in the CAPTCHA image
    # @return [String] the bytes of the generated image
    def self.generate(captcha_text, width = 100, height = 32)
      image = create_image(width, height)
      draw_text!(captcha_text, image)
      
      image = apply_distortion!(image)

      data = image.to_blob
      image.destroy!

      return data
    end

    private

    def self.create_image(width, height)
      image = Magick::Image.new(width, height)
      image.format = "jpg"
      image.gravity = Magick::CenterGravity
      image.background_color = 'white'

      image
    end

    def self.draw_text!(text, image)
      draw = Magick::Draw.new

      draw.annotate(image, image.columns, image.rows, 0, 0, text) {
        self.gravity = Magick::CenterGravity
        self.pointsize = 22
        self.fill = 'darkblue'
        self.stroke = 'transparent'
      }

      nil
    end

    def self.apply_distortion!(image)
      image = image.wave *random_wave_distortion
      image = image.implode random_implode_distortion
      image = image.swirl rand(10)
      image = image.add_noise Magick::ImpulseNoise
      image
    end

    def self.random_wave_distortion
      [4 + rand(2), 40 + rand(20)]
    end

    def self.random_implode_distortion
      (2 + rand(2)) / 10.0
    end

  end
  
end


