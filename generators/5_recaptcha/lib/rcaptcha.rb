require 'RMagick'
require 'rcaptcha/generator'

module RCaptcha

  def self.generate(*args)
    RCaptcha::Generator.generate *args
  end

end



