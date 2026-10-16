module Jekyll
  module NumberWithDelimiter
    # 3770.4 | number_with_delimiter => "3,770"
    def number_with_delimiter(input)
      input.to_f.round.to_s.reverse.scan(/\d{1,3}/).join(",").reverse
    end
  end
end

Liquid::Template.register_filter(Jekyll::NumberWithDelimiter)
