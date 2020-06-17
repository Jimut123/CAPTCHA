$: << File.expand_path("./lib", __FILE__)
require "bundler/gem_tasks"

task :random_image do
  require 'rcaptcha'
  f = File.open('test.jpg', 'wb')

  numbers = (0..9).to_a
  captcha = 8.times.collect{numbers.sample}.join('')

  f.write RCaptcha.generate(captcha)
  f.close
end