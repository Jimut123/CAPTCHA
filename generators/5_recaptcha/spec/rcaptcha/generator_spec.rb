require 'spec_helper'

describe RCaptcha::Generator do
  subject { RCaptcha::Generator }
  describe '#generate' do
    it 'returns a String' do
      subject.generate('text').should be_an_instance_of String
    end
  end
end