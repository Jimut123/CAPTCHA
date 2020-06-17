# coding: utf-8
lib = File.expand_path('../lib', __FILE__)
$LOAD_PATH.unshift(lib) unless $LOAD_PATH.include?(lib)
require 'rcaptcha/version'

Gem::Specification.new do |spec|
  spec.name          = "rcaptcha"
  spec.version       = RCaptcha::VERSION
  spec.authors       = ["Kyle Dayton"]
  spec.email         = ["kyle@grol.ly"]
  spec.summary       = "A simple CAPTCHA image generator for Ruby"
  spec.description   = spec.summary
  spec.homepage      = "http://github.com/kyledayton/rcaptcha"
  spec.license       = "MIT"

  spec.files         = `git ls-files -z`.split("\x0")
  spec.executables   = spec.files.grep(%r{^bin/}) { |f| File.basename(f) }
  spec.test_files    = spec.files.grep(%r{^(test|spec|features)/})
  spec.require_paths = ["lib"]

  spec.add_development_dependency "bundler", "~> 1.5"
  spec.add_development_dependency "rake"
  spec.add_development_dependency "rspec"

  spec.add_dependency "rmagick"
end
